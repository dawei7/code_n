# Guided Example: Mice and Cheese

## 1. The instance, its two reward vectors, and the required outcome

Each cheese type $i$ is worth a different number of points depending on which mouse eats it. The representative input is

$$\text{reward1} = [1, 1, 3, 4], \qquad \text{reward2} = [4, 4, 1, 1], \qquad k = 2,$$

so there are $n = 4$ cheese types and the first mouse must eat **exactly** two of them.

| Index $i$ | Points if mouse 1 eats it | Points if mouse 2 eats it | Mouse 1 advantage $\text{reward1}[i] - \text{reward2}[i]$ |
|---|---|---|---|
| 0 | 1 | 4 | $-3$ |
| 1 | 1 | 4 | $-3$ |
| 2 | 3 | 1 | $+2$ |
| 3 | 4 | 1 | $+3$ |

The required outcome is $15$, achieved by giving mouse 1 the types at indices 2 and 3 and leaving types 0 and 1 to mouse 2, which scores $3 + 4 + 4 + 4 = 15$. Every cheese type is eaten by exactly one mouse, the first mouse eats exactly $k = 2$ types, and the total is what gets maximized.

The instance is chosen because it punishes the two most natural first attempts. The first mouse has the *larger* reward on indices 2 and 3, so a method that ranks by `reward1` works here by luck; and the gains on offer are of different sizes, so a method that swaps one cheese at a time without comparing all of them can stop early and lose the $+3$.

## 2. Rewriting the objective as a baseline plus $k$ swap gains

Assignments interact, but only through a single count: exactly $k$ indices go to mouse 1 and the remaining $n - k$ go to mouse 2. That makes it profitable to start from a reference assignment and treat every change as a *swap*.

Start with the baseline in which mouse 2 eats everything:

$$B = \sum_{i=0}^{n-1} \text{reward2}[i] = 4 + 4 + 1 + 1 = 10.$$

Moving cheese type $i$ from mouse 2 to mouse 1 replaces the contribution $\text{reward2}[i]$ with $\text{reward1}[i]$, so it changes the total by

$$d_i = \text{reward1}[i] - \text{reward2}[i].$$

For any set $S$ of indices handed to the first mouse, with $\lvert S \rvert = k$, the total score is therefore

$$\text{total}(S) = B + \sum_{i \in S} d_i,$$

because the baseline already counts every index, and each index in $S$ is counted once more with its gain. The constraint "exactly $k$ types" becomes "exactly $k$ terms in the sum", and the objective is additive over the chosen indices. Maximizing $B + \sum_{i \in S} d_i$ over all $k$-element sets $S$ means maximizing the sum of the chosen gains, which has an obvious answer: take the $k$ largest gains. Section 5 proves that this is the only optimum.

| Index $i$ | Contribution under the baseline | Swap gain $d_i$ | Effect of the swap |
|---|---|---|---|
| 0 | 4 | $-3$ | loses 3 points |
| 1 | 4 | $-3$ | loses 3 points |
| 2 | 1 | $+2$ | gains 2 points |
| 3 | 1 | $+3$ | gains 3 points |

## 3. The greedy selection and the exchange that certifies it

The selection rule is: sort the indices by descending $d_i$ and take the first $k$. For this instance the descending order of gains is

$$d_3 = +3 \;>\; d_2 = +2 \;>\; d_1 = -3 \;=\; d_0 = -3,$$

so with $k = 2$ the selected set is $S = \{3, 2\}$ and the total is

$$B + d_3 + d_2 = 10 + 3 + 2 = 15.$$

Two details of this rule matter more than the arithmetic. First, the rule is **exact-k**, not "take all positive gains": when $k$ exceeds the number of positive gains, the selection must continue into negative territory and take the least damaging ones. Second, the rule ranks by the *difference* $d_i$, never by `reward1` alone, because a cheese with a large first-mouse reward can still be a bad swap if the second mouse would have scored even more on it.

## 4. Step-by-step execution on the instance

The table walks the instance in the order the rule examines it, after the gains have been sorted. The running total starts at the baseline and each selected index adds its gain.

| Step | Index considered | Swap gain $d_i$ | Position in sorted order | Action | Running total |
|---|---|---|---|---|---|
| 0 | — | — | — | start from the all-mouse-2 baseline | 10 |
| 1 | 3 | $+3$ | 1st | select: mouse 1 eats type 3 | 13 |
| 2 | 2 | $+2$ | 2nd | select: mouse 1 eats type 2; $k$ selections complete | 15 |
| 3 | 1 | $-3$ | 3rd | stop: the first mouse already has $k$ types | 15 |
| 4 | 0 | $-3$ | 4th | stop: the first mouse already has $k$ types | 15 |

The final assignment is mouse 1 on types 2 and 3, mouse 2 on types 0 and 1. Adding the raw rewards confirms the running total without reference to the gains: mouse 1 scores $3 + 4 = 7$, mouse 2 scores $4 + 4 = 8$, and $7 + 8 = 15$. Whenever a candidate answer can be re-derived this way, it should be, because the baseline-plus-gains arithmetic and the direct sum exercise different symbols of the same claim.

The rule reproduces every authored instance of this package.

| Instance | $k$ | Baseline $\sum \text{reward2}$ | The $k$ largest gains | Total |
|---|---|---|---|---|
| `reward1=[1,1,3,4]`, `reward2=[4,4,1,1]` | 2 | 10 | $+3, +2$ | 15 |
| `reward1=[1,1]`, `reward2=[1,1]` | 2 | 2 | $0, 0$ | 2 |
| `reward1=[10,1,1]`, `reward2=[1,10,10]` | 1 | 21 | $+9$ | 30 |
| `reward1=[5,6,7]`, `reward2=[7,6,5]` | 0 | 18 | none selected | 18 |
| `reward1=[2,3,4,5]`, `reward2=[10,9,8,7]` | 2 | 34 | $-2, -4$ | 28 |
| `reward1=[6,7,8,9]`, `reward2=[1,2,3,4]` | 3 | 10 | $+5, +5, +5$ | 25 |
| `reward1=[3,8,2,6]`, `reward2=[5,1,7,4]` | 3 | 17 | $+7, +2, -2$ | 24 |

The fifth row is the instructive one: all four gains are negative, yet exactly two of them must be accepted, and the two *largest* — that is, the two least negative — are the right ones. The fourth row shows the other extreme, where $k = 0$ makes the selection empty and the answer is the baseline itself.

## 5. Invariant and correctness of the exchange argument

**Invariant.** At every point of the greedy pass, the selected set consists of the largest gains examined so far, and its size never exceeds $k$. The invariant holds initially with an empty set; when a new gain arrives it is selected exactly when the set is not yet full or when it beats the smallest selected gain, in which case the smallest selected gain is discarded. Either way the selected set remains the best $k$-subset of the gains seen so far.

**Soundness.** The rule returns a genuine assignment: it names exactly $k$ indices for the first mouse, every index belongs to exactly one mouse, and the reported total is the sum of the corresponding rewards. Nothing outside the two reward vectors is introduced.

**Optimality by exchange.** Let $S$ be the set chosen by the rule and let $T$ be any other set of exactly $k$ indices, and suppose for contradiction that $T$ scores strictly more. Then $\sum_{i \in T} d_i > \sum_{i \in S} d_i$, so some index $b \in T \setminus S$ has $d_b$ strictly greater than some index $a \in S \setminus T$. (If every such $d_b$ were at most every such $d_a$, the two sums would satisfy the opposite inequality.) Now exchange $a$ for $b$ inside $S$: the new set still has $k$ indices, and its gain sum changes by $d_b - d_a > 0$, contradicting the invariant's claim that $S$ is the best $k$-subset. Hence no set beats $S$, and the rule is optimal.

**Ties and multiplicities of optima.** When gains are equal, several sets achieve the maximum, as in the instance whose four gains are all $+5$: every $3$-element subset scores $25$. The optimum *value* is unique even when the optimum assignment is not, which is why only the total is required as output.

## 6. Traps, boundary behaviour, and rejected alternatives

| Situation | Instance or probe | Correct handling | What goes wrong otherwise |
|---|---|---|---|
| Fewer positive gains than $k$ | `reward1=[2,3,4,5]`, `reward2=[10,9,8,7]`, $k=2$ | accept the two least negative gains, total $28$ | taking only positive gains yields fewer than $k$ types for mouse 1 |
| All gains equal | `reward1=[6,7,8,9]`, `reward2=[1,2,3,4]`, $k=3$ | any $3$ of the $4$ indices, total $25$ | assuming a unique answer wastes effort or breaks comparisons |
| $k = 0$ | `reward1=[5,6,7]`, `reward2=[7,6,5]` | mouse 2 eats everything, total $18$ | forcing a selection produces an invalid assignment |
| $k = n$ | `reward1=[1,1]`, `reward2=[1,1]` | mouse 1 eats everything, total $2$ | same failure in the opposite direction |
| Ranking by `reward1` instead of by the gain | probe `reward1=[10,9]`, `reward2=[100,1]`, $k=1$ | gains are $-90$ and $+8$; give mouse 1 index 1 for $109$ | ranking by `reward1` picks index 0 and scores $11$ |
| One greedy swap at a time | any instance with mixed gains | compare every gain before committing | an early local win can block a larger later one |

The fifth row is a deliberately constructed probe, not part of the package's case set; it exists only to separate the two rankings, and its arithmetic is checkable in one line: $\text{reward2}[0] + \text{reward1}[1] = 100 + 9 = 109$ beats $\text{reward1}[0] + \text{reward2}[1] = 10 + 1 = 11$. The lesson is that the correct ranking key is the *gain*, because the gain is the only quantity the objective actually contains.

| Method | Time | Always optimal | Weakness |
|---|---|---|---|
| Enumerate every $k$-element subset | $\Theta\binom{n}{k}$ | yes | astronomically slow once $n$ reaches $10^{5}$ |
| Rank by `reward1`, take its $k$ largest | $O(n \log n)$ | no | ignores the alternative reward of the second mouse |
| Rank by the gain $d_i$, take the $k$ largest | $O(n \log n)$ | yes | none; this is the method the lesson derives |
| Keep a min-heap of the $k$ best gains | $O(n \log k)$ | yes | same optimum with less work when $k \ll n$; needs care with negative gains |

## 7. Complexity of the gain-ranking method

The method performs one pass to form the gains and the baseline, then a sort of $n$ numbers, then one final pass over the selected prefix. With $n = \text{reward1.length} \le 10^{5}$ the dominant term is the sort, so the running time is

$$O(n \log n),$$

and $O(n)$ additional passes contribute nothing asymptotically. Replacing the sort with a bounded min-heap of capacity $k$ reduces the time to $O(n \log k)$, which is strictly better when $k$ is small and never worse than $O(n \log n)$ because $k \le n$; the enumeration alternative, by contrast, is exponential in $k$ and cannot be repaired.

The auxiliary space is $O(n)$ for the stored gains and the ordering, or $O(k)$ for the heap variant, excluding the input vectors and the single returned integer. The arithmetic itself stays within ordinary integer range: each reward is at most $1000$ and $n \le 10^{5}$, so the maximum possible total is bounded by $10^{8}$, and the intermediate gains lie between $-999$ and $+999$.
