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

  rotate () {
    [this.width, this.height] = [this.height, this.width];
    // const temp = this.width;
    // this.width = this.heigth;
    // this.heigth = temp;
  }

  double () {
    this.width *= 2;
    this.heigth *= 2;
  }
}
module.exports = Rectangle;
