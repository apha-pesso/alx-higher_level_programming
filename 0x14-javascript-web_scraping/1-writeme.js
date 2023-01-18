#!/usr/bin/node
// a script that writes a string to a file

const write = require('fs');
write.writeFile(process.argv[2], process.argv[3], (err) => {
  if (err) throw err;
});
