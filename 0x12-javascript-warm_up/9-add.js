#!/usr/bin/node
const argv = process.argv;
const num1 = parseInt(argv[2]);
const num2 = parseInt(argv[3]);

function add (a, b) {
  return (a + b);
}

if ((isNaN(num1)) || (isNaN(num2))) {
  console.log('NaN');
} else {
  console.log(`${add(num1, num2)}`);
}
