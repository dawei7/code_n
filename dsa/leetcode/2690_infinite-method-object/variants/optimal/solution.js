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
