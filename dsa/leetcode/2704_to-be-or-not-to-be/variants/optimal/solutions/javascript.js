/**
 * @param {string} val
 * @return {Object}
 */
var expect = function(val) {
    return {
        toBe(other) {
            if (val !== other) {
                throw new Error("Not Equal");
            }
            return true;
        },
        notToBe(other) {
            if (val === other) {
                throw new Error("Equal");
            }
            return true;
        }
    };
};

function solve(val, method, other) {
    try {
        return { value: expect(val)[method](other), error: null };
    } catch (error) {
        return { value: null, error: error.message };
    }
}

module.exports = { expect, solve };
