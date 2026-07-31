function undefinedToNull(obj) {
    const stack = [obj];

    while (stack.length > 0) {
        const current = stack.pop();

        for (const key of Object.keys(current)) {
            const value = current[key];
            if (value === undefined) {
                current[key] = null;
            } else if (value !== null && typeof value === 'object') {
                stack.push(value);
            }
        }
    }

    return obj;
}

function buildInput(value, undefinedPaths, objectPlan) {
    if (objectPlan?.kind === 'wideUndefined') {
        const obj = {};
        for (let i = 0; i < objectPlan.count; i += 1) {
            obj[`k${i}`] = undefined;
        }
        return obj;
    }

    const obj = JSON.parse(JSON.stringify(value));
    for (const path of undefinedPaths) {
        let current = obj;
        for (let i = 0; i + 1 < path.length; i += 1) {
            current = current[path[i]];
        }
        current[path[path.length - 1]] = undefined;
    }
    return obj;
}

function summarize(result, objectPlan) {
    const keys = Object.keys(result);
    let nullCount = 0;
    for (const key of keys) {
        if (result[key] === null) nullCount += 1;
    }
    return {
        keyCount: keys.length,
        nullCount,
        lastValue: result[`k${objectPlan.count - 1}`],
    };
}

function solve(value, undefinedPaths, objectPlan) {
    const result = undefinedToNull(buildInput(value, undefinedPaths, objectPlan));
    return objectPlan === null ? result : summarize(result, objectPlan);
}

module.exports = { buildInput, solve, summarize, undefinedToNull };
