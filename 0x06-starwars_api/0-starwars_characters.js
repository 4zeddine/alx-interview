#!/usr/bin/node
//  Module for prints all characters of a Star Wars movie
const request = require('request');
const API_URL = 'https://swapi-api.alx-tools.com/api/';

request(`${API_URL}films/${process.argv[2]}/`, (error, _, body) => {
  if (error) {
    console.log(error);
  }
  const data = JSON.parse(body);
  const charactersURL = data.characters;
  const charactersName = charactersURL.map(
    url => new Promise((resolve, reject) => {
      request(url, (promiseError, __, charactersBody) => {
        if (promiseError) {
          reject(promiseError);
        }
        resolve(JSON.parse(charactersBody).name);
      });
    }));

  Promise.all(charactersName)
    .then(names => console.log(names.join('\n')))
    .catch(Err => console.log(Err));
});
