#!/usr/bin/node

// Import the file system module
const fs = require('fs');
// Import request module
const request = require('request');

// Assign values to the string and filepath
const url = process.argv[2];
const filePath = process.argv[3];

request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    fs.writeFile(filePath, body, 'utf-8', (error) => {
      if (error) {
        console.error(error);
      }
    });
  }
});
