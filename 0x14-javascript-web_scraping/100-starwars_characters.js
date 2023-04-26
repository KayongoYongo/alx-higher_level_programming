#!/usr/bin/node

// Response module to help in acquiring the body
const request = require('request');
// Assigning movie Id to the second argument
const movieId = process.argv[2];

// Constructing a URL for the Star Wars API endpiont
// It returns information about hte mmovie ID
const url = 'https://swapi-api.alx-tools.com/api/films/' + movieId;

request(url, function (error, response, body) {
  if (!error) {
    const characters = JSON.parse(body).characters;
    characters.forEach((character) => {
      request(character, function (error, response, body) {
        if (!error) {
          console.log(JSON.parse(body).name);
        }
      });
    });
  }
});
