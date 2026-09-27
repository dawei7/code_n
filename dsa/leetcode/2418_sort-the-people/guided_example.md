# Guided Example: Sort the People

The representative instance is `names = ["Alice", "Bob", "Bob"]` with `heights = [155, 185, 150]`, whose required answer is `["Bob", "Alice", "Bob"]`. It is chosen because the two people named `"Bob"` are *different people* with different heights, so the instance separates value identity from index identity — the trap that decides whether the method is correct.

## 1. The Instance and Its Two Parallel Arrays

The contract supplies two arrays of the same length $n$: a string array `names` and an integer array `heights`. Position $i$ of each array describes the same person, so the input is really a list of $n$ records

$$
\bigl(\text{index } i,\; \text{names}[i],\; \text{heights}[i]\bigr),
$$

and the required output is the sequence of names ordered by **descending** height. The heights are guaranteed to be *distinct*, which means the descending order of heights is unique and every position in the output is forced.

| Index $i$ | `names[i]` | `heights[i]` | Person identity |
|:---:|:---|:---:|:---|
| 0 | `"Alice"` | `155` | the person at position 0 |
| 1 | `"Bob"` | `185` | the tall `"Bob"` |
| 2 | `"Bob"` | `150` | the short `"Bob"` |

Reading the table already shows the crux of the instance: the two rows named `"Bob"` carry different heights, so they must be *ordered differently* in the output — the tall one first, the short one last. Any method that keys the output off the string `"Bob"` cannot express that.

## 2. The Ordering Key Is Height, and Only Height

The sort key is the height, ordered descending. Two facts from the contract make the key well behaved:

- **Distinctness.** All `heights[i]` are distinct, so no two records share a key. There are no ties to break, and no secondary key (such as the name or the index) can influence the result. This is why the problem has a single correct output rather than a family of valid outputs.
- **No name-based ordering.** The names are payload, not keys. They never participate in comparisons, so `"Alice"` being alphabetically before `"Bob"` is irrelevant; only `155 < 185` matters.

For the traced instance the descending height order is `185`, then `155`, then `150`. Mapping each height back to its index gives the permutation $(1, 0, 2)$, and reading `names` at those indices gives `["Bob", "Alice", "Bob"]`.

| Rank | Height | Source index $i$ | `names[i]` | Emitted into the output |
|:---:|:---:|:---:|:---|:---|
| 1 | `185` | 1 | `"Bob"` | position 0 of the answer |
| 2 | `155` | 0 | `"Alice"` | position 1 of the answer |
| 3 | `150` | 2 | `"Bob"` | position 2 of the answer |

The middle column is the part that makes the rearrangement mechanical: the method sorts **indices**, not names and not heights. Heights provide the comparison values; indices remember which record each value came from.

## 3. Step-by-Step Trace of the Rearrangement

The trace below performs the ordering as a sequence of "take the tallest remaining person" decisions. At each step the state is the set of indices not yet emitted and the output prefix already produced, so the table doubles as a before/after record of the algorithm's state.

| Step | Remaining indices | Heights still available | Tallest remaining | Chosen index | Name emitted | Output after the step |
|:---:|:---|:---|:---:|:---:|:---|:---|
| 1 | $\{0, 1, 2\}$ | `155`, `185`, `150` | `185` | 1 | `"Bob"` (the tall one) | `["Bob"]` |
| 2 | $\{0, 2\}$ | `155`, `150` | `155` | 0 | `"Alice"` | `["Bob", "Alice"]` |
| 3 | $\{2\}$ | `150` | `150` | 2 | `"Bob"` (the short one) | `["Bob", "Alice", "Bob"]` |

Three properties of the trace are worth naming explicitly.

- **The chosen index is always the argmax of the remaining heights.** Step 1 selects index 1 because `heights[1] = 185` is the largest value; step 2 selects index 0 because `heights[0] = 155` beats the only alternative `heights[2] = 150`.
- **The output is built in descending order**, so the prefix is already final when it is written. No later step can insert a taller person before an earlier one, because all the taller candidates were removed first.
- **The two `"Bob"` rows are consumed by different steps.** Step 1 emits index 1 and step 3 emits index 2; the string `"Bob"` appears twice in the output because it appears twice in the input, once per person.

The instance has $n = 3$ records. A selection-style ordering performs $\binom{3}{2} = 3$ pairwise height comparisons in total (step 1 uses two, step 2 uses one, step 3 uses none). A comparison-based sort would need at most $\lceil \log_2(3!) \rceil = 3$ comparisons here as well, which is why the two strategies are indistinguishable on such a small input but diverge as $n$ grows.

## 4. Index Identity Versus Value Identity

The decisive trap is stated cleanly by this instance. Consider three plausible-looking rules and what each produces:

| Rule | Produces for the traced instance | Correct? | Why it fails or succeeds |
|:---|:---|:---:|:---|
| Order the *distinct name strings* by the height of their first occurrence | `["Bob", "Alice"]` — only two names | no | the output must have exactly $n$ entries; the second `"Bob"` is a different person and is missing |
| Order names by height after grouping equal names together | `["Bob", "Bob", "Alice"]` | no | grouping destroys the height order that the contract requires |
| Order the *index set* by `heights[index]` descending, then read `names` at those indices | `["Bob", "Alice", "Bob"]` | yes | the permutation preserves one output slot per input record |

The naming distinction matters because the input has a genuine duplicate value paired with a unique index. `names[1]` and `names[2]` are the *same string* but refer to *different records*, and the height array distinguishes them: `heights[1] = 185` and `heights[2] = 150`. Sorting indices keeps that distinction; sorting names erases it.

A second, subtler point: the names are **case-sensitive data**, not sort keys. In an instance like `names = ["z", "A", "m"]` with `heights = [20, 30, 10]`, the answer is `["A", "z", "m"]` — driven entirely by `30 > 20 > 10`. The fact that `"A"` would precede `"z"` under an uppercase-first collation is a coincidence of that instance, not a rule of the problem.

## 5. Invariant and Correctness

Let the method produce an ordered list of indices $\pi = (\pi_1, \pi_2, \dots, \pi_n)$ and return the names `names[π_1], names[π_2], …, names[π_n]`.

**Permutation invariant.** $\pi$ is a permutation of $\{0, 1, \dots, n-1\}$: exactly $n$ indices are placed into exactly $n$ output slots, so no person is dropped or duplicated.

**Ordering invariant.** After rank $j$ is written, `heights[π_1] ≥ heights[π_2] ≥ … ≥ heights[π_j]`, and every unplaced index has height at most `heights[π_j]`. In the trace, after step 2 the prefix is `185, 155` and the only remaining height is `150`.

*Proof by induction.* Before any step the prefix is empty and the invariant is vacuous. Assume it after $j - 1$ steps: the next index $\pi_j$ is the argmax of the remaining heights, so `heights[π_j]` is at most the previously placed `heights[π_{j-1}]` and at least every height left after its removal, which restores the invariant for rank $j$. $\square$

**Correctness.** At $j = n$ the ordering invariant gives a non-increasing height sequence; distinctness makes that order unique, so the result is exactly the required descending arrangement, and the permutation invariant makes it a rearrangement of the input names rather than a filtered copy. **Termination** is immediate: one index is placed per rank and there are $n$ ranks, regardless of the height values. Distinctness is needed only for uniqueness of the answer, not for termination.

## 6. Boundaries

The constraints are $1 \le n \le 10^{3}$, $1 \le \text{heights}[i] \le 10^{5}$, $1 \le \lvert \text{names}[i] \rvert \le 20$, and all heights distinct.

| Boundary instance | Answer | Mechanism | What it exposes |
|:---|:---|:---|:---|
| `n = 1`, `["Alex"]`, `[100]` | `["Alex"]` | one record, one rank | the minimum-size input; the rearrangement is the identity and must not crash or emit an empty list |
| `["Tall","Mid","Low"]`, `[300,200,100]` | `["Tall","Mid","Low"]` | already descending | an already-sorted input must be left alone, not reversed |
| `["A","B","C"]`, `[1,2,3]` | `["C","B","A"]` | ascending input | descending order reverses a fully ascending list |
| `["Min","Max"]`, `[1, 100000]` | `["Max","Min"]` | extreme legal heights | the height range end points are ordinary comparison values, with no special handling |
| `["z","A","m"]`, `[20,30,10]` | `["A","z","m"]` | names ignored as keys | the names' collation order does not influence the answer |
| `["A","B","C"]`, `[3,1,2]` | `["A","C","B"]` | arbitrary input order | the input order carries no information; only the height pairing does |
| `["Alice","Bob","Bob"]`, `[155,185,150]` | `["Bob","Alice","Bob"]` | traced instance | duplicate names must survive as separate records |
| two names of length `20`, heights `100000` and `1` | taller name first | extreme name length | name length is irrelevant to the key, and long names do not truncate |

One boundary the contract *excludes* deserves note: because all heights are distinct, the method never orders two people of equal height. Without that guarantee the problem would be ambiguous (several outputs valid) and a tie-breaking rule would be required — so distinctness buys uniqueness of the answer, not termination.

## 7. Alternative Formulations

| Alternative | Work performed | Cost | Trade-off against sorting indices |
|:---|:---|:---|:---|
| Repeatedly select the maximum remaining height and emit its name | $n + (n-1) + \dots + 1 = n(n+1)/2$ height comparisons | time $O(n^{2})$, auxiliary space $O(n)$ for the emitted output | simple and clearly correct; acceptable at $n \le 10^{3}$ but needlessly quadratic |
| Sort the index set by the key $-\text{heights}[i]$ | one comparison sort over $n$ indices, $O(n \log n)$ comparisons | time $O(n \log n)$, auxiliary space $O(n)$ | chosen: keeps each name attached to its own index by construction |
| Sort pairs of (height, name) descending | one comparison sort over $n$ pairs, names moved with the heights | time $O(n \log n)$, auxiliary space $O(n)$ | correct because heights are distinct, but it couples the payload to the key, and it stops working the moment a tie-break or a second payload array is introduced |
| Bucket heights into an array of size $10^{5}+1$, then read buckets in decreasing order | one pass to scatter, one pass over the height range | time $O(n + H)$ with $H = 10^{5}$, auxiliary space $O(H)$ | asymptotically attractive for huge $n$, but here $H \gg n$, so it allocates far more memory than it saves in comparisons |
| Build a map from height to name and sort the distinct heights | one map insertion per record, then a sort of the heights | time $O(n \log n)$, auxiliary space $O(n)$ | a valid restatement, but it silently assumes heights are unique keys — exactly the distinctness guarantee, so it is no more general than sorting indices |

The bucket variant exploits the bounded height range rather than the problem's structure: with $n \le 1000$ and $H = 10^{5}$ it scans about a hundred times more slots than the number of records, so the comparison sort is the better trade here.

## 8. Complexity Derivation

Let $n = \lvert \text{heights} \rvert = \lvert \text{names} \rvert$.

**Time.** Sorting the index permutation by the height key costs $O(n \log n)$ comparisons, each reading two integers; emitting the answer reads `names` once per rank, $O(n)$ references. Names are never compared, so their lengths do not affect the cost. The total is $O(n \log n)$, which is optimal in the comparison model: any method that only compares heights must distinguish all $n!$ input orderings, giving the $\Omega(n \log n)$ lower bound. Under $n \le 10^{3}$ even the quadratic selection variant would pass, so the logarithmic method is chosen for clarity rather than necessity.

**Auxiliary space.** The permutation holds $n$ indices and the returned array holds $n$ name references, so the ordering uses $O(n)$ auxiliary space beyond the input. No memory grows with the magnitude of the heights, because heights are compared and never indexed; the bucket alternative breaks that property with its $O(H)$ array.

**Summary.** The people are sorted in $O(n \log n)$ time using $O(n)$ auxiliary space, with the index permutation carrying the identity of each person through the rearrangement.
