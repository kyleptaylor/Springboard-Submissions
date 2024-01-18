// Original Function ->

function double(arr) {
    return arr.map(function(val) {
      return val * 2;
    });
  }

// Arrow Shorthand ->

const double = arr => arr.map ( val => val * 2);


// Original Function ->

function squareAndFindEvens(numbers){
    var squares = numbers.map(function(num){
      return num ** 2;
    });
    var evens = squares.filter(function(square){
      return square % 2 === 0;
    });
    return evens;
  }

  // Arrow Shorthand ->

  const squareAndFindEvens = numbers => numbers.map(num => num **2).filter(square => square % 2 === 0)