function findFloor(arr, target) {
  let left = 0;
  let right = arr.length - 1;
  let result = -1;

  while (left <= right) {
    let mid = Math.floor(left + (right - left) / 2);

    if (arr[mid] <= target) {
      result = mid;
      left = mid + 1;
    } else {
      right = mid - 1;
    }
  }

  return arr[result];
}

module.exports = findFloor;
