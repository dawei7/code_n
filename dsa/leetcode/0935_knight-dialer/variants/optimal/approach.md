## General

**Model the keypad as a small directed graph**

Each numeric key is a vertex. Draw a directed edge from digit `a` to digit `b` whenever a chess knight can jump from `a` to `b` on the phone keypad. The geometric board then becomes a fixed graph with ten vertices.

For example, a knight on `0` can jump to `4` or `6`. A knight on `4` can jump to `0`, `3`, or `9`. Digit `5` has no valid knight neighbor, so a sequence that starts on `5` cannot be extended beyond length one.

Once this graph is known, the problem is no longer about simulating coordinates. It asks how many walks of exactly `n - 1` edges exist when any of the ten vertices may be the starting point. The initial key contributes the first digit, and every jump contributes one additional digit.

**The dynamic-programming meaning**

The array `f` has ten entries. Before a transition round, `f[d]` means the number of valid phone numbers of the current length whose final digit is `d`.

For length one, `f = [1] * 10`. There is exactly one one-digit number ending at each key: the number consisting of that key itself. This also explains why `5` begins with one even though it cannot participate in later jumps.

The loop runs `n - 1` times. Each round creates numbers that are one digit longer. A fresh array `g` is necessary because all new counts must be calculated from the same previous length. Updating `f` in place would allow a value computed earlier in the current round to influence a later value, effectively mixing paths of different lengths.

**Reading every assignment as incoming edges**

Each assignment to `g[d]` sums counts from the digits that can jump into `d`:

- `g[0] = f[4] + f[6]` because only `4` and `6` can reach `0`.
- `g[1] = f[6] + f[8]`.
- `g[2] = f[7] + f[9]`.
- `g[3] = f[4] + f[8]`.
- `g[4] = f[0] + f[3] + f[9]`.
- `g[6] = f[0] + f[1] + f[7]`.
- `g[7] = f[2] + f[6]`.
- `g[8] = f[1] + f[3]`.
- `g[9] = f[2] + f[4]`.

There is no assignment to `g[5]`. The new array starts with zeros, so `g[5]` remains zero, correctly expressing that no knight jump can end at `5`.

The moves happen to be reversible on this keypad, so the digits that can jump into `d` are also the digits to which `d` can jump. Nevertheless, the recurrence should be understood in the incoming direction: to count sequences ending at `d`, ask where their previous digit could have been.

After all ten new ending counts have been formed, `f = g` advances the state by exactly one digit.

**A trace for the first two lengths**

At length one, every `f[d]` is one, so the total is ten.

After one transition, `g[0]` is two because `40` and `60` are valid. `g[4]` is three because `04`, `34`, and `94` are valid. Each of `1`, `2`, `3`, `7`, `8`, and `9` has two incoming choices, `6` has three, and `5` has none. The new counts sum to twenty, matching the twenty valid two-digit numbers.

A third round does not need to list those twenty strings. It groups them by final digit and extends each group through the same fixed transitions. This aggregation is the saving supplied by dynamic programming: all sequences with the same length and final digit have identical possible next moves.

**Why summing the last state is correct**

After `n - 1` rounds, `f[d]` counts all valid length-`n` numbers ending at digit `d`. Every valid number has exactly one final digit, so these ten groups are disjoint and exhaustive. The answer is their sum.

Correctness follows by induction on the represented length. The initialized state is correct for length one. Assume `f[d]` correctly counts all valid sequences of some length ending at `d`. A sequence of the next length ending at `x` has a unique previous digit, and that digit must be one of the sources named in the assignment for `g[x]`. Conversely, appending `x` to any sequence counted by one of those source states makes a valid knight jump and creates a valid longer sequence. Summing those source counts therefore counts every valid longer sequence exactly once. The induction reaches length `n`, and the final sum is correct.

**Where the modulus is applied in this exact solution**

The code computes exact Python integers throughout the loop and applies `% (10**9 + 7)` only to the final sum. This is mathematically valid because reducing after all additions gives the same remainder as reducing after every addition.

It is worth distinguishing mathematical validity from implementation cost. Counts grow exponentially with `n`, so the intermediate Python integers grow in bit length. Applying the modulus during every transition would keep them small and is the usual implementation choice in languages with fixed-width integers. The checked-in code relies on Python's arbitrary-precision integers and postpones reduction until the return statement.

## Complexity detail

The exact solution performs `n - 1` transition rounds. Each round carries out a fixed number of additions over ten states, so under the customary unit-cost arithmetic model its time complexity is `O(n)`. It keeps two arrays of ten integers, giving `O(1)` state space because keypad size is fixed.

The optimal manifest currently states `O(log n)` time, but that bound does not describe this checked-in loop. Logarithmic time would require exponentiating a transition matrix or an equivalent recurrence transformation. This approach document follows the exact solution and therefore reports its linear number of transition rounds.

If arbitrary-precision bit operations are counted, postponing the modulus makes later additions more expensive because the integers contain `O(n)` bits. Reducing every state modulo the required constant on each round restores the usual practical `O(n)` behavior with bounded-size values. The arrays are still constant in count, although the exact unmodded integers occupy growing storage internally.

## Alternatives and edge cases

- **Ten-state DP with per-transition modulus:** This is the same recurrence and is generally preferable in production. Apply the modulus to every `g[d]` so intermediate values remain bounded and the code also works in fixed-width languages.
- **Transition-matrix exponentiation:** Express one round as multiplication by a fixed `10 by 10` matrix and raise it to power `n - 1`. This achieves `O(log n)` matrix multiplications and matches the manifest's claimed time, but it is substantially more machinery for a ten-state recurrence.
- **Symmetry-compressed states:** Several keypad digits have equivalent transition behavior and can be grouped. That reduces the state to a few counts, though it makes the group multiplicities less obvious than the explicit per-digit assignments.
- **Top-down memoization:** A recursive state consisting of remaining jumps and current digit gives `O(n)` states because the keypad is constant. It adds recursion depth and cache storage without improving the asymptotic running time.
- **Enumerating every number:** Explicitly generate all valid walks. Their count grows exponentially, so this performs work proportional to the huge answer instead of combining paths that share the same length and ending digit.
- **The case `n = 1`:** The loop runs zero times and all ten initialized counts are summed. Digit `5` is valid as a one-digit starting number even though it cannot be extended.
- **Digit `5` for larger lengths:** Its state becomes zero in the first round and stays zero. No special conditional is needed because `g` starts with zeros and has no assignment for index five.
- **Leading zero:** A dialed phone number may start at any numeric cell, including `0`. These are sequences of keypad presses, not decimal integers whose leading zero is discarded.
- **Simultaneous update:** `g` must be completed before `f = g`. Reusing partially updated values would count paths with inconsistent lengths.
- **Large `n`:** The required modulus is essential for the returned result. In this exact Python code, applying it only at the end is correct but less efficient than reducing throughout.
