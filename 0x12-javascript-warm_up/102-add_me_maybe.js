#!/usr/bin/node
function addMeMaybe (number, theFunction) {
  const result = number + 1;
  console.log('New value: ' + result);
  return result;
  theFunction();
}
module.exports.addMeMaybe = addMeMaybe;
