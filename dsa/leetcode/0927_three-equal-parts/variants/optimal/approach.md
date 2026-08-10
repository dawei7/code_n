## General

Leading zeros do not affect a binary value, but the number and placement of ones do. If three parts represent the same value, each must contain the same number of ones. This gives the first necessary condition.

Let total ones be $T$. The solution computes

$$
(cnt,mod)=\operatorname{divmod}(T,3).
$$

If `mod` is nonzero, the ones cannot be divided equally and no answer exists.

**All-zero special case.** If `cnt == 0`, every part represents zero regardless of how many zeros it contains. The solution returns `[0, n - 1]`:

- first part is index 0;
- second part is indices 1 through $n-2$;
- third part is index $n-1$.

All are nonempty because $n\ge3$.

**Locate the significant start of each part.** When each part must contain `cnt` ones, its binary representation begins at its first one after ignoring leading zeros.

Helper `find(x)` returns the index of the $x$-th one in the entire array. Therefore:

- `i = find(1)` is the first significant one of part one;
- `j = find(cnt + 1)` is the first significant one of part two;
- `k = find(2 * cnt + 1)` is the first significant one of part three.

The third part's significant representation must extend all the way to the end of the array, including every trailing zero. Those trailing zeros are part of its binary value and cannot be discarded.

**Compare all three significant suffixes together.** While `k < n` and `arr[i] == arr[j] == arr[k]`, advance all three pointers.

This compares each bit of the first and second significant representations with the third representation. Because the third pointer must reach `n`, the comparison length is exactly the full significant length of the third part, including its trailing zeros.

If any bits differ before `k` reaches the end, equal values are impossible. If `k == n`, all three matched for the entire required length.

**Turn advanced pointers into cut positions.** Let the matched significant length be $L=n-k_0$, where $k_0$ was the original third start. After comparison:

- advanced `i = i_0 + L` is the first index after part one's significant representation, so first part ends at `i - 1`;
- advanced `j = j_0 + L` becomes the start index of the third returned part;
- the second returned part begins at advanced `i` and ends at `j - 1`.

Zeros between the end of one significant pattern and the next pattern become leading zeros of the following part. They do not alter its value.

The solution therefore returns `[i - 1, j]`.

For `[1,0,1,0,1]`, each part needs one 1. Significant starts are 0, 2, and 4. The third significant length is one; after one matching step, pointers are 1, 3, and 5. The cuts `[0,3]` produce `[1]`, `[0,1]`, and `[0,1]`, all representing one.

**Why equal one counts plus bit comparison is sufficient.** Each part's leading zeros can be ignored. Starting at its first one, equal binary values must have identical remaining bit strings, including trailing zeros. The synchronized loop tests exactly those strings. Equal one counts ensure the chosen start positions divide the occurrences among the three parts correctly.

**Why a mismatch proves impossibility.** The first one in each part is forced by equal one allocation, and the third pattern's trailing length is forced by the array end. Cut positions may move through leading-zero gaps, but they cannot change any significant bit or remove required trailing zeros. A mismatching significant string cannot be repaired by different cuts.

## Complexity detail

Let $n$ be the array length. Summing ones, each `find` scan, and the synchronized comparison are all linear; a constant number of linear passes remains $O(n)$.

- **Time complexity:** $O(n)$.
- **Space complexity:** $O(1)$ auxiliary space.

The helper scans the original array and stores only counters and indices. No bit strings or slices are allocated.

## Alternatives and edge cases

- **Build three significant slices:** Locate starts and compare array slices. This is clear but uses $O(n)$ temporary space, matching the editorial rather than the exact constant-space scan.
- **Convert parts to integers:** Binary values may be extremely large, and trying cut pairs is quadratic.
- **Try every two cuts:** There are $O(n^2)$ partitions and expensive value comparisons.
- **Total ones not divisible by three:** Immediately impossible.
- **All zeros:** Any three nonempty parts work; the chosen indices are valid.
- **Trailing zeros:** Every part must include the same number after its final one, because they change the binary value by powers of two.
- **Leading zeros:** They may be distributed around cut boundaries freely because they do not change value.
- **One one per part:** Starts are simply the first, second, and third ones.
- **Bit mismatch:** Return failure even when one counts match.
- **Third pointer reaches end:** This is the success condition proving full significant patterns matched.
- **Nonempty parts:** The selected one positions and returned boundaries satisfy the required cut ordering in successful cases.
- **Any valid answer:** Other placements of leading zeros may give different accepted cuts; only one is needed.
