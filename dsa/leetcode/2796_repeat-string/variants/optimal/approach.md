## General

**Represent the repetition count in binary**

Appending the receiver once per copy performs $n$ concatenations. Instead, maintain a `block` that initially contains one copy of the receiver. After each doubling, `block` represents $2$, $4$, $8$, and then higher powers of two copies. At the same time, inspect the least significant bit of `times`. When that bit is $1$, append the current block to `result`; that selects the corresponding power of two in the binary decomposition of $n$.

After processing a bit, replace `times` by `Math.floor(times / 2)`. The loop therefore visits exactly the significant bits of the count. For example, $13 = 8 + 4 + 1$, so the selected blocks contain one, four, and eight receiver copies. Their concatenation contains exactly thirteen copies.

**Preserve order while doubling**

Every block is formed as `block + block`, so it remains consecutive copies of the original receiver. Appending selected blocks to the end of `result` cannot change their characters or introduce separators. When the loop finishes, all and only the set-bit contributions have been selected, and their copy counts sum to the original `times`. This proves that the returned string is the receiver repeated exactly $n$ times.

The prototype method converts its receiver with `String(this)` so the computation uses the primitive string value even though JavaScript may box a primitive receiver during method dispatch. It never calls the prohibited built-in `repeat` method.

## Complexity detail

Let $m$ be the receiver length and $n$ be `times`. Under the problem's stated assumption that concatenation costs $O(1)$, halving `times` on every iteration gives $O(\log n)$ time. The result contains exactly $mn$ characters, so its output storage is $O(mn)$; aside from the returned string and constructed blocks, the algorithm keeps only a fixed number of variables.

The asymptotic-optimality certificate reflects that special unit-cost model instead of benchmarking native JavaScript allocation. Starting from one copy, a concatenation can at most double the number of copies represented by a constructed block, so producing $n$ copies requires $\Omega(\log n)$ such operations. Binary doubling matches that bound.

## Alternatives and edge cases

- **Built-in `String.prototype.repeat`:** It directly provides the requested value but is explicitly forbidden.
- **Linear concatenation loop:** Appending the receiver `times` times is straightforward but takes $O(n)$ concatenations under the problem's model.
- **Recursive divide and conquer:** Repeating half the count and doubling it has the same logarithmic idea, but recursion adds call-stack overhead and needs careful handling of odd counts.
- A repetition count of one selects the initial block and returns the receiver unchanged.
- Powers of two select a single doubled block after earlier zero bits, while other counts combine several blocks.
- Spaces, punctuation, and repeated characters are ordinary string content and must remain byte-for-byte in every copy.
- The largest allowed count still requires only $O(\log n)$ loop iterations, although the returned value necessarily contains all $mn$ output characters.
