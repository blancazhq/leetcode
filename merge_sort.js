function sort(array) {
  var halfLength = array.length / 2;
  var firstHalf = array.slice(0, halfLength);
  var secondHalf = array.slice(halfLength, array.length);
  if (firstHalf.length > 1) {
    firstHalf = sort(firstHalf);
  }

  if (secondHalf.length > 1) {
    secondHalf = sort(secondHalf);
  }
  
  return merge(firstHalf, secondHalf);
}

function merge(array1, array2) {
  var result = [];
  var counter1 = 0;
  var counter2 = 0;
  while(counter1 < array1.length && counter2 < array2.length) {
    if (array1[counter1] < array2[counter2]) {
      result.push(array1[counter1]);
      counter1 ++;
    } else {
      result.push(array2[counter2]);
      counter2 ++;
    }
  }

  while(counter1 < array1.length) {
    result.push(array1[counter1]);
    counter1 ++;
  }

  while(counter2 < array2.length) {
    result.push(array2[counter2]);
    counter2 ++;
  }

  return result;
}

console.log("final", sort([1, 2, 3, 7, 4, 5, 9]));