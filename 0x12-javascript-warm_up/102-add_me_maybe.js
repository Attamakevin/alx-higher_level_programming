#!/usr/bin/node
function addMeMaybe (number, theFunction) {
  number++;
  console.log('New value: ' + number);
}
module.exports.addMeMaybe = addMeMaybe;
