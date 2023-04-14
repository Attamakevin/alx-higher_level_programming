#!/usr/bin/node
const args = process.argv.slice(2);
const numArgs = args.length;

/* If no argument is passed, print 0 */
if (numArgs === 0) {
  console.log(0);
  /* If only one argument is passed, print 0 */
} else if (numArgs === 1) {
  console.log(0);
} else {
  /* Convert arguments to integers */
  const nums = args.map(Number);

  /* Find the maximum number in the list */
  const maxNum = Math.max(...nums);

  /* Remove the maximum number from the list */
  const numsWithoutMax = nums.filter(num => num !== maxNum);

  /* Find the second maximum number in the list */
  const secondMaxNum = Math.max(...numsWithoutMax);

  /* Print the second maximum number */
  console.log(secondMaxNum);
}
