function invertObject(obj) {
    const inverted = new Map();

    for (const [key, value] of Object.entries(obj)) {
        if (!inverted.has(value)) {
            inverted.set(value, key);
            continue;
        }

        const previous = inverted.get(value);
        if (Array.isArray(previous)) {
            previous.push(key);
        } else {
            inverted.set(value, [previous, key]);
        }
    }

    return Object.fromEntries(inverted);
}

function solve(obj) {
    return invertObject(obj);
}

module.exports = { invertObject, solve };
