function cal(num) {
  if (num.toString().length === 1) {
    return num;
  }else {
    var divider = Math.pow(10, num.toString().length - 1);
    return cal(num % divider) * 10 + Math.floor(num / divider);
  }
}

console.log(cal(54321))
