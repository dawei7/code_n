# Formal Mathematical Specification: Sieve of Eratosthenes

## 1. Definitions and Notation

Let $\mathbb{N} = \{0, 1, 2, \dots\}$ be the set of natural numbers. Given a target integer $N \in \mathbb{N}$, we define the objective as the identification of the set of prime numbers $\mathcal{P}_N \subseteq \{2, 3, \dots, N\}$ such that:
$$\mathcal{P}_N = \{p \in \mathbb{N} : 2 \le p \le N \land \forall a, b \in \mathbb{N}, p = ab \implies a=1 \lor b=1\}$$

We define a state space $\mathcal{S} = \{0, 1\}^{N+1}$, represented by a boolean vector $\mathbf{v} = (v_0, v_1, \dots, v_N)$, where $v_i = 1$ denotes that $i$ is a candidate prime, and $v_i = 0$ denotes that $i$ is composite. The algorithm acts as a transformation $T: \mathcal{S} \to \mathcal{S}$ that iteratively refines the set of candidates.

## 2. Algebraic Characterization

The algorithm relies on the Fundamental Theorem of Arithmetic, which implies that any composite number $n \le N$ must have a prime factor $p \le \sqrt{N}$. 

**Initialization:**
The initial state $\mathbf{v}^{(0)}$ is defined as:
$$v_i^{(0)} = \begin{cases} 1 & \text{if } i \ge 2 \\ 0 & \text{if } i < 2 \end{cases}$$

**Iterative Refinement:**
Let $\mathcal{P}_{\sqrt{N}} = \{p \in \mathbb{N} : p \le \sqrt{N}, v_p^{(k)} = 1\}$ be the set of primes identified up to the threshold $\lfloor \sqrt{N} \rfloor$. For each $p \in \mathcal{P}_{\sqrt{N}}$, we define the sieve operator $\sigma_p$ acting on the state vector $\mathbf{v}$:
$$\sigma_p(\mathbf{v})_i = \begin{cases} 0 & \text{if } i \in \{kp : k \in \mathbb{N}, k \ge p\} \\ v_i & \text{otherwise} \end{cases}$$

The final state $\mathbf{v}^*$ is the composition of these operators:
$$\mathbf{v}^* = \left( \prod_{p \le \sqrt{N}, p \in \mathcal{P}} \sigma_p \right) \mathbf{v}^{(0)}$$
The set of primes is then recovered as $\mathcal{P}_N = \{i \in \{0, \dots, N\} : v_i^* = 1\}$.

## 3. Complexity Analysis

### Time Complexity
The total number of operations $T(N)$ is proportional to the number of times the inner loop executes. For each prime $p \le \sqrt{N}$, the inner loop performs $\frac{N}{p} - p + 1$ assignments. Summing over all primes $p \le \sqrt{N}$:
$$T(N) = \sum_{p \le \sqrt{N}} \left( \frac{N}{p} \right) = N \sum_{p \le \sqrt{N}} \frac{1}{p}$$

By Mertens' Second Theorem, the sum of the reciprocals of primes up to $x$ is given by:
$$\sum_{p \le x} \frac{1}{p} = \ln(\ln x) + M + O\left(\frac{1}{\ln x}\right)$$
where $M$ is the Meissel-Mertens constant. Substituting $x = \sqrt{N}$:
$$T(N) = N \left( \ln(\ln \sqrt{N}) + M \right) = N \left( \ln\left(\frac{1}{2} \ln N\right) + M \right)$$
Since $\ln(\frac{1}{2} \ln N) = \ln(\ln N) - \ln 2$, the leading term is $N \ln(\ln N)$. Thus, $T(N) = O(N \log \log N)$.

### Space Complexity
The algorithm maintains a boolean array of size $N+1$. Each element $v_i$ requires constant space $O(1)$ (typically 1 bit or 1 byte depending on implementation). 
$$S(N) = \sum_{i=0}^{N} \text{space}(v_i) = (N+1) \cdot O(1) = O(N)$$
The auxiliary space is dominated by the boolean vector, yielding a total space complexity of $O(N)$.