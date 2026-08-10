## General

**The objective favors the cheapest allowed integers**

Every eligible integer contributes the same benefit: it increases the chosen count by exactly one. Their costs are different because choosing integer $i$ adds $i$ to the sum. When equal-benefit items compete for a limited budget, taking cheaper items first leaves at least as much budget for further choices as taking expensive ones.

The solution therefore considers integers in ascending order from $1$ through $n$. A hash set `ban` stores all forbidden values. If the current integer is allowed and fits within `maxSum`, the algorithm adds it to the running sum `s` and increments `ans`. This constructs the cheapest possible set of one item, then the cheapest possible set of two allowed items, and so on.

The set is important for efficiency. Testing `i not in ban` is expected $O(1)$ time, whereas scanning the original `banned` list for every candidate could require $O(m)$ work per integer. Converting the list to a set also removes any effect from duplicate banned entries: a number is either forbidden or allowed, regardless of how many times it appears in the input.

**Why ascending greedy order is optimal**

Suppose some valid selection contains a larger allowed integer $b$ but omits a smaller allowed integer $a$, where $a<b$. Replacing $b$ with $a$ keeps the number of selected integers unchanged, respects the banned restriction because $a$ is allowed, and can only decrease the total sum. This exchange never makes a valid selection invalid.

By repeatedly making such exchanges, any valid selection of $q$ integers can be transformed into the $q$ smallest allowed integers without increasing its sum. Therefore, among all selections of size $q$, the first $q$ allowed values in ascending order have the minimum possible sum.

This yields the crucial conclusion: if the greedy prefix of $q$ allowed values exceeds `maxSum`, then every selection of $q$ allowed values exceeds the budget. Conversely, whenever that prefix fits, it is itself a valid selection of size $q$. The largest prefix that fits must therefore have the maximum achievable count.

For example, let the allowed values begin `[2, 4, 7, 8]` and let the budget be $10$. Greedy takes $2$ and $4$, reaching sum $6$. It cannot add $7$. No different set of three allowed values can work, because the three cheapest already cost $2+4+7=13$. Choosing $2$ and $8$ would also use the budget, but it still selects only two values and leaves no advantage.

**Why it is safe to stop**

At the top of each iteration, the code checks `s + i > maxSum` before it checks whether $i$ is banned. At first this may look surprising: if $i$ is forbidden, the algorithm would not add it anyway. The early `break` is still correct because all later candidates are greater than $i$. If the remaining budget is smaller than $i$, it is also smaller than every later allowed integer. Skipping a banned $i$ cannot reveal a cheaper number later, so no future choice can fit.

If `s + i <= maxSum` and $i$ is banned, the algorithm simply continues without changing either `s` or `ans`. If $i$ is allowed, it is the cheapest allowed integer not yet considered, so taking it follows the proven greedy rule.

This distinction also explains why the code checks affordability before membership without corrupting the answer. When $i$ fits, it can be skipped if banned or taken if allowed. When $i$ does not fit, every later integer fails too, whether $i$ itself is banned or allowed.

**Following the exact variables**

Initially, `ans = s = 0` represents an empty selection. After processing every value smaller than the current $i$, `ans` equals the number of allowed values selected so far, and `s` is their exact sum. Moreover, those selected values are all allowed values in that processed prefix, because taking each one was affordable.

If the loop finishes normally, every allowed number from $1$ to $n$ has been chosen and the count is plainly maximal. If it breaks, the next and every later allowed value is too costly for the remaining budget. The exchange argument shows that replacing any already selected smaller number with a later larger one cannot create room for an additional item. Thus the current count is maximal in either termination mode.

With `banned = [1,6,5]`, $n=5$, and `maxSum = 6`, the scan skips $1$, takes $2$, then takes $3$, reaching sum $5$. The next value $4$ cannot fit, so this exact implementation returns two choices, represented by the valid set $\{2,3\}$. The statement's example uses $\{2,4\}$; both have count two, and only the maximum count matters.

## Complexity detail

Let $m$ be the length of `banned`. Constructing `ban = set(banned)` takes expected $O(m)$ time and stores at most $m$ distinct values. The loop performs at most $n$ iterations, with an expected $O(1)$ hash lookup in each iteration. Total expected time is therefore $O(m+n)$, matching the manifest. Hash-table operations can theoretically degrade under pathological collisions, but Python's normal set model uses expected constant time.

The set uses $O(m)$ auxiliary space in the worst case. The counters, running sum, and loop variable use $O(1)$ space. No collection proportional to $n$ is created, and the input list is not modified.

## Alternatives and edge cases

- **Sort and sweep the banned list:** Sorting `banned` and advancing a pointer while scanning $1$ through $n$ avoids hashing, but costs $O(m\log m+n)$ time and needs careful handling of duplicate forbidden values.
- **Binary search for every candidate:** A sorted banned list supports $O(\log m)$ membership checks, giving $O(m\log m+n\log m)$ total time, slower than expected hash-set lookup.
- **Try arbitrary subsets:** Backtracking examines exponentially many selections and ignores the equal-benefit structure that makes the greedy exchange possible.
- **All values banned:** Every candidate is skipped, so `ans` remains zero.
- **Banned values above `n`:** They occupy space in the set but are never queried and have no effect on the result.
- **Duplicate banned entries:** Set construction collapses them automatically, preserving the intended yes-or-no meaning of being banned.
- **Very small budget:** If even $1$ is unaffordable, the first iteration breaks and returns zero. Since all candidates are positive and no later value is cheaper, this is final.
- **Budget exactly exhausted:** The test uses `>` rather than `>=`, so an integer that makes the sum exactly `maxSum` is valid and is selected.
- **Every allowed value fits:** The loop reaches $n$ and returns the total number of non-banned values in the range.
- **Why positivity matters:** The stopping and greedy arguments depend on all candidate costs being positive and increasing. Negative or reusable values would define a different problem and invalidate this proof.
