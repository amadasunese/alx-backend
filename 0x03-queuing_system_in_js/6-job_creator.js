import kue from 'kue';

// Create a Kue queue
const queue = kue.createQueue();

const jobData = {
  phoneNumber: '1234567890', // replace with actual phone number
  message: 'This is a test message',
};

// Create a job in the 'push_notification_code' queue
const job = queue.create('push_notification_code', jobData)
  .save((err) => {
    if (err) {
      console.log(`Error creating job: ${err}`);
    } else {
      console.log(`Notification job created: ${job.id}`);
    }
  });

job.on('complete', () => {
  console.log('Notification job completed');
}).on('failed', (errorMessage) => {
  console.log(`Notification job failed: ${errorMessage}`);
});

