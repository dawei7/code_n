## General

**Reframe one subsequence as one left-to-right pass**

A subsequence of `source` keeps characters in their original relative order while allowing arbitrary characters to be skipped. Therefore, choosing one subsequence is equivalent to making one left-to-right pass over `source` and taking some matching characters along the way.

The selected subsequences must concatenate to `target`. This means the first pass must form a prefix of `target`, the second pass must continue exactly where the first stopped, and so on until all target characters have been consumed.

The central greedy choice is to match as many consecutive target characters as possible during every pass over `source`. Skipping a source character that matches the next required target character can never help: accepting it leaves at least as much of the remaining source available for all later target characters.

**The helper performs one greedy source pass**

The nested helper is:

```python
def f(i, j):
    while i < m and j < n:
        if source[i] == target[j]:
            j += 1
        i += 1
    return j
```

Here `i` is the position currently inspected in `source`, and `j` is the index of the first target character not yet formed.

On every loop iteration, `i` advances. If `source[i]` equals the next required character `target[j]`, the helper also advances `j` to record that one more target character has been matched. If they differ, only `i` advances, which means that source character is deleted from the chosen subsequence.

The scan stops for one of two reasons:

- `i == m`, meaning this copy of `source` is exhausted.
- `j == n`, meaning the entire `target` has already been formed.

The returned value of `j` is the boundary immediately after the target prefix covered so far. If the helper starts at target index three and returns seven, the current pass formed `target[3:7]` as a subsequence of `source`.

Although `f` accepts an arbitrary source index `i`, the main loop always calls `f(0, j)`. Every selected piece is allowed to be a fresh subsequence of the complete `source`, so each new piece must restart at the beginning.

The helper refers to `m` and `n` even though they are assigned after the function definition:

```python
m, n = len(source), len(target)
```

This works because defining a Python closure does not execute its body. The values exist by the time the main loop actually calls `f`.

**Track how much of the target is complete**

The assignment:

```python
ans = j = 0
```

initializes both variables to zero. `j` means no target characters have yet been formed. `ans` counts how many nonempty subsequences of `source` have been used.

The main loop continues while `j < n`:

```python
while j < n:
    k = f(0, j)
```

Each call makes one complete greedy attempt to extend the matched target prefix using a fresh copy of `source`. `k` is the new boundary returned by that pass.

For `source = "abc"` and `target = "abcbc"`, the first call starts at `j = 0`. It matches `"abc"` and returns three. The second call starts at target index three, matches `"bc"`, and returns five. The loop has used two subsequences and covered the entire target.

**Detect impossibility through zero progress**

Immediately after a pass, the code checks:

```python
if k == j:
    return -1
```

If `k == j`, scanning the entire source failed to match even the current character `target[j]`. That character does not appear anywhere in `source`. Every allowed piece is a subsequence of the same source, so starting another pass would fail in exactly the same way. No number of pieces can produce that character, and returning minus one is necessary.

This progress check avoids a separate character-set prepass. It also prevents an infinite loop: every successful iteration strictly increases `j`, while every unsuccessful iteration returns immediately.

If a pass makes any progress, the code commits it:

```python
j = k
ans += 1
```

The newly matched target segment is one nonempty subsequence, so `ans` increases exactly once. When `j` reaches `n`, the loop ends and `ans` is returned.

**Why matching the earliest possible source occurrence is safe**

Suppose the next required target character can match more than one source position. Choosing its earliest available occurrence leaves a suffix of `source` that contains every position the later choice would leave, plus possibly more positions. Therefore, the early choice cannot reduce the number of following target characters that fit in this pass.

The helper always uses this earliest-match rule because it scans `source` from left to right and accepts the first match. Repeating the argument for each next target character shows that one call to `f` matches the longest possible prefix of the remaining target that any single subsequence could match.

More formally, compare the greedy matches with any other subsequence that forms a prefix of the same remaining target. After matching the first character, the greedy source index is no later than the other subsequence's index. If this is true after some matched characters, the greedy scan takes the earliest occurrence of the next required character after its current index, so its next position is also no later. By induction, whenever another subsequence can match a certain number of characters, the greedy pass can match at least that many.

**Why longest possible passes minimize their count**

Consider the first subsequence of any valid construction. It can cover no more target characters than the greedy first pass. Replacing that first subsequence with the greedy one therefore leaves no larger target suffix to be completed.

Apply the same reasoning after the first boundary: the greedy second pass covers as much as any second subsequence can from that point, and so on. After any fixed number of passes, the greedy process has matched at least as long a target prefix as any competing process using the same number of passes.

If the greedy process needs `K` passes, no construction using fewer than `K` passes can have completed the target, because after that many passes it could not be ahead of greedy. The returned count is therefore minimal.

This proof also explains why dynamic programming is unnecessary. There is no beneficial tradeoff where matching fewer characters now allows a better global result later. Consuming the longest possible prefix always leaves the smallest remaining problem.

## Complexity detail

Let `S` be `len(source)`, `T` be `len(target)`, and `K` be the number of subsequences returned for a possible target.

One call to `f(0, j)` examines at most `S` source characters. There are exactly `K` successful calls. An impossible input may have several successful calls followed by one failing call. Thus the exact running time is `O(KS)` for a possible input and is bounded by `O(TS)` in the worst case because every successful pass matches at least one new target character, so `K <= T`.

The helper uses integer indices and reads the two existing strings. The main function stores only `m`, `n`, `ans`, `j`, and `k`. It creates no array proportional to either string, so the exact auxiliary-space complexity is `O(1)`.

The manifest records `O(AS + T)` time and `O(AS)` space, where `A` is the alphabet size. Those bounds describe a precomputed next-occurrence table rather than the repeated-scan source shown here. For each source boundary and each of the `A = 26` lowercase letters, that table stores the next index at which the letter occurs. It can be built by scanning `source` backward in `O(AS)` time and space.

Once that table exists, each target character can be processed in constant time. If no occurrence exists after the current source position, a new subsequence begins and the lookup restarts from the start of `source`. If the character does not occur even from the start, the answer is minus one. Processing all target characters takes `O(T)` additional time, producing the manifest's `O(AS + T)` total.

With a fixed lowercase alphabet, `A` is a constant, so the table method is linear in `S + T`. It is the stronger asymptotic choice when both strings can be large. The exact implementation favors a very small constant-space greedy scan and therefore has the honest worst-case bound `O(ST)`.

## Alternatives and edge cases

- **Next-occurrence table for the manifest target:** Precompute the next position of every lowercase letter from every source boundary. Then each target character takes constant-time transition work, yielding `O(AS + T)` time and `O(AS)` space.
- **Inverted indices with binary search:** Store the sorted source positions of each character. For each target character, binary-search for the first position greater than the previous match. Restart a subsequence when none exists. This takes `O(S + T log S)` time and `O(S)` space.
- **Explicit character-set precheck:** Building `set(source)` and verifying every target character can reject impossible inputs before scanning. It uses up to `O(A)` space. The exact code obtains the same fact lazily from `k == j`.
- **Concatenate source repeatedly:** One could build `source + source + ...` until `target` becomes a subsequence. Repeated immutable-string construction wastes time and space, and checking increasingly long prefixes repeats work.
- **Dynamic programming over target prefixes:** Trying every possible split into subsequences can compute the answer but is unnecessary and much slower. The earliest-match greedy property removes the need to explore competing boundaries.
- **Target is already a subsequence:** The first helper call advances `j` to `n`, `ans` becomes one, and the function returns one.
- **A target character is absent:** The first pass that reaches that character makes no progress if it is the current character at pass start. The function returns minus one rather than retrying forever.
- **Repeated target character:** If `source` contains that character only once, each pass may match only one copy, so the answer can be as large as `T`. This is the worst-case pattern for repeated scans.
- **Source length one:** A possible target must consist entirely of that one character. Each target character requires one subsequence, and any different character causes minus one.
- **Both strings nonempty:** The stated constraints make the returned count at least one for every possible input. If an empty target were allowed, the existing initialization and loop would naturally return zero.
- **Skipped source characters:** Characters not needed at the current point are harmless because a subsequence may delete any number of characters while preserving the order of those retained.
- **Order, not just membership:** Even when every target character occurs in `source`, one pass may not be enough. For example, target order can force a restart after the source pointer has passed an earlier position.
- **No input mutation:** Strings are immutable in Python, and the solution only reads them. All progress is represented by integer indices.
