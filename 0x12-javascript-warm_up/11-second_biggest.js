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

  const maxi = Math.max(...arr);
  const maxIndex = arr.indexOf(maxi);
  arr.splice(maxIndex, 1);
  console.log(Math.max(...arr));
}
