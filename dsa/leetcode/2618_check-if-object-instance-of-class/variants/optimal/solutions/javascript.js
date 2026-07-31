/**
 * @param {*} obj
 * @param {*} classFunction
 * @return {boolean}
 */
var checkIfInstanceOf = function(obj, classFunction) {
    if (obj == null || typeof classFunction !== "function") {
        return false;
    }

    let prototype = Object.getPrototypeOf(Object(obj));
    const target = classFunction.prototype;
    while (prototype !== null) {
        if (prototype === target) {
            return true;
        }
        prototype = Object.getPrototypeOf(prototype);
    }
    return false;
};

/**
 * checkIfInstanceOf(new Date(), Date); // true
 */

class Animal {}
class Dog extends Animal {}

function resolveFixture(fixture) {
    const targets = {
        Animal,
        Array,
        Date,
        Number,
        Object,
        Symbol,
        undefined: undefined,
    };

    if (fixture.value === "deep-instance") {
        function Root() {}
        let prototype = Root.prototype;
        for (let index = 0; index < fixture.depth; index += 1) {
            prototype = Object.create(prototype);
        }
        const obj = Object.create(prototype);
        return [obj, fixture.target === "Root" ? Root : targets[fixture.target]];
    }

    const values = {
        array: [],
        "date-instance": new Date(0),
        "Date-constructor": Date,
        "dog-instance": new Dog(),
        null: null,
        "null-prototype-object": Object.create(null),
        "number-primitive": 5,
        "plain-object": {},
        "symbol-primitive": Symbol("fixture"),
    };
    return [values[fixture.value], targets[fixture.target]];
}

function solve(fixture) {
    const [obj, classFunction] = resolveFixture(fixture);
    return checkIfInstanceOf(obj, classFunction);
}

module.exports = { checkIfInstanceOf, solve };
