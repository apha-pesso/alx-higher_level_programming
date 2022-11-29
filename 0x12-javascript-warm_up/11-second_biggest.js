#!/usr/bin/node
const argv = process.argv;
const arr = [];

if (argv.length === 2) {
  console.log(0);
} else if (argv.length === 3) {
  console.log(1);
} else {
  for (let i = 2; i < argv.length; i++) {
    arr.push(argv[i]);
  }
  console.log(`${Math.max(...arr)}`);
}
