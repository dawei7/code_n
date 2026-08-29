## General

**Turn the goal into a limit on the opposite answer**

A consecutive block can be made entirely `T` when it contains at most `k` occurrences of `F`, because those are precisely the positions that must be changed. Symmetrically, a block can be made entirely `F` when it contains at most `k` occurrences of `T`.

The source handles these two possible final answers separately. The helper `f(c)` finds the greatest window length containing at most `k` copies of character `c`. Calling `f("F")` therefore finds the best all-`T` block, while `f("T")` finds the best all-`F` block. The final `max` chooses the better possibility.

This separation is especially simple because the alphabet contains only two characters. Once all occurrences of one character in a window are changed, every character in that window must equal the other character.

**Meaning of the helper's state**

Inside `f(c)`, `l` is the left boundary of an implicit window and `cnt` is the number of occurrences of `c` currently represented by that window. The loop reads the string from left to right. The current loop character is the new right endpoint.

The expression `ch == c` is a Boolean. In Python, `True` contributes one and `False` contributes zero when added to an integer, so

`cnt += ch == c`

increments the count only when the newly included answer equals `c`.

If the expanded window has `cnt <= k`, it is feasible: every copy of `c` can be changed, so the window becomes uniform. The helper leaves `l` fixed, which makes the represented window one position longer.

If `cnt > k`, the expanded window cannot be made uniform with the available changes. The code removes the character at the old left boundary from the count when appropriate and increments `l` once:

`cnt -= answerKey[l] == c`

followed by `l += 1`. Adding one position on the right and removing one on the left keeps the candidate length from growing.

**Why moving the left boundary only once is enough**

A conventional sliding window would use a `while` loop until the current window becomes valid again. The exact source deliberately uses only `if`. That is correct, but its invariant is subtler: the represented window need not be valid after every iteration.

Suppose the greatest feasible length discovered so far is $L$. To improve the answer, a future step must find a feasible window of length $L+1$. When adding a new right endpoint creates an invalid length-$L+1$ window, there is no benefit in shrinking below length $L$. A feasible window of length $L$ is already known from earlier work. The code instead advances `l` exactly once, retaining a candidate of length $L$, and the next iteration tests the next possible length-$L+1$ window.

If that retained length-$L$ candidate is itself invalid, that does not invalidate the earlier result. Its maintained count still accurately describes the candidate. Further one-position shifts continue testing later windows of the same prospective larger length. As soon as an expanded candidate has at most `k` copies of `c`, `l` does not move, so the maintained length grows. Thus the algorithm grows its recorded best only when a genuinely feasible larger window is found.

**A concrete trace**

Take `answerKey = "TTFTTFTT"` and `k = 1`. To search for an all-`T` block, `f("F")` treats `F` as the character that costs a change.

The first five characters, `TTFTT`, contain one `F`, so they form a feasible length-five window. Adding the next `F` produces `TTFTTF` with two costly characters. The helper advances the left boundary once and keeps searching without increasing the candidate length. As the candidate shifts right, the old `F` eventually leaves it. The suffix `TTFTT` is another feasible length-five window, but no length-six window contains only one `F`. The helper returns five.

The other call treats `T` as costly and searches for an all-`F` block. Taking the maximum of the two results returns five.

**Why `len(answerKey) - l` is the answer**

At every iteration, the right boundary advances exactly once. The left boundary advances only when the attempted one-position growth fails. Therefore the represented length never decreases: it either grows by one or stays unchanged.

After the last character has been processed, that nondecreasing represented length is `len(answerKey) - l`. Every growth was authorized by a window with at most `k` costly characters, so this length is achievable. Conversely, the code examines every next candidate capable of increasing the current best; an invalid candidate is shifted rather than allowed to increase the length. No larger feasible window can be skipped. The returned value is consequently the greatest feasible length for that chosen costly character.

**Why both helper calls prove the original result**

Every valid final block is either all `T` or all `F`. An all-`T` block is counted by the pass that limits `F` occurrences, and an all-`F` block is counted by the pass that limits `T` occurrences. The two passes cover all possible uniform blocks, and each helper returns the best block in its category. Their maximum is exactly the requested answer.

The method counts changes inside a chosen substring only. Answers outside the substring do not affect its consecutiveness and never need to be changed.

## Complexity detail

Let $N=\lvert\texttt{answerKey}\rvert$. Each helper traverses all $N$ characters once. Every iteration performs constant-time comparisons, additions, and at most one left-boundary update. Running the helper twice takes $2N$ iterations, which is $O(N)$ time.

The algorithm stores only `cnt`, `l`, the loop character, and the helper's parameter. It neither copies the string nor builds a frequency table whose size grows with $N$. Its auxiliary space is $O(1)$. The two helper calls execute sequentially, so their constant state is not multiplied into an input-dependent space cost.

## Alternatives and edge cases

- **Standard valid-window loop:** Maintain counts of both characters and repeatedly move the left boundary while the smaller count exceeds `k`; it is also $O(N)$ and keeps the current window valid at all times.
- **One pass with the majority count:** Track the largest character frequency in the window and require `window length - maximum frequency <= k`; for this two-character problem it gives the same linear bound.
- **Binary search on the answer:** Test each proposed length with a fixed-size window, but this costs $O(N\log N)$ rather than $O(N)$.
- **Brute-force substrings:** Checking every substring and its character counts is at least quadratic and unnecessary for $N$ up to $5\cdot10^4$.
- **All answers already equal:** One helper returns the full length without needing any change.
- **`k` equals the string length:** Every position may be changed, so both categories can reach the full length.
- **Unused changes:** The operation is allowed at most `k` times; a valid block does not need to spend the entire budget.
- **Alternating answers:** The maintained costly-character count determines exactly how far a uniform block can extend.
- **Equal best `T` and `F` blocks:** The final `max` needs only the common length, not which final character achieves it.
- **Boolean arithmetic:** `ch == c` and `answerKey[l] == c` are intentionally used as zero-or-one values in Python.
- **Temporary invalid candidate:** The one-step `if` version may retain an invalid window of the already-known length; its proof relies on searching only for a strictly larger answer.
- **Input preservation:** The string is read but never modified; changes are considered conceptually.
