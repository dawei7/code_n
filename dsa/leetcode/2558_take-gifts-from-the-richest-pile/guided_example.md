# Guided Example: Take Gifts From the Richest Pile

## 1. The Prescribed Process and the Instance Traced

The piles in `gifts` are operated on once per second. Each second the pile holding
the *largest* number of gifts is selected — any one of them when several are tied —
and its count is replaced by the integer square root of what it held:

$$
v \;\longmapsto\; \lfloor \sqrt{v} \rfloor .
$$

After exactly `k` seconds the total number of gifts left in all piles is reported.
Nothing is optimised: the process is prescribed, and the only freedom is the
tie-breaking rule, so the task is to reproduce the process efficiently and to be
sure the total does not depend on how the ties are broken.

The instance traced here is the authored sample

```text
gifts = [25, 64, 9, 4, 100],  k = 4
```

with required output `29`. It is the right instance because four seconds are more
than enough to show the two decisive phenomena: the richest pile changes identity
as the process runs, and a pile that has just been reduced can become the richest
pile again.

| Index | `gifts[i]` | Initial rank by size | Reduced once to | Reduced twice to |
|:---:|:---:|:---:|:---:|:---:|
| 0 | `25` | 3rd | `5` | `2` |
| 1 | `64` | 2nd | `8` | `2` |
| 2 | `9` | 4th | `3` | `1` |
| 3 | `4` | 5th | `2` | `1` |
| 4 | `100` | 1st | `10` | `3` |

## 2. The Operation as a Decreasing Map

The square-root step has three properties that the whole lesson rests on.

**It never increases a pile.** For every integer $v \ge 1$,
$\lfloor \sqrt{v} \rfloor \le v$, with equality only at $v = 1$ (and at $v = 0$,
which the constraints exclude). Piles of size $1$ are fixed points: they are
"chosen" when the maximum is $1$ and they come back unchanged.

**The gift removed is monotone in the pile size.** Define

$$
d(v) = v - \lfloor \sqrt{v} \rfloor .
$$

Because $v \mapsto v$ grows faster than $v \mapsto \lfloor \sqrt{v} \rfloor$, the
function $d$ is non-decreasing over the positive integers: a larger pile always
yields at least as many gifts as a smaller one, and strictly more except across a
block where the floor square root is constant.

| Pile size $v$ | `floor(sqrt(v))` | Gifts removed $d(v)$ | Comment |
|:---:|:---:|:---:|:---|
| `1` | 1 | 0 | Fixed point; nothing can be taken |
| `4` | 2 | 2 | Perfect square |
| `9` | 3 | 6 | Perfect square |
| `10` | 3 | 7 | Just past a perfect square |
| `25` | 5 | 20 | Perfect square |
| `64` | 8 | 56 | Perfect square |
| `100` | 10 | 90 | Perfect square |

**The total never rises.** Every second the running sum decreases by $d(v)$ for
the chosen pile, so the running sum is non-increasing and is bounded below by the
number of piles (every pile is at least $1$ forever). This is why the process must
be simulated rather than averaged: the whole answer is the initial total minus the
sum of the $k$ decreases, and each decrease depends on which pile was chosen.

## 3. Second-by-Second Trace of the Instance

At each second the maximum is read off the current multiset, replaced by its floor
square root, and the running total drops by $d$ of the chosen value.

| Second | Piles before choosing | Richest pile | Chosen $v$ | New value `floor(sqrt(v))` | Gifts removed $d(v)$ | Piles after choosing | Running total |
|:---:|:---|:---:|:---:|:---:|:---:|:---|:---:|
| 1 | `[25, 64, 9, 4, 100]` | index 4 | `100` | `10` | 90 | `[25, 64, 9, 4, 10]` | 202 |
| 2 | `[25, 64, 9, 4, 10]` | index 1 | `64` | `8` | 56 | `[25, 8, 9, 4, 10]` | 146 |
| 3 | `[25, 8, 9, 4, 10]` | index 0 | `25` | `5` | 20 | `[5, 8, 9, 4, 10]` | 126 |
| 4 | `[5, 8, 9, 4, 10]` | index 4 | `10` | `3` | 7 | `[5, 8, 9, 4, 3]` | 119 |

The initial total is $25 + 64 + 9 + 4 + 100 = 202$ and the removals are
$90 + 56 + 20 + 7 = 173$, leaving $202 - 173 = 29$, which matches the required
output. Read the fourth row carefully: the pile chosen in the *first* second is
chosen again in the fourth, because reducing `100` to `10` still left it larger
than every other pile once `25` and `64` had themselves been reduced. The identity
of the richest pile is not a one-time decision.

## 4. Why the Result Does Not Depend on Tie-Breaking

The statement allows any pile to be chosen when several share the maximum. Two
piles holding equal counts are interchangeable objects for this process: the
operation applied to either of them produces the same new value, and the rest of
the multiset is untouched. Exchanging the labels of two equal piles therefore
maps one legal run of the process onto another legal run with exactly the same
multiset at every second, hence the same final total.

| Instance | Tied piles | Choice A | Choice B | Final total |
|:---|:---|:---|:---|:---:|
| `gifts = [9, 9]`, `k = 1` | two piles of `9` | first `9` becomes `3` | second `9` becomes `3` | both give `12` |
| `gifts = [2, 2, 2]`, `k = 1000` | three piles of `2` | reduce in any order | reduce in any order | all reach `1`; total `3` |
| `gifts = [10, 10, 4]`, `k = 2` | two piles of `10` | first `10` becomes `3`, then the other becomes `3` | same order reversed, same multiset `[3, 3, 4]` | both give `10` |

By induction on the number of elapsed seconds, the *multiset* of pile sizes is a
function of the elapsed time alone; only the arrangement into labelled indices can
differ. The answer is a sum over the multiset, so it is well defined.

## 5. What Structure the Process Needs

Every second needs the current maximum, then one element changes and the maximum
must be available again. Three ingredients therefore matter, and none of them is
optional.

- **A maximum-finding structure.** A scan of all piles costs $O(n)$ per second,
  which is $O(nk)$ overall. A max-heap keeps the maximum at the root in $O(1)$ and
  restores the ordering after a change in $O(\log n)$.
- **A single update per second.** Only the chosen pile changes, and its new value
  is smaller than its old value, so the repaired structure re-establishes the heap
  property by sifting the changed value *downwards* only. Rebuilding the structure
  from scratch each second would waste the $O(n)$ build cost.
- **Exact floor square roots.** The replacement value must be $\lfloor \sqrt{v} \rfloor$
  exactly, including for perfect squares at the top of the range ($10^{9}$ is
  itself a perfect square: $31623^{2} = 1{,}000{,}014{,}129$ is larger, and
  $31622^{2} = 999{,}950{,}884$, so the floor root of $10^{9}$ is `31622`).

| Second | Piles before | Max after replacement | Is the replaced pile the maximum again? |
|:---:|:---|:---:|:---|
| 1 | `[25, 64, 9, 4, 100]` | `64` | no, `100` became `10` |
| 2 | `[25, 8, 9, 4, 10]` | `25` | no |
| 3 | `[5, 8, 9, 4, 10]` | `10` | yes, the pile reduced in second 1 is the maximum again |
| 4 | `[5, 8, 9, 4, 3]` | `9` | no, `10` became `3` |

## 6. Boundary Behaviour and the Traps This Instance Exposes

| Instance | Total after `k` seconds | What it tests |
|:---|:---:|:---|
| `gifts = [1, 1, 1, 1]`, `k = 4` | `4` | Every pile is a fixed point; the process is a no-op |
| `gifts = [2, 2, 2]`, `k = 1000` | `3` | `k` far exceeds the number of useful operations; the state saturates at all ones |
| `gifts = [10]`, `k = 1` | `3` | Non-perfect square: $\lfloor \sqrt{10} \rfloor = 3$, not $4$ and not $3.16\ldots$ |
| `gifts = [1000000000]`, `k = 3` | `13` | Repeated application to one pile: `31622`, then `177`, then `13` |
| `gifts = [4, 2]`, `k = 3` | `2` | Operations outnumber piles, so reduced piles are chosen again |
| `gifts = [10000, 2, 2]`, `k = 2` | `14` | The reduced maximum stays the maximum: `10000`, then `100`, then `10` |

The traps worth naming:

- **Assuming `k` distinct piles are used.** Seconds do not consume piles.
  `[10000, 2, 2]` with `k = 2` reduces the same pile twice, and `[1000000000]`
  with `k = 3` reduces the only pile three times.
- **Rounding the square root instead of flooring it.** `10` must become `3`, and
  `2` must become `1`; rounding `10` to `3` happens to agree, but rounding
  $\sqrt{2} = 1.41$ up to `2` would break the fixed-point behaviour and leave the
  total too high.
- **Treating tiny piles as exhausted.** A pile of `1` is still selected when it is
  the maximum, and it stays `1`; there is no "remove the pile" step.
- **Recomputing the maximum with a full scan per second.** Correct but
  $O(nk)$; the constraints allow it, yet it ignores the one-change-per-second
  structure that makes the process logarithmic per second.
- **Rebuilding the heap each second.** The heap is built once; afterwards only the
  single changed pile moves, and it only ever moves down.
- **Ignoring saturation.** Once every pile is `1`, the remaining seconds change
  nothing, so a naive simulation of `k = 1000` seconds over many piles still does
  a thousand heap operations where a saturation test could stop early — a valid
  optimisation, but not a correctness requirement.

## 7. Alternatives and Their Trade-offs

| Alternative | Per second cost | Total time | Trade-off |
|:---|:---:|:---:|:---|
| Linear scan for the maximum | $O(n)$ | $O(nk)$ | Simplest to reason about; at $n = k = 10^{3}$ it is about $10^{6}$ comparisons, acceptable here but the wrong structure for large inputs |
| Max-heap with replacement | $O(\log n)$ | $O(n + k \log n)$ | The natural fit: the maximum is at the root and the single changed key sifts down; needs a decrease-key style replacement rather than a full rebuild |
| Sorted array with binary-search insertion | $O(n)$ | $O(nk)$ worst case | Keeps the front as the maximum, but removing and reinserting shifts elements |
| Counted buckets over the reduced values | $O(\log^{*} v)$ amortised | $O(n + k)$ | Exploits the fact that values collapse geometrically, but it is far more machinery than the process needs |

All correct variants simulate the identical multiset dynamics; they differ only in
how quickly the next maximum is found.

## 8. Time and Auxiliary Space

Let $n$ be the number of piles. Building the maximum structure from the initial
array takes $O(n)$ work, and each of the `k` seconds performs one maximum read, one
floor square root, and one replacement that sifts a single key down a tree of
height $\lceil \log_2 n \rceil$.

- **Time:** $O(n + k \log n)$. Each second costs $O(\log n)$ and there are `k` of
  them, on top of the one-time $O(n)$ build. With $n, k \le 10^{3}$ and
  $\texttt{gifts[i]} \le 10^{9}$ this is at most about $10^{3} + 10^{4}$ elementary
  operations.
- **Space:** $O(n)$ for the structure that holds one key per pile. The simulation
  itself keeps no per-second history: the state is the multiset, and each second
  overwrites one entry, so the auxiliary space beyond the input array is a single
  heap of $n$ keys plus $O(1)$ scalars.
