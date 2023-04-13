#!/usr/bin/node
const x = process.argv[2];
const xNum = parseInt(x);
if (!isNaN(xNum)) {
  for (let i = 0; i < xNum; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
