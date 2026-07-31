/**
 * @return {Object}
 */
var createInfiniteObject = function() {
    return new Proxy({}, {
        get: function(target, property) {
            return function() {
                return property;
            };
        }
    });
};

function solve(method) {
    const object = createInfiniteObject();
    return object[method]();
}

module.exports = { createInfiniteObject, solve };
