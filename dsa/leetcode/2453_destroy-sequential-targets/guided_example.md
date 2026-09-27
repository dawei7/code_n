# Guided Example: Destroy Sequential Targets

## 1. The Instance We Will Trace

- **Input:** `nums = [3, 7, 8, 1, 1, 5]`, `space = 2`
- **Required output:** `1`

Seeding the machine with a value $v$ lets it destroy every target whose value can be written as $v + c \cdot \texttt{space}$ for some non-negative integer $c$. We must return the **smallest** seed value that destroys the **maximum** number of targets in `nums`. This instance is chosen because it contains a duplicated seed candidate ($1$ appears twice), a target ($8$) that is unreachable from the winning seed, and a class structure where the optimal seed is not the largest value present.

## 2. Reachability Is Decided by a Residue

The destroyed set of a seed $v$ is

$$
\mathcal{D}(v) = \{\, t \in \texttt{nums} : t = v + c \cdot \texttt{space},\ c \in \mathbb{Z}_{\ge 0} \,\}.
$$

Two facts follow immediately and together reduce the whole problem to arithmetic on residues.

First, $t = v + c \cdot \texttt{space}$ forces $t \equiv v \pmod{\texttt{space}}$, so a seed can only reach targets that share its residue modulo `space`. The residues split the number line into the disjoint classes $\{r, r + \texttt{space}, r + 2\,\texttt{space}, \dots\}$, one for each $r \in \{0, \dots, \texttt{space}-1\}$, and the classes are determined before any seed is chosen.

Second, the factor $c$ is restricted to be non-negative, so a seed only reaches targets **at or above itself** within its own class. Seeding higher inside a class therefore discards part of that class, and it never gains anything outside it. For the winning class, the best seed is its smallest member, because that member reaches every other member of the same class.

Because every target is a positive integer, "residue modulo `space`" is exactly the remainder computed by ordinary integer division, so the class of a value $v$ is identified by `v % space` with no sign correction.

## 3. Counting State in a Single Pass

The state is a count of how many targets belong to each residue class, together with a running best choice. Reading the array left to right:

| step | value $v$ read | class $v \bmod 2$ | class counts after the read | running best (count, value) |
|---|---|---|---|---|
| 1 | $3$ | $1$ | $\{1 \mapsto 1\}$ | $(1, 3)$ |
| 2 | $7$ | $1$ | $\{1 \mapsto 2\}$ | $(2, 3)$ |
| 3 | $8$ | $0$ | $\{1 \mapsto 2,\ 0 \mapsto 1\}$ | $(2, 3)$ |
| 4 | $1$ | $1$ | $\{1 \mapsto 3,\ 0 \mapsto 1\}$ | $(3, 3)$ |
| 5 | $1$ | $1$ | $\{1 \mapsto 4,\ 0 \mapsto 1\}$ | $(4, 1)$ |
| 6 | $5$ | $1$ | $\{1 \mapsto 5,\ 0 \mapsto 1\}$ | $(5, 1)$ |

The running best is updated whenever the current value's class count exceeds the best count so far, or ties it while the current value is smaller. Step 5 is the interesting update: the second copy of $1$ lifts its class to four members, and because $1 < 3$ the best pair becomes $(4, 1)$ — the tie-break rule is exercised even though the residue class itself did not change.

| class $r$ | member targets in `nums` | count | minimum member |
|---|---|---|---|
| $0$ | $8$ | $1$ | $8$ |
| $1$ | $3, 7, 1, 1, 5$ | $5$ | $1$ |

Class $1$, the odd numbers, wins with five members, and its minimum member is $1$. Note that the winning class does **not** contain the largest target ($8$ is even) and that membership, not value ordering, decides the contest.

## 4. Why the Class Minimum Is the Only Seed Worth Choosing

It is worth checking explicitly that seeding with a larger member of the winning class destroys strictly less. The arithmetic progression reachable from seed $v$ is $\{v, v + 2, v + 4, \dots\}$ when `space` is $2$.

| seed $v$ | reachable targets in `nums` | destroyed count | comment |
|---|---|---|---|
| $1$ | $1, 1, 3, 5, 7$ | $5$ | the class minimum; reaches the whole class |
| $3$ | $3, 5, 7$ | $3$ | two targets (both copies of $1$) fall below the seed |
| $5$ | $5, 7$ | $2$ | only targets at or above $5$ remain reachable |
| $7$ | $7$ | $1$ | the largest member reaches only itself |
| $8$ | $8$ | $1$ | a different class, and a singleton |

Every increase of the seed inside class $1$ removes the class members strictly below it, and no target outside the class ever becomes reachable, since the residue of $v + c \cdot \texttt{space}$ is fixed. Hence within a class the destroyed count is non-increasing as the seed grows, and it is maximal precisely at the class minimum. This eliminates every other seed in the class without evaluating it separately: the comparison table above is an illustration of a monotonicity argument, not an enumeration required by the method.

## 5. The Tie-Break and the Complete Selection

The rule is: among all classes, take those with the largest member count; among those, return the smallest member value. The second example in the statement shows why the tie-break is needed.

| instance | class $0$ members | class $1$ members | largest count | smallest member of a tied class | answer |
|---|---|---|---|---|---|
| `[3, 7, 8, 1, 1, 5]`, `space = 2` | $8$ (count $1$) | $3,7,1,1,5$ (count $5$) | $5$ | $1$ | $1$ |
| `[1, 3, 5, 2, 4, 6]`, `space = 2` | $2,4,6$ (count $3$) | $1,3,5$ (count $3$) | $3$ (tied) | $\min(2, 1) = 1$ | $1$ |
| `[2, 4, 6, 8]`, `space = 4` | $4,8$ (count $2$) | $2,6$ (count $2$) | $2$ (tied) | $\min(4, 2) = 2$ | $2$ |
| `[1, 12, 22, 32]`, `space = 10` | $12,22,32$ (count $3$) | $1$ (count $1$) | $3$ | $12$ | $12$ |

The last row is the instructive one: the global minimum of the array is $1$, but its class is a singleton, so the answer is $12$. A method that returns the minimum array element whenever the counts tie, or that starts from the global minimum, fails here.

The first row reproduces the traced instance: answer $1$, matching the authored expected output.

## 6. The Invariant and Why the Method Is Correct

**Partition invariant.** At every point during the pass, the residue counts describe a partition of the values read so far: every value increments exactly one counter, namely the counter of its residue class, and no counter is ever decremented. Therefore, when the pass finishes, the count stored for a residue $r$ equals the number of positions $i$ with `nums[i] % space == r`, which is exactly $\lvert \mathcal{D}(m_r) \rvert$ for the class minimum $m_r$.

**Optimality within a class.** For any seed $v$ in class $r$, reachability requires a non-negative multiple of `space`, so $\mathcal{D}(v) \subseteq \mathcal{D}(m_r)$ whenever $m_r \le v$ and both lie in class $r$. The class minimum therefore dominates every other seed of its class, and no seed outside the class can reach any class member at all. Maximizing over all seeds is thus the same as maximizing the class counts.

**Tie-break soundness.** Among classes tied at the maximum count, the returned value must be the smallest member of any tied class. The sweep achieves this by comparing values, not class identifiers: every member $v$ of a tied class reports the same count, so the minimum over all values reporting the maximum count is the minimum of the tied classes' minima. Distinct classes have distinct minimum members — equal values necessarily share a residue — so the tie-break never has to resolve an equality between two different candidates, and the answer is unique.

**Completeness.** Every target belongs to exactly one residue class, so no target is invisible to the selection; every class is considered, so no seed with a larger destroyed set can be missed. The returned value is a seed drawn from `nums`, as the statement requires, and it attains the maximum destroyed count.

## 7. Boundaries and Traps This Instance Exposes

| situation | concrete instance | outcome and the trap it exposes |
|---|---|---|
| Tied class counts | `[1, 3, 5, 2, 4, 6]`, `space = 2` | Both classes destroy three targets, so the tie-break decides: return the smaller class minimum, $1$. Without the tie-break the answer is not determined. |
| Dominant class avoids the global minimum | `[1, 12, 22, 32]`, `space = 10` | The largest class is $\{12, 22, 32\}$ and the answer is $12$, although $1$ is the smallest value present. Minimum of the array is not the answer. |
| `space` larger than every target | `[6, 2, 5]`, `space = 100` | All residues are distinct, so every class has one member and every seed destroys exactly one target; the answer is the smallest value, $2$. |
| `space = 1` | `[9, 3, 7, 3]`, `space = 1` | A single residue class contains everything, so the seed $3$ destroys all four targets and the class minimum $3$ is the answer. |
| Duplicate target values | the two copies of $1$ in the traced instance | Each position counts separately: both copies raise the count of class $1$ and both are destroyed. Deduplicating the input would undercount. |
| Largest seed inside a class | seed $7$ in the traced instance | Destroys only itself. Seeds are not interchangeable inside a class; only the class minimum is optimal. |
| Values near the upper limit | `[1000000000, 999999993, 999999993, 999999986]`, `space = 7` | All four values share residue $6$ modulo $7$, so all four are destroyed and the answer is the smallest, $999999986$. Large magnitudes change nothing because only residues and comparisons are used. |
| Single target | `[5]`, `space = 3` | One class with one member; the answer is $5$. |
| Positivity of targets | any input | Targets are positive, so remainders are ordinary residues. Were negative values allowed, the mathematical class of $v$ would differ from `v % space` and the correspondence would need an explicit correction. |
| Membership versus value order | any input | Selection is by class size first, value second. Sorting the array alone does not reveal class sizes; the count of residues is what orders the candidates. |

## 8. Alternative Methods and Their Trade-Offs

| method | time | auxiliary space | trade-off |
|---|---|---|---|
| Residue counting with a sweep for the best value (derived above) | $O(N)$ expected | $O(N)$ | One modulo and one map increment per target, then one linear sweep. No ordering assumptions about the input. |
| Sort the array, then group equal residues in order | $O(N \log N)$ | $O(N)$ | Sorting ascending makes the first element of each residue run the class minimum automatically, so the tie-break falls out of the order; it costs a logarithmic factor and mutates or copies the input. |
| Scan every candidate seed against every target | $O(N^2)$ | $O(1)$ | Directly evaluates $\mathcal{D}(v)$ for each $v$ by testing reachability. Correct and space-free, but quadratic; hopeless at $N = 10^5$. |
| Enumerate reachable values up to the maximum target | $O\bigl(N + \max(\texttt{nums})/\texttt{space}\bigr)$ | $O\bigl(\max(\texttt{nums})/\texttt{space}\bigr)$ | Builds an explicit grid of the number line. Values reach $10^9$, so the grid is astronomically large; residues avoid it entirely. |
| Sort by value descending and take the first full class | $O(N \log N)$ | $O(N)$ | Works only if the class minima are tracked alongside counts; by itself, descending order visits the *worst* seed of each class first, so it must be paired with a class-completion rule. |
| Count residues after minimizing each class | $O(N)$ expected | $O(N)$ | Equivalent to the derived method: compute each class minimum first, then count with the minimum as the seed. One extra map for minima and no gain over counting directly. |

## 9. Complexity Derivation

Let $N = \texttt{nums.length}$ and let $R \le \min(N, \texttt{space})$ be the number of distinct residue classes actually present.

- **Counting pass.** Each target costs one modulo operation and one hash-map increment. The increment is expected $O(1)$ and never depends on `space` or on the magnitude of the values, so the pass costs $O(N)$ expected time. Its table holds at most $R$ entries.
- **Selection sweep.** One more pass over `nums` performs a constant number of comparisons per element — the map lookup plus the two-part tie-break test — so it is $O(N)$.
- **Total.** $O(N)$ expected time, with no sorting and no dependence on `space` other than through the modulo itself. The worst case degrades only if hash collisions are adversarial, exactly as in any hash-based count.

For auxiliary space, the residue table stores at most one counter per distinct residue, so it needs $O(R) \subseteq O(N)$ entries; the selection sweep keeps only two scalars, the best count and the best value. Because $R \le N$ and the input is read-only, the bound is $O(N)$ auxiliary space, and it is genuinely used only when many distinct residues appear — in the extreme `space > max(nums)` case the table holds $N$ entries of count $1$.