import express from 'express';
import { promisify } from 'util';
import redis from 'redis';

const app = express();
const client = redis.createClient(); // Connect to your Redis server
const getAsync = promisify(client.get).bind(client);

const listProducts = [
    { id: 1, name: 'Suitcase 250', price: 50, stock: 4 },
    { id: 2, name: 'Suitcase 450', price: 100, stock: 10 },
    { id: 3, name: 'Suitcase 650', price: 350, stock: 2 },
    { id: 4, name: 'Suitcase 1050', price: 550, stock: 5 }
    // ... other products
  ];
  
  function getItemById(id) {
    return listProducts.find(product => product.id === id);
  }

app.get('/list_products', (req, res) => {
  res.json(listProducts.map(product => ({
    itemId: product.id,
    itemName: product.name,
    price: product.price,
    initialAvailableQuantity: product.stock
  })));
});

app.get('/list_products/:itemId', async (req, res) => {
  const item = getItemById(parseInt(req.params.itemId));
  if (!item) {
    return res.status(404).json({ status: 'Product not found' });
  }
  
  const currentStock = await getCurrentReservedStockById(item.id) || item.stock;
  res.json({ ...item, currentQuantity: currentStock });
});

// ... other routes
app.get('/reserve_product/:itemId', async (req, res) => {
    const itemId = parseInt(req.params.itemId);
    const item = getItemById(itemId);
  
    if (!item) {
      return res.status(404).json({ status: 'Product not found' });
    }
  
    const currentStock = await getCurrentReservedStockById(itemId) || item.stock;
    if (currentStock <= 0) {
      return res.json({ status: 'Not enough stock available', itemId });
    }
  
    reserveStockById(itemId, currentStock - 1);
    res.json({ status: 'Reservation confirmed', itemId });
  });

  
function reserveStockById(itemId, stock) {
  client.set(`item.${itemId}`, stock);
}

async function getCurrentReservedStockById(itemId) {
  const stock = await getAsync(`item.${itemId}`);
  return stock ? parseInt(stock) : null;
}


app.listen(1245, () => {
  console.log('Server is running on port 1245');
});








