## General

**Count valid substrings by where they end**

Every all-ones substring has a unique ending position. The stored solution tracks `cur`, the length of the current consecutive run of ones ending at the character being processed.

If the current character is zero, no all-ones substring can end there, and the run is broken, so `cur` becomes zero.

If the character is one, it extends the preceding run, so `cur` increases by one. Exactly `cur` valid substrings end at this position: the one-character suffix, the two-character suffix if available, and every longer suffix through the entire current run.

The source adds this `cur` contribution to `ans` immediately and reduces modulo $10^9+7$.

**A direct example**

For a run `111`:

- At the first one, `cur = 1`, counting `1`.
- At the second, `cur = 2`, counting the suffixes `1` and `11` ending there.
- At the third, `cur = 3`, counting `1`, `11`, and `111` ending there.

The run contributes one plus two plus three, which is six. When a zero follows, resetting `cur` prevents a later one from forming a substring across that zero.

For `0110111`, the first run has length two and contributes three. The second run has length three and contributes six. The total is nine.

**The invariant**

After processing a prefix of `s`:

1. `cur` equals the number of consecutive ones at the end of that prefix.
2. `ans` equals the number of all-ones substrings contained in the prefix, modulo the required modulus.

The empty prefix has both values zero. If the next character is zero, the suffix run becomes empty and no new valid substring ends there. If it is one, every valid new substring must be a suffix consisting of that character plus zero or more of the immediately preceding consecutive ones. There are exactly the new `cur` of those.

Adding that amount preserves the answer invariant. Induction proves correctness for the full string.

**Why this matches the triangular-number view**

A maximal run of $L$ ones contains

$$
1+2+\cdots+L
=
\frac{L(L+1)}{2}
$$

all-ones substrings. The online method adds the same sequence as the run is read. It avoids waiting for a zero or handling a final unfinished run after the loop.

Both interpretations are correct. Counting by endpoints is especially convenient because every iteration performs the entire update needed for that character.

**Why every substring is counted once**

Take any valid substring. Its final character is one, and its start lies within the consecutive-one run ending there. It is one of the `cur` suffixes counted at that final index.

No other iteration counts it because no other character is its endpoint. Conversely, every suffix counted by `cur` contains only ones by the definition of the current run. Thus the counting is exact.

**Modulo during accumulation**

The actual number of substrings can be quadratic in string length. The source reduces `ans` after each addition, keeping it bounded. Modular addition preserves the final remainder.

`cur` itself is not reduced because it represents a real run length needed for the next step. With a maximum length of one hundred thousand, it remains small anyway.

The distinction between substrings and subsequences is important here. A substring must occupy consecutive indices, which is why only the uninterrupted suffix run matters. Ones occurring before a zero cannot be combined with ones after it. A subsequence-counting method would allow such gaps and would produce a much larger, incorrect answer for this contract.

## Complexity detail

Let $N$ be the string length. The loop visits each character once and performs constant work, so time is $O(N)$.

Only `mod`, `ans`, `cur`, and the current character are stored. Auxiliary space is $O(1)$, matching the manifest.

The algorithm never builds substrings. Python string iteration yields existing characters, and all arithmetic values remain bounded enough for efficient integer operations. Even without intermediate modulo, the maximum count is $N(N+1)/2$, but reducing online follows the contract directly.

## Alternatives and edge cases

- **Run-at-a-time triangular formula:** Measure each maximal run and add `L * (L + 1) // 2` when it ends. It has the same bounds but needs a final post-loop addition.
- **Enumerate every substring:** Checking each candidate is quadratic or cubic and unnecessary.
- **Dynamic programming array:** Store the count of valid suffixes for every index. It reproduces `cur` but wastes $O(N)$ space because only the previous value matters.
- **All zeros:** `cur` repeatedly resets and the result is zero.
- **All ones:** Contributions one through N sum to $N(N+1)/2$ modulo the required value.
- **Alternating characters:** Every one contributes exactly one single-character substring.
- **One-character string:** One returns one, while zero returns zero.
- **Zero between runs:** Resetting prevents invalid substrings from crossing it.
- **Modulo placement:** Reducing the accumulated answer is safe; reducing or changing the run length would obscure its meaning.
- **Nonempty substrings:** Every contribution has an endpoint and positive length, so the empty string is never counted.
