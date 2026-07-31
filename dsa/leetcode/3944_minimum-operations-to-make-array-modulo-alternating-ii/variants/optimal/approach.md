## General

**Reduce every value to a point on a residue cycle.** Suppose an element currently has remainder $r$ and its parity group chooses target remainder $t$. Repeated unit changes may approach $t$ clockwise or counterclockwise around the cycle of $k$ residues, so the exact minimum contribution of this element is

$$
d(r,t)=\min\!\left(\lvert r-t\rvert,\ k-\lvert r-t\rvert\right).
$$

Only the remainder is relevant. Count the occurrences of every residue separately for even and odd indices. For either parity group with frequency array $f$, define

$$
C_t=\sum_{r=0}^{k-1} f_r\,d(r,t),
$$

the total cost of choosing target remainder $t$. Computing this sum independently for all $k$ targets would repeat the same work. Instead, derive all totals from one circular sweep.

**Move the target while maintaining a half-circle window.** Let $m=\lfloor k/2\rfloor$, let $N=\sum_r f_r$, and for a current target $t$ define the clockwise half-window

$$
W_t=\sum_{j=1}^{m} f_{(t+j)\bmod k}.
$$

Initialize $C_0$ directly as $\sum_r f_r\min(r,k-r)$. When the target advances from $t$ to $t+1$, every residue in the half-window becomes one step closer and contributes `-1` per occurrence; residues on the other side become one step farther and contribute `+1`.

For even $k$, this gives

$$
C_{t+1}=C_t+N-2W_t.
$$

For odd $k$, the residue at $(t+m+1)\bmod k$ is tied between the two directions before and after the move, so its distance does not change. Correcting the provisional `+1` for that residue gives

$$
C_{t+1}=C_t+N-2W_t-f_{(t+m+1)\bmod k}.
$$

After each step, remove $f_{(t+1)\bmod k}$ from the window and add $f_{(t+m+1)\bmod k}$. Thus every target cost for each parity group is produced in one linear sweep. The recurrence is exact because the distance change of every residue belongs to exactly one of the closer, farther, or odd-cycle tied cases.

**Enforce distinct parity residues without a quadratic search.** Find the smallest and second-smallest totals among the odd-group costs. For each even target `x`, pair it with the cheapest odd target unless that target is also `x`; in that one case, use the second-cheapest odd target. This considers the best legal partner for every possible `x`, so the smallest combined total is exactly the global optimum. Tied minima are retained as two separate residues, which also handles an empty parity group when `n = 1`.

## Complexity detail

Let $n=\lvert\texttt{nums}\rvert$. Building the two residue-frequency arrays takes $O(n)$ time. Each circular cost sweep, the two-minimum scan, and the final combination scan take $O(k)$ time, for $O(n+k)$ total time.

The two frequency arrays and two cost arrays contain $O(k)$ integers. All remaining state is constant-sized, so auxiliary space is $O(k)$.

For scaling evidence, each benchmark sets both $n$ and $k$ equal to its size and uses three tiers with sizes `32`, `128`, and `512`. The accepted recurrence grows linearly in the tier size, whereas recomputing every target from every array element takes $\Theta(nk)=\Theta(n^2)$ time on this workload.

## Alternatives and edge cases

- **Recompute each target cost directly:** Summing every element's distance for every possible target is correct, but it costs $O(nk)$ time and is the principal slower class exercised by the benchmark.
- **Enumerate every pair `(x, y)`:** Even after obtaining both cost arrays, checking all distinct residue pairs costs $O(k^2)$. The two smallest odd totals provide the best legal partner in constant time per even residue.
- **Use ordinary absolute difference:** The residues form a cycle. Ignoring the wraparound path overcharges transformations such as remainder `0` to remainder `k - 1`.
- **Choose the independent minimum for each parity:** If both minima use the same residue, that pair is forbidden. The second-best cost is required even when it ties the best value at another residue.
- **Treat even and odd moduli identically:** An odd cycle has one residue whose distance is unchanged during each target step; omitting its correction corrupts the recurrence.
- **Single-element input:** The odd-index group is empty, but `k >= 2` always leaves a distinct zero-cost odd residue, so the minimum can still be zero.
- **Large original values:** Reduce values modulo `k` before counting them; the quotient cannot affect the number of operations needed to reach a target residue.

