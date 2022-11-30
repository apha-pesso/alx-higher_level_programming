#!/usr/bin/node
const Square = require('./5-square');

class Square1 extends Square {

  charPrint (c) {
    for (let i = 0; i < this.width; i++) {
      const out = [];
      for (let j = 0; j < this.height; j++) {
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

module.exports = Square1;
