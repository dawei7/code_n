## General

The iterator must consume a potentially enormous decoded sequence without expanding it. The encoded array already groups equal consecutive values into runs, so the state needs only a run position and an offset inside that run.

The object stores:

- `self.i`: the index of the current run's count in `encoding`. Its value is always even.
- `self.j`: how many elements of the current run have already been consumed.

For current pair `encoding[i], encoding[i + 1]`, the number of remaining copies is

```text
encoding[i] - j
```

and their value is `encoding[i + 1]`.

**When the request crosses the current run.** If remaining copies are fewer than requested `n`, the call consumes all of them. It subtracts that remaining amount from `n`, advances `i` by two to the next count-value pair, resets `j` to zero, and continues.

The comparison is strict:

```text
if remaining < n
```

When remaining equals `n`, the last exhausted element belongs to the current run, so the method must return the current run's value. The else branch increments `j` by `n` and returns that value. The now-exhausted run will be skipped at the beginning of the next call because its remaining count is zero.

**Zero-length runs need no special branch.** If a run count is zero, remaining is zero. Since every request has `n >= 1`, zero is less than `n`. The loop subtracts zero, advances to the next pair, and continues.

**Why partial consumption is represented correctly.** Suppose a run contains five copies and `j = 2`. Exactly three copies remain. A request for two follows the else branch, changes `j` to four, and returns the run value. One copy remains for the next call. No decoded elements are allocated or shifted.

**Failure after partial exhaustion.** A call may consume the last available elements and still need more. When `i` reaches the encoded-array length, no current run exists, and the method returns `-1`. This is correct even though some elements were exhausted during the failed call: the contract says return the last requested element, and that element does not exist.

For instance, if exactly one encoded element remains and `next(2)` is called, the loop consumes that one element, reduces the outstanding request to one, and then reaches the end. Returning the remaining element's value would be wrong because it was only the first of the two requested positions; the second requested position has no value. The state still remains exhausted for all later calls.

For encoding `[3,8,0,9,2,5]`:

- `next(2)` consumes two of the three 8s, leaves `j=2`, and returns 8.
- `next(1)` consumes the final 8, sets `j=3`, and returns 8.
- The next request first skips the exhausted 8 run, then skips the zero-length 9 run, consumes a 5, and returns 5.

**State invariant.** At the start of each loop iteration, all encoded runs before `i` are fully exhausted, and `j` elements of the run at `i` are exhausted. The cross-run branch fully consumes that run and restores the invariant for `i+2`. The within-run branch consumes exactly the request and returns the correct last value. By induction over calls and loop iterations, state always matches the conceptual decoded iterator position.

The constructor keeps a reference to the supplied encoding but does not modify its counts. All consumption is represented by `i` and `j`.

## Complexity detail

Let $m$ be the number of encoded count-value pairs and $q$ the number of calls to `next`. Each run is advanced past at most once over the object's lifetime. Each call also performs at least one constant amount of work.

- **Total time across all calls:** $O(m+q)$.
- **Amortized time per call:** $O(1)$, although one call can skip many runs.
- **Space complexity:** $O(1)$ auxiliary space beyond the referenced input encoding.

The decoded sequence length may be far larger than $m$, but it never appears in time or space complexity.

## Alternatives and edge cases

- **Expand the sequence:** Counts may be as large as $10^9$, making materialization impossible.
- **Subtract directly from encoded counts:** This can work in place but mutates caller data. The offset field preserves the input.
- **Prefix sums plus binary search:** Record cumulative run lengths and locate each cumulative consumed position. It gives $O(\log m)$ per call and uses $O(m)$ extra space, unnecessary for forward-only iteration.
- **Zero-count run:** It is skipped automatically without reducing the request.
- **Request exactly remaining run length:** Return that run's value, then skip it on the next call.
- **Request spanning several runs:** The loop subtracts each exhausted run until the final requested element is located.
- **Request exceeds all remaining elements:** Existing elements are still exhausted and `-1` is returned.
- **Repeated values in adjacent runs:** They may remain separate in the encoding; processing them separately gives the same decoded behavior.
- **Large counts and requests:** Only integer subtraction and comparison are used, so Python handles the range exactly.
- **Nonempty request:** `n >= 1` ensures zero runs always advance rather than return.
- **Even encoding length:** Every count at `i` has a corresponding value at `i + 1`.
- **No rewind:** The design is a forward iterator; exhausted state is permanent across calls.
