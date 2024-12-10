#!/usr/bin/node
/**
 * Write a script that prints all characters of a Star Wars movie:
 * The first positional argument passed is the Movie ID - example: 3 = “Return of the Jedi”
 * Display one character name per line in the same order as the “characters” list in the /films/ endpoint
 * You must use the Star wars API
 * You must use the request module
 */

const request = require('request');
const process = require('process');

if (process.argv.length < 3) {
  console.error('Usage: node script.js <Movie ID>');
  process.exit(1);
}
// movie url & movieId
const movieId = process.argv[2];
const movieUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request.get(movieUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error(error);
    return;
  }

  try {
    const data = JSON.parse(body);

    const movieCharacters = data.characters;

    movieCharacters.forEach((person) => {
      request.get(person, (error, response, body) => {
        if (error) {
          console.error(error);
          return;
        }

        if (response.statusCode === 200) {
          const characterNames = JSON.parse(body);

          console.log(characterNames.name);
        } else {
          console.error(`Failed to fetch character details. Status code: ${response.statusCode}`);
        }
      });
    });
  } catch (error) {
    throw new Error(error);
  }
});
