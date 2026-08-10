## General

After all removals, every nonempty bag must contain one common positive number of beans. Call that target $x$. A bag with fewer than $x$ beans cannot reach the target because beans may only be removed, never added. Such a bag must be emptied. A bag with at least $x$ beans can remain nonempty by removing its excess and keeping exactly $x$.

The exact solution sorts the bag sizes, considers every sorted value as the target, and chooses the target that leaves the most beans—or equivalently, removes the fewest.

**Turn minimization into retained-bean maximization**

Let `s = sum(beans)` be the original total. If a plan retains $R$ beans, it removes exactly $s-R$. Because $s$ is fixed, minimizing removed beans is identical to maximizing retained beans.

For a chosen target $x$, every surviving bag contains exactly $x$. If $k$ bags survive, the retained total is $xk$. This means the algorithm only needs to determine which target values are worth considering and how many bags can support each one.

**Sort to make eligible bags a suffix**

After `beans.sort()`, the counts are in nondecreasing order. At index `i`, let `x = beans[i]`. Every bag before `i` has a count no greater than $x$, and every bag from `i` onward has at least $x$ beans.

Using $x$ as the common amount, the algorithm empties all bags before `i` and reduces all `n-i` bags in the suffix to exactly $x$. Those surviving bags retain

$$
x(n-i)
$$

beans in total. The number removed is consequently

$$
s-x(n-i).
$$

The generator expression computes this value for every pair `(i, x)` produced by `enumerate(beans)`, and `min` returns the smallest removal total.

**Why an optimal target is one of the original bag sizes**

At first, it may appear necessary to try every positive integer up to the largest bag. That is not needed.

Consider any feasible target $t$ and the bags that remain nonempty. If every surviving bag originally contained strictly more than $t$, then $t$ can be increased until it reaches the smallest original count among those survivors. The same bags can still support the larger target, and increasing the retained amount in every survivor removes fewer beans. Therefore the smaller $t$ could not have been optimal.

So, in an optimal plan, the target equals the original size of at least one surviving bag—specifically, the smallest survivor. Every such value appears somewhere in the sorted array and is considered by the generator.

**Why the suffix for a candidate is the right set of survivors**

For target `beans[i]`, no bag with a smaller count can survive because it cannot be increased. Every bag with a larger or equal count can be kept at the target. Emptying one of those eligible bags would discard `beans[i]` additional retainable beans and cannot help any other bag, since removals are independent. Therefore all eligible bags should survive.

Sorting places those eligible bags in a suffix. For the first occurrence of a target value $x$, that suffix contains every bag with at least $x$ beans, exactly the maximum possible survivor set.

The code also evaluates later occurrences when duplicates exist. A later duplicate uses the same $x$ with fewer suffix bags and therefore retains no more beans. Those redundant candidates are harmless because `min` will prefer the first occurrence or another genuinely better target.

**Connect the formula to actual removals**

The expression `s - x * (n - i)` includes both kinds of removal in one subtraction:

- all beans from bags that are too small and lie before `i`;
- only the excess above $x$ from each bag in the suffix.

To see this algebraically, the final configuration contains $n-i$ nonempty bags and exactly $x$ beans in each. Its total is $x(n-i)$. Everything not in that final total was removed, regardless of which bag supplied it.

For `[4,1,6,5]`, sorting produces `[1,4,5,6]` and `s = 16`. Choosing target four at index one keeps three bags with four beans each, retaining twelve and removing four. Target one removes twelve, target five keeps ten and removes six, and target six keeps six and removes ten. The minimum is four.

**Why the chosen candidate is globally minimal**

Every candidate formula describes a legal plan: empty the prefix and reduce the suffix to its first value. Thus the returned number is achievable.

Conversely, take any optimal plan. Its target must equal an original bag size, as shown above. Choose the first sorted occurrence of that size. Every smaller bag must be emptied, while keeping every bag at least that large is never worse than emptying an eligible bag. The generator includes exactly this plan's retained total. Therefore no feasible plan removes fewer beans than the minimum candidate, and the returned value is globally optimal.

## Complexity detail

Let $n$ be the number of bags. Python's sort takes $O(n\log n)$ time. Computing the sum is $O(n)$, and the generator evaluates one constant-time arithmetic expression for each element, adding another $O(n)$. Sorting dominates, so total time is $O(n\log n)$.

The exact code sorts `beans` in place, so it mutates the input list. Python's sorting implementation may use $O(n)$ auxiliary memory in the worst case, matching the manifest's $O(n)$ space bound. Apart from sorting's internal storage, the method keeps only `s`, `n`, generator state, and a few integers.

The result can be much larger than an individual bag count because it sums removals across all bags. Python integers safely represent that total without overflow.

## Alternatives and edge cases

- **Prefix sums after sorting:** Explicit prefix sums can calculate removal from the emptied prefix and reduced suffix separately. They are correct but unnecessary because total original beans minus total retained beans gives the candidate in one formula.
- **Frequency counting by value:** Since bag sizes are bounded, a frequency array can aggregate equal counts and scan possible targets. This can avoid comparison sorting but uses space tied to the maximum value and is less direct than the stored solution.
- **Try every positive target:** Values between consecutive bag sizes cannot be better than raising the target to the next eligible bag size, so testing them wastes work.
- **Keep only the largest bag:** This is always legal and corresponds to the last sorted index, providing a fallback candidate.
- **One bag:** Choosing its existing size removes zero beans, and the only generator candidate returns zero.
- **All bags equal:** The first occurrence keeps all beans, so the answer is zero.
- **Highly uneven counts:** Emptying many small bags may be cheaper than reducing a very large bag to a tiny common amount; checking all targets captures this tradeoff.
- **Duplicate target values:** Later equal occurrences keep fewer bags and cannot improve on the first occurrence, but including them does not change the minimum.
- **Positive-input guarantee:** Every considered target is positive, so every suffix bag remains nonempty as required.
- **No bean transfers:** The retained-total formula never moves beans between bags; it only discards the difference between original and final totals.
- **All eligible bags should remain:** Once a bag has at least the target, keeping $x$ beans from it strictly increases retention and has no effect on other bags.
- **Input mutation:** `beans.sort()` permanently reorders the caller's list. The returned count is correct, but callers that need the original order must pass a copy or use `sorted(beans)` in a different implementation.
- **Generator memory:** `min` consumes candidate values lazily, so the formula does not allocate a separate length-$n$ list.
- **Large totals:** With up to $10^5$ bags and $10^5$ beans per bag, the total can reach $10^{10}$; Python handles this exactly.
