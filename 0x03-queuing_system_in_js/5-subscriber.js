const { createClient } = require('redis');

const subscriber = createClient();

subscriber.on('error', (err) => {
  console.log('Redis client not connected to the server:', err.toString());
});

subscriber.on('connect', () => {
  console.log('Redis client connected to the server');
  subscriber.subscribe('holberton school channel');
});

subscriber.on('message', (channel, message) => {
  console.log(`Received message on channel ${channel}: ${message}`);
  if (message === 'KILL_SERVER') {
    subscriber.unsubscribe('holberton school channel');
    subscriber.quit();
  }
});
