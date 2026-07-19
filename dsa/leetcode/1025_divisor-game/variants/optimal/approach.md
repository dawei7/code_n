## General
**Classify positions by parity:** The number `1` is losing because it has no positive divisor smaller than itself. More generally, every odd divisor of an odd number is odd. Subtracting any valid divisor from an odd `n` therefore produces an even number.

**Give every even position a winning move:** For every even `n > 1`, `1` is a valid divisor. Subtracting it produces the odd number `n - 1`. Thus an even position can always hand the opponent an odd position.

Starting from the losing odd base case `1`, these two observations inductively classify every positive integer: odd positions can move only to even winning positions, while even positions can move to an odd losing position. Alice wins exactly when the initial `n` is even, so testing `n % 2 == 0` is sufficient.

## Complexity detail
The algorithm performs one parity test regardless of the value of `n`, so it takes $O(1)$ time and $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Bottom-up game-state dynamic programming:** Mark a number winning if it has a divisor leading to a losing smaller state. This directly models optimal play but costs up to $O(n^2)$ time with a simple divisor scan and $O(n)$ space.
- **Recursive minimax with memoization:** Explore legal subtractions until a losing reply is found. Memoization avoids repeated states, but divisor enumeration is unnecessary once the parity structure is proved.
- **Smallest input:** At `n = 1`, Alice has no legal choice and loses.
- **Even boundary:** At `n = 2`, subtracting `1` wins immediately.
- **Optimal-play requirement:** The result asks whether a forced win exists, not whether every legal first move wins.
