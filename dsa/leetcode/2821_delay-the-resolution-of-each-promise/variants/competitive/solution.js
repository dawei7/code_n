/**
 * @param {Array<Function>} functions
 * @param {number} ms
 * @return {Array<Function>}
 */
var delayAll = function(functions, ms) {
    return functions.map((fn) => () =>
        fn().then(
            (value) =>
                new Promise((resolve) => {
                    setTimeout(() => resolve(value), ms);
                }),
            (reason) =>
                new Promise((_, reject) => {
                    setTimeout(() => reject(reason), ms);
                })
        )
    );
};
