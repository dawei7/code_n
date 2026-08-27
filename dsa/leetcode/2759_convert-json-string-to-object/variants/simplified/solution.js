/**
 * @param {string} str
 * @return {null|boolean|number|string|Array|Object}
 */
var jsonParse = function(str) {
    let index = 0;

    const skipWhitespace = () => {
        while (index < str.length && " \n\r\t".includes(str[index])) {
            index++;
        }
    };

    const parseString = () => {
        index++;
        const start = index;
        while (str[index] !== '"') {
            index++;
        }
        const value = str.slice(start, index);
        index++;
        return value;
    };

    const parseNumber = () => {
        const start = index;
        if (str[index] === '-') index++;
        if (str[index] === '0') {
            index++;
        } else {
            while (index < str.length && str[index] >= '0' && str[index] <= '9') {
                index++;
            }
        }
        if (str[index] === '.') {
            index++;
            while (index < str.length && str[index] >= '0' && str[index] <= '9') {
                index++;
            }
        }
        if (str[index] === 'e' || str[index] === 'E') {
            index++;
            if (str[index] === '+' || str[index] === '-') index++;
            while (index < str.length && str[index] >= '0' && str[index] <= '9') {
                index++;
            }
        }
        return Number(str.slice(start, index));
    };

    const parseValue = () => {
        skipWhitespace();
        const token = str[index];

        if (token === '"') return parseString();
        if (token === '[') return parseArray();
        if (token === '{') return parseObject();
        if (str.startsWith('true', index)) {
            index += 4;
            return true;
        }
        if (str.startsWith('false', index)) {
            index += 5;
            return false;
        }
        if (str.startsWith('null', index)) {
            index += 4;
            return null;
        }
        return parseNumber();
    };

    const parseArray = () => {
        const result = [];
        index++;
        skipWhitespace();
        if (str[index] === ']') {
            index++;
            return result;
        }

        while (true) {
            result.push(parseValue());
            skipWhitespace();
            if (str[index] === ']') {
                index++;
                return result;
            }
            index++;
        }
    };

    const parseObject = () => {
        const result = {};
        index++;
        skipWhitespace();
        if (str[index] === '}') {
            index++;
            return result;
        }

        while (true) {
            skipWhitespace();
            const key = parseString();
            skipWhitespace();
            index++;
            const value = parseValue();
            Object.defineProperty(result, key, {
                value,
                writable: true,
                enumerable: true,
                configurable: true,
            });
            skipWhitespace();
            if (str[index] === '}') {
                index++;
                return result;
            }
            index++;
        }
    };

    return parseValue();
};
