#!/usr/bin/node

// Import the built-in fs (file system) module
const fs = require('fs');

// Get the file path from the first command-line argument
const filePath = process.argv[2];

// Use the fs.readFile method to read the contents of the file
// // with utf-8 encoding and a callback function to handle the result
fs.readFile(filePath, 'utf8', (err, data) => {
	if (err) {
		console.error(err);
	} else {

		console.log(data);
	}
});
