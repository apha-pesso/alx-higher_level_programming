#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      const x = [];
      for (let j = 0; j < this.width; j++) {
        x.push('X');
        // process.stdout.write('X');
        // x += 'X';
      }
      // if (i < (this.h - 1)) {
      // console.log();
      // }
      console.log(`${x.join('')}`);
    }
  }
}
module.exports = Rectangle;
