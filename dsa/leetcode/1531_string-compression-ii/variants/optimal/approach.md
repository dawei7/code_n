## General

**Define a suffix problem with a deletion budget**

`dp[start][deletions]` is the minimum compressed length obtainable from suffix `s[start:]` when at most `deletions` characters may still be deleted.

The table has `n+1` rows and `k+1` budget columns. At `start = n`, the suffix is empty, so its compressed length is zero for every remaining budget.

Filling starts from `n-1` and moves backward, ensuring every transition to `end+1` or `start+1` is already known.

**Option one: delete the current character**

If at least one deletion remains, the source can discard `s[start]` and use

`dp[start + 1][deletions - 1]`.

This option matters when removing the character merges runs on either side or avoids paying for a short run.

**Option two: keep it as the next run's character**

If `s[start]` is kept, it begins the first encoded run of this suffix. The inner loop chooses how far that run's construction extends.

`kept` counts occurrences equal to `s[start]` from `start` through `end`. `removed` counts all different characters in that interval. Deleting those different characters makes the equal occurrences consecutive in the remaining string, forming one run.

If `removed > deletions`, this and every later endpoint are unaffordable, so the loop breaks.

For an affordable endpoint, the remaining suffix begins at `end+1` with budget `deletions - removed`. The candidate length is the encoded length of the created run plus the optimal table value for that remaining suffix.

**How run length changes encoded length**

A run of one character is encoded as just its letter, length one.

Counts two through nine use one count digit, giving length two. Counts ten through ninety-nine use two digits, giving length three. Count one hundred uses three digits, giving length four.

The source assigns:

- One when `kept = 1`.
- Two when `2 <= kept <= 9`.
- Three when `10 <= kept <= 99`.
- Four when `kept >= 100`.

The input length is at most one hundred, so no larger count width is needed.

**Why enumerating end positions is complete**

Consider an optimal result where `s[start]` is kept. Its first compressed run contains that character plus some later equal occurrences. Every different character between the first and last kept occurrence of the run must be deleted; otherwise it would break the run.

Choose `end` at the last input position consumed while forming that run. The inner loop reaches this endpoint, records exactly those equal characters as `kept` and intervening different ones as `removed`, then delegates the rest optimally to `dp[end+1]`.

If the optimal plan deletes `s[start]` instead, the first transition covers it. Thus every optimal plan appears among the candidates.

Conversely, each candidate describes a legal deletion set and a valid first run followed by an optimal suffix plan.

The endpoint need not stop exactly at an equal character for completeness, although candidates ending after an extra different character spend a deletion without enlarging the current run and usually cannot improve the result. Enumerating every endpoint keeps the transition simple and still stays within the stated bound.

**Why at most k is represented correctly**

The state budget is a maximum, not an exact number that must be spent. Base states are zero for every leftover budget, so a plan may reach the end with unused deletions.

Transitions subtract only deletions actually used. Therefore, `dp[0][k]` minimizes over every plan using no more than `k` deletions.

**The infinity sentinel**

`infinity = n + 1` exceeds every possible compressed length, since leaving the original string uncompressed cannot require more than `n` characters. It safely marks states before real candidates lower them.

For every nonempty suffix, at least keeping its first character is feasible, so values become finite.

## Complexity detail

There are $O(nk)$ table states. For each state, the endpoint loop can inspect up to $O(n)$ positions, and all work per endpoint is constant. Total time is $O(n^2k)$.

The table contains $(n+1)(k+1)$ integers, using $O(nk)$ space, matching the manifest. Loop variables add constant space.

The source does not construct deleted strings or compressed strings. It tracks only their minimum lengths.

## Alternatives and edge cases

- **Memoized character-by-character DP:** Track index, previous character, run count, and remaining deletions. It directly models compression thresholds but has a larger conceptual state.
- **Brute-force deletion subsets:** There can be exponentially many, so it is infeasible.
- **k equals n:** Every character may be deleted, and the empty result has compressed length zero.
- **k equals zero:** Only keep-run transitions are affordable, reproducing ordinary run-length encoding.
- **Single-character run:** No digit one is written, so its encoded length is one.
- **Threshold from nine to ten:** The count gains a digit, increasing encoded length from two to three.
- **Threshold from ninety-nine to one hundred:** Encoded length increases from three to four.
- **Deleting separators:** Removing different characters between equal groups can merge them into one shorter encoded run.
- **Unused deletions:** They are allowed because the contract says at most k.
- **Input length bound:** It is why the run-length cases stop at three count digits.
