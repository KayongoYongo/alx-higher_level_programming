#!/usr/bin/node
const arg = parseInt(process.argv[2]);
console.log(isNaN(arg) ? 'Not a number' : 'My number: ' + arg);
