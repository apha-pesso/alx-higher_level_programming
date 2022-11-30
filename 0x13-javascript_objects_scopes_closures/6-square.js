#!/usr/bin/node
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    for (let i = 0; i < this.size; i++) {
      const out = [];
      for (let j = 0; j < this.size; j++) {
        if (c) {
          out.push(c);
        } else {
          out.push('X');
        }
      }
      console.log(`${out.join('')}`);
    }
  }
}

module.exports = Square;
