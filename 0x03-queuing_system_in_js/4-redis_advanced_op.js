const { createClient, print } = require('redis');

const client = createClient();

client.on('error', (err) => {
  console.error('Redis client error:', err);
});

client.on('connect', () => {
  console.log('Connected to Redis server');
  createHash();
});

function createHash() {
  // Using hset to store the hash values
  client.hset(
    'HolbertonSchools',
    'Portland',
    50,
    print
  );

  client.hset(
    'HolbertonSchools',
    'Seattle',
    80,
    print
  );

  client.hset(
    'HolbertonSchools',
    'New York',
    20,
    print
  );

  client.hset(
    'HolbertonSchools',
    'Bogota',
    20,
    print
  );

  client.hset(
    'HolbertonSchools',
    'Cali',
    40,
    print
  );

  client.hset(
    'HolbertonSchools',
    'Paris',
    2,
    (err, reply) => {
      if (err) {
        console.error('Error setting Paris:', err);
      } else {
        console.log('Set result for Paris:', reply);
        displayHash();
      }
    }
  );
}

function displayHash() {
  // Using hgetall to display the hash
  client.hgetall('HolbertonSchools', (err, reply) => {
    if (err) {
      console.error('Error getting hash:', err);
    } else {
      console.log('Hash:', reply);
      client.quit();
    }
  });
}
