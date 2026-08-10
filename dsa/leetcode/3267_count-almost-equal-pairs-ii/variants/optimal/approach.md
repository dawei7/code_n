## General

This version permits up to two digit swaps. The solution sorts the numbers, generates every distinct integer reachable from the current value with zero, one, or two swaps, and counts matching earlier originals.

Sorting handles leading-zero asymmetry. A longer number such as `100` can become `001`, interpreted as one. Processing the larger representation later ensures its generated shorter result can find the earlier value.

`vis` begins with current `x` for the zero-swap case. The first nested pair `i < j` performs one swap and inserts its integer result. Before undoing that swap, the inner pair `p < q` performs a second swap, inserts the result, and undoes it. The first swap is then undone.

The second pair is restricted to indices greater than `i`. This removes redundant representations of two-transposition permutations. If a second transposition also uses the smallest involved position, the same resulting permutation can be expressed by reordering and transforming the two swaps so the second uses later positions. Original value and one-swap results are already inserted separately.

Repeated digits, canceling swaps, and different swap sequences can produce the same number. `vis` deduplicates them so one earlier index contributes at most once to the current pair count.

`cnt` stores frequencies of original values already processed. Summing `cnt[y]` over reachable `y` counts every earlier index almost equal to the current one. Then the current original value is inserted for future numbers.

Although the generator writes `x` as its local variable in `sum(cnt[x] for x in vis)`, Python 3 comprehension scope leaves the outer current `x` intact for `cnt[x] += 1`.

Two swaps are reversible. For equal-length values, if earlier $a$ can become current $b$, applying the inverse swaps to $b$ produces $a$. A shorter displayed value cannot create more digits by swapping, while a larger value can lose leading zeros. Sorted one-sided generation therefore covers operation on either member.

For `1023` and `2310`, two swaps can realize the required digit permutation, so the generated set contains the match. For `1,10,100`, the larger values generate shorter integers through leading zeros, causing all three unordered pairs to be counted.

The array is sorted in place. Original index order is unnecessary because the goal is a count of unordered pairs, but caller-visible order changes.

## Complexity detail

Let $d$ be the maximum digit count. There are $O(d^2)$ first swaps and up to $O(d^2)$ second swaps for each, giving $O(d^4)$ generated sequences. Joining and parsing one sequence costs $O(d)$, so generation is $O(d^5)$ per number.

Including sorting, expected time is $O(n\log n+nd^5)$. The reachable set can hold $O(d^4)$ results, and the frequency map up to $n$ values, for $O(n+d^4)$ auxiliary space, aside from sort workspace.

Here $d\le7$, so the high polynomial is over a very small fixed digit count.

## Alternatives and edge cases

- **Compare all number pairs:** A direct two-swap distance check costs at least $O(n^2d)$ and is too large for five thousand inputs.
- **Enumerate arbitrary digit permutations:** Two swaps reach only a subset of permutations; generating all $d!$ arrangements solves a different condition.
- **Generate from both pair members:** Sorted processing and reversibility make this redundant.
- **Omit sorting:** Pairs requiring leading-zero shortening can be missed by one-sided generation.
- **Zero swaps:** Equal values are almost equal and are included by initializing `vis` with `x`.
- **One swap:** First-level results are inserted even if no meaningful second swap follows.
- **Two identical or canceling swaps:** They return an already stored result and are harmlessly deduplicated.
- **Repeated digits:** Many swap paths collapse to one integer; the set prevents overcounting.
- **Leading zeros:** Integer conversion intentionally removes them, matching the statement.
- **More than two transpositions required:** Such a permutation never enters `vis` and is correctly excluded.
- **Input mutation:** `nums.sort()` changes the passed list; sorting a copy would preserve it at $O(n)$ extra storage.
- **Frequency rather than membership:** If a reachable value occurred three times earlier, all three earlier indices form distinct pairs with the current index. A set of prior values would undercount; `defaultdict(int)` preserves multiplicity.
- **Pair counted once:** Only earlier frequencies are queried, and the current value is inserted afterward. This ordering prevents pairing an index with itself and prevents revisiting the same unordered index pair later.
- **Second-swap restoration:** The code undoes `s[p],s[q]` before trying the next second pair, then undoes `s[i],s[j]` after the inner enumeration. Without both restorations, later candidates would accidentally contain three or more accumulated swaps.
- **Displayed-length mismatch:** Shorter and longer values can match only when swaps in the longer representation move zeros to the front. Sorting ensures the representation capable of that transformation is the one whose results are enumerated.
- **Small digit count:** The $d^5$ expression looks large, but $d$ is at most seven. The method trades a bounded transformation set per value for avoiding the $n^2$ pair explosion.
