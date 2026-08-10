## General

**Understand what makes one string lexicographically smaller.** Compare two equal-length strings from left to right. The first position where they differ decides which string is smaller. A smaller digit at that earliest differing position wins, regardless of every later character.

One adjacent swap at indices $i$ and $i+1$ changes no position before $i$. At position $i$, it replaces `s[i]` by `s[i+1]`. Such a swap improves the string only when the right digit is smaller:

$$
s[i]>s[i+1].
$$

If the pair is already increasing, swapping makes the string larger. If the digits are equal, swapping changes nothing.

**Check the parity rule through character codes.** The source maps every character to `ord` and receives adjacent code pairs `a,b` from `pairwise`. Decimal digit code points are consecutive: `ord("0")=48`, `ord("1")=49`, and so on. Because $48$ is even, a digit's code has the same parity as the digit itself.

Two integers have equal parity exactly when their sum is even. Therefore

`(a + b) % 2 == 0`

correctly tests that both adjacent digits are even or both are odd. Code-point comparison `a > b` also matches digit comparison because character codes increase from zero through nine.

**Swap the first legal inversion.** The loop scans adjacent pairs from left to right. It returns immediately when it finds a pair that:

1. has equal parity and is therefore legal to swap;
2. is descending, so the swap places a smaller digit first.

The returned expression

`s[:i] + s[i + 1] + s[i] + s[i + 2:]`

keeps the prefix before `i`, writes the two digits in reverse order, and keeps the suffix after them. It creates a new string because Python strings are immutable.

**Why the earliest improving swap is globally best.** Suppose the algorithm finds its first legal inversion at index `i`. Its result agrees with the original string before `i` and has the smaller digit `s[i+1]` at `i`.

Any legal swap at an index greater than `i` leaves the original digit `s[i]` at position `i`. Since `s[i+1] < s[i]`, the algorithm's result is lexicographically smaller immediately at that position, no matter what the later swap does.

What about an earlier index? The scan already examined every earlier adjacent pair. If one was not parity-compatible, it could not be swapped. If it had equal parity but was increasing, swapping would place a larger digit at the earliest changed position and make the string worse than leaving it alone. If equal, its swap would not change the string and would waste the at-most-one opportunity. Therefore no earlier legal choice can beat the algorithm.

This proves the first same-parity inversion gives the lexicographically smallest obtainable string.

**Why no swap is sometimes optimal.** If the scan finishes without returning, every legal adjacent pair is already nondecreasing. Any legal unequal swap would move a larger digit left and increase the string; any equal swap would leave it unchanged. Because the operation is allowed at most once rather than exactly once, returning the original `s` is optimal.

**Trace `"45320"`.** Pair `"45"` has different parity, so it cannot be swapped. Pair `"53"` contains two odd digits and is descending. Swapping it produces `"43520"`. Even if a later legal inversion existed, it could not beat the smaller digit $3$ now placed at index one.

For `"001"`, pair `"00"` is parity-compatible but equal, so `a > b` is false. Pair `"01"` has different parity. No improving legal swap exists, and the original is returned.

**Lazy adjacent iteration.** `map(ord, s)` produces code points lazily, and `pairwise` yields consecutive overlapping pairs without allocating a separate pair list. The loop stops as soon as the optimal swap is identified.

## Complexity detail

Let $n$ be string length. At most $n-1$ adjacent pairs are examined, with constant work per pair, so time is $O(n)$. If a swap occurs, slicing and concatenating the $n$ output characters also takes $O(n)$; the total remains linear.

The newly returned swapped string and intermediate slice/concatenation objects use $O(n)$ memory in the worst case. The lazy iterators themselves use constant state. If no swap occurs, the method can return the original immutable string object, but worst-case auxiliary/output allocation is $O(n)$ as stated in the manifest.

## Alternatives and edge cases

- **Convert to a character list:** Scan adjacent digits, swap the first legal inversion in place, and join. It is often easier to read but always allocates an $O(n)$ list.
- **Try every legal swap and take `min`:** Correct for $n\le100$, but it constructs up to $O(n)$ strings of length $n$, costing $O(n^2)$ time and space traffic.
- **Swap the largest difference:** Incorrect. Lexicographic order prioritizes the earliest changed index, not the magnitude of a later improvement.
- **Different parity:** The pair cannot be swapped even when it is descending.
- **Equal digits:** They have the same parity, but swapping has no effect and is unnecessary.
- **Already optimal:** Returning `s` is valid because the operation is optional.
- **First pair is a legal inversion:** It is immediately optimal; no later position can compete with improving index zero.
- **Leading zeros:** They are ordinary string digits. Moving a zero left can make the result smaller, and no numeric conversion should remove it.
- **Two-character string:** There is one pair; it is swapped exactly when parity matches and it descends.
- **Character-code parity:** The trick relies on consecutive decimal digit code points. It should not be generalized blindly to arbitrary characters.
- **`pairwise` availability:** The exact source assumes an environment providing Python's adjacent-pair iterator and `map`/`ord` built-ins.
- **Input preservation:** Strings are immutable, so the original value is never modified.
