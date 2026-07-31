def solve(numBottles, numExchange):
    return numBottles + (numBottles - 1) // (numExchange - 1)
