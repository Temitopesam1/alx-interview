#!/usr/bin/node
const request = require('request');

const url = 'https://swapi-api.alx-tools.com/api/';
const arg = process.argv[2];
const charsName = [];
if (arg) {
  request(`${url}films/${arg}`, (error, response, body) => {
    if (error) { console.log(error); }
    const characters = JSON.parse(body).characters;
    for (const chars of characters) {
      const name = new Promise((resolve, reject) => {
        request(chars, (promErr, response, charsReqBody) => {
          if (promErr) { reject(promErr); }
          resolve(JSON.parse(charsReqBody).name);
        });
      });
      charsName.push(name);
    }
    Promise.all(charsName)
      .then(names => console.log(names.join('\n')))
      .catch(allErr => console.log(allErr));
  });
}
