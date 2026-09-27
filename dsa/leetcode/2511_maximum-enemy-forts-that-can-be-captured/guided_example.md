# Guided Example: Maximum Enemy Forts That Can Be Captured

## 1. Reading the array: three kinds of positions

The array `forts` encodes a one-dimensional battlefield. Every index carries one
of exactly three states, and the state decides the role that index can play in a
move.

| Value | Reading | Role in a move |
|:---:|:---|:---|
| `1` | a fort under your command | a legal **starting** position or a legal **destination** |
| `0` | an enemy fort | never an endpoint; it is a cell the army crosses, and each one crossed is captured |
| `-1` | no fort at all | a legal destination, and a hard wall that ends a run of enemies |

The army travels from one of your forts to an empty position, crossing only enemy
forts. So a productive move is a trip from a `1` to a `-1`, or from a `-1` to a
`1`, with nothing but `0` entries strictly between the two endpoints. The
captured count is the number of those interior zeros, which is
$\lvert j - i \rvert - 1$ for endpoints at indices $i$ and $j$.

Two consequences shape the whole method. First, a gap between two own forts
(`1` and `1`) or between two empty positions (`-1` and `-1`) cannot be a move at
all: no army of yours stands at a `-1`, and a `1` is not an empty position to
move *to*. Second, any interior `-1` or `1` interrupts the enemy run, so only
maximal runs of zeros matter.

## 2. The move rule as a three-part test

Reading the statement's formal condition carefully, a pair of indices $i < j$
supports a capture exactly when all three hold:

1. `forts[i]` and `forts[j]` are both non-zero — the endpoints are real
   positions of the battlefield;
2. every index $k$ with $i < k < j$ satisfies `forts[k] == 0` — the interior is
   purely enemy territory;
3. `forts[i] + forts[j] == 0` — one endpoint is yours and the other is empty,
   which is the compact way of saying the two ends are of *opposite* non-zero
   type.

The third test is the elegant one: the only way two values from $\{-1, 1\}$ sum
to zero is the combination $(1, -1)$ or $(-1, 1)$. Both orders describe the same
move read in opposite directions, so a single symmetric test replaces a
direction-dependent case split.

The natural scan follows the shape of the condition: stand on a non-zero
position $i$, walk right across zeros, and stop at the next non-zero position
$j$. If the endpoints sum to zero, the interior length $\lvert j - i \rvert - 1$
is a candidate answer.

## 3. Worked trace of the official instance

The statement's first example is
`forts = [1, 0, 0, -1, 0, 0, 0, 0, 1]`, whose expected answer is `4`.

| Index | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `forts[index]` | 1 | 0 | 0 | -1 | 0 | 0 | 0 | 0 | 1 |
| Reading | ours | enemy | enemy | empty | enemy | enemy | enemy | enemy | ours |

Scanning left to right, the first non-zero position is index 0. Walking right
crosses the enemies at 1 and 2 and stops at index 3, which is `-1`. The pair
$(0, 3)$ passes the opposite-type test, so the gap $3 - 0 - 1 = 2$ enemies is a
candidate. The scan then resumes at index 3, the previous stop, and reaches
index 8, which is `1`; the pair $(3, 8)$ also passes, and its gap is
$8 - 3 - 1 = 4$ — the four enemies at indices 4, 5, 6, and 7. That beats 2, and
with index 8 having no non-zero position to its right, the answer is `4`. This
matches the official explanation: moving from position 8 to position 3 captures
four enemy forts.

The two candidates also show why the interior-zero condition is checked
implicitly by the scan rather than separately: the walk from index 3 stops early
if any non-zero state appears, so the gap it measures is automatically a maximal
enemy run.

## 4. The per-step scan, state by state

The trace below records the full state at every iteration of the scan: the
current start $i$, the stop $j$ found by walking over zeros, the sum test, the
candidate gap, and the running maximum.

| Step | $i$ | `forts[i]` | Stop $j$ | `forts[j]` | `forts[i] + forts[j]` | Gap $j - i - 1$ | Running answer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 1 | 0 | 1 | 3 | -1 | 0, valid | 2 | 2 |
| 2 | 3 | -1 | 8 | 1 | 0, valid | 4 | 4 |
| 3 | 8 | 1 | 9 (past the end) | — | not evaluated | — | 4 |

Step 3 is the terminating state: the walk runs off the right edge, no destination
exists, and the previous maximum stands. The second official example shows the
same machinery producing a zero-length candidate:

| Step | $i$ | `forts[i]` | Stop $j$ | `forts[j]` | `forts[i] + forts[j]` | Gap $j - i - 1$ | Running answer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 1 | 0 | 0 | 1 | 0 | not evaluated | — | 0 |
| 2 | 1 | 0 | 2 | 1 | not evaluated | — | 0 |
| 3 | 2 | 1 | 3 | -1 | 0, valid | 0 | 0 |
| 4 | 3 | -1 | 4 (past the end) | — | not evaluated | — | 0 |

For `forts = [0, 0, 1, -1]` the move is legal but the two endpoints are adjacent,
so zero enemies lie strictly between them. The method reports `0`, and the
statement agrees: adjacent endpoints capture nothing.

## 5. Why the two endpoints must be of opposite type

The sum test deserves its own table, because it is the only place where a
genuinely wrong interpretation can hide. All four non-zero endpoint
combinations occur in the authored cases.

| Left endpoint | Right endpoint | Sum | Move legal? | Captured | Example instance |
|:---:|:---:|:---:|:---|:---:|:---|
| `1` | `-1` | 0 | yes | interior zeros | `[1,0,0,-1]`, official sample 1 |
| `-1` | `1` | 0 | yes, travelling right | interior zeros | `[-1,0,0,1]`, reverse-direction case |
| `1` | `1` | 2 | no | — | `[1,0,0,0,1]`, same-boundary case |
| `-1` | `-1` | -2 | no | — | `[1,0,-1,0,0,-1,0,0,0,1]`, interruption case |

The two rejected rows are rejected for different reasons. A `1`-to-`1` pair has a
legal army at each end but no empty destination, so the move is not permitted by
the rules at all. A `-1`-to-`-1` pair has no army at either end — `-1` means
there is no fort there — so no move can start, and the enemy forts that may lie
between the two positions are never crossed. The sum test distinguishes both from
the two legal orientations without needing to know which direction the army
travels, which is why the method does not track a direction.

## 6. Boundary and edge cases

| Instance | Input | Expected | Deciding reason |
|:---|:---|:---:|:---|
| widest of several gaps | `[-1,0,1,0,0,0,-1,0,1]` | 3 | pairs $(0,2)$ and $(6,8)$ give gaps 1, the pair $(2,6)$ gives the maximum 3 |
| reverse direction | `[-1,0,0,1]` | 2 | the symmetric sum test accepts `-1` on the left |
| same boundary type | `[1,0,0,0,1]` | 0 | endpoint sum is 2, so no move exists |
| interrupted run | `[1,0,-1,0,0,-1,0,0,0,1]` | 3 | the `-1` at index 2 ends the first enemy run; only the run from index 5 to 9 counts |
| adjacent endpoints | `[0,0,1,-1]` | 0 | legal move, empty interior |
| only enemies | `[0,0,0,0]` | 0 | no own fort to start from and no empty position to reach |
| single own fort | `[1]` | 0 | no position to the right; the scan immediately runs off the edge |
| no zeros at all | `[1,1]` | 0 | the stop $j$ is adjacent and its value sums to 2, not 0 |

Two traps are visible here. The first is the "no zeros at all" row: a stop can be
adjacent to the start, so the method must not assume at least one interior cell
before evaluating the sum test — doing so would skip a valid (but worthless) pair
rather than the invalid same-type pair it actually is. The second is the
interrupted-run row: an interior `-1` terminates the walk and must be treated as
the next start afterwards, not as an obstacle to skip; skipping it would merge two
separate enemy runs into one fictitious gap.

## 7. Correctness: the maximal-run invariant

The method maintains one invariant as the scan advances:

> **Maximal-run invariant.** When the scan stands on a non-zero position $i$, the
> positions strictly between $i$ and the next non-zero position $j$ are all
> enemies, and $j$ is the *nearest* non-zero position to the right of $i$.

Why the invariant holds: the inner walk stops at the first index whose value is
not zero, so by construction every interior position is an enemy fort and no
non-zero position was skipped. Therefore every legal move whose left endpoint is
$i$ has right endpoint exactly $j$ — there are no other candidates — and the gap
$\lvert j - i \rvert - 1$ equals the captured count. The method records the
maximum over all such $i$, so its answer equals the maximum over all legal moves.

Completeness needs one more observation: the scan advances $i$ to $j$, so **every
non-zero position is eventually examined as a left endpoint**. Zeros are never
used as a start (they fail the non-zero test), and no non-zero position is
jumped over, because the walk between two non-zero positions contains only zeros.
Hence no legal move escapes the enumeration, and the running maximum is exact.

Termination is immediate: $i$ strictly increases at every iteration, either to
the next non-zero position or by one when the current position is an enemy, so
the scan reaches the end of the array in finitely many steps.

## 8. Alternatives and their failure modes

| Approach | How it works | Time | Auxiliary space | Failure mode |
|:---|:---|:---|:---|:---|
| Linear scan with jump-to-next-non-zero | advance a start pointer, walk zeros, test the endpoint sum | $O(n)$ | $O(1)$ | none; this is the method traced above |
| Enumerate all index pairs | test every $i < j$ for the three conditions | $O(n^2)$ | $O(1)$ | correct but quadratic; re-verifies interiors the scan already knows are pure enemies |
| Split on non-zero separators | cut the array into zero runs, then look at the two positions flanking each run | $O(n)$ | $O(n)$ | correct, but materializes subarrays the running maximum does not need |
| Count zeros between every pair of own forts | measure distances between the `1` positions only | $O(n)$ | $O(1)$ | wrong: the destination must be an empty position, so `1`-to-`1` gaps such as `[1,0,0,0,1]` are not moves |
| Two independent directional passes | one left-to-right and one right-to-left sweep, each tracking the last boundary | $O(n)$ | $O(1)$ | correct but redundant; the symmetric sum test already covers both directions in one pass |

## 9. Complexity: time and auxiliary space

**Time.** Each iteration of the outer scan advances the start index $i$ to a
strictly larger value, and the inner walk touches each zero index at most once
during the whole traversal, because those zeros lie before the next start. Every
array entry is therefore inspected a constant number of times, giving $O(n)$
time with $n = \texttt{forts.length} \le 1000$. The only work per inspected entry
is one comparison against zero, one addition of two endpoint values, and one
maximum update, all $O(1)$.

**Auxiliary space.** The method keeps only the start index, the stop index, and
the running maximum, so auxiliary space is $O(1)$ — it never copies the array or
stores the list of gaps. The input itself is read-only, and no subarray, prefix
table, or index list is materialized.