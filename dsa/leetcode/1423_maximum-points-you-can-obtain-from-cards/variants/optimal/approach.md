## General

**Every valid result chooses a prefix and a suffix**

Although the cards are taken one step at a time, the final selected set has a simple shape. If $i$ cards are taken from the beginning, the remaining $k-i$ selected cards must come from the end. Their interleaving order does not affect the final sum.

Therefore, there are only $k+1$ relevant combinations:

$$
(0,k),(1,k-1),\ldots,(k,0),
$$

where each pair means number from the left and number from the right.

The solution evaluates these combinations by starting with all $k$ cards from the right and replacing one selected right card with one selected left card at each iteration.

**Initialize the all-right choice**

`cardPoints[-k:]` is the suffix containing exactly the final $k$ cards. The statement:

```python
ans = s = sum(cardPoints[-k:])
```

sets `s` to the score for taking zero cards from the left and $k$ from the right. `ans` receives the same value because this is the first valid candidate.

Chained assignment makes both names refer to the same integer value. Integers are immutable, so later updating `s` does not alter `ans`.

**Slide from right choices to left choices**

The loop visits the first $k$ cards:

```python
for i, x in enumerate(cardPoints[:k]):
```

At iteration `i`, `x` is `cardPoints[i]`, the next card to add from the left.

The currently selected right block must shrink by removing its leftmost remaining card. That card is:

```python
cardPoints[-k + i]
```

At `i = 0`, index `-k` points to the first card of the original $k$-card suffix. At each later iteration, the index moves one position right. Thus:

```python
s += x - cardPoints[-k + i]
```

replaces exactly one right-end selection with exactly one left-end selection while keeping the number of selected cards equal to $k$.

After iteration `i`, the candidate uses $i+1$ cards from the beginning and $k-i-1$ cards from the end.

**Why overlapping end regions cause no double-count**

When $k$ is more than half the array length, the first-$k$ and last-$k$ slices overlap as raw regions. The replacement sequence still represents valid choices. A card entering from the left is paired with the specific suffix card leaving the selection, so the maintained set always contains exactly a prefix and a nonoverlapping suffix totaling $k$ positions.

For example, with five cards and `k = 4`, the all-right set uses indices 1, 2, 3, and 4. The first replacement removes index 1 and adds index 0, producing indices 0, 2, 3, and 4. The next removes index 2 and adds index 1, producing 0, 1, 3, and 4. No index is counted twice.

**Record the maximum after every replacement**

`ans = max(ans, s)` keeps the best score among all combinations seen so far. The initial candidate covers $(0,k)$. The $k$ loop iterations cover $(1,k-1)$ through $(k,0)$. Therefore, all $k+1$ possible prefix-suffix length pairs are evaluated.

**Trace the main example**

For `cardPoints = [1, 2, 3, 4, 5, 6, 1]` and `k = 3`:

| Left count | Right count | Selected values | Score |
|---:|---:|---|---:|
| 0 | 3 | `5, 6, 1` | 12 |
| 1 | 2 | `1` and `6, 1` | 8 |
| 2 | 1 | `1, 2` and `1` | 4 |
| 3 | 0 | `1, 2, 3` | 6 |

The initial all-right score 12 remains the maximum.

The update reaches the same values incrementally. It begins at 12, adds left 1 and removes right-block 5 to get 8, then adds 2 and removes 6 to get 4, and finally adds 3 and removes the last right 1 to get 6.

**Why intermediate pick order is irrelevant**

Suppose a final strategy takes $i$ cards from the beginning and $k-i$ from the end. Regardless of whether it alternates ends, taking from one end never changes the internal order of the other end's cards. The selected cards are exactly the original prefix of length $i$ and suffix of length $k-i$.

Conversely, every such prefix-suffix combination can be achieved by taking its prefix cards from the beginning and suffix cards from the end in any compatible order. Thus enumerating length pairs covers every legal strategy and no illegal set.

Because `s` is updated by removing the right card that leaves one combination and adding the left card entering the next, it equals the exact score for each pair. The maximum recorded value is therefore optimal.

**The all-cards case**

When `k == len(cardPoints)`, the initial suffix is the whole array. In the loop, the entering left card and leaving suffix card refer to the same positions in sequence, so `s` remains the total sum. The method returns the required sum without a special branch.

## Complexity detail

Let $n$ be the number of cards. The algorithm sums $k$ suffix cards and performs $k$ constant-time replacements, so its tight running time is $O(k)$. Since $k \le n$, this is also $O(n)$, matching the manifest.

The mathematical rolling-sum algorithm uses only `s`, `ans`, `i`, and `x`, giving $O(1)$ auxiliary state. In exact Python execution, both `cardPoints[-k:]` and `cardPoints[:k]` allocate lists of length $k$, so the stored syntax uses $O(k)$ temporary space. Using indexed summation and `range(k)` would realize strict $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Complement sliding window:** Taking $k$ end cards leaves one contiguous block of length $n-k$. Subtracting the minimum such block sum from the total yields the answer in $O(n)$ time and $O(1)$ algorithmic space.
- **Prefix and suffix sum arrays:** Precompute scores for taking each possible count from both ends, then combine pairs. It is clear but uses $O(k)$ explicit storage.
- **Recursive choice of ends:** A binary decision at every pick explores $2^k$ sequences and repeatedly reaches the same prefix-suffix count pair.
- **Memoization by left and right counts:** This reduces repeated recursion but still stores many states when only $k+1$ final combinations matter.
- **`k = 1`:** The two candidates are the first and final cards; the loop compares them through one replacement.
- **`k = n`:** Every card must be taken, and the rolling score remains the total.
- **Equal card values:** Different choices can tie; `max` correctly keeps their common score.
- **Positive-points guarantee:** All scores are positive, but the enumeration proof does not rely on positivity and would still compare every legal combination with other integer values.
- **Negative indexing:** `-k + i` intentionally walks from the beginning of the selected suffix toward the array's last element.
- **Slice allocation:** The manifest's constant-space claim describes the rolling method; replacing the two slices with index loops removes Python's temporary lists.
