function sort(array) {
  var pivotIndex = Math.floor(Math.random() * (array.length - 1));
  var pivot = array[pivotIndex];
  var left = [];
  var right = [];
  array.forEach(function(item, idx) {
    if (idx === pivotIndex) {
      return;
    }
    if (item < pivot) {
      left.push(item);
    } else {
      right.push(item);
    }
  })
  
  if (left.length) {
    left = sort(left);
  }

  if (right.length) {
    right = sort(right);
  }


  result = left.concat([pivot]).concat(right);
  return result;
}

console.log(sort([3, 4, 5, 8, 2, 1]));