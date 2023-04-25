#!/usr/bin/node

// Response module to help in acquiring status code
const request = require('request');
// The url is assigned to the argument
const url = process.argv[2];

request.get(url).on('response', function (response) {
  console.log(`code: ${response.statusCode}`);
});
