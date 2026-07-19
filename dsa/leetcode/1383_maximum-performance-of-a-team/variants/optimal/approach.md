## General
**Fix efficiency thresholds in descending order.** Sort engineers from greatest to least efficiency. When processing an engineer with efficiency `e`, every engineer seen so far has efficiency at least `e`; any team drawn from this prefix can therefore use `e` as its current minimum-efficiency threshold.

**Retain the largest speeds.** Keep a min-heap of at most `k` speeds from the processed prefix and their running sum. Insert the current speed, and if the heap grows beyond `k`, remove its smallest speed. The heap then holds the speed choices that maximize the sum under this threshold. Multiply the retained sum by `e` and update the best raw performance.

For an optimal team, consider the iteration containing its least-efficient member. Every team member is then available. Keeping the best speeds cannot produce a worse sum; if the threshold member itself is displaced, the replacement team has only higher-efficiency members and was also eligible at an earlier threshold. Thus some iteration attains the optimum. Apply the modulus only after selecting the largest raw product, because modular residues do not preserve numeric order.

## Complexity detail
Sorting the `n` engineers takes $O(n \log n)$ time. Each speed enters and leaves a heap of size at most `k` once, adding $O(n \log k)$ time, which is within $O(n \log n)$. The sorted pairs and heap use $O(n)$ space.

## Alternatives and edge cases
- **Enumerate teams:** Trying all subsets of size at most `k` is exponential and infeasible.
- **Resort every efficiency prefix:** Recompute the largest `k` speeds after each threshold. It is correct but can take $O(n^2 \log n)$ time.
- **Choose only the fastest engineers:** A very fast engineer with low efficiency can reduce the whole team's multiplier.
- **Choose only the most efficient engineers:** High efficiency may not compensate for a small total speed.
- **Team size is at most `k`:** The optimum may use fewer than `k` members; every prefix candidate naturally uses no more than the limit.
- **Single allowed member:** Maximize `speed[i] * efficiency[i]`.
- **Modulo timing:** Compare full-precision products and reduce only the final maximum.
