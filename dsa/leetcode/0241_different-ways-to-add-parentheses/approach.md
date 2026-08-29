## General

A fully parenthesized expression has one operator evaluated last. That final operator separates the expression into a completely parenthesized left expression and a completely parenthesized right expression. This gives the recursive structure needed for the whole problem: try every operator as the final, outermost operation; recursively obtain every result from each side; then combine every left result with every right result through that operator.

This is different from evaluating with normal arithmetic precedence. The input is only a sequence of unsigned numbers separated by `+`, `-`, and `*`, and the task asks for every result obtainable by grouping it. Each possible full grouping must contribute one output entry, even when two different groupings happen to produce the same integer.

**A substring is a complete subproblem**

The helper `dfs(exp)` means: return a list containing the result of every valid full parenthesization of the substring `exp`. Its answer depends only on those characters, making `exp` a sufficient memoization key.

If `exp.isdigit()` is true, the substring is one complete number with no operator. There is exactly one way to evaluate it, so the helper returns `[int(exp)]`. Using `isdigit()` instead of checking the substring length correctly supports both one-digit and two-digit numbers such as `7` and `42`.

Otherwise, the helper scans every character. Whenever it sees an operator at index `i`, that operator is considered as the last operation:

- `exp[:i]` is the left subexpression;
- `exp[i + 1:]` is the right subexpression;
- `dfs` returns all possible values for each side;
- the nested loops combine every left value `a` with every right value `b` using the selected operator.

For subtraction, order is particularly important: the combination is `a - b`, never `b - a`. Addition and multiplication are commutative for individual integers, but the algorithm still preserves the expression's left and right structure consistently.

**Why every pair must be combined**

Suppose one chosen split gives three possible left results and two possible right results. Any of the three left parenthesizations can coexist with either of the two right parenthesizations, producing six complete parenthesizations whose root is that operator. The Cartesian product of the two result lists represents these independent choices. Taking only corresponding positions or only distinct values would lose valid groupings.

The answer is deliberately a list rather than a set. If two structurally different parenthesizations evaluate to the same number, that number must occur twice. In `2*3-4*5`, two different groupings produce `-10`, so both nested-loop combinations append `-10`. Deduplicating would violate the required output multiplicity.

**Trace for `2-1-1`**

There are two operators, so the top-level helper considers two possible final operations.

1. Choose the first `-` as the final operator. The left substring `2` evaluates to `[2]`. The right substring `1-1` has one split and evaluates to `[0]`. Combining them gives `2 - 0 = 2`, corresponding to `2-(1-1)`.
2. Choose the second `-` as the final operator. The left substring `2-1` evaluates to `[1]`. The right substring `1` evaluates to `[1]`. Combining them gives `1 - 1 = 0`, corresponding to `(2-1)-1`.

The helper returns `[2, 0]`. The problem permits any result order, so this is equivalent to the example's `[0, 2]`.

**Why selecting the final operator enumerates all groupings**

Every full parenthesization of an expression with at least one operator has a unique root in its expression tree: the operator evaluated last. Removing that root divides the tree into a left subtree that uses exactly the text before the operator and a right subtree that uses exactly the text after it. By recursively enumerating each side and taking their Cartesian product, the algorithm produces that full parenthesization.

Conversely, every value the algorithm appends comes from choosing a real operator, choosing a valid full grouping of its left substring, and choosing a valid full grouping of its right substring. Joining those two groupings under the operator creates a valid full grouping of the current substring. Thus the recursion produces no invalid structures. Because each full grouping has one unique root split and unique left and right grouping choices, it is enumerated once as a structure. Equal numerical values can still appear more than once because different structures may evaluate equally, exactly as required.

**Why memoization matters**

Different root choices repeatedly request the same subexpression. Without caching, a substring such as `3-4` might have its entire recursion reconstructed from several branches. Decorating `dfs` with `@cache` stores the returned list under the substring text. Later calls with the same `exp` return that already-computed list.

The cache uses substring content, not start/end indices. If identical text occurs in multiple locations, such as the two appearances of `2-2`, they legitimately have identical possible results because there are no variables or position-dependent operators. Reusing one cached answer is safe and can save more work than caching the locations separately.

The cached value is a mutable list, but the implementation only iterates over lists returned by recursive calls; it never changes them. Each helper builds its own `ans` list and returns it. Avoiding mutation is important because modifying a cached list would corrupt every later caller sharing that cached result.

**Multi-digit numbers are not split internally**

The loop examines every character but recurses only when `c in '-+*'`. Digits are never split points. Therefore, `10+5` produces the numeric leaf `10`, not separate leaves `1` and `0`. The input grammar excludes unary signs, so every `-` encountered is safely treated as a binary subtraction operator rather than part of a negative literal.

## Complexity detail

Let $p$ be the number of binary operators. There are

$$
C_p=\frac{1}{p+1}\binom{2p}{p}
$$

full binary parenthesization structures, where $C_p$ is the $p$th Catalan number. The final output preserves one result per structure, so merely constructing the answer requires $\Omega(C_p)$ time and space in the worst case. This unavoidable output growth is why no polynomial-time algorithm can explicitly return the complete list for arbitrary $p$.

Memoization ensures that each distinct substring text is expanded only once, but each cached subproblem must still materialize all of its results and combine Cartesian products. Scanning split positions and creating Python slices adds factors bounded by the expression length. A standard output-sensitive upper bound is $O(pC_p)$ time and $O(pC_p)$ stored result space, matching the manifest's `O(C_n · n)` notation when its $n$ denotes the number of operators up to a constant relationship with expression length.

The recursion depth is at most $O(p)$ when splits repeatedly peel off one number. That stack is smaller than the exponential cached result storage once $p$ grows. The cache can contain $O(p^2)$ position intervals in a generic expression, or fewer distinct text keys when repeated substrings coincide; each entry holds a result list whose size depends on the operators within that subexpression.

The input length is at most `20` and the number of returned results is capped at $10^4$, making the necessarily exponential output manageable under the stated test limits.

## Alternatives and edge cases

- **Plain recursion without memoization:** The same split-and-combine reasoning is correct, but identical subexpressions are expanded repeatedly. Memoization removes that avoidable recomputation while preserving the unavoidable cost of producing every result.
- **Interval memoization:** Tokenize the expression and cache by a pair of number indices rather than by substring text. This avoids creating string slices and keeps occurrences distinct. It has the same core recurrence; content-key caching may additionally reuse identical textual subexpressions.
- **Bottom-up interval dynamic programming:** Begin with individual numbers and build result lists for intervals of increasing length. It avoids recursive stack usage but requires more indexing machinery and still performs every necessary Cartesian-product combination.
- **A set instead of a list:** A set would incorrectly erase multiplicity. Different parenthesizations that evaluate to the same integer must produce repeated entries.
- **One number and no operator:** `isdigit()` returns true, so the only result is that complete integer. This also covers the value `0` and two-digit values through `99`.
- **Subtraction:** Parentheses can dramatically change subtraction because it is not associative. Preserving ordered left and right operands is essential.
- **Addition or multiplication only:** Different groupings may all yield the same value because these operations are associative, but every grouping still contributes an entry; the output can therefore contain many duplicates.
- **Repeated substring text:** Reusing one cached list is valid because evaluation is determined entirely by the substring. Callers must treat that cached list as read-only, as this implementation does.
- **Unary signs:** Inputs do not contain leading `+` or `-` on numeric literals. If unary operators were allowed, blindly splitting at every sign would create empty or malformed subexpressions and a parser would be needed.
- **Ordinary precedence:** The solution intentionally does not privilege multiplication over addition or subtraction. Every operator is eligible to be the root because parentheses may override the usual evaluation order.
- **Result order:** Operator positions are visited left to right and nested lists in their generated order, but callers must not rely on that ordering because the contract allows any order.
