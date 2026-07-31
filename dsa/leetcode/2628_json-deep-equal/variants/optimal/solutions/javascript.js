function areDeeplyEqual(o1, o2) {
    if (o1 === o2) return true;
    if (o1 === null || o2 === null || typeof o1 !== 'object' || typeof o2 !== 'object') {
        return false;
    }

    const firstIsArray = Array.isArray(o1);
    if (firstIsArray !== Array.isArray(o2)) return false;

    if (firstIsArray) {
        if (o1.length !== o2.length) return false;
        for (let index = 0; index < o1.length; index += 1) {
            if (!areDeeplyEqual(o1[index], o2[index])) return false;
        }
        return true;
    }

    const keys = Object.keys(o1);
    if (keys.length !== Object.keys(o2).length) return false;
    for (const key of keys) {
        if (!Object.prototype.hasOwnProperty.call(o2, key) || !areDeeplyEqual(o1[key], o2[key])) {
            return false;
        }
    }
    return true;
}

function solve(o1, o2) {
    return areDeeplyEqual(o1, o2);
}

module.exports = { areDeeplyEqual, solve };
