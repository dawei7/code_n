## General

**Convert each possible target segment into a cost**

To create at least one run of $k$ black blocks, choose some contiguous substring of length $k$ and recolor every white block inside it. Existing black blocks need no operation, and blocks outside the chosen substring do not affect whether that target run becomes all black.

Therefore, the exact cost for one length-$k$ window is simply its number of `'W'` characters. The answer is the minimum white count among all such windows.

This reformulation proves that no more complicated recoloring plan is needed. Any successful result contains some all-black length-$k$ segment; every position that was white in that segment had to be recolored, providing the same lower bound. Recoloring precisely those whites achieves it.

**Initialize the first complete window**

The first candidate segment is `blocks[:k]`. The expression:

```python
blocks[:k].count('W')
```

counts its white blocks. Both `cnt` and `ans` receive this value. `cnt` represents the current window cost, while `ans` is the smallest cost seen so far.

Because `1 <= k <= len(blocks)`, this slice always contains exactly $k$ characters. There is no empty-window special case.

**Slide one position at a time**

The loop begins with `i = k`. On that iteration, `blocks[i]` is the new character entering at the right, and `blocks[i - k]` is the old character leaving at the left.

The code updates:

```python
cnt += blocks[i] == 'W'
cnt -= blocks[i - k] == 'W'
```

In Python arithmetic, Boolean `True` acts as one and `False` as zero. Thus, the first line increments only when the entering block is white, and the second decrements only when the leaving block was white.

Every shared character between consecutive windows remains in `cnt` automatically. This is the sliding-window benefit: after the initial count, each new window is updated in constant time rather than rescanned.

Then `ans = min(ans, cnt)` records the best target cost through the current window.

**Maintain the window invariant**

Before loop iteration `i`, `cnt` counts whites in the window ending at `i - 1`, namely indices `i-k` through `i-1`. Adding the entering position `i` and removing the leaving position `i-k` transforms it into the white count for indices `i-k+1` through `i`.

That is exactly the next length-$k$ window. The invariant is true initially by `count('W')` and remains true through every update.

**Trace a short example**

For `blocks = "WBWBBBW"` and `k = 2`, the first window `"WB"` has one white, so `cnt = ans = 1`.

The next window `"BW"` adds a white and removes a white, leaving count one. The following window `"WB"` also has one. When the window `"BB"` is reached, a black enters and a white leaves, reducing `cnt` to zero. `ans` becomes zero, proving that no recoloring is required. Remaining windows cannot improve below zero.

The exact code continues scanning even after reaching zero. An optional early return could stop immediately, but continuing remains linear and simple.

**Why the minimum window count is globally optimal**

For every possible length-$k$ position, the algorithm computes exactly how many white blocks it contains. Recoloring all those whites produces a valid run using that many operations, so each count is an achievable cost.

Conversely, consider any sequence of recolorings that succeeds. The final string contains at least one run of $k$ black blocks. Every originally white block in that particular segment must have been recolored, so the number of operations is at least that segment's original white count. The algorithm's minimum is no larger than this count.

Thus, the minimum scanned count is both achievable and a lower bound on every successful plan. It is exactly the minimum number of operations.

**Why extra recolorings never help**

Only white-to-black changes are allowed. Recoloring a white outside the selected run cannot reduce how many whites remain inside it. Once one target window is fixed, its cost is independent of all outside positions. The method correctly avoids considering supersets of necessary operations.

## Complexity detail

Let $n$ be the string length. Counting whites in the initial length-$k$ slice takes $O(k)$ time. The loop processes each remaining character once, taking $O(n-k)$ time. Total time is $O(k+n-k)=O(n)$.

The slice `blocks[:k]` creates a temporary string of length $k$ in Python, so the exact implementation can use $O(k)$ transient space during initialization. After that expression is evaluated, the running algorithm stores only scalar values and uses $O(1)$ auxiliary space. The manifest reports $O(1)$ under the usual algorithmic interpretation that the initial window count can be performed without materializing a slice; operationally, Python slicing deserves this small distinction.

The returned integer itself uses constant space.

## Alternatives and edge cases

- **Rescan every window:** Calling `count('W')` on each length-$k$ slice is correct but takes $O(nk)$ time in the general case.
- **Prefix sums:** Build cumulative white counts and query each window in $O(1)$. This gives $O(n)$ time but uses $O(n)$ extra space.
- **Early return at zero:** No answer can beat zero, so the scan may stop when an all-black window appears. The exact code simply finishes the short linear pass.
- **`k = 1`:** The answer is zero if any black block exists, otherwise one.
- **`k = n`:** There is only the initial window, so the answer is the total number of white blocks in the entire string.
- **All blocks black:** Initial or later window count is zero and no recoloring is needed.
- **All blocks white:** Every length-$k$ window costs exactly $k$ operations.
- **Entering and leaving colors match:** Their Boolean contributions cancel, leaving `cnt` unchanged.
- **Overlapping candidate runs:** Sliding updates reuse their shared positions while still evaluating every possible start.
- **Only one required occurrence:** Taking the minimum over windows is sufficient; there is no need to make all windows black.
