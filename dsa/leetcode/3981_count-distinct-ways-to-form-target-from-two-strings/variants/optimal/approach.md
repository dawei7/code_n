## General

Each target character is chosen from exactly one source string. Indices must increase inside `word1` and inside `word2` independently, but the two strings have no shared ordering. A choice from a low index of `word2` may occur after a high index of `word1` because only same-source indices are compared.

The future legality of a partial construction depends on:

- how much of `target` has already been formed;
- the last index used in `word1`;
- the last index used in `word2`.

The outer loop supplies the target-prefix length, so the table needs only the two last-index coordinates.

**One-based stored indices**

Let `n_1=\lvert word1\rvert` and `n_2=\lvert word2\rvert`. The source uses table indices from zero through each word length.

- stored value zero means that source word has never been used;
- stored value `p\ge1` means the last chosen character was at ordinary zero-based index `p-1`.

This one-based representation is useful because zero simultaneously means “no previous index” and proves that the source has not contributed any character.

After some target prefix has been processed, `dp[last1][last2]` counts constructions of that prefix whose latest selected positions have those stored values.

The initial empty target prefix has one construction that uses neither word:

```python
dp[0][0] = 1
```

Every other initial state is impossible and remains zero.

**A new table for each target character**

For each required character `needed`, the source creates a zero-filled `next_dp`. Every transition chooses exactly one matching source position for this target character and moves from `dp` to `next_dp`.

Using a separate next table is essential. Updating `dp` in place could allow one target character to be chosen multiple times during the same outer iteration.

After all transitions for `needed`, `dp = next_dp` advances the represented target prefix by exactly one character.

**Choosing the next character from `word1`**

Suppose the new stored index in `word1` will be `new1`, meaning actual position `new1-1` is chosen. Its character must satisfy:

```python
word1[new1 - 1] == needed
```

The previous stored `last1` may be zero or any positive value strictly smaller than `new1`. This exactly enforces increasing actual indices. The latest `word2` index remains unchanged.

For fixed `last2`, the desired transition count is:

$$
\texttt{nextDp}[new1][last2]
=
\sum_{p=0}^{new1-1}\texttt{dp}[p][last2].
$$

Computing that sum from scratch for every `new1` would add another factor of `n_1`. The source maintains a running prefix:

```python
prefix = 0
for new1 in range(1, n1 + 1):
    prefix = (
        prefix + dp[new1 - 1][last2]
    ) % modulo
    if word1[new1 - 1] == needed:
        next_dp[new1][last2] = prefix
```

At iteration `new1`, `prefix` contains exactly table rows zero through `new1-1`. It therefore sums every legal predecessor once.

The assignment rather than addition is safe here because this loop is the only collection of transitions that choose the current target character from `word1` and end at this exact `(new1,last2)` state. All eligible old histories have already been combined into `prefix`.

**Choosing the next character from `word2`**

The second half is symmetric. For fixed `last1`, a prefix sum over old `last2` values counts all ways whose previous `word2` index is smaller than `new2`:

$$
\texttt{nextDp}[last1][new2]
\mathrel{+}=
\sum_{p=0}^{new2-1}\texttt{dp}[last1][p].
$$

The exact loop builds that sum with:

```python
prefix = (
    prefix + dp[last1][new2 - 1]
) % modulo
if word2[new2 - 1] == needed:
    next_dp[last1][new2] = (
        next_dp[last1][new2] + prefix
    ) % modulo
```

When `word2[new2-1]` matches `needed`, the source adds this prefix into the destination cell.

Here `+=` is necessary because a state with both stored indices positive can be reached in two conceptually different ways:

- the newest target character came from `word1`, leaving `last2` unchanged;
- the newest target character came from `word2`, leaving `last1` unchanged.

Those construction sets are disjoint because they choose the current target position from different sources, so their counts must be added.

**Why state compression does not merge distinct ways incorrectly**

Many histories can end with the same pair of last indices. They have identical future options because only indices after those positions can be selected next.

The table stores their number, not merely whether the state is reachable. When several predecessor histories choose the same new index, prefix addition retains all multiplicities. Choices using different earlier indices or different source assignments remain distinct contributions even after they share a state.

Modulo reduction preserves the required count modulo `10^9+7`.

**Enforcing that both words are used**

After all target characters have been formed, states with `last1=0` used no character from `word1`. States with `last2=0` used no character from `word2`.

The source sums only:

```python
dp[last1][last2]
for last1 in range(1, n1 + 1)
for last2 in range(1, n2 + 1)
```

Both stored indices are positive, so both source strings contributed at least once. This avoids separate boolean flags.

For a one-character target, no construction can use both words because each target position chooses exactly one character. The final positive-positive region is empty of counts, producing zero automatically.

**A short example**

Take `word1="ab"`, `word2="cde"`, and `target="ace"`.

For `'a'`, only stored state `(1,0)` becomes nonzero by choosing `word1[0]`.

For `'c'`, the next choice must come from `word2[0]`, producing state `(1,1)`. The separate index orders allow this even though the stored indices belong to different words.

For `'e'`, choosing `word2[2]` advances the second stored index to three, producing `(1,3)`. Both coordinates are positive, so the one construction is included in the answer.

**Why the prefix optimization is the key**

A direct transition from every old index pair to every possible next index would cost roughly `O(tn_1n_2(n_1+n_2))`. The prefix sums aggregate all smaller same-source last indices as the new index moves right.

For every fixed coordinate from the other word, one linear sweep handles all new positions. This reduces each target-character layer to `O(n_1n_2)`.

## Complexity detail

Let

$$
n=\lvert word1\rvert,\qquad
m=\lvert word2\rvert,\qquad
t=\lvert target\rvert.
$$

For each target character:

- allocating `next_dp` initializes `(n+1)(m+1)=O(nm)` cells;
- the `word1` transition loops over `m+1` fixed second indices and `n` new first indices, costing `O(nm)`;
- the `word2` transition similarly costs `O(nm)`.

Total time complexity is:

$$
O(tnm).
$$

At any layer, `dp` and `next_dp` each contain `O(nm)` integers. They may coexist until the assignment at the end of the layer, but a constant number of such tables remains `O(nm)` space.

Prefix accumulators and loop indices require only constant additional storage. The source does not modify any input string.

The final double sum costs `O(nm)`, which is already dominated by the target-layer work because `t\ge1`.

## Alternatives and edge cases

- **Enumerate every source assignment:** Even before choosing indices, each of `t` target positions has two source choices, giving up to `2^t` assignments.

- **Backtracking over matching indices:** Repeated characters can create exponentially many increasing subsequences. Dynamic programming aggregates histories with the same future constraints.

- **Track only how many characters were consumed from each word:** A source may skip arbitrary characters, so the last selected index—not merely the number selected—determines future choices.

- **Use one global index order:** Indices from different source strings are incomparable. Only each word's own chosen indices must increase.

- **Add separate “used word” flags:** They are redundant because stored last index zero already means unused and a positive value means used.

- **Update the table in place:** That can reuse a newly created state for the same `needed` character and consume multiple source characters for one target position. A fresh layer prevents this.

- **Recompute predecessor sums:** Summing every smaller last index for every new index introduces an unnecessary extra factor. Running prefixes make each row or column sweep linear.

- **Target length one:** No valid way can use both words, so the answer is zero.

- **Target longer than combined source lengths:** No sequence can choose enough distinct increasing indices, and all DP states eventually become zero.

- **One source cannot match any target character:** Positive-positive final states cannot survive, so the result is zero even if the other word alone forms the target.

- **Repeated characters:** Different matching indices are distinct ways and are all accumulated by prefix sums.

- **Same textual construction from different sources:** It remains distinct because choosing a target character from a different source leads through a different transition and is counted separately.

- **Modulo placement:** Prefixes and destination additions are reduced throughout, preventing large intermediate counts while preserving the final residue.

- **Empty target:** The stated contract excludes it. If allowed, the requirement to use both words would make the answer zero; the stored final sum would also exclude `dp[0][0]`.

- **Assignment in the first transition loop:** `next_dp[new1][last2] = prefix` is correct because all word-one predecessors for that exact destination are already inside one prefix. The later word-two loop adds its separate constructions.

- **Final summation bounds:** Starting both ranges at one is the exact enforcement of “at least one from both,” not an optimization that may be omitted.
