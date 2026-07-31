/**
 * @param {Array} arr
 * @return {(string | number | boolean | null)[][]}
 */
var jsonToMatrix = function(arr) {
    const rows = arr.map((item) => {
        const flattened = {};

        const visit = (value, path) => {
            if (value !== null && typeof value === "object") {
                for (const [key, child] of Object.entries(value)) {
                    const childPath = path === "" ? key : path + "." + key;
                    visit(child, childPath);
                }
            } else {
                flattened[path] = value;
            }
        };

        visit(item, "");
        return flattened;
    });

    const columns = [...new Set(rows.flatMap((row) => Object.keys(row)))].sort();
    const matrix = [columns];

    for (const row of rows) {
        matrix.push(columns.map((column) =>
            Object.prototype.hasOwnProperty.call(row, column) ? row[column] : ""
        ));
    }

    return matrix;
};

function solve(arr) {
    return jsonToMatrix(arr);
}

class Solution {
    solve(arr) {
        return jsonToMatrix(arr);
    }
}

module.exports = { jsonToMatrix, solve };
