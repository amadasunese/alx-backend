import redis from 'redis';
import { promisify } from 'util';
import kue from 'kue';
import express from 'express';

const app = express();

const client = redis.createClient();
const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

let reservationEnabled = true;

function reserveSeat(number) {
  return setAsync('available_seats', number);
}

async function getCurrentAvailableSeats() {
  const seats = await getAsync('available_seats');
  return seats ? parseInt(seats) : null;
}

// Initialize available seats to 50 at startup
reserveSeat(50);


const queue = kue.createQueue();


app.get('/available_seats', async (req, res) => {
  const seats = await getCurrentAvailableSeats();
  res.json({ numberOfAvailableSeats: seats });
});

app.get('/reserve_seat', (req, res) => {
  if (!reservationEnabled) {
    return res.json({ status: "Reservations are blocked" });
  }

  const job = queue.create('reserve_seat', {}).save(err => {
    if (err) return res.json({ status: "Reservation failed" });
    res.json({ status: "Reservation in process" });
  });

  job.on('complete', () => {
    console.log(`Seat reservation job ${job.id} completed`);
  }).on('failed', errorMessage => {
    console.log(`Seat reservation job ${job.id} failed: ${errorMessage}`);
  });
});

app.get('/process', (req, res) => {
  queue.process('reserve_seat', async (job, done) => {
    const seats = await getCurrentAvailableSeats();
    if (seats > 0) {
      await reserveSeat(seats - 1);
      if (seats - 1 === 0) reservationEnabled = false;
      done();
    } else {
      done(new Error("Not enough seats available"));
    }
  });

  res.json({ status: "Queue processing" });
});

app.listen(1245, () => {
  console.log('Server is running on port 1245');
});
