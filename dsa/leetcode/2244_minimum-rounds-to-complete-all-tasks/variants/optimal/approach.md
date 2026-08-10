## General

**Different difficulty levels are independent**

One round may contain only tasks of the same difficulty. Therefore, tasks of one difficulty can never help form a pair or triple with tasks of another difficulty.

The solution first builds `cnt = Counter(tasks)`. For each difficulty, its frequency `v` becomes an independent grouping problem: partition `v` identical tasks into groups of size two or three using as few groups as possible. The overall minimum is the sum of the independent minima.

**A single occurrence makes the whole task impossible**

If `v = 1`, neither an allowed pair nor an allowed triple can contain that lone task. No grouping of other difficulty levels changes this fact. The method immediately returns `-1`.

This is the only impossible positive frequency. Every integer `v >= 2` can be formed from twos and threes:

- two is one pair;
- three is one triple;
- four is two pairs;
- every larger value can add a pair or triple to one of these constructions.

**Use as many triples as the remainder permits**

A triple completes more tasks per round than a pair, so minimizing rounds generally means maximizing triples. Write `v = 3q + r`, where `r` is zero, one, or two.

- If `r = 0`, use `q` triples. This requires `q` rounds.
- If `r = 2`, use `q` triples and one pair, for `q + 1` rounds.
- If `r = 1` and `v >= 4`, using `q` triples would leave one impossible task. Replace one conceptual group of four tasks with two pairs. Algebraically, `v = 3(q - 1) + 2 + 2`, again requiring `q + 1` rounds.

These cases are compactly counted by

`v // 3 + (v % 3 != 0)`.

In Python, the Boolean comparison contributes one when the remainder is nonzero and zero otherwise. For every feasible `v`, this equals `ceil(v / 3)`.

**Why this number of rounds is minimal**

No round completes more than three tasks. Completing `v` tasks therefore requires at least `ceil(v / 3)` rounds, regardless of grouping.

For every `v >= 2`, the constructions above achieve exactly that lower bound using only allowed pairs and triples. Since a feasible construction meets an unavoidable lower bound, it is optimal.

The exception `v = 1` explains why the formula is applied only after the explicit impossibility check. Its ceiling would be one, but there is no legal one-task round.

**Accumulate independent optima**

`ans` starts at zero. For each frequency, the method adds that difficulty's minimum round count. Rounds cannot mix difficulties, so any global schedule must spend at least this many rounds for every frequency. Conversely, concatenating each difficulty's optimal grouping produces a valid schedule with exactly the summed count.

Thus, summing local minima gives the global minimum.

**Trace the sample frequencies**

For `[2,2,3,3,2,4,4,4,4,4]`, frequencies are three for difficulty two, two for difficulty three, and five for difficulty four.

- three uses one triple;
- two uses one pair;
- five uses one triple and one pair.

The total is four rounds.

For `[2,3,3]`, difficulty two has frequency one. The method returns `-1` immediately because that task can never be completed legally.

**Ordering is irrelevant**

`Counter` ignores input order because rounds may choose any tasks sharing a difficulty. Only multiplicities affect feasibility and round count.

The solution never modifies `tasks`. Hash-map iteration order also cannot change the numerical sum or impossibility result.

**Why no cross-difficulty scheduling decision remains**

Rounds can be performed in any chronological order, but reordering them cannot merge groups or change their sizes. One may finish all rounds for one difficulty before another, or interleave them, with exactly the same total count. This is why the algorithm needs no simulation of a work schedule: the frequency decomposition already contains every decision that can affect the minimum.

## Complexity detail

Let `n = len(tasks)` and `u` be the number of distinct difficulties. Building the counter takes expected `O(n)` time. Scanning its `u` frequencies takes `O(u)`, and `u <= n`, so total expected time is `O(n)`.

The counter stores one entry per distinct difficulty, using `O(u)` space. All other variables are scalar.

Python integers safely hold frequencies and the answer up to the input length.

## Alternatives and edge cases

- **Sort and count runs:** Sorting exposes equal difficulties together but costs `O(n \log n)` time; hashing counts directly in expected linear time.
- **Dynamic programming for each frequency:** A coin-change DP with group sizes two and three works but repeats a pattern captured by the remainder formula.
- **Always take triples:** A remainder of one would be stranded; one triple must effectively become two pairs.
- **Always take pairs:** It works only for even frequencies and uses more rounds than triples when possible.
- **Frequency one:** It makes the entire answer `-1`.
- **Frequency two:** Exactly one pair is required.
- **Frequency three:** Exactly one triple is optimal.
- **Frequency four:** Two pairs are required.
- **Frequency five:** One triple and one pair use two rounds.
- **Multiple impossible difficulties:** The first encountered frequency one is enough to return `-1`.
- **One difficulty only:** The same remainder analysis directly gives the complete answer.
- **Interleaved difficulty values:** Their positions in `tasks` do not constrain which tasks can share a round.
- **Round ordering:** Changing the order of independently formed rounds never changes how many rounds are required.
- **Input order and value size:** Neither matters; only equal-value counts are used.
