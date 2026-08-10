## General

**The condition combines global counts with local adjacency.** Whether a digit is eligible depends on its frequency in the entire string, but the returned pair must be two neighboring positions. The source therefore uses two passes: first count every digit globally, then inspect adjacent pairs from left to right.

`cnt = [0] * 10` allocates one slot for each numeric digit $0$ through $9$. The input contract actually uses only `"1"` through `"9"`, but the extra zero slot makes direct indexing simple and harmless.

The loop

`for x in map(int, s)`

converts each one-character digit to its integer value and increments `cnt[x]`. After this pass, `cnt[d]` is exactly the total number of occurrences of digit $d$ anywhere in `s`.

**Scan consecutive positions in required order.** A fresh `map(int, s)` iterator feeds `pairwise`. For digit sequence $d_0,d_1,\ldots,d_{n-1}$, `pairwise` yields

$$
(d_0,d_1),(d_1,d_2),\ldots,(d_{n-2},d_{n-1}).
$$

These are precisely all adjacent pairs, in left-to-right order. Recreating the map is necessary because the first map iterator was consumed while counting.

For a pair `(x, y)`, the condition has three parts:

- `x != y` enforces distinct digits;
- `cnt[x] == x` says the first digit occurs exactly its numeric value times;
- `cnt[y] == y` says the same for the second digit.

When all are true, `f"{x}{y}"` converts the two numeric digits back into their two-character string and returns immediately.

Immediate return is what implements “first valid pair.” A later valid pair is never considered after an earlier one succeeds. If the entire adjacency scan finishes without success, the method returns the required empty string.

For `"2523533"`, the count pass finds two `2` digits and three `3` digits. The adjacent pairs before `"23"` fail at least one condition. When `pairwise` reaches $2,3$, both counts match their numeric values and the digits differ, so `"23"` is returned.

For `"22"`, digit $2$ does occur twice, but the only adjacent pair has equal members. The explicit inequality rejects it, showing that frequency eligibility alone is insufficient.

**Why counting once is enough.** Pair validity refers to occurrences in the whole original string, not within the pair or within a prefix. No operation changes the string, so the global count array remains valid for every adjacency test. Recounting for each pair would repeat identical work.

**Why the first matching pair is the required answer.** After the first pass, every count lookup is exact. The second pass visits adjacent starting indices $0$ through $n-2$ in increasing order. At each one, the Boolean expression is identical to the definition of a valid pair. Therefore, the first returned pair is the leftmost valid pair. If none is returned, every possible adjacent pair has been tested and failed, so the empty result is correct.

The method uses integer conversion only for convenient indexing and comparison. Since each character is one decimal digit, formatting `x` and `y` without a separator reconstructs exactly the original two digit characters. The input excludes multi-digit tokens and signs.

The constraint also excludes digit zero. If zero were allowed, the rule “appears exactly zero times” could never hold for a zero that is present in the candidate pair. The allocated count slot would still behave consistently and reject it.

## Complexity detail

Let $n=\lvert\texttt{s}\rvert$. The count pass reads $n$ characters. `pairwise` reads the string again and yields $n-1$ pairs in the worst case. Every conversion, lookup, and comparison is constant time, so total time is $O(n)$.

The count array always has ten entries. Both map iterators and `pairwise` retain constant state, and no list of digits or pairs is created. Auxiliary space is $O(1)$, matching the manifest.

## Alternatives and edge cases

- **Use `Counter(s)`:** A dictionary counter is equally correct and concise, but a fixed ten-slot array has predictable constant space and direct numeric indexing.
- **Count during the pair scan only:** A pair may depend on occurrences later in the string, so complete global counts must be known before validation.
- **Build a digit list:** Converting all characters up front simplifies reuse but allocates $O(n)$ space; two lazy map passes avoid it.
- **Equal eligible digits:** Even when a digit's count matches its value, a pair such as `"22"` is invalid because the two positions must contain different digits.
- **Several valid pairs:** Returning inside the ordered pairwise loop guarantees the leftmost one.
- **No valid pair:** The explicit final `""` matches the required sentinel.
- **Overlapping pairs:** `pairwise` correctly checks both $(i,i+1)$ and $(i+1,i+2)$; sharing a position is allowed during searching.
- **Digit nine:** A `9` is eligible only if it occurs nine times in the full string, and the same direct count comparison handles it.
- **Minimum length:** With two characters, exactly one adjacency is tested.
- **Input immutability:** Mapping and counting read `s` without changing it.
