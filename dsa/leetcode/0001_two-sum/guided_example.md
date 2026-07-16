# Guided Example: Two Sum

We will solve the representative instance

- **Input:** `nums = [3, 2, 4]`, `target = 6`
- **Required output:** the two distinct indices `[1, 2]`

This example is deliberately more instructive than `[2, 7, 11, 15]`: the first value is half of the target, but it occurs only once. A correct method must not use index $0$ twice.

## 1. Replace pair enumeration with a complement query

For a current value $x$, any valid partner is forced by the equation

$$
x+y=6 \quad\Longleftrightarrow\quad y=6-x.
$$

The second value is therefore not another independent choice. It is the **complement** of the current value. This converts the problem from “try every pair” into the membership question “has this complement already appeared?”

We maintain a finite map $H$ whose keys are previously observed values and whose values are their indices.

| Index | 0 | 1 | 2 |
|---:|---:|---:|---:|
| Value | 3 | 2 | 4 |

> **Invariant.** Before examining index $i$, $H$ contains only values from indices strictly smaller than $i$.

That word *strictly* is what prevents an element from being paired with itself.

## 2. Examine index 0

The current value is $x=3$, so its required complement is also $3$.

| Current index | Current value $x$ | Required complement $6-x$ | Map before lookup | Result |
|---:|---:|---:|---|---|
| 0 | 3 | 3 | $\varnothing$ | not present |

No earlier `3` exists. Only after that failed lookup do we record the current occurrence.

| Map after the step |
|---|
| $H=\{3\mapsto 0\}$ |

### Why lookup must precede insertion

If the current `3` were inserted first, an immediate lookup for `3` would find index $0$ and incorrectly form the pair $(0,0)$. The target equation would hold numerically, but the contract requires two different array positions.

The operation order encodes the distinct-index constraint without a separate special case.

## 3. Examine index 1

Now $x=2$, hence the complement is $4$.

| Current index | Current value $x$ | Required complement $6-x$ | Map before lookup | Result |
|---:|---:|---:|---|---|
| 1 | 2 | 4 | $\{3\mapsto0\}$ | not present |

Record the newly observed value:

| Map after the step |
|---|
| $H=\{3\mapsto0,\;2\mapsto1\}$ |

At this point, every possible pair ending at index $1$ has been resolved. There is no reason to compare index $1$ with every earlier index explicitly; the map represents those earlier choices by value.

## 4. Examine index 2 and close the pair

The current value is $x=4$, so the complement is $2$.

| Current index | Current value $x$ | Required complement $6-x$ | Map before lookup | Result |
|---:|---:|---:|---|---|
| 2 | 4 | 2 | $\{3\mapsto0,\;2\mapsto1\}$ | found at index 1 |

The successful lookup establishes

$$
\texttt{nums}[1]+\texttt{nums}[2]=2+4=6.
$$

The map contained index $1$ before index $2$ was examined, so the indices are distinct by construction. The answer is therefore `[1, 2]`.

## Complete state trace

| Step | Examined value | Complement | Earlier values represented by $H$ | Decision |
|---:|---:|---:|---|---|
| 1 | 3 | 3 | none | store $3\mapsto0$ |
| 2 | 2 | 4 | $3\mapsto0$ | store $2\mapsto1$ |
| 3 | 4 | 2 | $3\mapsto0,\;2\mapsto1$ | return indices $1,2$ |

## Why the reasoning is correct

**Every reported pair is valid.** A result is produced only when the map contains the exact complement $6-x$. If that complement was stored at index $j$, then $j<i$ and `nums[j] + nums[i] = 6`. Thus the indices are distinct and their values have the required sum.

**The promised pair cannot be missed.** Let the unique valid pair have indices $p<q$. When the scan reaches $q$, the value at $p$ has already been placed in $H$. Because `nums[p] = 6 - nums[q]`, the complement lookup at $q$ succeeds.

Together, these statements establish **soundness**—no invalid pair is returned—and **completeness**—the valid pair is found.

## Traps this example exposes

- **Reusing one position:** `[3, 2, 4]` contains only one `3`; index $0$ cannot be selected twice. Lookup before insertion prevents this error.
- **Returning values instead of indices:** the pair values are $2$ and $4$, but the required answer is `[1, 2]`.
- **Confusing a value with its complement:** for current value $x$, search for `target - x`, not for $x$ unless those quantities happen to be equal.
- **Destroying index identity by sorting:** sorting permits a two-pointer search but changes positions. The original indices would then need to be carried through the sort.
- **Treating duplicates as interchangeable positions:** equal values at different indices are distinct array elements and may form a valid pair.

## Cost of the method

Each array position causes one expected-constant-time map lookup and, unless the answer is found, one insertion. For $n$ values, the total expected time is $O(n)$ and the map uses $O(n)$ auxiliary space.

