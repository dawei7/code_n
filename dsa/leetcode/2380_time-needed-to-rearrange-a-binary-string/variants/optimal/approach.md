## General

**Simulate one simultaneous second at a time**

The exact implementation follows the process literally. As long as the current string contains `"01"`, it replaces every occurrence with `"10"` and increments the elapsed-second counter.

The transformation moves a `'1'` one position to the left across a neighboring `'0'`. Equivalently, the zero moves one position right. When no `"01"` remains, no one has a zero immediately to its left, so all ones must appear before all zeros. The process is then finished.

**Why one `str.replace` models simultaneous changes**

Python's:

```python
s.replace('01', '10')
```

finds non-overlapping occurrences in the original string and produces a new string with all of them replaced. This matches the requirement that every eligible pair changes during the same second.

Occurrences of `"01"` cannot overlap one another. For two length-two occurrences to begin one position apart, the shared character would need to be both the first occurrence's `'1'` and the second occurrence's `'0'`, which is impossible. Therefore, there is no conflict or ambiguity among the pairs replaced in one call.

It would be different to scan a mutable character array left to right and immediately change a pair, then allow a newly created `"01"` to change again in the same pass. That would perform sequential rather than simultaneous updates. Creating a new Python string from the old one avoids this error.

**Use the presence test as the loop condition**

The loop checks:

```python
while s.count('01'):
```

`count` returns zero when no occurrence exists and a positive integer otherwise. Python interprets zero as false and a positive count as true. The exact number of pairs is not otherwise used; the condition merely asks whether another second is necessary.

One could write `while '01' in s` to express that intent more directly, but both scan for the pattern and make the same decision.

**Trace simultaneous movement**

For `s = "0110101"`, the first string contains several eligible `"01"` pairs. Replacing all of them based on the same old string yields `"1011010"`. The algorithm increments `ans` to one only after completing that whole simultaneous step.

Repeating produces:

```text
0110101
1011010
1101100
1110100
1111000
```

Four transformations occurred. The final form has all ones to the left of all zeros and contains no `"01"`, so the loop stops and returns four.

For `"11100"`, the initial count is zero. The body never runs, and the returned time is zero.

**Why termination is guaranteed**

Consider the number of inverted zero-one pairs in which a zero appears before a one somewhere later in the string. Every adjacent `"01"` swap changes that particular pair into the correct `"10"` order. Adjacent swapping does not create a new long-range zero-before-one pair that was absent; it moves the one left and the zero right.

Thus, every second containing at least one replacement strictly reduces a finite nonnegative disorder measure. Eventually, no replacement remains possible.

Another view is that each one moves only left and each zero moves only right. Since positions are finite, movement cannot continue forever.

**Why the returned counter is exact**

The string stored before each loop body is exactly the configuration after `ans` seconds: this holds initially at time zero. One call to `replace` applies precisely all rule-mandated swaps for the next second, so after incrementing, the invariant holds again.

The loop exits exactly when the rule would make no change. Consequently, `ans` is neither early nor late; it is the number of simultaneous rounds required by the stated process.

**Exact implementation versus the linear recurrence**

The Optimal manifest describes tracking how many zeros have appeared and the finishing time of each later one. That method computes the answer without constructing intermediate strings. The shipped source instead calls `count` and `replace` once per second.

This distinction affects complexity. The simulation is correct and easy to visualize, but it does not satisfy the follow-up's $O(n)$ time bound. A faithful explanation must not claim the linear recurrence is executed when it is not present.

## Complexity detail

Let $n$ be the string length and $T$ the number of seconds returned. Both `s.count('01')` and `s.replace('01', '10')` scan a length-$n$ string, so each loop round costs $O(n)$. There is also one final $O(n)$ condition check. Exact time is $O(nT)$.

For this process, $T=O(n)$: a one moves left at most $n-1$ positions, with additional waiting caused by earlier ones still bounded by the number of positions. Therefore, worst-case time is $O(n^2)$, not the manifest's $O(n)$.

Strings are immutable, so `replace` allocates a new length-$n$ string. Peak auxiliary storage is $O(n)$, though old strings become reclaimable. `ans` itself is constant space.

## Alternatives and edge cases

- **Linear zero-count recurrence:** Scan left to right, count zeros, and for each one after a zero set its finishing time to `max(time + 1, zeros)`. This achieves the follow-up's $O(n)$ time and $O(1)$ space.
- **Mutable two-buffer simulation:** Build each next state from the previous one explicitly. It still takes $O(nT)$ time but makes simultaneous semantics obvious.
- **In-place sequential swapping:** Careless mutation can move a character more than once in one second and is incorrect.
- **Already arranged as ones then zeros:** There is no `"01"`, so the answer is zero.
- **All zeros or all ones:** No opposite adjacent pair exists, and the answer is zero.
- **One character:** It cannot contain a length-two pattern, so no second is needed.
- **Alternating string:** Many swaps occur per round, but `replace` handles all non-overlapping occurrences simultaneously.
- **New pair created by a round:** It is processed only by the next loop iteration, exactly one second later.
- **Pattern detection cost:** `count` computes more information than needed; `'01' in s` would be a clearer presence check with the same asymptotic scan.
