## General

**Track letter multiplicities instead of physical tile identities**

If two tiles both show `A`, swapping which physical tile was used does not create a new sequence. Treating tile positions as distinct would generate duplicates.

The solution begins:

```python
cnt = Counter(tiles)
```

For each distinct letter, `cnt[letter]` stores how many unused copies remain. The recursive state depends only on these counts, not on original tile indices.

For `"AAB"`, the state is two available `A` tiles and one available `B` tile. There is one choice named `A` at the first step, not two indistinguishable choices.

**Interpret one recursive call**

`dfs(cnt)` returns the number of distinct nonempty continuations that can be formed from the currently available tiles.

It initializes:

```python
ans = 0
```

Then it considers every distinct letter key:

```python
for i, x in cnt.items():
    if x > 0:
```

`i` is the letter and `x` is its available count at the start of this loop iteration. A letter with zero remaining copies cannot be chosen.

The Counter's keys do not change during recursion; only their numeric values are decremented and restored. Mutating values while iterating `cnt.items()` is safe because the dictionary size and key set stay fixed.

**Count the sequence ending after the chosen next letter**

For an available letter:

```python
ans += 1
```

counts the sequence formed by appending that letter and stopping immediately.

This step is why the recursion counts sequences of every positive length, not only sequences that consume all tiles. Every chosen prefix is itself a valid nonempty result.

At the root for `"AAB"`, choosing `A` counts sequence `"A"`, while choosing `B` counts sequence `"B"`.

**Consume one copy and explore longer continuations**

The code temporarily removes the chosen tile:

```python
cnt[i] -= 1
ans += dfs(cnt)
```

The recursive call counts all sequences that begin with the chosen letter and then append at least one more letter from the remaining multiset.

Although the recursive helper does not store the prefix text, the call path implicitly represents it. A path choosing `A`, then `B`, then `A` represents `"ABA"`.

The numeric result from the child is added because every child continuation becomes a unique longer sequence when prefixed by the current chosen letter.

**Backtrack before trying another letter**

After the child returns:

```python
cnt[i] += 1
```

restores the consumed copy. The next loop choice must start from the same original multiset as the current frame, except that it chooses a different first letter.

Without restoration, choices explored earlier would permanently remove tiles and cause later branches to miss valid sequences.

Backtracking changes state in place rather than copying the Counter for every call, saving allocation and making the state transition explicit.

**Why duplicate sequences are never generated**

At any recursion frame, the loop has one branch per distinct available letter, not one branch per copy. Therefore there is exactly one way to choose the next character `A`, even when several `A` tiles remain.

Consider any possible output sequence. Reading it from left to right determines one unique recursive path: at each depth, take the branch named by the next character. The frequency checks permit the path exactly when the sequence does not use any letter more times than available.

Two different paths differ at their first different chosen letter, so they spell different sequences. Thus every valid sequence appears once and no set is needed for deduplication.

**Why every valid sequence is counted**

Take any nonempty sequence that can be made from the tiles. Its first letter has positive count at the root, so the corresponding branch exists and counts the one-letter prefix. If the sequence is longer, decrementing that letter leaves enough counts for its suffix.

Apply the same argument recursively to every next character. The path exists through the full sequence, and the `ans += 1` at its final chosen letter counts it.

Therefore the recursion is both complete and duplicate-free.

**Base behavior**

There is no explicit base-case statement. When all counts are zero, every `x > 0` test fails, the loop adds nothing, and `dfs` returns zero.

This implicit base case is correct: with no tile available, there is no nonempty continuation. The empty sequence is never added, so the final answer already matches the nonempty requirement without subtracting one.

**Trace AAB**

From two `A` and one `B`:

- Choose `A` and count `"A"`. From the remaining `AB`, count `"AA"`, `"AAB"`, `"AB"`, and `"ABA"`.
- Restore, choose `B`, and count `"B"`. From remaining `AA`, count `"BA"` and `"BAA"`.

The total is eight, matching the example.

## Complexity detail

Let `n` be the number of tiles, `M` the number of distinct letters, and `D` the number of distinct nonempty sequences that can be formed.

The recursion tree contains one root plus one node for each distinct sequence prefix, so it has `D + 1` calls. Each call iterates over all `M` Counter keys, even when some counts are zero. Exact time is `O(DM)`.

The Counter stores `M` entries. Recursion depth is at most `n` because every descent consumes one tile. The implementation stores no generated strings or sequence set, so auxiliary space is `O(M + n)`.

These exact bounds match the manifest. In the all-distinct worst case, `D` grows on the order of the sum of partial permutations, so factorial growth is unavoidable because the answer itself is factorially large.

## Alternatives and edge cases

- **Position-based backtracking plus a set:** It generates the same string through different identical tiles and needs a potentially huge set to deduplicate results.
- **Sorted tiles with duplicate skipping:** Backtrack over positions and skip equal unused choices at each depth. This also avoids duplicate sequences but requires more delicate used-index logic.
- **Memoize by remaining counts:** Different prefixes can reach the same remaining multiset, and the number of suffix continuations is identical. Caching can reuse that numeric result while still adding it under each distinct prefix.
- **Combinatorial frequency formula:** Enumerate how many copies of each letter a sequence uses, then count multiset permutations. It avoids spelling paths but requires careful enumeration and factorial arithmetic.
- **One tile:** The root has one available branch, counts one sequence, and the child returns zero.
- **All tiles identical:** There is exactly one sequence of each length from one through `n`, so the answer is `n`.
- **All tiles distinct:** Every partial permutation is unique, producing the largest recursion tree.
- **Counter keys with zero values:** They remain in the map and are skipped by `x > 0`.
- **No empty sequence:** The helper counts only after selecting a letter, so empty is excluded naturally.
- **Backtracking restoration:** Every decrement must be paired with an increment before the loop continues.
- **Uppercase alphabet:** Counter keys handle only letters actually present; the code does not waste iterations over all 26 possible letters.
- **Input preservation:** `tiles` is immutable, and only the separate Counter is modified and restored.
