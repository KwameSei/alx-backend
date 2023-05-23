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

// Creating functions to set values

const setNewSchool = (schoolName, value) => {
  client.set(schoolName, value, (err, reply) => {
    redis.print(`Reply: ${reply}`);
  });
};

async function  displaySchoolValue(schoolName){
  try {
    const value = await client.get(schoolName, (err, value) => {
      console.log(value);
    });
  } catch (error) {
    console.log(error);
  }
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
