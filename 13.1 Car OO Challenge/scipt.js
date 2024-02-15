// Part 1

class Vehicle {
    constructor(make, model, year){
        this.make = make;
        this.model = model;
        this.year = year;
    };
    honk(){
        return "Beep Beep"
    };
    toString(){
        const {make, model, year} = this;
        return `This vehicle is a ${make} ${model} from ${year}!`
    }
}

// Part 2

class Car extends Vehicle {
    constructor(make, model, year){
        super(make, model, year);
        this.numWheels = 4;
    };
}

class Motercycle extends Vehicle {
    constructor(make, model, year){
        super(make, model, year);
        this.numWheels = 2;
    };
    revEngine(){
        return "VROOOM!"
    }
}

class Garage {
    constructor(capacity){
        this.capacity = capacity;
        this.vehicles = [];
    }
    add(vehicle){
        if (!(vehicle instanceof Vehicle)){
            return "No Papi, Vehicles Only in Here!"
        }
        if (this.vehicles.length >= this.capacity){
            return "No Papi, We at Capacity. No More!"
        }
        this.vehicles.push(vehicle)
        return "Added!"
    }
}