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

// url for extracting the characters in films api
const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;

// send a request using a request module
request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
  }

  if (response.statusCode === 200) {
    const data = JSON.parse(body);

    data.characters.forEach((person) => {
      request.get(person, (error, response, body) => {
        if (error) {
          console.error(error);
        }

        if (response.statusCode === 200) {
          const peopleCharacter = JSON.parse(body);

          console.log(peopleCharacter.name);
        }
      });
    });
  }
});
