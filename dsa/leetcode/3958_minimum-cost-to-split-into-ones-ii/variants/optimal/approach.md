## General

The final state is fixed: the original integer `n` must eventually become exactly `n` copies of `1`. What is not fixed is the order of the splits. For example, one strategy might repeatedly separate a single `1` from the remaining number, while another strategy might first divide the number into two nearly equal parts and recursively split both parts. Because splitting `x` into `a + b` costs `a \cdot b`, it is natural to wonder whether carefully choosing unbalanced or balanced splits can reduce the total.

The key observation is that the total cost does not actually depend on the splitting order. Every legal complete strategy pays for exactly the same collection of pairs of final units.

**Give the final ones temporary identities**

Although all final values are numerically identical, imagine labeling them so that they can be followed through the process. A piece of value `x` contains `x` of these labeled units. When that piece is split into parts of sizes `a` and `b`, exactly `a` labeled units go to one child and `b` labeled units go to the other.

There are `a \cdot b` unordered pairs having one unit in the first child and one unit in the second child: each of the `a` choices on one side can be paired with each of the `b` choices on the other side. This is precisely the operation's cost.

Now follow any particular pair of final units. Initially the pair is together inside the original piece. Eventually the two units exist as separate copies of `1`, so there must be a first split that sends them to different children. That split charges exactly one unit of cost for this pair because the pair is one of its cross-child pairs. Afterward the two units remain in different pieces forever: later operations only split an existing piece and never merge pieces. Therefore the same pair can never be charged again.

This establishes two important facts:

- every unordered pair of final units is charged at least once, because its units must eventually become separate;
- every unordered pair is charged at most once, because after its first separation it can never be reunited.

Consequently, every pair is charged exactly once. The total cost is therefore the number of unordered pairs among `n` final units:

$$
\binom{n}{2} = \frac{n(n-1)}{2}.
$$

This pair-counting view explains why there is no search, greedy choice, or dynamic program in the Optimal solution. The apparent decisions in the splitting process change only when each pair is charged, not whether it is charged.

**The same result through algebra**

The identity can also be checked recursively. Suppose a first split divides `n` into positive integers `a` and `b`, where `a+b=n`. If fully splitting any size `x` costs `x(x-1)/2`, then the entire cost after this first choice is

$$
ab+\frac{a(a-1)}{2}+\frac{b(b-1)}{2}.
$$

Combining the terms gives

$$
\frac{2ab+a^2-a+b^2-b}{2}
=\frac{(a+b)^2-(a+b)}{2}
=\frac{n(n-1)}{2}.
$$

Notice that `a` and `b` disappear from the final expression. Thus every possible first split has the same total, assuming the two smaller parts are completely reduced. The base case is `n=1`, for which no operation is required and the formula gives zero. This is also a complete induction argument.

**How the implementation expresses the idea**

The source consists of one return statement:

```python
return n * (n - 1) // 2
```

The multiplication computes `n(n-1)`, and integer division by two produces the binomial coefficient. The division is always exact. Of the consecutive integers `n` and `n-1`, one must be even, so their product is divisible by two.

There is no simulation because simulation cannot improve the answer and would only reconstruct a quantity already known in closed form. There is also no need to choose an actual sequence of splits: the function is asked only for the minimum cost, and the proof shows that every complete sequence reaches that same cost.

For a small example, take `n=4`. There are six final pairs, so the answer is six. Splitting `4` as `1+3` costs three, then splitting `3` as `1+2` costs two, and finally splitting `2` costs one, totaling six. Splitting `4` as `2+2` costs four and splitting each `2` costs one more, again totaling six. These are different split trees, but both charge the same six pairs exactly once.

The boundary `n=1` is handled automatically: `1 \cdot 0 / 2=0`. This matches the meaning of the process, since a unit that is already one requires no split.

## Complexity detail

Let `n` be the input integer. The implementation performs a fixed number of arithmetic operations: one subtraction, one multiplication, one integer division, and the return. It neither loops over `n` nor recursively constructs the splitting tree.

- Time complexity is `O(1)` under the standard problem-model assumption that arithmetic on the constrained integer values takes constant time.
- Auxiliary space complexity is `O(1)` because the computation uses only temporary numeric values and allocates no collection or recursion stack.

The mathematical proof may discuss all `\binom{n}{2}` pairs, but the program does not enumerate those pairs. Pair counting is the reasoning used to derive the formula, not an operation performed at runtime.

In a bit-complexity model for arbitrarily large integers, multiplication and division would depend on the number of bits in `n`. Competitive-programming complexity conventions instead treat the problem's bounded integer arithmetic as constant time. Python also avoids fixed-width overflow by using arbitrary-precision integers, so the expression remains numerically correct even beyond common 32-bit limits, with the preceding bit-complexity qualification applying only to extraordinarily large values.

## Alternatives and edge cases

- **Dynamic programming over every split:** One could define `dp[x]` as the minimum cost to reduce `x` and try every `a` from `1` to `x-1` using `dp[a] + dp[x-a] + a(x-a)`. This repeats work to rediscover that every candidate has the same value. A straightforward implementation costs at least quadratic time and linear storage, whereas the pair invariant yields the answer directly.

- **Greedily peeling off one unit:** Repeatedly splitting `x` into `1` and `x-1` produces costs `n-1,n-2,\ldots,1`, whose sum is `n(n-1)/2`. This is a valid constructive strategy, but simulating its `n-1` operations takes linear time and does not beat any other strategy in total cost.

- **Always making balanced splits:** Balanced splitting may look attractive because an individual product reflects both child sizes, but it produces the same accumulated total. It changes the shape and depth of the split tree, not the set of final pairs that must be separated.

- **Searching for a special first split:** There is no uniquely optimal first decision. The algebraic identity shows that every positive `a,b` satisfying `a+b=n` leads to the same complete cost.

- **Already fully split input:** For `n=1`, the operation sequence is empty and the result is zero. The formula and source handle this without a special branch.

- **Exact division:** The use of `// 2` does not round away information. Since `n` and `n-1` are consecutive, one is even, so `n(n-1)` is always divisible by two.

- **Integer overflow in other languages:** Python's integers grow as needed. In a fixed-width language, the multiplication should be performed in a sufficiently wide type before division; dividing one even factor by two first is another safe way to reduce overflow risk.

- **Why the word “minimum” is not hiding a choice:** A minimum normally suggests comparing strategies. Here all legal complete strategies tie, so their shared cost is automatically the minimum as well as the maximum.
