#!/usr/bin/node
// a script that writes a string to a file

const request = require('request');
const url = process.argv[2];
request(url, (error, response, body) => {
  console.log('error:', error);
  console.log('code:', response.statusCode);
});
