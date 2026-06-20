# Freivalds' Algorithm (Matrix Product Check)

| | |
|---|---|
| **ID** | `randomized_07` |
| **Category** | randomized |
| **Complexity (required)** | $O(k * N^2)$ |
| **Difficulty** | 5/10 |
| **Interview relevance** | 2/10 |
| **Wikipedia** | [Freivalds' algorithm](https://en.wikipedia.org/wiki/Freivalds%27_algorithm) |

## Problem statement

Given three N x N matrices A, B, and C, verify whether the matrix multiplication of A and B equals C (i.e., verify if A x B = C).
A naive check would simply multiply A x B and compare the result to C, which takes $O(N^3)$ time using standard multiplication.
Design a randomized algorithm to verify the equality in $O(N^2)$ time with high probability!

**Input:** Three 2D arrays A, B, C of size N x N.
**Output:** Boolean `True` if A x B = C, `False` otherwise.

## When to use it

- When verifying a computationally expensive answer is vastly cheaper than generating the answer yourself.
- A classic example of a one-sided error Monte Carlo algorithm (if it says False, it is 100% False. If it says True, it is *probably* True).

## Approach

If we try to compute A x B, it takes $O(N^3)$.
Freivalds' beautiful trick is to introduce a random N x 1 column vector r containing only `0`s and `1`s.

Instead of checking if A x B = C, we check if A x (B x r) = C x r.

**Why is this faster?**
Because matrix multiplication is associative!
1. Multiplying B (an N x N matrix) by r (an N x 1 vector) results in a new N x 1 vector. This takes exactly $O(N^2)$ time!
2. Multiplying A (N x N) by that new vector (N x 1) takes another $O(N^2)$ time!
3. Multiplying C (N x N) by r (N x 1) takes $O(N^2)$ time!
By multiplying by the random vector first, we completely avoid the $O(N^3)$ matrix-matrix multiplication and only do three $O(N^2)$ matrix-vector multiplications!

**The Math (Probability of Failure):**
If A x B = C, then A x (B x r) will ALWAYS equal C x r. (0% chance of failure).
If A x B \neq C, what is the chance that they miraculously equal each other after being multiplied by r?
Freivalds proved that the probability of a false positive for a randomly generated 0/1 vector is at most \frac{1}{2}!
If we repeat this test k times with k different random vectors, the probability of a false positive drops exponentially to \frac{1}{2^k}.
With just k=10 iterations, the error rate is < 0.1\%. With k=40, the error rate is less than one in a trillion.

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for randomized_07: Freivald's Algorithm (Matrix Product Check).

Given three square n x n matrices A, B, C,
"""


def solve(mat_a, mat_b, mat_c, size, trials, seed_value):
    """Freivald's algorithm: k iterations of random
    vector r in {0, 1}^n; check if A*(B*r) == C*r.
    """
    import random
    rng = random.Random(seed_value)
    n = size
    A = mat_a
    B = mat_b
    C = mat_c
    for _ in range(max(1, trials)):
        r = [rng.randint(0, 1) for _ in range(n)]
        # Compute B * r.
        Br = [0] * n
        for i in range(n):
            s = 0
            for j in range(n):
                s += B[i][j] * r[j]
            Br[i] = s
        # Compute C * r.
        Cr = [0] * n
        for i in range(n):
            s = 0
            for j in range(n):
                s += C[i][j] * r[j]
            Cr[i] = s
        # Compute A * (B * r).
        ABr = [0] * n
        for i in range(n):
            s = 0
            for j in range(n):
                s += A[i][j] * Br[j]
            ABr[i] = s
        # Check A * (B * r) == C * r componentwise.
        if ABr != Cr:
            return False
    return True
```

</details>

## Walk-through

Let's assume A x B \neq C, and there is an error in the first row.
`N = 2`.
`A * B = [[5, 5], [0, 0]]`
`C =     [[5, 6], [0, 0]]` *(Error is 6 instead of 5)*.

1. Random vector `r = [1, 1]`.
2. Compute ABr = [[5, 5], [0, 0]] x [1, 1]^T = [10, 0]^T.
3. Compute Cr = [[5, 6], [0, 0]] x [1, 1]^T = [11, 0]^T.
4. `[10, 0] != [11, 0]`. Algorithm immediately returns `False`!

What if `r = [1, 0]`?
- ABr = [5, 0]^T.
- Cr = [5, 0]^T.
- `[5, 0] == [5, 0]`. FALSE POSITIVE!
This is why we must run it k times. The next run will likely roll `[1, 1]` or `[0, 1]` and catch the error.

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(N^2)$ | $O(N)$ |
| **Average** | $O(k * N^2)$ | $O(N)$ |
| **Worst** | $O(k * N^2)$ | $O(N)$ |

For each of the k iterations, we perform exactly three Matrix-Vector multiplications. Each multiplication requires iterating over N x N elements. Total time is $O(k \cdot N^2)$. Since k is a small constant, this is strictly $O(N^2)$, bypassing the Strassen algorithm bound for Matrix Multiplication ($O(N^{2.81})$).
Space complexity is $O(N)$ to store the 1D vectors `r`, `Br`, `ABr`, and `Cr`.

## Variants & optimizations

- **Fingerprinting:** Freivalds' algorithm is a specific application of "Polynomial Identity Testing" (Schwartz-Zippel Lemma). This overarching concept—compressing massive mathematical structures using random seeds to check equality—is heavily used in string fingerprinting (Rabin-Karp) and Merkle Trees.

## Real-world applications

- **Hardware Verification:** When designing specialized ASICs or GPUs for tensor calculations, you can use Freivalds' algorithm in the testing suite to rapidly verify that the silicon logic is correctly multiplying matrices without waiting for full $O(N^3)$ CPU validation.

## Related algorithms in cOde(n)

- **[randomized_06 - Estimating Pi](randomized_06_estimating-pi-via-monte-carlo.md)** — Another fundamental Monte Carlo algorithm.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
