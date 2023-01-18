#!/usr/bin/node
// prints the title of a Star Wars movie
// with the given integer

const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
request(url, (error, response, body) => {
  if (error) console.log('error:', error);
  const res = JSON.parse(body);
  console.log(res.title);
});
