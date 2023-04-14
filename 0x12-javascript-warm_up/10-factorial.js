#!/usr/bin/node

function factorial (n) {
  if (isNaN(n)) {
    return 1;
  } else if (n === 0) {
    return 1;
  } else {
    const result = n * factorial(n - 1);
    return result;
  }
}

const arg = parseInt(process.argv[2]);
console.log(factorial(arg));
