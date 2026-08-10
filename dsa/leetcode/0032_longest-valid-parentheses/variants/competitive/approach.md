## General

**Use balance counters, but scan in both directions**

In a left-to-right scan, treat `'('` as `+1` and `')'` as `-1`. A negative balance means a closer has no opener inside the current segment, so no valid substring can cross that point. Whenever balance returns to zero without having gone negative, the segment since the last invalid boundary is balanced and well formed.

One forward scan is not enough. In `"(()"`, balance never becomes negative and never returns to zero after the first character, yet the suffix `"()"` is valid. Excess opening parentheses hide valid suffixes. Scanning again from right to left with the roles reversed exposes those cases.

**Generalize both scans with one helper**

The nested function `length(it, start, c)` accepts:

- `it`, the index order;
- `start`, a boundary just outside the current candidate segment; and
- `c`, the character counted as opening in that scan direction.

For the forward pass, indices increase, `start = -1`, and `c = '('`. For the reverse pass, indices decrease, `start = len(s)`, and `c = ')'`. A closing parenthesis becomes the “opening” event when reading backward because it must be encountered before the opener it matches.

**Maintain a directional depth**

At each scanned index:

```python
if s[i] == c:
    depth += 1
else:
    depth -= 1
```

`depth` counts unmatched directional opening characters since the last invalid boundary. In the forward pass this is ordinary unmatched `'('`; in reverse it is unmatched `')'` waiting for `'('` farther left.

If `depth < 0`, the current opposite character cannot be matched within the active segment. The source sets

```python
start, depth = i, 0
```

The invalid character becomes the new excluded boundary. Any candidate crossing it would inherit the same unmatched character, so resetting loses no valid substring.

**Measure a valid segment whenever depth becomes zero**

If `depth == 0`, every directional opener since `start` has been paired, and the balance never went negative after the last reset. The whole segment between the boundary and `i` is valid. Its length is

```python
abs(i - start)
```

In the forward pass, `i > start`, so this is `i - start`. With initial boundary `-1`, a valid prefix ending at index one has length `1 - (-1) = 2`.

In the reverse pass, `i < start`, so the raw difference is negative. `abs` gives the number of characters between the exclusive boundary and current index. Initial boundary `len(s)` correctly measures a valid suffix extending to the final character.

The helper keeps the maximum balanced segment length found in that direction.

**Why the forward scan catches surplus closers**

Consider `")()())"`. At index zero, depth becomes negative, so zero is recorded as an invalid boundary. The next four characters `"()()"` maintain nonnegative balance and return to zero at index four, giving length `4 - 0 = 4`. The final closer becomes another invalid boundary.

Any valid substring cannot cross a point where forward closers outnumber openers, so the reset is exact.

**Why the reverse scan catches surplus openers**

For `"(()"`, reverse traversal starts at the final `')'`, which is counted as directional opening. The `'('` at index one reduces depth to zero, and `abs(1 - 3) = 2` records `"()"`. Continuing to index zero makes depth negative in reverse orientation, identifying the unmatched leading opener as a boundary.

Thus the reverse scan is not redundant; it handles valid regions obscured by unmatched `'('` in a forward-only counter.

**Why taking the maximum of both passes is complete**

Every valid substring has equal counts and obeys the prefix condition in its natural direction. If it lies after a surplus closer, the forward reset isolates it and a zero balance records a segment at least as long. If a candidate is instead limited by surplus openers that never force a forward reset, the symmetric reverse scan treats those openers as invalid opposite characters and isolates the valid region from the other side.

Both helpers report only intervals whose directional balance never became negative and ends at zero, which is exactly the well-formed condition. Taking their maximum therefore returns the longest valid substring and never an invalid length.

**Understand boundaries rather than substring starts**

`start` names an excluded invalid index, not the first included character. This explains why the length is the difference rather than the difference plus one. After a reset at index `q`, the next candidate begins at `q + 1` forward or `q - 1` backward. The distance to a later balanced endpoint already counts all included positions.

## Complexity detail

Let $n$ be the string length.

- **Time complexity: $O(n)$.** The forward range visits all $n$ indices once, and the reversed range visits them once more. Each visit performs constant work, so $2n$ simplifies to $O(n)$.
- **Auxiliary space: $O(1)$.** The helper stores scalar counters, boundaries, and iterator state. Python `range` and `reversed(range(...))` are lazy objects and do not construct arrays of all indices.

The two calls execute sequentially, so their local variables do not multiply with input size.

## Alternatives and edge cases

- **Dynamic programming:** Store the longest valid suffix ending at each position. It is linear time but uses $O(n)$ space in the exact Optimal source.
- **Stack of indices:** It naturally records unmatched openers and invalid closer boundaries, using up to $O(n)$ memory.
- **Forward counter only:** It misses valid suffixes hidden behind surplus openers, such as `"(()"`.
- **Reverse counter only:** Symmetrically misses regions separated by surplus closers.
- **Empty input:** Both ranges are empty and both helpers return zero.
- **One character:** Neither scan reaches a nonzero balanced segment.
- **Already valid whole string:** At least the forward pass returns its full length.
- **Nested and adjacent forms:** Both produce nonnegative directional balance and zero at their valid endpoint.
- **Invalid characters:** The contract permits only parentheses, so the `else` branch safely means the opposite parenthesis.
- **`abs` in reverse:** It converts decreasing-index boundary distance to a positive substring length; removing it would yield negative candidates.
- **Reset index:** The invalid character itself is excluded by assigning it to `start`.
