#!/usr/bin/node

// Response module to help in acquiring the body
const request = require('request');

// Assigning URL to the second argument
const url = process.argv[2];

request.get(url, (error, response, body) => {
  if (!error) {
    // Assigning the JSON object to a value
    const result = JSON.parse(body);

    const completed = {};

    for (let i = 0; i < result.length; i++) {
      if (result[i].completed === true) {
        if (!completed[result[i].userId]) completed[result[i].userId] = 0;
        completed[result[i].userId]++;
      }
    }
    console.log(completed);
  }
});
