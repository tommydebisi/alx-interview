#!/usr/bin/node
/*
    Program to solve the StarWars Api task
*/
const request = require('request');
let arg = process.argv.slice(2);

// error management
if (arg.length === 0) {
  console.log(`USAGE: ${process.argv.slice(1, 2)} <Number>`);
  process.exit(1);
} else if (arg.length >= 1) {
  arg = arg.slice(0, 1);

  if (!Number(arg)) {
    console.log('Error: Argument must be a number');
    process.exit(1);
  }
}

const url = `https://swapi-api.alx-tools.com/api/films/${arg}`;
const promUrl = new Promise((resolve, reject) => {
  request.get({ url, json: true }, (err, res, body) => {
    if (err) {
      reject(console.log(err));
    }

    body.characters.forEach(element => {
      request.get({ url: element, json: true }, (err, res, body) => {
        if (err) {
          reject(console.log(err));
        }

        resolve(console.log(body.name));
      });
    });
  });
});

async function getReq () {
  await promUrl;
}

getReq();
