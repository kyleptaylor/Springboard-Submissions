function sortedFrequency(arr, target) {
  let left = 0;
  let right = arr.length - 1;

  function findFirst() {
    let result = -1;

    while (left <= right) {
      let mid = Math.floor(left + (right - left) / 2);
      if (arr[mid] === target) {
        if (mid === 0 || arr[mid - 1] < target) {
          return mid;
        }
        right = mid - 1;
      } else if (arr[mid] < target) {
        left = mid + 1;
      } else {
        right = mid - 1;
      }
    }
    return result;
  }

  function findLast() {
    let result = -1;

    while (left <= right) {
      let mid = Math.floor(left + (right - left) / 2);
      if (arr[mid] === target) {
        if (mid === arr.length - 1 || arr[mid + 1] > target) {
          return mid;
        }
        left = mid + 1;
      } else if (arr[mid] < target) {
        left = mid + 1;
      } else {
        right = mid - 1;
      }
    }
    return result;
  }

  firstIdx = findFirst();

  if (firstIdx === -1) return 0;

  left = 0;
  right = arr.length - 1;

  lastIdx = findLast();

  totaIdx = arr.length - 1;

  return lastIdx - firstIdx + 1;
}

module.exports = sortedFrequency;
