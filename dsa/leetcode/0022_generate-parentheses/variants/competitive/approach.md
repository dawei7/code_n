## General

**Simulate recursive backtracking with explicit events**

The competitive source generates only well-formed prefixes, just as a recursive backtracker would, but replaces the language call stack with its own `stk`. The mutable list `curr` holds the characters on the current search path. Instead of calling a function, the algorithm pushes small instructions that say what to do next.

This organization is unusual, so understanding the three instruction types is more important than memorizing the code:

- step `1` processes a backtracking state;
- step `2` appends one character to `curr`; and
- step `3` removes the most recently appended character when a branch finishes.

Because `stk.pop()` is last-in, first-out, instructions are pushed in reverse of the order in which they must execute.

**Track remaining counts rather than used counts**

A state `(left, right)` records how many `(` and `)` characters remain available. The initial event

```python
stk = [(1, (n, n))]
```

therefore represents an empty path with all $2n$ characters still to place. Appending `(` changes the next state to `(left - 1, right)`, while appending `)` changes it to `(left, right - 1)`.

At any point, the number of already used openers is $n-left$, and the number of used closers is $n-right$. A valid prefix requires

$$
n-\texttt{left}\ge n-\texttt{right},
$$

which simplifies to `left <= right`. That is why a closer is allowed only when `left < right`: a strict inequality means at least one previously used opener is still unmatched.

**Process a state event**

When `step == 1`, the source first checks whether both remaining counts are zero. If so, `curr` is a complete valid path, and

```python
result.append("".join(curr))
```

copies it into an immutable result string. No child events are scheduled because neither branch condition can hold.

If `left < right`, a closing parenthesis is legal. If `left > 0`, an opening parenthesis is legal. These tests prevent invalid calls before they enter the stack, unlike the Optimal source, which makes both calls and prunes bad children at function entry.

**Decode the three-event branch pattern**

For an opening branch, the source pushes

```python
stk.append((3, tuple()))
stk.append((1, (left-1, right)))
stk.append((2, ('(')))
```

LIFO order makes these execute as follows:

1. step `2` appends `(` to `curr`;
2. step `1` explores the child state with one fewer opener; and
3. step `3` pops `(` after the entire child subtree finishes.

This is exactly the recursive append–recurse–pop backtracking pattern. The closing branch schedules the same pattern with `)` and `right - 1`.

The expressions `('(')` and `(')')` are strings rather than one-element tuples because Python requires a trailing comma for a single-element tuple. That does not break the code: step `2` reads `args[0]`, which is the one-character string in either case. The empty `tuple()` carried by step `3` is likewise only a placeholder; step `3` ignores `args`.

**Why openings are explored before closings**

The source schedules the closing branch first and the opening branch second. Since a stack executes the most recently pushed work first, the opening branch runs first. All three opening events sit above the earlier closing events. Only after the opening subtree's final pop does execution return to the deferred closing branch.

This produces the familiar order beginning with the most nested answer, such as `"((()))"` for `n = 3`. The result order is permitted but not required by the problem.

**Maintain the path invariant**

Whenever a step-`1` state is processed, `curr` is exactly the prefix whose remaining counts are carried by that state, and it is well formed so far. Step `2` extends the path with a branch proven legal by its parent. Step `3` restores `curr` to the precise parent prefix. Because every append has a corresponding later pop, characters from one sibling branch cannot leak into another.

The conditions preserve validity. `left > 0` prevents using more than $n$ openers. `left < right` allows a closer only when a previously used opener remains unmatched. Counts never become negative. When both reach zero, the path has exactly $n$ of each character and every prefix was valid.

**Why generation is complete and duplicate-free**

Every well-formed result has a unique left-to-right sequence of opening and closing choices. At any opener in that result, some opener remains, so the source schedules the opening branch. At any closer, the valid prefix has an unmatched opener, so `left < right` and the source schedules the closing branch. Therefore its unique path reaches `(0, 0)`.

Conversely, every path that reaches `(0, 0)` obeyed the legality conditions at every step, so its joined string is well formed. Distinct paths differ at some character position and create distinct strings. The output therefore contains every valid string exactly once.

## Complexity detail

Let $C_n=\frac{1}{n+1}\binom{2n}{n}$ be the number of returned strings.

- **Time complexity: $O(nC_n)$.** The event machine explores the valid-prefix search tree with constant work per event. At each of the $C_n$ leaves, `"".join(curr)` copies $2n$ characters. Output construction alone is $\Theta(nC_n)$ and dominates the customary bound. The source comment's Catalan-only $O(C_n)$ expression omits the cost of materializing length-$2n$ strings; the manifest's $O(n\cdot C_n)$ is the more complete claim.
- **Auxiliary space: $O(n)$, excluding results.** `curr` contains at most $2n$ characters. The explicit event stack stores only a linear number of active/deferred instructions along the depth-first frontier; completed branch events are popped before the next sibling finishes. Each event holds constant-size state, so peak non-output storage is linear. `result` requires $O(nC_n)$ characters.

Avoiding language recursion does not make the search constant-space: the explicit event stack represents the same pending work. Its benefit is direct control and freedom from Python's recursion-depth mechanism.

## Alternatives and edge cases

- **Ordinary recursive mutable-buffer backtracking:** It expresses append–recurse–pop more readably and has the same $O(nC_n)$ time and $O(n)$ auxiliary space.
- **Immutable-prefix recursion:** It needs no explicit undo, but repeated string concatenation adds copying overhead and can retain multiple prefix strings along the call chain.
- **Brute-force generation:** Creating every length-$2n$ parenthesis string explores $4^n$ leaves, including permanently invalid prefixes.
- **Dynamic Catalan construction:** Combine valid left and right substructures according to the Catalan recurrence; memoization is needed to avoid repeated work.
- **`n = 1`:** Opening is the only legal first branch, closing then becomes legal, and the result is `['()']`.
- **Never begin with `)`:** Initially `left == right`, so `left < right` is false and no closing branch is scheduled.
- **Never use too many `(`:** Once `left == 0`, the opening condition fails.
- **Finish forced closers:** When `left == 0 < right`, only closing branches remain until completion.
- **Step ordering:** Changing push order changes output order; omitting either cleanup step corrupts `curr` for sibling branches.
- **Single-character argument syntax:** `('(')` is a string, but `args[0]` deliberately retrieves its only character; no tuple unpacking is required.
- **Maximum `n = 8`:** There are $C_8=1430$ outputs, so output-sensitive cost is unavoidable.
- **Out-of-contract `n = 0`:** The initial state is already `(0, 0)`, so the exact implementation returns `['']`, the conventional empty combination.
