// 1. Original Function //

    function filterOutOdds() {
        var nums = Array.prototype.slice.call(arguments);
        return nums.filter(function(num) {
        return num % 2 === 0
        });
    }

    // Refactored Function //
    
    const filterOutOdds2 = (...args) => args.filter (num => num % 2 === 0);


// 2. findMin Function //

    const findMin = (...args) => Math.min(...args);


// 3. mergeObjects Function //

    const mergeObjects = (obj1, obj2) => ({...obj1, ...obj2})


// 4. doubleAndReturnArgs Function //

    const doubleAndReturnArgs = (arr, ...args) => [...arr, ...args.map(num => num * 2)]

// 5. Slice and Dice! //

    /** remove a random element in the items array
    and return a new array without that item. */

    function removeRandom(...items) {
        const randomInx = Math.floor(Math.random() * items.length);
        items.splice(randomInx, 1);
        return items;
    }

    /** Return a new array with every item in array1 and array2. */

    function extend(array1, array2) {

    }

    /** Return a new object with all the keys and values
    from obj and a new key/value pair */

    function addKeyVal(obj, key, val) {

    }


    /** Return a new object with a key removed. */

    function removeKey(obj, key) {

    }


    /** Combine two objects and return a new object. */

    function combine(obj1, obj2) {

    }


    /** Return a new object with a modified key and value. */

    function update(obj, key, val) {

    }