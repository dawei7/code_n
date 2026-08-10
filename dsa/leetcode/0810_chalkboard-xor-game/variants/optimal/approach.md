## General

**Reduce the game to two facts**

At first glance, this looks like a game that needs recursive search over every possible number Alice or Bob might erase. The decisive information is much smaller:

- the bitwise XOR `S` of all numbers currently on the board;
- whether the number of remaining elements is even or odd.

The exact solution returns

`len(nums) % 2 == 0 or reduce(xor, nums) == 0`.

In words, Alice wins if the initial number of elements is even or if the initial XOR is zero. Understanding why this one-line condition is correct requires carefully respecting the unusual losing rule.

**An XOR of zero at the start is an immediate win**

The statement says that a player who starts a turn while the board's XOR is zero wins. Therefore, if the initial XOR is zero, Alice wins before erasing anything. This includes arrays with nonzero values that cancel under XOR, such as `[1, 2, 3]` because `1 ^ 2 ^ 3 = 0`.

This starting-turn rule is different from the rule for making a move. If a player erases a number and that erasure makes the remaining XOR zero, the player who made the move loses immediately. Thus, when the current XOR is nonzero, a “safe” move is one whose resulting XOR is still nonzero.

**How removing one number changes the XOR**

Let the current board contain `x_1, x_2, ..., x_k`, and let

$$
S=x_1\oplus x_2\oplus\cdots\oplus x_k.
$$

If the player erases `x_i`, the XOR of the remaining values is

$$
S\oplus x_i.
$$

This follows because XORing `S` with `x_i` cancels the erased value: `x_i \oplus x_i = 0`, and zero does not affect XOR.

The move loses immediately exactly when

$$
S\oplus x_i=0.
$$

When `S` is nonzero, this equation is equivalent to `x_i = S`. Consequently, a move is unsafe precisely when the erased value equals the current total XOR.

**Why an even-sized nonzero-XOR position always has a safe move**

Suppose the board contains an even number `k` of elements and its XOR `S` is nonzero. Assume, for contradiction, that every possible erasure loses. Then every element must equal `S`, because only removing `x_i = S` makes the remaining XOR zero.

But the XOR of an even number of identical values is zero: values cancel in pairs. The board's total XOR would therefore be

$$
\underbrace{S\oplus S\oplus\cdots\oplus S}_{k\text{ copies}}=0,
$$

contradicting the assumption that the current XOR is `S \ne 0`. The contradiction proves that at least one element differs from `S`. Removing that element leaves a nonzero XOR, so an even-sized nonzero position always offers a safe move.

This existence proof is enough. The implementation does not need to find or simulate the move because the question asks only which player wins under optimal play.

**Classifying every nonzero-XOR position by parity**

We can now classify game states:

- a nonzero-XOR state with an even number of elements is winning for the player whose turn it is;
- a nonzero-XOR state with an odd number of elements is losing for the player whose turn it is.

The reasoning can be made rigorous by induction on the number of elements.

For the smallest odd case, one nonzero element remains. Erasing it leaves the empty board, whose XOR is zero, so the player who erases it loses. Thus, a one-element nonzero state is losing.

Now take an even-sized nonzero state. The safe-move proof guarantees a move that leaves a nonzero XOR. Erasing one element changes the count from even to odd. By the parity classification for the smaller state, that odd nonzero position is losing for the opponent. Therefore, the current even state is winning.

Next take an odd-sized nonzero state. Any move has one of two outcomes:

- If it leaves XOR zero, the current player loses immediately under the move rule.
- If it leaves XOR nonzero, it leaves an even number of elements. That is a winning state for the opponent.

So an odd nonzero state has no winning move and is losing. These two arguments reinforce each other as the number of elements grows, establishing the classification for every size.

**Applying the classification to Alice**

Alice begins at the original array:

- If its XOR is zero, she wins immediately by the explicit starting-turn rule.
- Otherwise, if its length is even, she begins in an even nonzero state, which is winning.
- Otherwise, its length is odd and its XOR is nonzero, so she begins in a losing state.

This gives exactly the Boolean expression used by the solution. The length test appears first, so Python's short-circuit `or` avoids computing the XOR for even-length arrays. That optimization does not change the answer: even length alone has already proved Alice can force a win.

For `[1, 1, 2]`, the length is odd and the total XOR is `2`, which is nonzero, so the answer is `False`. For `[0, 1]`, the length is even, so Alice wins. One safe move is to erase `0`, leaving XOR `1` for Bob with one element. Bob must erase that last `1`, make the XOR zero, and lose. For `[1, 2, 3]`, the starting XOR is zero, so Alice wins immediately even though the length is odd.

**Why the actual values otherwise do not matter**

The numbers determine the initial XOR, but once that XOR is known to be nonzero, the win/loss classification depends only on parity. The safe-move contradiction works for any bit patterns and duplicates. There is no need to count individual values, sort the array, or identify a particular strategy sequence.

The proof also explains the empty-board convention. XOR of no elements is zero. If a player erases the last remaining nonzero number, that move produces zero and the mover loses immediately; the other player never needs to take a turn on the empty board.

## Complexity detail

Let `n` be the number of elements in `nums`.

For an odd-length array, `reduce(xor, nums)` combines all `n` values, so the time complexity is `O(n)`. Each XOR operation is constant time for the bounded integers in the problem. For an even-length array, short-circuit evaluation returns `True` after the parity test, using `O(1)` time. The worst-case time over all valid inputs remains `O(n)`, matching the manifest.

The reduction keeps only an accumulated XOR value and the next array element. The parity calculation also uses constant storage. No game tree, table, copied array, or recursion is created, so the auxiliary space complexity is `O(1)`.

The mathematical strategy is what removes the exponential factor. A direct game search could branch once for every remaining element at each turn, even though many branches share the same win/loss classification. Proving the parity theorem lets the implementation answer from one aggregate XOR and one length bit.

## Alternatives and edge cases

- **Minimax over erased subsets:** A recursive game search can model the rules directly, but there are up to `2^n` subsets of remaining elements. With `n` as large as 1000, even memoization by subset is impossible. The XOR/parity theorem gives the same optimal-play result in linear time.

- **Searching for Alice's actual first move:** When the length is even and XOR is nonzero, the proof guarantees a safe value exists. The function only needs a Boolean answer, so locating that value would add work without changing the result.

- **Using ordinary sum or parity of values:** Addition does not have XOR's cancellation property. Only the bitwise XOR aggregate determines whether an erasure immediately loses.

- **Starting XOR equals zero:** Alice wins immediately, regardless of whether the length is odd or even. She must not erase a number first; the game's special starting-turn rule has already ended the game in her favor.

- **Even length and nonzero XOR:** Alice can always remove some value that does not make the XOR zero. The contradiction using an even number of copies of `S` is the reason this guarantee holds.

- **Odd length and nonzero XOR:** Alice cannot force a win. An unsafe move loses immediately, while every safe move hands Bob an even nonzero state.

- **A single nonzero number:** The state has odd length and nonzero XOR. Removing the only value leaves XOR zero, so Alice loses, and the expression returns `False`.

- **A single zero:** The starting XOR is already zero, so Alice wins before moving. The expression's XOR branch returns `True`.

- **All values are zero:** The total XOR is zero for any length, so Alice wins immediately.

- **Duplicate values:** Duplicates cause no difficulty. XOR cancellation is already incorporated into `reduce(xor, nums)`, and the parity proof explicitly allows identical values.

- **Short-circuit behavior:** On even-length input, `reduce` is not evaluated because the first side of `or` is true. This is safe and can make that execution constant-time, but the advertised worst-case complexity is still linear.

- **No identity initializer for `reduce`:** The input is guaranteed nonempty, so `reduce(xor, nums)` always has a first element and cannot fail because of an empty sequence.

- **Bit width:** Values are below `2^{16}`, but the proof does not depend on a particular number of bits. XOR's associativity, commutativity, and self-cancellation are the only required properties.
