# Guided Example: Apply Transform Over Each Element in Array

## 1. The instance we will transform

A map is the most position-preserving operation in this family: it visits every element, replaces each one with the callback's answer, and keeps the slot occupied. Nothing is removed, nothing is reordered, and the output length always equals the input length. What this statement adds is that the callback may consult the element's **index**, which breaks two intuitions a learner often carries into the problem — that equal inputs must give equal outputs, and that the output's values tell you something about the input's values. The instance below breaks both at once.

$$
\text{arr} = [-3,\ -3,\ 4], \qquad \text{callback}(n, i) = n^{2} + i
$$

The required outcome is the array `[9,10,18]`.

Read that target alongside the input. The two occurrences of $-3$ produced *different* outputs, $9$ and $10$, because they sit at different positions. The value $4$ vanished from the output entirely, replaced by $18$. And the output contains $9$ and $10$, neither of which appears in the input. If the traversal had treated the callback as a function of the element alone, or had tried to recognise already-computed results, it would have produced the wrong array.

## 2. The correspondence the contract fixes

The statement requires that the returned array satisfy

$$
\text{returnedArray}[i] = fn(\text{arr}[i],\ i)
$$

for every index $i$. That single equation is the entire specification, and it fixes three separate things: which element the callback receives, which positional number accompanies it, and which output slot the answer occupies. The table reads the equation position by position for our instance.

| Source index $i$ | Element $\text{arr}[i]$ | Index passed as the second argument | Callback result $n^{2} + i$ | Output slot $i$ |
|---|---|---|---|---|
| 0 | $-3$ | 0 | $9 + 0 = 9$ | `returnedArray[0] = 9` |
| 1 | $-3$ | 1 | $9 + 1 = 10$ | `returnedArray[1] = 10` |
| 2 | $4$ | 2 | $16 + 2 = 18$ | `returnedArray[2] = 18` |

Rows 0 and 1 are the decisive pair: identical first arguments, different second arguments, different answers. The contract never asks whether two source elements are equal, so the traversal must never compare them either. Each position is an independent evaluation.

## 3. The positional pass, step by step

The traversal holds a single write cursor that advances with the read cursor. Because it writes into the slot matching the position it just read, the output length after $i + 1$ evaluations is exactly $i + 1$ — it tracks the number of evaluations, not the number of "interesting" results.

| Step | Position $i$ | Element read | Arguments offered | Callback result | Output after the step | Output length |
|---|---|---|---|---|---|---|
| 1 | 0 | $-3$ | $-3$ and 0 | 9 | `[9]` | 1 |
| 2 | 1 | $-3$ | $-3$ and 1 | 10 | `[9,10]` | 2 |
| 3 | 2 | $4$ | $4$ and 2 | 18 | `[9,10,18]` | 3 |
| 4 | 3, past the end | none | not offered | not evaluated | `[9,10,18]` | 3 |

At step 4 the read cursor has reached the source length, so no further evaluation happens and the traversal stops. The output length equals the input length at that moment, and it did so at every earlier step as well; that lockstep is what distinguishes a map from a selection.

| Property | A selection (filter) pass | This transformation (map) pass |
|---|---|---|
| Output length | number of accepted elements, unknown until the pass ends | always exactly the input length |
| Write cursor | advances only on acceptance, so it lags the read cursor | advances with the read cursor on every step |
| Element identity | output entries are source elements, unchanged | output entries are callback results; source elements may not appear at all |
| Order | stable subsequence of the input | one slot per input position, in the same order |

The third row is why the two operations cannot share a mechanism: in a filter the accepted value *is* the source value, so reusing it is free, while here the source value is an argument that the callback may discard entirely.

## 4. Invariant and correctness of the positional pass

Write $A$ for the source array of length $n$ and $F$ for the callback.

**Invariant.** Immediately before position $i$ is evaluated, the output array has length exactly $i$ and satisfies

$$
\text{output}[j] = F(A[j],\ j) \qquad \text{for every } 0 \le j < i .
$$

*Preservation.* Evaluating position $i$ offers $F$ the arguments $A[i]$ and $i$, and appends the returned value at output index $i$, which is one past the current last index because the output length was exactly $i$. The new output therefore has length $i + 1$ and satisfies the required equation at every index below $i$ by the invariant and at index $i$ by construction. The invariant is restored for $i + 1$. Initially $i = 0$, where an output of length 0 satisfies the statement vacuously.

*Termination and conclusion.* The read cursor starts at 0 and increases by exactly one per iteration, so after exactly $n$ iterations it reaches $n$ and the traversal halts. At that point the invariant quantifies over all $0 \le j < n$, so every output slot equals the callback's answer for its position: the pass is *sound* (no slot holds anything else) and *complete* (no slot is left unwritten). Consequently the output length is $n$, and each slot was produced by exactly one evaluation — the traversal never evaluates the callback for a position that has already been written, and never writes a slot twice.

**Why no memoisation appears.** A natural instinct is to cache callback results by element value so that the repeated $-3$ is computed once. The instance shows why that is unsound here: the two evaluations legitimately disagree because their second arguments differ, so a cache keyed on the value would return $9$ at position 1 and produce `[9,9,18]`. Any shortcut that skips evaluations would have to prove the callback ignores the index, which the statement does not allow, and the authored check that maps four copies of `99` to `[0,1,2,3]` shows how completely the output can depend on position alone.

## 5. Traps this instance exposes

| Trap | The tempting but wrong move | What this instance reveals |
|---|---|---|
| Equal inputs | reuse the previous result when the same value appears again | positions 0 and 1 hold the same $-3$ yet must produce $9$ and $10$ |
| Caching | key a result cache on the element value | the cache would return the wrong slot's value and shrink the output |
| Identity | assume output values are drawn from the input | $9$, $10$ and $18$ are all absent from the input, while $-3$ and $4$ are absent from the output |
| Injectivity | assume distinct inputs give distinct outputs | the authored square check maps `[-3,0,4]` to `[9,0,16]`, and once a callback is not injective, two different inputs share an image |
| Length | drop or compress "uninteresting" results | the constant check maps `[10,20,30]` to `[42,42,42]`; three identical outputs must all be kept |
| Order | sort or rank the results | the negate check maps `[-5,7,0]` to `[5,-7,0]`, where the output order is the input order even though the output magnitudes are unrelated to it |
| Empty source | treat length 0 as a special case needing a guard | the constraint admits $0 \le \text{arr.length}$, and the correct output for an empty source is the empty array |
| Arithmetic range | assume the element bound also bounds the callback's result | the constraint bounds elements by $10^{9}$ but only requires the callback to return an integer, so a squaring callback can reach about $10^{18}$, beyond the range where floating-point numbers represent every integer exactly |

The last row is a warning about where the guarantee stops. The traversal promises a slot per position and an exact copy of whatever the callback returns; it cannot promise that the callback's own arithmetic stayed inside the exactly representable integer range, because that bound depends on the callback rather than on the traversal.

## 6. Complexity: one evaluation and one write per position

Let $n$ denote the source length, with $0 \le n \le 1000$ as the statement guarantees.

**Time.** The read cursor advances exactly once per element, so the traversal performs exactly $n$ evaluations and exactly $n$ writes; no position is visited twice, and none is skipped, because every slot of the result is required. The traversal's own work per iteration is a constant number of operations around the callback call, so the traversal costs

$$
O(n)
$$

steps, plus the internal cost of the $n$ callback evaluations, which belongs to the supplied callback. This is asymptotically optimal: a correct result must place a value in every one of the $n$ slots, so any method performs at least $n$ writes and $\Omega(n)$ work.

**Auxiliary space.** The traversal holds only the single position integer, so its own state is $O(1)$; the result array holds $n$ slots, and it is fresh storage rather than a rearrangement of the source, so the total space attributable to the operation is $O(n)$. Building the result into new storage is what lets the traversal write slot $i$ immediately after reading element $i$ without ever disturbing a position it has not yet read.

**A note on the length guarantee.** Because writes are one per position and never conditional, the output length is fixed at $n$ before the callback's behaviour is known. A pass that instead pushed results only when some condition held would have an output length that depends on the data, which is precisely the difference between this traversal and the selection traversal compared in section 3.
