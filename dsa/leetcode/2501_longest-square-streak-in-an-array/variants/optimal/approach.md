## General

**Sorting the chosen subsequence makes input order irrelevant**

A square streak is selected as a subsequence, but the selected values are sorted before the square relationship is checked. Therefore, the relevant question is whether the needed values occur in `nums`, not where they occur.

Because every value is at least two, repeated squaring creates a strictly increasing chain:

$$
x,\ x^2,\ x^4,\ x^8,\ldots
$$

No value can repeat within one such chain. A hash set is enough to record whether each required value exists; multiplicities are unnecessary for the chain relation.

**Store all distinct available values**

`s = set(nums)` removes duplicate values and provides expected $O(1)$ membership tests.

The outer loop still starts a chain from every element in the original `nums` rather than every distinct set member. Duplicate starting values may repeat work, but they cannot change correctness. Each occurrence produces the same chain length.

**Follow a repeated-square chain**

For each starting value `x`, the code initializes length `t=0`. While the current `x` belongs to `s`:

1. square `x` for the next membership check;
2. increment `t` because the current value was present.

Suppose the set contains 2, 4, and 16. Starting from 2:

- 2 is present, so length becomes one and `x` becomes 4;
- 4 is present, so length becomes two and `x` becomes 16;
- 16 is present, so length becomes three and `x` becomes 256;
- 256 is absent, so the loop stops.

The measured chain length is three.

The squaring occurs before incrementing in the source, but `t` counts the value whose successful membership test began that iteration. The next squared value is only a candidate for the following iteration.

**Why every counted chain forms a valid streak**

The loop's successive present values are `x`, `x^2`, $(x^2)^2$, and so on. Each is exactly the square of the preceding one. Since they are strictly increasing, they already appear in the same order they would have after sorting.

Each distinct value exists somewhere in `nums`, so one occurrence of each can be selected. Their original positions do not matter because the selected subsequence is sorted for validation. Hence every length `t` produced by the loop corresponds to a real square streak whenever `t>=2`.

**Why the longest streak is found**

Take any valid square streak after sorting and let its smallest value be $a$. Its values must be

$$
a,\ a^2,\ a^4,\ldots.
$$

The outer loop eventually uses an occurrence of $a$ as a start. The membership loop follows every value of that streak and possibly continues farther if more squared values exist. Its `t` is therefore at least the streak length.

Since every reported chain is valid and every valid chain is covered from its first value, the maximum reported length is exactly the optimum.

**Why `ans` begins at `-1`**

The problem recognizes only streaks of length at least two. A single available number always gives `t=1`, but that must not turn the answer into one.

The code updates `ans` only under `if t>1`. If no start reaches two values, `ans` remains `-1` and the required failure value is returned.

**Growth makes chains very short**

Starting from at least two, values square extremely rapidly. The exponent doubles on every step. Once the current value exceeds the largest value in the set, it cannot be present, so the loop terminates.

For example, $2,4,16,256,65536$ already approaches the maximum input value $10^5$. The next square is far beyond it. This doubly exponential growth is why following a chain from every input element is efficient.

Python can represent the one oversized squared candidate without overflow. In a fixed-width language, one should stop before squaring past the safe numeric range.

**Duplicates do not lengthen a chain**

Values begin at two, so $x^2>x$. A valid chain never asks for the same value twice. Ten copies of 4 do not make `[4,4]` a square streak because $4^2=16$, not 4.

Converting to a set therefore preserves all information needed for the answer.

## Complexity detail

Let $n$ be the input length and $M=\max(\texttt{nums})$. Starting from $x\ge2$, after $t$ squarings the magnitude is $x^{2^t}$. The number of successful membership steps before exceeding $M$ is $O(\log\log M)$.

The outer loop has $n$ iterations, so expected time is $O(n\log\log M)$ with expected constant-time hash membership. Building the set costs expected $O(n)$ and is dominated by the stated bound.

The set stores at most $n$ values, giving $O(n)$ auxiliary space. The scalar chain variables use constant space.

## Alternatives and edge cases

- **Iterate distinct starts only:** Looping over `s` avoids repeated work for duplicate inputs while preserving the same asymptotic bound.
- **Dynamic programming after sorting:** Record the best chain ending at each value using integer square roots; it costs sorting time.
- **Binary search membership:** Sort the array and search for each square, producing extra logarithmic factors.
- **No pair `x,x^2`:** Return `-1` rather than one.
- **Duplicate values:** They do not extend a strictly increasing square chain.
- **Values two or greater:** This avoids fixed points such as 0 and 1 that could make the loop non-terminating.
- **Chain suffix starts:** The outer loop may rediscover shorter suffixes, but the maximum remains correct.
- **Large square:** Python safely forms it; fixed-width languages should guard overflow.
- **Original order:** It is irrelevant because the chosen subsequence is sorted before checking.
- **Set membership:** Expected bounds assume ordinary hash-table behavior.
