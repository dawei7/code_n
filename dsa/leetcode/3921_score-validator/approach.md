## General

The events must be processed in order, and each event changes only two scalar totals. The source directly simulates the valid prefix:

- numeric events add their integer value to `score`;
- `"W"` increments `counter` and may stop processing;
- `"WD"` and `"NB"` each add one to `score`.

No earlier state besides the two accumulated totals is needed.

**Starting state**

The assignment

```text
score = counter = 0
```

matches the problem's initial state. The forward loop then handles events in their given order, which is essential because reaching the tenth `"W"` makes every later event irrelevant.

**Recognizing numeric events**

Allowed numeric strings are `"0"`, `"1"`, `"2"`, `"3"`, `"4"`, and `"6"`. For each one, `event.isdigit()` is true.

The source converts the event with `int(event)` and adds it to `score`. This handles `"0"` correctly: adding zero changes nothing, but the event is still processed.

The constraints guarantee there are no other digit strings, so the broad `isdigit` recognition does not accept an unintended event under the contract.

**Handling a \(W\) event**

The explicit second branch tests `event == "W"`. It increments `counter` by one and adds nothing to `score`.

Immediately afterward:

```text
if counter == 10:
    break
```

The tenth `"W"` is itself processed—the counter reaches ten—and then the loop stops before reading the next array entry.

Because the loop breaks at exactly ten, `counter` can never exceed ten. An eleventh `"W"` or any intervening score event after the tenth one is ignored.

**Why the final \(else\) means exactly one point**

After the numeric and `"W"` branches fail, the constraints leave only `"WD"` and `"NB"`. Both contribute exactly one point and do not affect the counter.

The shared

```text
else:
    score += 1
```

therefore implements both symbolic score events without duplicating code.

This is safe because the event domain is closed. If arbitrary strings were allowed, the branch would incorrectly award one point to unknown events, but no such inputs belong to the contract.

**A loop invariant**

After processing any prefix that ends before the stop condition:

- `score` equals the sum of all numeric values plus one for every `"WD"` and `"NB"` in that processed prefix;
- `counter` equals the number of `"W"` entries in the prefix.

Each branch applies exactly the current event's contribution and leaves the unrelated accumulator unchanged. Thus the invariant is preserved one event at a time.

If the tenth `"W"` occurs, the break ends the processed prefix at that event, inclusive. If it never occurs, the loop exhausts the whole array. These are precisely the two stopping cases in the statement.

**Examples**

For `["1","4","W","6","WD"]`:

- `"1"` and `"4"` make the score 5;
- `"W"` makes the counter 1;
- `"6"` makes the score 11;
- `"WD"` makes the score 12.

The result is `[12,1]`.

For eleven consecutive `"W"` events, the first ten increment the counter to ten. The loop breaks immediately, and the eleventh is ignored. The result is `[0,10]`.

**Why the returned pair is exact**

Every processed event belongs to one of the three mutually exclusive branches and contributes exactly according to its rule. The loop visits all and only events in the permitted prefix. Returning `[score, counter]` therefore reports the final state after the specified stopping behavior.

## Complexity detail

Let $N=\lvert\texttt{events}\rvert$ and let $P$ be the number of events actually processed before exhaustion or the tenth `"W"`.

The loop performs constant work per processed event, so its precise running time is

$$
O(P),
$$

with worst case

$$
O(N).
$$

The source stores two integers and the current event reference. Its auxiliary-space complexity is

$$
O(1).
$$

The returned list always contains exactly two integers and is also constant size. The input event array is never modified.

Early termination can make execution much shorter than $N$, but does not change the worst-case bound when fewer than ten `"W"` events occur.

## Alternatives and edge cases

- **Mapping score events to values:** A dictionary can map every allowed token to its score contribution, but `"W"` still needs separate counter and stop logic.
- **Process a sliced prefix:** Finding the tenth `"W"` first and then scanning that prefix requires an extra pass; direct simulation stops naturally.
- **Numeric zero:** `int("0")` adds zero, as required.
- **No \(W\) events:** The counter remains zero and every array element is processed.
- **Exactly ten \(W\) events:** Processing ends at the final one if it is last, or ignores later entries if it occurs earlier.
- **More than ten \(W\) events:** Only the first ten are processed; the counter remains ten.
- **Score event after the tenth \(W\):** It is ignored because `break` has already ended the loop.
- **\(WD\) and \(NB\):** Neither string is considered numeric, and both reach the one-point fallback.
- **Closed event domain:** The fallback relies on the guarantee that every nonnumeric non-`W` token is `WD` or `NB`.
- **Order matters:** Score events before the tenth `W` count, while identical events after it do not.
- **Input preservation:** Iteration reads tokens without changing the list.
