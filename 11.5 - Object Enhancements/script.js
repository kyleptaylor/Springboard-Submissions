// 1. Original Function //

function createInstructor(firstName, lastName){
    return {
      firstName: firstName,
      lastName: lastName
    }
}

// ES2015 version //

function createInstructor(firstName, lastName){
    return {
      firstName,
      lastName
    }
}

// 2. Original Function //

var favoriteNumber = 42;

var instructor = {
firstName: "Colt"
}

instructor[favoriteNumber] = "That is my favorite!"

// ES2015 version //

var instructor = {
firstName: "Colt",
[favoriteNumber]: "That is my favorite!",
}

// 3. Original Function //

var instructor = {
    firstName: "Colt",
    sayHi: function(){
      return "Hi!";
    },
    sayBye: function(){
      return this.firstName + " says bye!";
    }
  }

// ES2015 version //

var instructor = {
    firstName: "Colt",
    sayHi(){
      return "Hi!";
    },
    sayBye(){
      return this.firstName + " says bye!";
    }
  }

// createAnimal function //

function createAnimal (species, verb, noise) {
    return {
        species,
        [verb](){
            return noise;
        }
    }
}
