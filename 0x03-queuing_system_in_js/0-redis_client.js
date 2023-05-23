// Import redis module
import redis from 'redis';

// Creating the redis client
const client = redis.createClient();

// Listening for connection
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Listening for errors
client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});
