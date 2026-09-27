# Guided Example: Left and Right Sum Differences

## 1. What each output position is really asking for

For every index $i$ of a 0-indexed array `nums` of length $n$, define

$$\text{leftSum}[i] = \sum_{k < i} \texttt{nums}[k], \qquad \text{rightSum}[i] = \sum_{k > i} \texttt{nums}[k],$$

where a sum over no indices is $0$. The output is the array of magnitudes $\text{answer}[i] = \lvert \text{leftSum}[i] - \text{rightSum}[i] \rvert$.

The element `nums[i]` itself belongs to neither side, which is the single most important detail in the problem: at index $i$ the array is split into three parts — everything strictly before $i$, the element at $i$, and everything strictly after $i$. Two useful consequences follow immediately.

- Every side sum is a sum of $n - 1$ elements at most, and the two sides together always total $T - \texttt{nums}[i]$, where $T = \sum_k \texttt{nums}[k]$ is the array total.
- Because the constraint guarantees $\texttt{nums}[i] \ge 1$, all elements are positive. Positivity is not needed for correctness of the running sums, but it produces the monotonicity described in section 4, which explains the shape of the output.

## 2. The worked instance

- Input: `nums = [10, 4, 8, 3]`
- Required output: `[15, 1, 11, 22]`

The array total is $T = 10 + 4 + 8 + 3 = 25$. Reading the definition literally gives the two side arrays and then the magnitudes:

| $i$ | $\text{leftSum}[i]$ | `nums[i]` | $\text{rightSum}[i]$ | Signed difference $D_i = \text{leftSum}[i] - \text{rightSum}[i]$ | $\lvert D_i \rvert$ |
|---|---|---|---|---|---|
| 0 | 0 | 10 | 15 | $-15$ | 15 |
| 1 | 10 | 4 | 11 | $-1$ | 1 |
| 2 | 14 | 8 | 3 | $11$ | 11 |
| 3 | 22 | 3 | 0 | $22$ | 22 |

The two boundary rows are the interesting ones. At $i = 0$ there is nothing to the left, so $\text{leftSum}[0] = 0$ and the magnitude equals the whole suffix sum $15$. At $i = 3$ there is nothing to the right, so $\text{rightSum}[3] = 0$ and the magnitude equals the whole prefix sum $22$. Computing these four rows directly would cost a separate scan per index; the next section shows how one pass over the array produces all of them.

## 3. One pass with two running sums

Keep a running left sum $\ell$ and a running right sum $\rho$. Initialize $\ell = 0$, because nothing precedes index $0$, and $\rho = T$, because the suffix starting at index $0$ is the whole array. Before index $i$ can be answered, `nums[i]` must leave the right side; after it is answered, `nums[i]` joins the left side. The order of those two movements is forced, and the correction is exactly what the element in the middle of the split demands.

| Step $i$ | $\ell$ before | $\rho$ before | $\rho$ after removing `nums[i]` | $\lvert \ell - \rho \rvert$ recorded | $\ell$ after adding `nums[i]` |
|---|---|---|---|---|---|
| 0 | 0 | 25 | 15 | 15 | 10 |
| 1 | 10 | 15 | 11 | 1 | 14 |
| 2 | 14 | 11 | 3 | 11 | 22 |
| 3 | 22 | 3 | 0 | 22 | 25 |

Four steps, four output entries, and every intermediate quantity is a genuine side sum: the $\rho$ column after the removal is $\text{rightSum}[i]$ and the $\ell$ column before the record is $\text{leftSum}[i]$. The invariant that keeps this honest is

$$\ell + \texttt{nums}[i] + \rho = T \qquad \text{before step } i,$$

which holds at the start because $\ell = 0$ and $\rho = T$ with $i = 0$, and is preserved because the step moves `nums[i]` out of $\rho$ and into $\ell$ while the next element becomes the new middle term: $\ell' + \texttt{nums}[i+1] + \rho' = (\ell + \texttt{nums}[i]) + \texttt{nums}[i+1] + (\rho - \texttt{nums}[i]) = T$.

Two failure modes are therefore excluded by construction. Recording the magnitude **before** removing `nums[i]` from $\rho$ would compare the left side against a right side that still contains the middle element, inflating $\rho$ by `nums[i]` and reporting $|0 - 25| = 25$ at $i = 0$ instead of $15$. Adding `nums[i]` to $\ell$ **before** recording would do the same damage to the other side, reporting $|10 - 15| = 5$ at $i = 0$. The correct discipline is: remove from the right, record, then add to the left.

## 4. The closed form and the monotonic invariant

Let $P_i = \sum_{k < i} \texttt{nums}[k]$ denote the prefix sum. Since the two sides total $T - \texttt{nums}[i]$, we have $\text{rightSum}[i] = T - P_i - \texttt{nums}[i]$, so each signed difference has a compact closed form:

$$D_i = \text{leftSum}[i] - \text{rightSum}[i] = 2P_i + \texttt{nums}[i] - T, \qquad \text{answer}[i] = \lvert D_i \rvert .$$

The signs in the worked instance are $-15, -1, 11, 22$: the left side starts smaller than the right and overtakes it exactly once. That crossing is not an accident of this input. Subtracting consecutive closed forms,

$$D_{i+1} - D_i = 2\left(P_{i+1} - P_i\right) + \texttt{nums}[i+1] - \texttt{nums}[i] = \texttt{nums}[i] + \texttt{nums}[i+1] \ge 2 > 0,$$

because every element is at least $1$. The signed differences therefore form a strictly increasing sequence, which has two sharp consequences worth stating as a single invariant:

> $D_i$ is strictly increasing in $i$, so the sequence $\lvert D_i \rvert$ falls while $D_i < 0$, reaches its minimum, and rises once $D_i > 0$; and $D_i = 0$ can hold for **at most one** index.

The second consequence is a real structural restriction on the output: a single index where both sides are equal is possible, but never two. An instance from the authored cases demonstrates the crossing at its exact zero:

| $i$ | Prefix $P_i$ | $D_i = 2P_i + \texttt{nums}[i] - T$ | Increment $D_i - D_{i-1}$ | $\lvert D_i \rvert$ |
|---|---|---|---|---|
| 0 | 0 | $-13$ | — | 13 |
| 1 | 2 | $-6$ | 7 | 6 |
| 2 | 7 | $0$ | 6 | 0 |
| 3 | 8 | $7$ | 7 | 7 |
| 4 | 14 | $14$ | 7 | 14 |

Here $T = 15$ for `nums = [2, 5, 1, 6, 1]`, the magnitudes $13, 6, 0, 7, 14$ form the predicted valley, and index `2` is the unique balanced position because $P_2 = 7$ makes both sides sum to $7$. The increments are $7, 6, 7, 7$, each equal to the sum of two adjacent elements, and never zero or negative.

## 5. Traps and boundary behaviour

| Situation | Instance | Expected output | What the lesson's reasoning says |
|---|---|---|---|
| Single element | `[1]` | `[0]` | both sides are empty sums equal to $0$, so $\lvert 0 - 0 \rvert = 0$; the empty sum is $0$, not undefined |
| Two elements, extreme values | `[1, 100000]` | `[100000, 1]` | each element is the entire opposite side, and the magnitude is the other value |
| Symmetric outer values | `[100000, 1, 100000]` | `[100001, 0, 100001]` | the middle index is the unique balanced position; the ends see one large element against the other |
| All values equal | `[5, 5, 5, 5]` | `[15, 5, 5, 15]` | equal elements at mirrored offsets produce mirrored magnitudes |
| Increasing values | `[1, 2, 3, 4, 5, 6, 7]` | `[27, 24, 19, 12, 3, 8, 21]` | the crossing lies between index `4` and index `5`; no index is balanced |
| Decreasing values | `[9, 8, 7, 6, 5, 4, 3, 2, 1]` | `[36, 19, 4, 9, 20, 29, 36, 41, 44]` | the minimum magnitude $4$ sits at index `2`, and the sequence rises afterwards |
| Alternating magnitudes | `[1, 100000, 2, 99999, 3, 99998]` | `[300002, 200001, 99999, 2, 100004, 200005]` | the crossing lies between index `2` and index `3`, where the largest magnitudes surround the smallest |
| Maximum size and values | $n = 1000$, $\texttt{nums}[i] = 10^5$ | side sums up to $10^8$ | the largest side sum is $999 \cdot 10^5 = 9.99 \times 10^7$, far inside a 32-bit signed range |

| Trap | Symptom | Correction |
|---|---|---|
| Including the middle element in a side | at $i = 0$ the reading becomes $\lvert 0 - 25 \rvert = 25$ instead of `15` | subtract `nums[i]` from the right sum before recording and add it to the left sum afterwards |
| Dropping the absolute value | the early entries of the worked instance come out as `-15`, `-1` | the contract asks for $\lvert \text{leftSum}[i] - \text{rightSum}[i] \rvert$, so the sign is discarded |
| Recomputing each side independently | $n$ separate scans, $\Theta(n^2)$ work | two running sums update both sides in one pass |
| Expecting several balanced indices | searching for multiple zeros in the output | $\lvert D_i \rvert$ has a single valley, so $D_i = 0$ occurs at most once |
| Treating the ends as special cases | guarding index `0` and index `n-1` separately | the empty-sum convention $0$ makes both boundaries ordinary steps of the same loop |

| Approach | Passes over the array | Extra space | When it is the right choice |
|---|---|---|---|
| Recompute each side per index | $n$ | $O(1)$ | never for $n \le 1000$ in a hurry, but it is the literal reading of the definition |
| Precompute prefix and suffix arrays | 2 | $\Theta(n)$ | useful when many different index ranges must be queried afterwards |
| One pass with two running sums | 1 | $O(1)$ | the intended method here: both sides are always available at the moment they are needed |

## 6. Time and auxiliary space

- **Time.** Computing the total $T$ costs one pass, and the answering pass performs a constant amount of work at each of the $n$ indices: one subtraction, one absolute difference, one addition. The running time is $\Theta(n)$, which is optimal because every element must be read at least once and every output entry must be written.
- **Auxiliary space.** Beyond the returned array, the method holds the two running sums, the total, and the loop position: $O(1)$ extra space. The output itself is $\Theta(n)$ and is required by the contract, so it is not counted as auxiliary.
- The bound does not depend on the magnitude of the values; only the number of elements matters, and the constraint $n \le 1000$ with $\texttt{nums}[i] \le 10^5$ shows the arithmetic stays small enough that no overflow handling is needed in a typical fixed-width language.