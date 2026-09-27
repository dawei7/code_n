# Guided Example: Filter Elements from Array

## 1. The instance we will filter

A filter is a *selection* problem, not a transformation problem: the output contains elements that already exist in the input, in the order they already occupy. What makes this statement worth a careful walkthrough is that the decision for each element is delegated to a callback, and the callback's answer is interpreted by **truthiness** rather than by a strict boolean test. The instance below is chosen so that the truthiness rule decides the outcome in a way that a value-based reading gets wrong.

$$
\text{arr} = [-2,\ -1,\ 0,\ 1,\ 2], \qquad \text{callback}(n) = n + 1
$$

The required outcome is the array `[-2,0,1,2]`.

Two features of that target are immediately informative. Element $-1$ is missing from the output even though $-1$ is itself a truthy number, and element $0$ is present even though $0$ is a falsy number. The element's own truthiness is therefore irrelevant; only the callback's returned value is tested. The other feature is that the four surviving elements appear in their original relative order, with $0$ — originally at position 2 — now sitting at output position 1.

## 2. What the callback is given for each position

The callback may be written to use either one parameter or two, and the traversal must always offer both. Ignoring the second argument is the callback author's choice; withholding it is not the traversal's.

| Argument position | Name in the statement | Meaning for the element at index $i$ | Value in our instance |
|---|---|---|---|
| first | the element | the number stored at that position | $-2, -1, 0, 1, 2$ in turn |
| second | the index | the 0-based position of that element in the source array | $0, 1, 2, 3, 4$ in turn |

Because the index is supplied, a predicate can depend on *position* rather than on value. In the authored check with source `[1,2,3]` and a predicate that accepts only index 0, the output is `[1]`: the elements $2$ and $3$ satisfy no value-based condition at all, and are rejected purely because of where they sit. Our instance exercises the value argument; the pass machinery below is identical for either style.

## 3. Truthiness: why $-1$ is dropped while $0$ survives

The statement defines a truthy value as one where the boolean conversion of that value yields true, and it asks for elements whose callback result is truthy. The test is therefore applied to the *result*, not to the element.

| Source index $i$ | Element $\text{arr}[i]$ | Callback result $n + 1$ | Boolean conversion of the result | Decision |
|---|---|---|---|---|
| 0 | $-2$ | $-1$ | true, every nonzero number is truthy | keep |
| 1 | $-1$ | $0$ | false, zero is the only falsy number | drop |
| 2 | $0$ | $1$ | true | keep |
| 3 | $1$ | $2$ | true | keep |
| 4 | $2$ | $3$ | true | keep |

Row 1 and row 2 together are the lesson. At index 0 the element is negative and the result is negative, and both are truthy, so the element is kept. At index 1 the element $-1$ is *also* truthy, but the callback returns exactly $0$, so the element is dropped. A traversal that tested the element instead of the result would keep $-1$ and would drop $0$ at index 2 only if it applied truthiness to the element — producing `[-2,-1,1,2]`, which is wrong in two positions at once.

## 4. The stable selection pass

The traversal walks the source once with a read cursor, and maintains the output as a growing list. Each source position is examined exactly once, and the element is copied only when the callback accepts it. Nothing is ever removed or reordered, which is what makes the selection stable.

| Step | Read cursor $i$ | Element | Callback result | Truthy? | Output after the step | Output length |
|---|---|---|---|---|---|---|
| 1 | 0 | $-2$ | $-1$ | yes | `[-2]` | 1 |
| 2 | 1 | $-1$ | $0$ | no | `[-2]` | 1 |
| 3 | 2 | $0$ | $1$ | yes | `[-2,0]` | 2 |
| 4 | 3 | $1$ | $2$ | yes | `[-2,0,1]` | 3 |
| 5 | 4 | $2$ | $3$ | yes | `[-2,0,1,2]` | 4 |
| 6 | 5, past the end | none | not evaluated | — | `[-2,0,1,2]` | 4 |

The read cursor and the output length are separate quantities, and that separation is the whole mechanism. After step 2 the read cursor is at 1 while the output length is still 1; the gap between them is exactly the count of rejected elements seen so far. Step 6 is the termination event: the loop condition compares the read cursor against the source length, so an array whose elements are all rejected ends the same way, with the cursor advancing while the output stays empty — exactly the authored check whose predicate rejects every element of `[1,2,3]` and whose expected output is `[]`.

## 5. Invariant and correctness of the single pass

Write $A$ for the source array of length $n$, and let $P$ be the callback.

**Invariant.** Immediately after the traversal has examined source positions $0$ through $i - 1$ — that is, before it examines position $i$ — the output list is exactly the sequence

$$
\bigl[\, A[j] \;\bigm|\; 0 \le j < i \ \text{and} \ P(A[j], j) \ \text{is truthy} \,\bigr]
$$

with the surviving positions taken in increasing order of $j$.

*Preservation.* Examining position $i$ either evaluates the callback, finds a truthy result, and appends $A[i]$ to the end of the output, or finds a falsy result and appends nothing. In the first case the new output is the old output followed by $A[i]$, which is precisely the qualifying sequence for positions $0$ through $i$, because $i$ is larger than every previously considered position. In the second case the old output is unchanged, which is again the qualifying sequence for the wider prefix. Either way the invariant is restored with $i$ increased by one. It holds initially for $i = 0$, where no position has been examined and the empty output is correct.

*Termination and conclusion.* The read cursor increases by exactly one on each iteration and starts at 0, so it reaches $n$ after exactly $n$ iterations and the traversal halts. At that moment the invariant describes positions $0 \le j < n$, which is the whole array, so the returned output contains exactly the elements whose callback result is truthy — the filter is *complete*, omitting nothing that qualifies, and *sound*, adding nothing that does not.

Two structural properties fall out of the same argument. The output is a *subsequence* of the input, because elements are copied in increasing index order and never rewritten. And the selection is *stable*: if two positions $j_1 < j_2$ both qualify, then $A[j_1]$ is appended strictly before $A[j_2]$, so their relative order in the output matches the input. The trace shows this when $0$, originally the third element, lands at output position 1 with the elements before it absent but the ones after it still behind it.

## 6. Traps this instance exposes

| Trap | The tempting but wrong move | What this instance reveals |
|---|---|---|
| Testing the wrong operand | apply truthiness to the element instead of to the callback result | $-1$ is truthy but must be dropped, and $0$ is falsy but must be kept |
| Numeric results | require an exact boolean from the callback | the callback returns a number here, and $0$ is the falsy case; no separate conversion branch is needed beyond ordinary truthiness |
| Predicate arguments | pass only the element | a predicate may be written against the index, so the position must always be supplied |
| Stability | gather matches into a set or sort them afterwards | the expected output preserves source order, and both trials that pass several elements depend on it |
| Boundary equality | treat a threshold comparison as inclusive | the authored check with `arr = [4,5,6]` and a strictly-greater-than-5 predicate returns `[6]`, excluding the element equal to the threshold |
| Empty source | special-case the empty array as an error | the constraint $0 \le \text{arr.length}$ admits length 0, whose correct output is the empty array |
| No matches | assume at least one element survives | an all-rejecting predicate over `[1,2,3]` must return the empty array, not the input and not an error |
| Built-in shortcut | reach for the array method the statement forbids | the selection has to be produced by the walk itself, so the cursor argument above is the mechanism to rely on |

The first two rows are the same misunderstanding seen from two sides: the callback is a *predicate whose answer is interpreted loosely*, and the element is mere data. Keeping those roles separate is what makes the pass correct on this instance rather than accidentally correct on easier ones.

## 7. Complexity: one callback call per element

Let $n$ denote the source length, with $0 \le n \le 1000$ as the statement guarantees, and let $k$ denote the number of elements the callback accepts, so the output length is $k$.

**Time.** The read cursor advances once per element, so the traversal performs exactly $n$ iterations and evaluates the callback exactly $n$ times — never twice for one position and never zero times for an examined one. Each iteration does a constant amount of work around that call: a comparison, and an append only when the predicate accepts. The number of appends is exactly $k$, which is at most $n$. The running time is therefore

$$
O(n)
$$

measured in traversal steps, plus the internal cost of the $n$ callback evaluations, which belong to the supplied predicate rather than to the traversal. Note that the traversal is *output-sensitive* only in its appends: it cannot become asymptotically cheaper by rejecting more elements, because every position is still evaluated.

**Auxiliary space.** Apart from the returned array, the traversal holds only the two integers — the current position and the current output length — so its own working space is $O(1)$. Including the result produced, the space is $O(k) \subseteq O(n)$. This is the one place where a filter differs from a partition performed in place: because the input is not to be rearranged, the accepted elements are collected into fresh storage rather than compacted into the front of the source, and that choice costs the output array but preserves the source for the caller.

**Why a single pass is optimal.** Every element must be evaluated, since an unevaluated element could be one the predicate accepts, and the callback's behaviour is not known in advance. So $\Omega(n)$ callback evaluations is a lower bound for any correct method, and the traversal above meets it exactly, with $O(1)$ auxiliary state beyond the output.
