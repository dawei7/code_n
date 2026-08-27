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
