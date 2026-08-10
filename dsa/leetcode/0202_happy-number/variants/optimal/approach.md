## General

**Follow a deterministic sequence of numbers**

Each positive integer has exactly one successor: the sum of the squares of its
decimal digits. Repeatedly applying that rule creates one deterministic chain.
The chain either reaches 1, after which the number is happy, or revisits an
earlier value, after which the same cycle repeats forever.

The exact optimal source detects repetition with set `vis`. It does not use
Floyd's two-pointer cycle detector, despite the manifest summary saying that it
does.

**Remember states before transforming them**

The outer loop continues while `n != 1` and `n not in vis`. At the beginning of
an iteration, current `n` has not previously been processed, so the method adds
it to `vis` before calculating its successor.

Recording before transition is important. If a later transition returns to
this value, membership is already present and the loop stops without following
the same cycle again.

If current `n` is 1, the first condition stops immediately and the final
comparison returns true. If current `n` is a repeated non-1 value, the second
condition stops and the final comparison returns false.

**Extract decimal digits numerically**

The inner loop initializes successor accumulator `x` to zero. `divmod(n, 10)`
returns the quotient and remainder from division by ten. The remainder `v` is
the current least significant decimal digit, and the quotient replaces `n`,
discarding that digit.

The update `x += v * v` adds its square. Repetition continues until the working
`n` becomes zero. Every original digit has then been extracted exactly once,
and `x` is the required digit-square sum. Assignment `n = x` advances the outer
chain.

Destroying the old numeric value during digit extraction is safe because it was
already stored in `vis`, and only its computed successor is needed afterward.

**Trace the happy example**

Starting at 19, the method records 19 and extracts digits 9 and 1, obtaining
$9^2 + 1^2 = 82$. It records 82 and obtains $8^2 + 2^2 = 68$. Next come 100
and then 1.

Once `n` is assigned 1, the outer condition fails and `return n == 1` yields
true. None of the intermediate values repeats.

**Trace an unhappy cycle conceptually**

Starting from 2 eventually reaches the known non-happy cycle containing
`4, 16, 37, 58, 89, 145, 42, 20`. The first time each value appears, it is
stored and transformed. When 4 appears again, it is already in `vis`; the loop
stops and returns false because 4 is not 1.

The algorithm does not need to know the cycle members in advance. It discovers
repetition for any deterministic cycle.

**Why the sequence cannot increase forever**

If a number has $d$ decimal digits, its next value is at most $81d$, attained
when every digit is 9. For sufficiently many digits, $81d$ is far smaller than
the original $d$-digit number. Under the signed 32-bit constraint there are at
most ten digits, so one transition is at most 810; subsequent transitions enter
a small bounded region.

A deterministic sequence in a finite region must either reach 1 or repeat a
state. This justifies the loop's two termination conditions and rules out an
unhandled path growing forever.

**Why the returned classification is exact**

If the method returns true, current `n` is 1, so the defined process reached 1
and the original input is happy.

If it returns false, current `n` appeared earlier. From the same integer, the
digit-square transformation always produces the same successor, so the future
will replay the already traversed segment indefinitely. Since the loop would
have stopped earlier if it had reached 1, this repeated cycle excludes 1 and
the original number is not happy.

**Set behavior and source/manifest mismatch**

Set membership and insertion have expected constant time. The set does grow
with the number of distinct chain values until termination. Therefore the exact
algorithm is a history-based detector, not a constant-state detector.

For the fixed 32-bit domain, the reachable bounded region has a constant finite
size, so one can call worst-case auxiliary storage $O(1)$ with respect to the
fixed word range. Under an input-magnitude or arbitrary-precision analysis, the
set and its integer keys should not be described as literally constant state.
Floyd's algorithm would genuinely retain only two current values.

## Complexity detail

Processing the initial number's decimal digits costs $O(\log n)$. Its successor
is at most 810 under the contract, after which the chain lies in a fixed bounded
region. With expected set operations, total time is therefore $O(\log n)$ as
the manifest records.

The exact source stores every distinct visited value. The editorial analyzes
history storage as $O(\log n)$ in an input-size model, while the fixed 32-bit
domain makes the count bounded by a constant. The manifest's $O(1)$ space is
defensible only under that fixed-domain convention, not because this code uses
Floyd's constant-state method.

## Alternatives and edge cases

- **Floyd cycle detection:** Advance one value by one transition and another by two; true constant auxiliary state and matches the manifest summary.
- **Known-cycle sentinel:** Stop when reaching 1 or 4, relying on the proven unique non-happy cycle for decimal digit squares.
- **Dictionary history:** Equivalent to the set but stores unnecessary values, as the competitive variant does.
- **String digit conversion:** Easier to read but allocates text for each transition.
- **Input 1:** Returns true without entering either loop.
- **Single-digit unhappy number:** Transitions normally and eventually repeats in the non-happy cycle.
- **Zeros inside a number:** Their square contributes zero and `divmod` handles them naturally.
- **Positive guarantee:** Avoids defining digit extraction and happiness for zero or negatives.
- **Fixed 32-bit domain:** Makes the reachable post-transition region a bounded constant.
- **Set growth:** Exact code remembers history even though a two-pointer alternative need not.
