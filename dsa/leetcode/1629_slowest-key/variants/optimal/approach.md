## General

**Compute durations from cumulative release times**

`releaseTimes[i]` is an absolute time, not the duration of press `i`. The first key starts at time 0, so its duration is simply `releaseTimes[0]`. Every later key starts exactly when the preceding key is released, which makes its duration

$$
\textit{releaseTimes}[i]-\textit{releaseTimes}[i-1].
$$

Because release times are strictly increasing, every duration is positive.

The source initializes `ans` to the first character and `mx` to the first release time. This treats the first press as the best press seen so far before the loop begins. The loop can then start at index 1 and use the same “compare current press with best press” logic for every remaining event.

**Maintain both parts of the ranking rule**

A press is preferable when it has a longer duration. If durations tie, its key is preferable when that key is lexicographically larger. The source encodes these priorities in one condition:

`d > mx or (d == mx and ord(keysPressed[i]) > ord(ans))`.

The first part handles the primary criterion. A strictly longer press always replaces the current answer, regardless of its letter.

The parenthesized second part is considered only when durations are equal. `ord` converts each lowercase letter to its character code. Lowercase English letters have increasing codes from `a` through `z`, so comparing those codes is equivalent to comparing the one-character strings lexicographically.

When either part is true, both `mx` and `ans` are updated together. Keeping them synchronized is essential: `mx` must always describe the particular best ranking represented by `ans`.

**Why repeated keys need no special storage**

The same key can appear several times with different durations, but the problem asks for the key belonging to the best individual keypress. It does not ask for the total time per key or even each key's maximum stored separately.

The scan compares every press as it occurs. If a later press of the same key is longer, it can replace the current best; if shorter, it is ignored. If the same letter ties itself, the lexicographic comparison is false, but retaining either occurrence yields the same returned key. A map from keys to durations would therefore store information that is not needed for the final decision.

**Trace the tie-breaking example**

For `releaseTimes = [9, 29, 49, 50]` and `keysPressed = "cbcd"`:

- The first `c` lasts 9, so initialization gives `mx = 9` and `ans = "c"`.
- The `b` lasts `29 - 9 = 20`. Since 20 is greater than 9, update to `mx = 20` and `ans = "b"`.
- The next `c` lasts `49 - 29 = 20`. Its duration ties `mx`, and `c` is lexicographically larger than `b`, so update only because of the tie rule.
- The `d` lasts `50 - 49 = 1`, which cannot replace the duration-20 winner.

The result is `"c"`. Notice that `d` being the lexicographically largest seen letter is irrelevant because its duration is shorter. Lexicographic order is only a secondary criterion.

**The scan invariant**

After processing indices 0 through $i$, `mx` is the greatest duration among those keypresses. Among presses attaining `mx`, `ans` is the lexicographically largest associated key.

Initialization establishes the invariant for the prefix containing only index 0. For the next press:

- If its duration is greater, it is the unique new duration maximum, so replacing both variables restores the invariant.
- If its duration is equal and its key is larger, the maximum duration stays the same but the correct tie winner changes, so replacement restores the invariant.
- Otherwise, the existing pair still outranks the current press, so leaving it unchanged preserves the invariant.

By induction, the invariant holds after the final keypress. At that point it is exactly the requested answer.

**Why a single pass is enough**

Each duration depends only on the current and previous release times. Each ranking decision depends only on the current event and the best event summarized by `mx` and `ans`. No future event can change a past duration, and a past loser never needs to be reconsidered: if it ranked below the saved best at the time, both are compared under the same fixed ordering, so it can never outrank that saved candidate later.

This is a streaming maximum with a compound comparison key. Conceptually, every press is ranked by the pair `(duration, character)`, with both components preferred in larger order. The source writes the comparison explicitly rather than allocating tuples.

## Complexity detail

Let $n$ be the number of keypresses. Initialization is constant time, and the loop processes indices 1 through $n-1$ once. Each iteration performs one subtraction and a constant number of comparisons and assignments. The total time complexity is $O(n)$.

The source stores only `ans`, `mx`, `i`, and `d` in addition to the input. None grows with $n$, so auxiliary space complexity is $O(1)$.

There is no extra array of durations. Computing `releaseTimes[i] - releaseTimes[i - 1]` on demand avoids $O(n)$ additional storage. Calling `ord` is constant time for each one-character lowercase key.

The absolute release times may be as large as $10^9$, but subtraction remains constant-time integer arithmetic in the standard model and every calculated duration fits within the same bound.

## Alternatives and edge cases

- **Build a duration array first:** Calculate all durations, then find the maximum with the tie rule. This remains $O(n)$ time but uses $O(n)$ extra space and separates two steps that can be combined.
- **Map each key to its longest press:** After one pass, scan the at most 26 keys for the best duration. It is correct but unnecessary because the answer concerns the best individual press and can be maintained directly.
- **Fixed 26-entry duration array:** This gives $O(1)$ bounded storage and can scan letters from `z` downward for ties. The direct scalar solution is still simpler.
- **Use tuple comparison:** Tracking `max((duration, key), ...)` captures the same priority because Python compares tuple components in order. The explicit condition makes the primary duration and secondary letter criteria easier to see.
- **First keypress:** Its start time is zero, so its duration is `releaseTimes[0]`. Subtracting `releaseTimes[-1]` would be incorrect Python wraparound.
- **Equal longest durations:** Choose the lexicographically larger key. The condition must use both equality of durations and a larger character.
- **A lexicographically larger but faster-released key:** It cannot win unless its duration ties the maximum. Letter order never overrides a shorter duration.
- **Repeated presses of one key:** They are separate events. The longest individual occurrence participates normally, and returning the character does not require returning which occurrence won.
- **Strictly increasing release times:** Durations are positive, so the first initialized press is always a valid baseline.
- **Two presses only:** Initialization handles the first and the single loop iteration compares the second, covering both possible winners and a tie.
- **Using release time as duration:** Only index 0 has duration equal to its release time. Later absolute release times must have the previous release subtracted.
- **Character comparison:** `ord` is safe because inputs are lowercase English letters. Direct `keysPressed[i] > ans` would be equivalent for these one-character strings.
