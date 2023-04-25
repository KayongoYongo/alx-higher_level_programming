#!/usr/bin/node

// Import the file system module
const fs = require('fs');
// Assign values to the string and filepath
const filePath = process.argv[2];
const string = process.argv[3];

// Write the info onto the file using writeFile
fs.writeFile(filePath, string, 'utf-8', (err) => {
// If an error exists, print it
  if (err) {
    console.error(err);
  }
});
