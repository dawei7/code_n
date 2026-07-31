## General

An integer whose binary representation contains only set bits is a run of $k$ ones. Its value is the geometric sum

$$
1+2+\cdots+2^{k-1}=2^k-1.
$$

Let $k$ be the bit length of `n`. Then $2^{k-1}\leq n<2^k$. The $k$-bit all-ones value $2^k-1$ is at least `n`: it is the largest value representable with $k$ bits. Every shorter all-ones value has at most $k-1$ bits and is no larger than $2^{k-1}-1$, which is strictly below `n`. Thus $2^k-1$ is the smallest eligible answer.

The construction is `(1 << n.bit_length()) - 1`. When `n` is already all ones, this expression reproduces it; otherwise it fills every position up to its most significant bit. The accepted native method and app-local `solve(n)` adapter use this identical expression.

## Complexity detail

Every legal `n` is at most $1000$, so it has at most ten binary digits. Under this source-bounded contract, reading the bit length, shifting, and subtracting have a fixed maximum cost: time is $O(1)$ and auxiliary space is $O(1)$.

For arbitrary-precision integers without the problem's upper bound, materializing the $k$-bit result would require $O(k)=O(\log n)$ bit work and output space. That generalized model is not the canonical contract. Because the complete legal workload ranges only from one to ten bits, runtime scaling cannot honestly distinguish asymptotic classes; the package uses a bounded-domain certificate with threshold-focused correctness cases instead.

## Alternatives and edge cases

- **Increment until all bits are set:** Testing `x & (x + 1) == 0` is correct, but the number of candidates examined depends on the gap to the next all-ones value.
- **Loop while building ones:** Repeatedly update `answer = (answer << 1) | 1` until it reaches `n`; this is clear but uses one iteration per bit rather than direct construction.
- **Convert through a binary string:** Replacing every position with `'1'` works, but allocates and parses text unnecessarily.
- **Already all ones:** Inputs such as `1`, `3`, `7`, and `15` must be returned unchanged.
- **Exact power of two:** Inputs such as `8` require one less than the next power of two, producing `15`.
- **Maximum input:** `1000` has ten bits, so the answer is `1023`.
