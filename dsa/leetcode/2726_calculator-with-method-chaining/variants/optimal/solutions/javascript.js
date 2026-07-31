class Calculator {
    constructor(value) {
        this.result = value;
    }

    add(value) {
        this.result += value;
        return this;
    }

    subtract(value) {
        this.result -= value;
        return this;
    }

    multiply(value) {
        this.result *= value;
        return this;
    }

    divide(value) {
        if (value === 0) throw new Error("Division by zero is not allowed");
        this.result /= value;
        return this;
    }

    power(value) {
        this.result **= value;
        return this;
    }

    getResult() {
        return this.result;
    }
}

function solve(actions, values) {
    const calculator = new Calculator(values[0]);
    let valueIndex = 1;
    try {
        for (let index = 1; index < actions.length; index += 1) {
            const action = actions[index];
            if (action === "getResult") return calculator.getResult();
            calculator[action](values[valueIndex]);
            valueIndex += 1;
        }
    } catch (error) {
        return error.message;
    }
}

module.exports = { Calculator, solve };
