#!/usr/bin/node
const argv = process.argv;
const num = parseInt(argv[2]);

if (isNaN(num)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < num; i++) {
    for (let i = 0; i < num; i++) {
      process.stdout.write('X');
    }
    if (i !== num - 1) {
      console.log();
    }
  }
}
