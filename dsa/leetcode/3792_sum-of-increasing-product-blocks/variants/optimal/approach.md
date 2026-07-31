## General

The blocks partition one increasing stream of positive integers. Keep `next_value` at the first unused integer. For each `block_length` from `1` through `n`, multiply exactly that many successive values into `block_product`, reducing after every multiplication, and advance `next_value` after each use. Add the completed product to `total`, again modulo $10^9+7$.

This directly enforces the source's block boundary rule. Before block $i$, `next_value` is one greater than the final value of block $i-1$. The inner loop therefore consumes precisely the next $i$ integers, neither skipping nor reusing any value. After the final iteration, every one of the first `n` block products has been added once, so `total` equals `F(n)` modulo the required modulus.

Reducing intermediate products is valid because modular multiplication and addition preserve the final remainder. It also prevents the integers held by the implementation from growing with the enormous unreduced block products.

## Complexity detail

Let $N=\texttt{n}$. The algorithm performs one multiplication for every value in the first $N$ blocks:

$$
1+2+\cdots+N=\frac{N(N+1)}{2}.
$$

The time complexity is therefore $O(N^2)$. Apart from loop counters, the next value, one block product, and the accumulated sum, it stores no data that grows with $N$, so the extra space complexity is $O(1)$.

## Alternatives and edge cases

- **Rescan the complete integer prefix for each block:** Testing every value through $N(N+1)/2$ separately for every block is correct, but it spends $O(N^3)$ time deciding which values belong to each product.
- **Materialize every block:** Building lists of the consecutive values before multiplying them preserves the result but uses $O(N^2)$ total storage unnecessarily.
- **Factorial quotients:** A block product can be written as a quotient of two factorials. Computing it modulo a prime requires modular inverses and offers no benefit over consuming the at most `500500` values directly.
- **Minimum input:** For `n = 1`, the only block is `1`, so the answer is `1`.
- **Block boundaries:** The first value of block $i$ is $i(i-1)/2+1$ and its final value is $i(i+1)/2$.
- **Modulo timing:** Reduce both each multiplication and each addition; postponing reduction creates extremely large intermediate integers even though the final answer is small.
