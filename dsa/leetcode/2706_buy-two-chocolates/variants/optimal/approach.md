## General

**The cheapest pair decides both feasibility and leftover**

The task requires buying exactly two different chocolate entries while minimizing their total price.

If the sorted prices are:

$$
p_0\le p_1\le p_2\le\cdots,
$$

then $p_0+p_1$ is the smallest possible sum of any two entries. Every other pair replaces at least one of these values with an equal or larger value.

Therefore the entire decision depends on the two smallest prices.

**Sort so the two minima are first**

The exact implementation calls `prices.sort()`, which rearranges the input list in ascending order.

Because the constraints guarantee at least two prices, `prices[0]` and `prices[1]` always exist after sorting.

Their sum is stored as `cost`.

**Why two positions still represent two chocolates**

The list may contain equal prices, such as `[1, 2, 2]`.

Sorting does not merge equal entries. Indices zero and one refer to two distinct chocolate entries even if their numeric values happen to match.

This satisfies the requirement to buy exactly two chocolates rather than one price value twice without two available items.

**Affordability is inclusive**

Leftover money must be non-negative. Thus a pair is affordable when:

$$
\texttt{cost}\le\texttt{money}.
$$

The exact return condition is `money if money < cost else money - cost`.

When cost equals money, the comparison `money < cost` is false and the method returns zero. That is valid because zero is non-negative.

**Why failure returns the original money**

If the cheapest pair costs more than `money`, every other pair costs at least as much and is also unaffordable.

No valid purchase exists, so the contract says to buy nothing and return the initial amount. The conditional returns `money` in exactly this case.

This is stronger than merely observing that the selected pair is too expensive: minimum-pair optimality proves all pairs are too expensive.

**Why success should buy the cheapest pair**

If the cheapest pair is affordable, buying it minimizes expenditure.

For fixed starting money:

$$
\text{leftover}=\text{money}-\text{cost}.
$$

Minimizing cost maximizes leftover. Although the statement phrases the goal as minimizing the pair's sum, the returned leftover follows directly.

No more expensive pair can produce a better answer.

**Trace an affordable example**

For `prices = [1, 2, 2]` and `money = 3`, sorting leaves the list in the same order.

The first two prices sum to three. Since three is not greater than the available money, the method returns `3 - 3 = 0`.

The third chocolate has the same price as the second, so choosing it instead would yield the same valid leftover.

**Trace an impossible example**

For `prices = [3, 2, 3]` and `money = 3`, sorting produces `[2, 3, 3]`.

The minimum pair costs five, which exceeds the budget. Every alternative also costs at least five.

The method returns the untouched amount three.

**Why checking arbitrary pairs is unnecessary**

An exhaustive method could inspect all $\binom n2$ pairs and track the cheapest affordable one.

But affordability cannot make a more expensive pair preferable. Once the global cheapest pair is known, either it is affordable and optimal or it is unaffordable and proves none work.

Sorting exposes that pair directly.

**Input mutation**

`list.sort` modifies `prices` in place. The original ordering is not preserved after the method returns.

The problem's answer does not depend on retaining order, so this does not affect correctness. A caller needing the old list would have to pass a copy or use a one-pass minimum method.

**Exact source versus manifest summary**

The manifest summary says the solution tracks two minima in one pass with $O(n)$ time and $O(1)$ space.

The checked-in source sorts the full list. It is correct, but its actual asymptotic time is $O(n\log n)$ and Python sorting may use linear temporary memory.

This explanation follows the executable source.


After sorting, the first two entries form a pair whose cost is no greater than every other pair.

If that cost exceeds money, no pair can be purchased without debt and returning money is required. Otherwise the pair is a valid minimum-cost purchase and subtracting it returns the correct non-negative leftover.

The two cases are exhaustive, proving the result.

## Complexity detail

For $n$ prices, Python sorting costs $O(n\log n)$ time. Reading the first two values and computing the conditional result take $O(1)$ additional time.

Python's sort can use $O(n)$ temporary memory in the worst case, although the list is rearranged in place. The scalar `cost` uses $O(1)$ space. These bounds differ from the manifest's intended one-pass summary.

## Alternatives and edge cases

- **Track two minima in one pass:** Achieves $O(n)$ time and $O(1)$ auxiliary space without mutating input.
- **Check every pair:** Correct but costs $O(n^2)$ time.
- **Min-heap:** Can extract two minima in $O(n)$ heap construction plus logarithmic extraction, but is unnecessary.
- **Exactly two prices:** They are the only possible pair.
- **Budget equals cost:** Return zero; the purchase is allowed.
- **Budget below minimum pair:** Return the original money.
- **Duplicate minimum prices:** They correspond to separate list entries and may both be bought.
- **All prices equal:** Any two form the same optimal pair.
- **Positive-price guarantee:** No negative or zero price changes the minimum-pair reasoning.
- **Input ordering:** Destroyed by `sort`.
- **Exactly two chocolates:** The algorithm never considers buying one or more than two.
