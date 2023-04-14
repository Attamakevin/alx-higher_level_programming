#!/usr/bin/node
function addMeMaybe (number, theFunction) {
  const result = number + 1;
  console.log('New value: ' + result);
  return result;
}
module.exports.addMeMaybe = addMeMaybe;
