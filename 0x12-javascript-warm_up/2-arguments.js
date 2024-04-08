#!/usr/bin/node
// Print string “Javascript is amazing”

if (process.argv.length == 2) {
	console.log('No argument found');
} else if (process.argv.length == 3) {
	console.log('Argument found');
} else {
	console.log('Arguments found');
}
