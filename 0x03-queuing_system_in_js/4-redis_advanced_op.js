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

// Create a hash key
const hashKey = 'HolbertonSchools';

// Create a hash table called 'HolbertonSchools' using the HSET command
client.hset(hashKey, 'Portland', '50', redis.print);
client.hset(hashKey, 'Seattle', '80', redis.print);
client.hset(hashKey, 'New York', '20', redis.print);
client.hset(hashKey, 'Bogota', '20', redis.print);
client.hset(hashKey, 'Cali', '40', redis.print);
client.hset(hashKey, 'Paris', '2', redis.print);

// Use the HGETALL command to view all values of the hash table
client.hgetall(hashKey, (err, res) => {
  if(err) {
    console.log(err);
  }
  console.log('{');
  for (const key in res) {
    console.log(`${key}: ${res[key]}`);
  }
  console.log('}');
});
