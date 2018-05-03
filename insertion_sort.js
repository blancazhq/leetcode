function sort(array) {
  var sorted = [];
  array.forEach(function(element, idx) {
    if (!sorted.length) {
      sorted.push(element);
    } else {
      sorted.some(function(sortedElement, sortedIdx) {
        if (element < sortedElement) {
          sorted.splice(sortedIdx, 0, element);
          return true;
        } else if (sortedIdx === sorted.length - 1) {
          sorted.push(element);
        }
      });
    }
  });
  return sorted;
}

console.log(sort([2, 3, 1, 4, 5]));