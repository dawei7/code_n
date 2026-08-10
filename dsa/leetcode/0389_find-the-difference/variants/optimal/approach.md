## General

**Shuffling removes positional information**

String `t` contains every occurrence from `s`, plus exactly one new occurrence, but those characters may appear in any order. Comparing `s[i]` with `t[i]` is therefore meaningless: an ordinary character from `s` can move to a different position and look like a mismatch even though it is not the addition.

What shuffling preserves is frequency. For every character except the added one, `s` and `t` contain the same number of occurrences. For the added character, `t` contains exactly one more occurrence.

The exact solution turns this observation into inventory accounting. It creates `cnt = Counter(s)`, then scans `t`. Every `t` character consumes one matching occurrence from the inventory by executing `cnt[c] -= 1`. The first count that becomes negative identifies the extra occurrence and is returned.

**Why an added character may already exist in `s`**

The answer is not necessarily a character absent from `s`. For example, `s = "aab"` and `t = "abaa"` are valid: the extra letter is another `a`. A membership set would know only that `a` appears in both strings and would miss the difference.

Frequencies solve this correctly. The counter begins with `a: 2`. The first two `a` occurrences encountered in `t` reduce that supply to zero. The third reduces it to `-1`, revealing that this occurrence cannot be matched with any copy from `s`.

Thus, the method finds an extra occurrence, not merely a new distinct character.

**The inventory invariant**

After processing any prefix of `t`, for each character `c`, the counter value is

$$
\texttt{cnt}[c]
=
\operatorname{freq}_{s}(c)
-
\operatorname{freq}_{\text{processed prefix of }t}(c).
$$

Initially the processed prefix is empty, so `Counter(s)` establishes the equation. Processing one character subtracts one from exactly its entry, maintaining the equation.

A nonnegative count means the processed copies of that character can still be matched one-for-one with copies from `s`. A negative count means the prefix of `t` has used more copies than all of `s` contains. Under the contract, exactly one total occurrence in `t` is unmatched, so the character that first crosses below zero is precisely the added letter.

**Why default zero handles a completely new letter**

Python’s `Counter` behaves as though a missing key has count zero. If `s = "abcd"` and the scan reaches added character `e`, `cnt['e']` starts at zero. Decrementing makes it `-1`, and the method immediately returns `e`.

No separate test such as `if c not in cnt` is required. A never-seen character and an exhausted character represent the same resource state: there are zero unmatched copies left in `s`.

**Why the first negative count is safe to return**

For ordinary occurrences inherited from `s`, the total number appearing anywhere in `t` equals their supply in `s`. No prefix can contain more of such a character than the complete string `t`, so its running count cannot become negative.

For the added character, `t` has one more copy than `s`. Its first original-frequency copies can be matched, but the next one makes its count negative. That is the unique unmatched occurrence guaranteed by the construction of `t`.

The shuffled order affects when this crossing occurs, but not which character crosses. Once it happens, later input cannot change the identity of the added character, so returning immediately is correct.

**Tracing two cases**

For `s = "abcd"` and `t = "abcde"`, initial counts are one for `a`, `b`, `c`, and `d`. Scanning the first four characters reduces each matching count to zero. `e` has an implicit count of zero, which becomes `-1`, so the answer is `e`.

Now consider a more shuffled case, `s = "aabc"` and `t = "cbaaa"`. The inventory changes as follows:

| Scanned character | Count after decrement | Meaning |
|:---:|---:|---|
| `c` | `0` | the only original `c` is matched |
| `b` | `0` | the only original `b` is matched |
| `a` | `1` | one original `a` remains |
| `a` | `0` | both original `a` copies are matched |
| `a` | `-1` | this is the added occurrence |

The algorithm returns `a` even though `a` appeared in the original string.

For the minimum case `s = ""` and `t = "y"`, the counter is empty. Its default count for `y` is zero, the only decrement makes it negative, and `y` is returned.

**Why a return is guaranteed**

The exact source has no explicit return statement after the loop. That is safe only because the input contract guarantees that `t` is a shuffled copy of `s` plus exactly one extra character.

Summing all counter values conceptually starts at `len(s)`. Each of the `len(t) = len(s) + 1` decrements reduces the sum by one. If no individual entry ever became negative, all character demands would be at most their supplies, which is impossible after consuming one more total character than exists in `s`. Therefore some decrement must go below zero, and the method must return from inside the loop.

On malformed inputs that violate the relationship, Python could fall off the end and return `None`. Such validation is outside this problem’s guaranteed domain.

**A direct correctness proof**

Let `x` be the added character. For every character `c != x`, `freq_t(c) = freq_s(c)`. During any prefix scan, the number of `c` occurrences processed is no greater than its total in `t`, which equals its supply in `s`; hence `cnt[c]` never becomes negative.

For `x`, `freq_t(x) = freq_s(x) + 1`. When the scan reaches the last of those occurrences, the number processed exceeds the original supply, so `cnt[x]` becomes `-1`. Since no other character can become negative, the value returned at the first negative count is exactly `x`.

## Complexity detail

Let $n$ be the length of `s`; then `t` has length $n+1$.

Building `Counter(s)` scans $n$ characters. The second loop scans at most $n+1$ characters and performs one expected constant-time counter update and comparison per character. Total time is $O(n)$.

If $k$ is the number of distinct characters, the counter uses $O(k)$ entries. Both strings contain only lowercase English letters, so $k \le 26$ and auxiliary space is $O(1)$ under the fixed-alphabet model. For a generalized unbounded alphabet, the more precise space bound would be $O(k)$.

The method returns a single character and does not construct a reordered string or output collection.

## Alternatives and edge cases

- **Bitwise XOR:** XOR the character codes from both strings. Equal occurrences cancel because $x \mathbin{\oplus} x = 0$, leaving the extra code. This also achieves $O(n)$ time and $O(1)$ space and is elegant for this exact one-extra-item contract, but frequency counting is often easier for beginners to generalize and audit.

- **Sum character codes:** Subtract the code-point sum of `s` from that of `t`. The difference is the added character code. Python avoids overflow, but fixed-width languages may need a wider type; XOR avoids arithmetic overflow.

- **Sort both strings:** Sorting aligns matching characters so the first mismatch reveals the extra one, but costs $O(n\log n)$ time and $O(n)$ storage in Python.

- **Counter subtraction:** Build counters for both strings and subtract them. This is correct but stores a second frequency map and traverses its result; consuming one inventory uses less state.

- **Empty `s`:** The sole character in `t` immediately makes a default-zero count negative and is returned.

- **Extra character absent from `s`:** Its first occurrence makes an implicit zero count negative.

- **Extra character already frequent in `s`:** The method matches all original copies first; exactly one later copy crosses below zero.

- **Extra occurrence appears early in shuffled order:** The algorithm cannot label a physical occurrence as “the added one,” because equal copies are indistinguishable. It returns the correct character when cumulative demand first exceeds supply, which may occur anywhere in the scan.

- **All characters equal:** If `s = "aaa"` and `t = "aaaa"`, the fourth decrement returns `a`.

- **Contract dependence:** The missing post-loop return is justified only by exactly one extra occurrence and no removals or substitutions. A more general string-difference problem would need different validation and possibly multiple results.

- **Fixed-alphabet space:** The $O(1)$ statement depends on the lowercase-English guarantee. The same code works for broader characters, but the counter could then grow with the input.
