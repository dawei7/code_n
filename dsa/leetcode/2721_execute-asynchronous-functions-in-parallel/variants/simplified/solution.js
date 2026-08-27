/**
 * @param {Array<Function>} functions
 * @return {Promise<any>}
 */
var promiseAll = function(functions) {
    return new Promise((resolve, reject) => {
        const results = new Array(functions.length);
        let completed = 0;

        functions.forEach((fn, index) => {
            fn().then((value) => {
                results[index] = value;
                completed += 1;
                if (completed === functions.length) resolve(results);
            }).catch(reject);
        });
    });
};
