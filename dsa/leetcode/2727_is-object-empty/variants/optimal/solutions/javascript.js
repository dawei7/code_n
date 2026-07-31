function isEmpty(obj) {
    for (const key in obj) return false;
    return true;
}

function solve(obj) {
    return isEmpty(obj);
}

module.exports = { isEmpty, solve };
