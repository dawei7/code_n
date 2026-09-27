# Guided Example: Find the Substring With Maximum Cost

## 1. The instance, and what a substring costs

Each lowercase letter carries a value. Letters named in the override string
`chars` take the value listed at the same position in `vals`; every other letter
takes its 1-indexed alphabet position, so `a` is worth `1`, `b` is worth `2`, and
`z` is worth `26`. The cost of a substring is the sum of the values of its
characters, the empty substring costs `0`, and the task is to maximize the cost.

This lesson follows the instance

$$s = \texttt{"abxabyab"},\qquad chars = \texttt{"xy"},\qquad vals = [-20, -30],$$

whose maximum substring cost is `3`.

The string has eight positions, and every letter in it is either a default-valued
letter or an overridden one:

| position $i$ | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|---|---|
| character | `a` | `b` | `x` | `a` | `b` | `y` | `a` | `b` |
| overridden? | no | no | yes | no | no | yes | no | no |
| value | `1` | `2` | `-20` | `1` | `2` | `-30` | `1` | `2` |

The instance is chosen because the two overridden letters are large negatives that
split the string into three identical positive runs `ab`, `ab`, `ab`. Every run is
worth `3`, and the lesson has to explain why no longer window beats `3` even
though extended windows contain more letters.

## 2. A substring as a difference of prefix sums

Define the prefix sums

$$P_0 = 0,\qquad P_k = \sum_{i=0}^{k-1} v_i \ \text{ for } 1 \le k \le 8,$$

where $v_i$ is the value of the character at position $i$. The cost of the
substring that starts at position $p$ and ends at position $q$ inclusive is
$P_{q+1} - P_p$, so maximizing a substring cost means maximizing a difference of
two prefix sums, with the left prefix taken no later than the right one:

$$\max_{0 \le p \le q+1 \le 8} \bigl(P_{q+1} - P_p\bigr).$$

Fixing the right end $q$ and choosing the left end freely, the best choice is the
*smallest* prefix sum available at or before that point:

$$\text{answer} = \max_{0 \le k \le 8}\ \Bigl(P_k - \min_{0 \le i \le k} P_i\Bigr).$$

The empty substring is the case $i = k$, whose difference is $0$, so the expression
above is automatically at least $0$ and the floor of the answer is `0`. No extra
special case is needed to respect the empty-substring rule, and no negative answer
can ever be produced.

The prefix sums of this instance are

| $k$ | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|---|
| $P_k$ | `0` | `1` | `3` | `-17` | `-16` | `-14` | `-44` | `-43` | `-41` |

Note the shape of the sequence: it climbs to `3`, collapses to `-17` at the
override `x`, climbs again by `3`, collapses to `-44` at the override `y`, and
climbs a final time by `3`. The answer `3` is exactly the height of each of those
three climbs.

## 3. Step-by-step trace of the running minimum

Sweep the string once, keeping $tot = P_k$ for the next unused prefix and
$mi = \min(P_0, \ldots, P_k)$ for the smallest prefix seen so far. At each step the
candidate $tot - mi$ is precisely the best substring that ends at the current
position, because $mi$ is the cheapest left endpoint available at that point.

Before each row below, $mi$ is the minimum over the prefixes up to and including
the current position's left boundary; the row reports the candidate before $mi$ is
allowed to absorb the new prefix, which is what keeps the left endpoint at or
before the right endpoint.

| $i$ | character | value $v_i$ | $tot = P_{i+1}$ | $mi$ before | candidate $tot - mi$ | best so far | $mi$ after |
|---|---|---|---|---|---|---|---|
| 0 | `a` | `1` | `1` | `0` | `1` | `1` | `0` |
| 1 | `b` | `2` | `3` | `0` | `3` | `3` | `0` |
| 2 | `x` | `-20` | `-17` | `0` | `-17` | `3` | `-17` |
| 3 | `a` | `1` | `-16` | `-17` | `1` | `3` | `-17` |
| 4 | `b` | `2` | `-14` | `-17` | `3` | `3` | `-17` |
| 5 | `y` | `-30` | `-44` | `-17` | `-27` | `3` | `-44` |
| 6 | `a` | `1` | `-43` | `-44` | `1` | `3` | `-44` |
| 7 | `b` | `2` | `-41` | `-44` | `3` | `3` | `-44` |

Three things in this table carry the method.

1. At $i = 2$ the candidate turns negative, which is the trace telling us that
   extending the window across the override `x` destroys value. The best answer
   stays at `3`.
2. The minimum prefix drops twice, at $i = 2$ and $i = 5$, which means the left
   endpoint of the best window moves to just after each override. That is the
   resets made visible: after `x`, the cheap left endpoint is $P_3 = -17$, and
   after `y` it is $P_6 = -44$.
3. Rows 4 and 7 both reproduce the candidate `3` from a different left endpoint
   each time, which is why the final answer is `3` and not a value produced by a
   single lucky window.

The table of whole-substring costs confirms the reading. Longer windows are
strictly worse, because each override hands back more than the following run
earns:

| substring | positions | cost | compared with `3` |
|---|---|---|---|
| `ab` | 0 to 1 | `1 + 2 = 3` | equal, optimal |
| `abx` | 0 to 2 | `3 - 20 = -17` | worse |
| `abxab` | 0 to 4 | `-17 + 3 = -14` | worse |
| `xab` | 2 to 4 | `-20 + 3 = -17` | worse |
| `ab` | 3 to 4 | `1 + 2 = 3` | equal, optimal |
| `xabya` | 2 to 6 | `-20 + 3 - 30 + 1 = -46` | worse |
| `ab` | 6 to 7 | `1 + 2 = 3` | equal, optimal |
| empty | — | `0` | worse |

## 4. Invariant and correctness of the running-minimum rule

The sweep maintains one invariant: **before the character at position $i$ is
absorbed, $tot = P_i$ and $mi = \min(P_0, \ldots, P_i)$; after the value $v_i$ is
added, $tot = P_{i+1}$ and the candidate $tot - mi$ is the maximum cost of any
substring ending exactly at position $i$.** The update
$mi \leftarrow \min(mi, tot)$ then restores the invariant for the next position,
because $\min(P_0, \ldots, P_{i+1}) = \min\bigl(\min(P_0, \ldots, P_i),\ P_{i+1}\bigr)$.

**Why the candidate is exact.** Every substring ending at position $i$ has the form
$P_{i+1} - P_p$ for some $p \le i$, and $mi \le P_p$ for all such $p$ because $mi$
is the minimum over exactly that range. Hence $P_{i+1} - mi \ge P_{i+1} - P_p$ for
every feasible left endpoint, so no substring ending at $i$ scores higher than the
candidate. The candidate is itself attained, because the prefix that realizes $mi$
is one of the allowed left endpoints. So the candidate is the exact optimum among
substrings ending at $i$, not merely a bound.

**Why the maximum over positions is the answer.** Every substring has a unique
right endpoint, so the family of "substrings ending at $i$" partitions the set of
all substrings as $i$ ranges over the positions. Maximizing an exact per-position
optimum over all positions therefore yields the global optimum. The empty
substring is included at every position, where the left endpoint equals the right
endpoint, giving cost `0`; that is why the answer is never negative and why the
initial value of the best-so-far can start at `0` without an explicit branch.

**Why the running minimum is enough.** The rule needs, at each position, only the
single smallest prefix value seen up to that point; all other prefix values are
strictly worse left endpoints and can never be optimal again, because the range of
admissible left endpoints only grows as the sweep advances. Discarding them is
therefore safe, and it is what makes the sweep constant-space in addition to
linear-time.

| Claim | Argument |
|---|---|
| candidate is attainable | The prefix realizing $mi$ occurs at some index $p \le i$, and the substring from $p$ to $i$ has cost $tot - mi$ |
| candidate is optimal for its right endpoint | Every other left endpoint has prefix value $P_p \ge mi$, so its substring cost $tot - P_p$ is no larger |
| per-position optima cover all substrings | Each substring has exactly one right endpoint |
| answer is never negative | The empty substring is always available and costs `0` |
| dropping prefix values is safe | Only the minimum prefix can serve as the best left endpoint, now or later |

## 5. A contrast instance: a positive override and the zero floor

Two further behaviours are worth seeing on authored instances, because the main
instance does not exhibit them.

**A large positive override.** With $s = \texttt{"leetcode"}$,
$chars = \texttt{"lt"}$, $vals = [100, -100]$, the values become `l = 100`,
`e = 5`, `t = -100`, `c = 3`, `o = 15`, `d = 4`. The prefix sums are
`100, 105, 110, 10, 13, 28, 32, 37`, and the minimum prefix stays at `0` for the
entire sweep, so the best candidate is the first three characters `lee` with cost
`100 + 5 + 5 = 110`. The override `t = -100` is a barrier that no optimal window
crosses, and the whole-string cost is only `37`.

| right endpoint | prefix $P_{q+1}$ | $mi$ | candidate | best so far |
|---|---|---|---|---|
| `l` | `100` | `0` | `100` | `100` |
| `e` | `105` | `0` | `105` | `105` |
| `e` | `110` | `0` | `110` | `110` |
| `t` | `10` | `0` | `10` | `110` |
| `c` | `13` | `0` | `13` | `110` |
| `o` | `28` | `0` | `28` | `110` |
| `d` | `32` | `0` | `32` | `110` |
| `e` | `37` | `0` | `37` | `110` |

The lesson from the contrast is that a positive prefix never forces a reset: the
best left endpoint stays at the very beginning of the string, and the answer is a
prefix rather than an interior window.

**The zero floor.** With $s = \texttt{"abc"}$, $chars = \texttt{"abc"}$ and
$vals = [-1, -1, -1]$, every value is `-1`, so the prefix sums are
`-1, -2, -3`. Every candidate is negative, the best-so-far never rises above `0`,
and the reported answer is `0`, realized by the empty substring. This is the case
that would break an implementation which initializes the answer to a very small
number or which insists on a non-empty window.

| instance | override effect | answer | realized by |
|---|---|---|---|
| `s = "abxabyab"`, `chars = "xy"`, `vals = [-20, -30]` | two large negative barriers | `3` | any of the three runs `ab` |
| `s = "leetcode"`, `chars = "lt"`, `vals = [100, -100]` | one large positive lead, one negative barrier | `110` | the prefix `lee` |
| `s = "abc"`, `chars = "abc"`, `vals = [-1, -1, -1]` | every letter negative | `0` | the empty substring |
| `s = "zaz"`, `chars = "a"`, `vals = [1000]` | one huge positive letter in the middle | `1052` | the whole string |
| `s = "adaa"`, `chars = "d"`, `vals = [-1000]` | one ruinous letter | `2` | the run `aa` |
| `s = "azby"`, `chars = "x"`, `vals = [-100]` | override never appears in `s` | `54` | the whole string, `1 + 26 + 2 + 25` |

## 6. Traps and boundary conditions

| Trap | What it looks like | Correction |
|---|---|---|
| Treating overridden letters as still holding their alphabet value | `x` contributing `24` instead of `-20` | The override replaces the alphabet value completely, and it may be far smaller |
| Letting a window cross a large negative letter | Extending `ab` to `abx` gives `-17` | The prefix minimum is what implements the cut; a window that spans a big negative is never optimal once the sweep sees the dip |
| Choosing the leftmost or rightmost window instead of the best one | All three `ab` runs tie at `3`, so positional heuristics give the right total by luck on this instance but not on `leetcode` | Only the running-minimum comparison is reliable |
| Assuming a non-empty substring is required | Returning a negative value on the all-negative instance | The empty substring is explicitly allowed and costs `0`, so the answer has a floor of `0` |
| Recomputing each substring from scratch | Comparing all $O(n^2)$ windows | The prefix formulation evaluates each right endpoint in constant time |
| Overwriting the minimum prefix before evaluating the candidate | Comparing `tot` against `tot` yields `0` at every step | The candidate must use the minimum over prefixes whose index is at most the left boundary of the current window |
| Assuming longer windows are worth more | `abxab` has two extra letters but costs `-14` | Cost is additive, not monotone in length |
| Assuming every letter of `chars` occurs in `s` | The override `x` on the `azby` instance is never used | Overrides only matter for letters that actually appear |

| Boundary situation | Authored instance | Answer | Why |
|---|---|---|---|
| single character | `s = "a"`, `chars = "d"`, `vals = [-1000]` | `1` | The one-letter substring costs `1` and the empty substring costs `0` |
| repeated character | `s = "aaa"`, `chars = "d"`, `vals = [-1000]` | `3` | The whole string is one additive run of `1`s |
| every value negative | `s = "abc"`, `chars = "abc"`, `vals = [-1, -1, -1]` | `0` | The empty substring is optimal |
| override far more negative than the run it interrupts | `s = "adaa"`, `chars = "d"`, `vals = [-1000]` | `2` | Each side of the barrier is evaluated independently and the longer side wins |
| override far more positive than the defaults | `s = "zaz"`, `chars = "a"`, `vals = [1000]` | `1052` | The whole string is a single climbing window |
| three separated runs | `s = "abxabyab"`, `chars = "xy"`, `vals = [-20, -30]` | `3` | Every run ties, and the barriers prevent any union from helping |

## 7. Complexity of the method

Building the value lookup costs $O(\lvert chars \rvert)$ using a table keyed by
character, and the sweep visits each character of $s$ exactly once. At every
position it performs one addition, one comparison against the running minimum and
one comparison against the best-so-far, so the total running time is

$$O(\lvert s \rvert + \lvert chars \rvert) = O(n + c)$$

with $n = s.length$ and $c = chars.length$. The auxiliary space is $O(c)$ for the
override table, or $O(1)$ if the table is fixed at the 26 letters of the alphabet;
the sweep itself keeps only the running prefix, the running minimum prefix and the
best answer.

| Component | Cost | Why |
|---|---|---|
| Override table construction | $O(c)$ | One entry per overridden letter |
| Value lookup per character | $O(1)$ | Direct table access |
| Prefix and minimum updates | $O(1)$ per character | One addition and two comparisons |
| Total time | $O(n + c)$ | One pass over the string |
| Auxiliary space | $O(c)$, or $O(1)$ with a fixed alphabet table | Only the override map and three counters are stored |
| Enumerating all substrings instead | $O(n^2)$ | Every window is summed separately, and $n$ can reach $10^{5}$ |

The reason a single pass suffices is that the objective decomposes into a
difference of prefix sums, and the best left endpoint for any right endpoint is
always the smallest prefix seen so far. That is the whole idea, and it turns a
quadratic search over windows into one linear sweep.