#!/usr/bin/node
const args = process.argv.slice(2);
console.log(args[0] === 'undefined' ? 'No argument' : process.argv[2]);
