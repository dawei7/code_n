## General

**Classify positions rather than simulate one particular game**

A game position is the number currently written on the board together with the fact that it is the current player's turn. A winning position has at least one legal move to a losing position. A losing position has no legal move, or every legal move gives the opponent a winning position.

The players' names do not affect this classification. Alice wins exactly when the initial value `n` is a winning position because she moves first.

The exact solution returns `n % 2 == 0`. This one-line test is justified by a complete parity theorem:

- Every positive even value is a winning position.
- Every positive odd value is a losing position.

The proof depends on how divisors behave under parity and on the fact that every move strictly decreases the board value.

**Why odd positions can move only to even positions**

Suppose `n` is odd and `x` is a legal divisor. A divisor of an odd integer must also be odd. If `x` were even, then `n = xq` would contain a factor of two and would be even, contradicting the assumption.

The next board value is `n - x`. Odd minus odd is even. Therefore, every legal move from an odd position hands the opponent an even position. The player cannot choose a special even divisor to stay on odd parity because no even divisor exists.

For an odd prime, the only proper positive divisor is one, so the forced next value is `n - 1`. For an odd composite, more choices may exist, but all of them are odd and all still lead to an even value.

**Why an even position always has a move to an odd position**

Every positive integer is divisible by one. For every even `n` in the input domain, `n >= 2`, so `x = 1` also satisfies `0 < x < n`. It is always a legal move.

Subtracting one from an even number produces an odd number. Thus a player at any even position can deliberately hand the opponent an odd position. The player does not need to search for a larger divisor; the universal divisor one is enough to establish a winning strategy.

**The base case**

At `n = 1`, there is no integer `x` satisfying `0 < x < 1`. The current player cannot move and loses immediately. One is odd, so this terminal case agrees with the claimed classification.

The game cannot reach zero through a legal move because `x` must be strictly smaller than `n`. The smallest reachable board value is one, which is the natural terminal state.

**A strong induction proof**

Assume the parity classification is correct for every positive value smaller than some `n`.

If `n` is even, choose `x = 1`. The resulting value `n - 1` is a smaller odd number. By the induction assumption, it is losing for the opponent. Therefore, the current even position is winning.

If `n` is odd, every legal divisor `x` is odd, so every resulting value `n - x` is a smaller even number. By the induction assumption, each such position is winning for the opponent. Since there is no move to a losing position, the current odd position is losing.

The base value one starts the induction. Because every move subtracts a positive number, every successor is smaller, so the induction covers the entire game graph. The theorem is not based on observing a few examples; it proves the outcome for every allowed `n`.

**How optimal play follows from the proof**

When Alice starts with even `n`, she chooses one. Bob receives an odd value. Whatever legal divisor Bob chooses, he must return an even value to Alice. Alice again chooses one and returns an odd value. This pattern continues until Bob receives one and has no move.

Alice does not need to predict Bob's composite-divisor choices. The invariant is enough: every Bob turn begins odd, every Bob move ends even, and Alice can always restore odd parity with `x = 1`.

When Alice starts with odd `n`, she cannot establish that invariant for herself. Every move she makes gives Bob an even value. Bob can then use the same choose-one strategy and ensure that Alice receives odd values thereafter. Under optimal play, Alice must lose.

**Small examples**

For `n = 2`, Alice chooses `x = 1` and leaves one. Bob has no legal move, so Alice wins.

For `n = 3`, Alice's only legal divisor is one, leaving two. Bob chooses one and leaves one to Alice, who loses.

For `n = 6`, Alice could choose one, two, or three. Choosing one is the proven move: it leaves odd five, a losing position. Choosing two would leave even four and unnecessarily give Bob a winning position. The theorem identifies existence of an optimal move, not that every move from an even value wins.

For `n = 9`, Alice may choose one or three. Both are odd, so the results eight and six are even. Each is winning for Bob, and Alice cannot avoid defeat.

**Why the code is exactly the theorem**

In Python, `n % 2` is zero exactly when `n` is even. The comparison `n % 2 == 0` directly produces a Boolean: `True` for winning even positions and `False` for losing odd positions.

No game state, divisor list, recursion, or table is needed after proving the classification. The mathematical proof compresses the entire optimal-play analysis into one parity test.

## Complexity detail

The method performs one remainder operation and one equality comparison. Under the problem's bounded integer model, both are constant-time operations, so time complexity is `O(1)`.

It stores no collection, recursion stack, or dynamic-programming table. The parameter and temporary arithmetic result require constant storage, so space complexity is `O(1)`. Both bounds match the manifest.

This is asymptotically and practically better than exploring moves. The improvement does not come from a faster divisor-enumeration technique; it comes from proving that divisor identities beyond parity are irrelevant to the win-or-lose result.

## Alternatives and edge cases

- **Bottom-up dynamic programming:** Mark one as losing, then for each larger value search its proper divisors for a move to a losing state. This reconstructs the same pattern but takes substantially more than constant time.
- **Recursive minimax:** Try every legal divisor and recursively ask whether the opponent loses. Memoization prevents repeated states, but divisor discovery and recursion are unnecessary once the parity theorem is known.
- **Enumerate divisors only up to the square root:** This accelerates move generation compared with checking all smaller integers, yet still solves a harder subproblem than required.
- **Always choose one without checking parity:** One is always a legal divisor when `n > 1`, but the strategy is winning only from even values. From an odd value it hands the opponent an even winning position.
- **Even composite choices:** An even position may have moves other than one, and some can be losing choices. The proof needs only the existence of `x = 1` leading to an odd losing state.
- **Odd composite values:** Extra divisors do not help because every divisor of an odd number remains odd, and every move still produces an even winning state.
- **The terminal value one:** It is odd, has no proper positive divisor, and correctly returns `False`.
- **The smallest winning value two:** One is a legal proper divisor, and the result is the terminal losing value one.
- **Upper constraint:** The same parity proof works for values far beyond 1000. The stated upper bound has no effect on the algorithm.
- **Zero is outside the domain:** The expression would label zero even, but the game contract starts at a positive integer. No claim is needed for an invalid zero position.
- **Optimal-play assumption:** The return value describes whether Alice has a forced win. On an even value, she could choose a bad divisor, but optimal play means she uses the guaranteed move to an odd state.
- **Strict divisor condition:** The rule `x < n` prevents choosing `x = n` and jumping to zero. The proof uses only `x = 1` for even values, which always satisfies the strict condition.
