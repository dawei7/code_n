## General

Two strings are anagrams exactly when they contain the same characters with the same multiplicities. Their order is irrelevant: `anagram` and `nagaram` place letters differently, but both contain three `a` characters and one each of `n`, `g`, `r`, and `m`. The problem is therefore a frequency-comparison problem rather than a positional string-comparison problem.

The exact solution builds `Counter(s)`, which maps each distinct character in `s` to the number of copies still available. It then consumes those copies while scanning `t`. If `t` ever asks for a character whose remaining count has fallen below zero, `t` contains more copies of that character than `s`, so the strings cannot be anagrams.

**Reject unequal lengths first**

An anagram is a rearrangement, and rearranging cannot change the number of characters. If `len(s) != len(t)`, the answer is immediately `False`. This check is both a quick rejection and an important part of the later proof: after equal numbers of increments and decrements, a “no count went negative” result is enough to conclude that every count ended at zero.

Without equal lengths, merely checking for negative counts while consuming `t` would handle the case where `t` is longer, but it could wrongly accept a shorter `t`. For example, with `s = "abc"` and `t = "ab"`, no counter becomes negative, yet one unused `c` remains. The initial length comparison rules out that situation.

**Treat the counter as an inventory**

After `cnt = Counter(s)`, `cnt[c]` is the inventory of character `c` supplied by `s`. For every character `c` in `t`, the algorithm performs `cnt[c] -= 1`, meaning one occurrence in `t` has been matched against one occurrence in `s`.

Python's `Counter` returns a zero count for a missing key. Thus, if `t` contains a character absent from `s`, its first decrement changes that implicit zero to `-1`, and the algorithm rejects immediately. No separate “does this key exist?” condition is needed.

More generally, after the first `r` characters of `t` have been processed,

$$
\text{cnt}[c]
=
\operatorname{freq}_s(c)
-
\operatorname{freq}_{t[0:r]}(c).
$$

A negative value means the processed prefix of `t` already contains more copies of `c` than the whole of `s`. Later characters cannot repair that shortage: the loop only subtracts counts and never adds them. Returning `False` at the first negative value is therefore safe.

**Why no final counter scan is necessary**

At first, it may seem that the function should verify that all counts are zero after scanning `t`. Equal lengths make that extra scan unnecessary.

Initially, the sum of all counts is `len(s)`. Each of the `len(t)` loop iterations subtracts exactly one from one entry. Since the lengths are equal, the final sum of all counts is zero. The early-exit rule also guarantees that every final count is nonnegative. A collection of nonnegative integers can sum to zero only when every integer is zero. Therefore, if the loop finishes without finding a negative count, every occurrence from `s` was matched exactly once and the function may return `True`.

The same fact can be viewed through contradiction. Suppose a positive count remained for some character from `s`. Because both strings have the same total length, some other character would have to be overused by `t` to compensate. That other counter would become negative, and the loop would already have returned `False`. Hence a leftover positive count cannot coexist with equal lengths and no negative count.

**Trace for an anagram**

For `s = "anagram"`, the initial relevant counts are `a: 3`, `n: 1`, `g: 1`, `r: 1`, and `m: 1`. Scanning `t = "nagaram"` consumes these inventories in its own order:

- `n` falls from `1` to `0`;
- the three appearances of `a` gradually take `a` from `3` to `0`;
- `g`, `r`, and `m` each fall from `1` to `0`.

No count becomes negative. Seven characters were supplied and seven were consumed, so all counts end at zero and the function returns `True`.

For `s = "rat"` and `t = "car"`, the initial count for `c` is zero. Processing the first character of `t` makes it `-1`, immediately proving that `t` cannot be formed by rearranging `s`.

**Why order does not enter the state**

Once the frequencies are known, original positions provide no further information relevant to anagrams. The counter intentionally collapses all occurrences of the same character into one number. This is exactly enough information: identical frequency functions imply that one string's characters can be permuted to form the other, while any differing frequency makes such a permutation impossible.

**Exact source versus the manifest wording**

The manifest describes a fixed 26-entry array balanced in one pass. The protected Python source instead constructs a general-purpose hash-based `Counter` from all of `s`, then scans `t`. Both methods implement the same frequency invariant and both are constant-space under the stated lowercase-English alphabet. The approach must nevertheless describe `Counter`, because that is the data structure the exact solution actually executes.

## Complexity detail

Let $n$ be the common string length after the early check. Computing the two lengths is constant time in Python. Constructing `Counter(s)` visits all $n$ characters, and consuming `t` visits at most all $n$ characters. Counter lookup and update are expected $O(1)$ hash-table operations, so total expected running time is $O(n)$. Early rejection may stop the second scan sooner, but the worst case still processes both strings completely.

Let $u$ be the number of distinct characters in `s`, plus any new characters inserted into the counter while scanning `t` before rejection. The counter uses $O(u)$ auxiliary space. Under this problem's fixed alphabet of 26 lowercase English letters, $u\le 26$, independent of $n$, so the stated auxiliary space is $O(1)$. For unrestricted Unicode input, the same code remains functionally usable, but $u$ can grow with the input and the more general space bound is $O(u)$, or $O(n)$ in the worst case.

## Alternatives and edge cases

- **Fixed 26-entry frequency array:** Map each lowercase letter to an index from `0` through `25`, increment for `s`, and decrement for `t`. It avoids hashing and makes the fixed-alphabet $O(1)$ space explicit. This is the manifest's described representation, but not the exact Python source.
- **Sort both strings:** Equal anagrams become identical after sorting, giving a short solution. Sorting costs $O(n\log n)$ time and typically allocates string or character-array storage, so counting is asymptotically faster.
- **Two counters compared for equality:** `Counter(s) == Counter(t)` is conceptually direct and still $O(n)$ expected time. The implemented inventory method needs only one initial counter and can reject as soon as `t` overuses a character.
- **Unequal lengths:** Return `False` before constructing the counter. A longer or shorter string cannot be a rearrangement of the other.
- **A character absent from `s`:** `Counter` treats its prior count as zero; decrementing makes it negative and triggers immediate rejection.
- **Too many copies of an existing character:** The count becomes negative at the first unmatched extra occurrence, so later input need not be inspected.
- **Repeated letters:** Multiplicity is the central reason a Boolean set is insufficient. For example, `aab` and `abb` have the same set of letters but are not anagrams.
- **Identical strings:** Every count is consumed back to zero, so the method correctly returns `True`; no special identity check is needed.
- **Single-character strings:** Equal characters consume one available count and succeed; different characters make a missing key negative and fail.
- **Unicode follow-up:** A hash map or Python `Counter` avoids allocating an enormous fixed table and can count arbitrary code points. If “character” is intended to mean a user-perceived grapheme cluster rather than a Unicode code point, the text would first need appropriate Unicode normalization and grapheme segmentation; that is outside the lowercase-English contract.
- **Case sensitivity:** The allowed input is lowercase. In a broader setting, `A` and `a` are different keys unless the contract explicitly requests case folding.
