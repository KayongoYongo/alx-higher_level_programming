#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (!Number.isInteger(w) || w <= 0 || !Number.isInteger(h) || h <= 0) {
      let Rectangle = {};
      return Rectangle.name;
    }
    this.width = w;
    this.height = h;
  }

  print () {
   for (let i = 0; i < this.height; i++) {
    let row = "";
    for (let j = 0; j < this.width; j++) {
      row += "X";
    }
    console.log(row);
   } 
 }
 
  rotate () {
   [this.width, this.height] = [this.height, this.width];
  }

  double () {
    [this.width, this.height] = [this.width * 2, this.height * 2];
  } 
};
