# Formal Mathematical Specification: Estimating Pi via Monte Carlo

## 1. Definitions and Notation

Let $N \in \mathbb{Z}^+$ be the total number of independent trials (iterations).
Let $\mathcal{S} = [0, 1] \times [0, 1] \subset \mathbb{R}^2$ be the unit square in the Cartesian plane, representing the sample space of our random variables.
Let $X_i = (x_i, y_i)$ be a sequence of $N$ independent and identically distributed (i.i.d.) random vectors, where $x_i, y_i \sim \text{Uniform}(0, 1)$.

We define the indicator random variable $I_i$ for each trial $i \in \{1, \dots, N\}$ as:
$$I_i = \begin{cases} 1 & \text{if } x_i^2 + y_i^2 \le 1 \\ 0 & \text{otherwise} \end{cases}$$

The output of the algorithm is the estimator $\hat{\pi}_N$, defined as:
$$\hat{\pi}_N = 4 \cdot \frac{1}{N} \sum_{i=1}^N I_i$$

## 2. Algebraic Characterization

The correctness of the algorithm relies on the Law of Large Numbers. Consider the area of the region $\mathcal{C} \subset \mathcal{S}$ defined by the unit disk quadrant:
$$\text{Area}(\mathcal{C}) = \iint_{\mathcal{S}} \mathbb{I}(x^2 + y^2 \le 1) \, dA = \int_0^1 \int_0^{\sqrt{1-x^2}} dy \, dx = \frac{\pi}{4}$$

Since the points are sampled from a uniform distribution over $\mathcal{S}$, the probability $p$ that a point falls within $\mathcal{C}$ is:
$$p = P(X_i \in \mathcal{C}) = \frac{\text{Area}(\mathcal{C})}{\text{Area}(\mathcal{S})} = \frac{\pi/4}{1} = \frac{\pi}{4}$$

The sum $S_N = \sum_{i=1}^N I_i$ follows a Binomial distribution $B(N, p)$. By the Strong Law of Large Numbers, the sample mean converges almost surely to the expected value:
$$\lim_{N \to \infty} \frac{S_N}{N} = E[I_i] = p = \frac{\pi}{4}$$

Thus, the estimator $\hat{\pi}_N = 4 \frac{S_N}{N}$ is a consistent estimator for $\pi$, as:
$$\lim_{N \to \infty} \hat{\pi}_N = 4 \left( \frac{\pi}{4} \right) = \pi$$

The variance of our estimator, which dictates the precision for finite $N$, is given by:
$$\text{Var}(\hat{\pi}_N) = 16 \cdot \text{Var}\left(\frac{S_N}{N}\right) = \frac{16}{N^2} \cdot Np(1-p) = \frac{16}{N} \left(\frac{\pi}{4}\right)\left(1 - \frac{\pi}{4}\right) = \frac{\pi(4-\pi)}{N}$$

## 3. Complexity Analysis

### Time Complexity
The algorithm performs a sequence of $N$ iterations. In each iteration $i$, the following operations are performed:
1. Generation of two uniform random variables $x_i, y_i$.
2. Two multiplications and one addition to compute $x_i^2 + y_i^2$.
3. One comparison against the constant $1.0$.
4. One conditional increment of the counter `inside`.

Each of these operations is performed in constant time, $O(1)$. The total time complexity $T(N)$ is the summation of the work per iteration:
$$T(N) = \sum_{i=1}^N O(1) = O(N)$$
Thus, the algorithm is linear with respect to the number of samples $N$.

### Space Complexity
The algorithm maintains a fixed number of scalar variables: the loop counter $i$, the accumulator `inside`, and the temporary variables $x$ and $y$. These variables occupy a constant amount of memory regardless of the input size $N$.
$$S(N) = O(1)$$
The space complexity is therefore constant, $O(1)$, assuming the random number generator state is treated as a constant-sized object.