#!/usr/bin/node
// a script that reads and prints the content of a file

const read = require('fs');
read.readFile(process.argv[2], 'utf-8', (err, data) => {
  if (err) throw err;
  console.log(data);
});
