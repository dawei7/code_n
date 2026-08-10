## General

**Partition possible starts by word-length alignment**

The selected Competitive `Solution` uses a sliding window. If every word has length `k`, a concatenation can be inspected only in `k`-character units. The outer loop runs once for each offset `0` through `k - 1`; within an offset, both `left` and the read index `j` move by exactly `k`.

Every character index has exactly one remainder modulo `k`, so this covers every possible start without making one independent full check per character.

The source variables are `m = len(s)`, `n = len(words)`, and `k = len(words[0])`. A complete answer window has `n` tokens and `n * k` characters.

**Reject impossible top-level inputs early**

Although the Reference guarantees a non-empty `words`, the source explicitly returns `[]` if it is empty, preventing an invalid `words[0]` access.

It also returns early when `m < n * k`. In that case the entire search string is shorter than one required concatenation, so no starting index can work.

**Build exact required frequencies**

`lookup` maps each distinct word to its required number of occurrences. Repeated words increment the same entry. This is essential: membership alone would incorrectly accept too many copies of one word while omitting another.

For each alignment, `tmp` counts words in the current window, and `count` is the number of tokens in that window. The invariant before adding the next token is that every current token belongs to `lookup`, every `tmp` count is within its quota, and `count` equals the number of aligned chunks from `left` through the previous `j`.

**Read only complete chunks**

The inner range is

```python
for j in range(i, m-k+1, k):
```

Its final possible `j` is at most `m - k`, so `s[j:j+k]` always has exactly `k` characters. The `+ 1` includes a word ending at the final character of `s`.

Creating `s1` extracts the new rightmost token. Membership is checked with `s1 in lookup`; because this is a membership operation on a `defaultdict`, it does not need to manufacture a missing quota entry.

**Reset when a word is not allowed**

An unknown `s1` cannot appear anywhere inside a valid concatenation. The source discards the whole current window by replacing `tmp`, setting `count = 0`, and moving `left = j + k` to the next aligned position.

Every prospective window crossing this bad token is impossible, so no answer is lost. Replacing the dictionary rather than clearing it is an implementation choice; the old object becomes unreachable.

**Add a known word, then remove excess copies**

For a recognized token, the method increments `tmp[s1]` and `count`. Only `s1` can now exceed its quota because all counts satisfied the invariant beforehand.

While it is excessive, the source removes tokens from the left:

```python
tmp[s[left:left+k]] -= 1
count -= 1
left += k
```

Eventually an older occurrence of `s1` leaves, restoring `tmp[s1] <= lookup[s1]`. Removing other words on the way can make them deficient but cannot make any count excessive. The normalized invariant is restored without scanning the full frequency table.

**Why `count == n` proves a complete multiset match**

After shrinking, every current count is no greater than its required count. The sum of required counts is exactly `n`. If the window also contains `n` tokens, no quota can be deficient: a deficiency would force some other word to be excessive to keep the total at `n`, contradicting normalization. Therefore all frequencies match exactly, and `left` is a valid answer.

The source appends `left` but does not immediately advance it. This is intentional. On the next added known word, the `n + 1` token window must contain an excess, and the while-loop slides just far enough to restore quotas. That supports overlapping matches.

**Trace duplicate handling**

Suppose `words = ["good", "good", "best"]`. `lookup["good"]` is two. The first and second `good` tokens are accepted. A third makes `tmp["good"] == 3`, so the left boundary advances and decrements counts until one old `good` has left. A set-based solution would not know whether two or three copies were allowed.

For an unknown token such as `"word"`, the state resets entirely because no concatenation using only the three required entries can cross it.

**Why the two-pointer work is linear per alignment**

`j` moves only right. Although shrinking is nested syntactically, `left` also moves only right and can pass each aligned token at most once before a reset or the end. The while-loop's total iterations over one alignment are therefore bounded by the number of right-loop iterations, not multiplied by it.

**Why the answer set is correct**

Each reported window has exactly `n` recognized chunks and respects all multiplicity ceilings, which forces exact quota equality. Conversely, consider a real concatenation. Its start is visited in exactly one alignment. No unknown token lies inside it, and quota shrinking cannot move past its start while its ending token is processed unless the preceding active window contains an excess that cannot belong to this valid multiset. When its last token is added, the normalized count reaches `n` and its start is appended.

## Complexity detail

Let $S=\lvert s\rvert$, $W=\lvert\texttt{words}\rvert$, $L=\lvert\texttt{words}[0]\rvert$, and $U$ be the number of distinct words.

- **Time complexity: $O((S+W)L)$ under Python substring and hashing costs.** Across all offsets, the right loops process $O(S)$ chunks, and all left-boundary removals are amortized to another $O(S)$ chunks. Each slice/hash may inspect $L$ characters. Building `lookup` processes $W$ words of length $L$.
- **Auxiliary space: $O(UL)$ when counting the character content of dictionary keys and active slices, or $O(U+L)$ at the object-entry level.** `lookup` and `tmp` have at most $U$ relevant word keys. The result array is required output space.

The source comment writes `O((m + n) * k)` time and `O(n * k)` space with `m`, `n`, and `k` meaning string length, word count, and word length. That matches the explicit notation above up to replacing total words with distinct words in the tight space bound.

## Alternatives and edge cases

- **`Solution2` in the same file:** It checks every candidate independently and can cost $O(SWL)$ time; it is not the selected entry point.
- **Fresh counter per starting index:** Easy to verify but repeats work shared by neighboring aligned candidates.
- **Permutation generation:** Factorial growth makes it unsuitable even before substring searching.
- **Empty word list outside the Reference:** The explicit guard returns an empty result.
- **Search string too short:** The length guard returns before allocating window dictionaries.
- **Unknown aligned word:** State resets and the next possible window begins after it.
- **Excess duplicate:** The same `j` token is retained while old left tokens are removed until its quota is legal.
- **Overlapping matches:** A recorded window stays active and is normalized after the next token.
- **Different offsets:** Results can emerge in offset-grouped rather than numeric order; any order is permitted.
- **Incomplete suffix:** The inner range never slices a short final token.
- **All words identical:** The quota permits exactly `n` copies and the sliding behavior reports every aligned run of that length.
- **Input strings remain unchanged:** Only counters, indices, slices, and the result list are created.
