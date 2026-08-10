## General

**Every expression requires two kinds of choices**

The digits must stay in their original order, but the algorithm must decide both where operands end and which operator separates consecutive operands. For `num = "123"`, possible operand partitions include `1 | 2 | 3`, `1 | 23`, `12 | 3`, and `123`. For a partition with more than one operand, every boundary can receive `+`, `-`, or `*`.

No greedy rule can know which boundary or operator will eventually reach `target`, and the problem asks for all valid expressions. The exact solution therefore uses depth-first backtracking to enumerate every legal combination while evaluating each partial expression incrementally.

At a recursive position `u`, the loop chooses every substring `num[u : i + 1]` as the next operand. Moving `i` farther right is the “do not insert an operator at this digit gap” choice; making the recursive call commits the resulting operand and places one operator before the next operand.

**Understand the four recursive state values**

The helper `dfs(u, prev, curr, path)` carries exactly the information needed to continue:

- `u` is the index of the next unused digit. Digits before `u` have all been placed in `path`.
- `path` is the expression text built from those consumed digits.
- `curr` is the correctly evaluated value of `path`, respecting multiplication precedence.
- `prev` is the signed value of the final additive term currently included in `curr`.

The first three meanings are direct. The role of `prev` is the important part: it lets a later multiplication revise the most recent term without reparsing the whole expression.

For example, after building `1+2`, `curr = 3` and `prev = 2`. After building `5-2`, `curr = 3` and `prev = -2`; the sign is stored with the term because the expression is effectively `5 + (-2)`.

**Choose every legal next operand**

For each endpoint `i` from `u` through the final digit, the source converts `num[u : i + 1]` to integer `next`. This enumerates all operand lengths beginning at `u`.

If `u == 0`, this is the expression's first operand. A binary operator cannot appear before it, so the solution makes only one recursive call with `prev = next`, `curr = next`, and `path` containing the operand. Handling the first operand separately avoids malformed expressions such as `+1+2` and prevents subtraction from being confused with a unary sign.

For every later operand, the source explores three disjoint branches: addition, subtraction, and multiplication. After each call returns, the loop can extend the operand farther or try another operator, which is the backtracking behavior.

**Addition appends a new positive term**

For `path + "+" + next`, ordinary left-to-right accumulation is valid because the newly appended term is added after the entire existing expression. The recursive state becomes

$$
\texttt{curr}'=\texttt{curr}+\texttt{next},
\qquad
\texttt{prev}'=\texttt{next}.
$$

The new final additive term is positive `next`, ready to be extended if a multiplication follows.

**Subtraction appends a signed negative term**

For subtraction, the evaluated total becomes `curr - next`. The source stores `-next` in `prev`:

$$
\texttt{curr}'=\texttt{curr}-\texttt{next},
\qquad
\texttt{prev}'=-\texttt{next}.
$$

Recording the negative sign is essential for a multiplication such as `5-2*3`. Before reading `*3`, the expression value is 3 and its last additive term is `-2`, not merely operand 2.

**Multiplication must replace, not append, the previous term**

Simply computing `curr * next` would be wrong because multiplication has higher precedence than earlier addition or subtraction. For `1+2*3`, multiplying the whole current value would produce 9, while the correct result is 7.

The state treats the expression as

$$
\texttt{curr}
=
\text{earlier additive terms}+\texttt{prev}.
$$

Appending `* next` changes only the final term from `prev` to `prev * next`. The source removes the old term and inserts the product:

$$
\texttt{curr}'
=
\texttt{curr}-\texttt{prev}+\texttt{prev}\cdot\texttt{next},
$$

while the new final term is

$$
\texttt{prev}'=\texttt{prev}\cdot\texttt{next}.
$$

For `1+2*3`, the state before multiplication is `curr = 3`, `prev = 2`. The update gives `3 - 2 + 2*3 = 7`.

For `5-2*3`, the state is `curr = 3`, `prev = -2`. The update gives

$$
3-(-2)+(-2)\cdot3=-1,
$$

which correctly evaluates `5 - 6`. Carrying the sign in `prev` is what makes the same formula work after either addition or subtraction.

Chained multiplication also works. After `2+3*4`, `prev` is 12. Appending `*5` replaces 12 with 60, exactly as operator precedence requires for `2 + (3*4*5)`.

**Reject multi-digit operands with leading zeros**

Operand `0` is legal, but `00`, `05`, and any other multi-digit operand beginning with zero are not. At endpoint `i`, a leading zero exists when `i != u` and `num[u] == '0'`.

The source then uses `break`, not merely `continue`. Once the operand starting at `u` has more than one digit and begins with zero, every still-longer substring has the same invalid leading zero. No later endpoint can become legal. The one-digit substring `"0"` is explored normally before the loop reaches this break.

This rule affects operand boundaries, not the expression's numerical result. Expressions such as `1*0+5` are legal because `0` is a one-digit operand, while `1+05` is never generated.

**Accept only after consuming every digit**

When `u == len(num)`, the expression has used every input digit exactly once in original order. The source compares `curr` with `target`. If they match, it appends `path` to `ans`; otherwise, that complete branch is discarded.

Checking only at this base case is important. A partial expression may already equal the target but still has unused digits, and the contract does not allow dropping them. Conversely, a partial value far from the target can later return through subtraction or multiplication, so ordinary magnitude-based pruning would not be sound.

**Why enumeration is complete and duplicate-free**

Any legal expression determines a unique sequence of operand substrings: its operators mark the exact digit boundaries. At each `u`, the loop tries the endpoint of that expression's next operand. For every boundary after the first operand, the three recursive branches try its exact operator. Therefore, one DFS path reproduces every legal expression.

No two DFS paths produce the same expression. Different operand endpoints give different digit groupings, while different operator branches place different characters in `path`. Because leading-zero groupings are excluded at their source, every generated leaf is syntactically legal. Incremental evaluation is exact by the `prev` replacement rule, so the base-case comparison selects exactly the required expressions.

**Trace `num = "232", target = 8`**

One successful path chooses operands `2`, `3`, and `2` with operators `*` then `+`:

| Path | `prev` | `curr` |
|---|---:|---:|
| `2` | 2 | 2 |
| `2*3` | 6 | 6 |
| `2*3+2` | 2 | 8 |

Another successful path chooses `+` then `*`:

| Path | `prev` | `curr` |
|---|---:|---:|
| `2` | 2 | 2 |
| `2+3` | 3 | 5 |
| `2+3*2` | 6 | `5 - 3 + 6 = 8` |

The multiplication update revises only the last term 3, producing the correct precedence without parsing `path`. Both expressions are appended. For `"3456237490"` and target 9191, the search still explores every legal expression, but no completed state matches, so `ans` remains empty.

## Complexity detail

Let $n$ be the number of digits. Each of the $n-1$ gaps has four conceptual choices: join the neighboring digits into one operand, or place `+`, `-`, or `*`. This gives at most $4^{n-1}$ complete expression structures before leading-zero pruning, conventionally written as $O(4^n)$.

The manifest records $O(4^n)$ time, which captures the exponential search tree. The exact Python source also slices operand substrings, converts them, and creates new immutable path strings. Those operations can copy up to $O(n)$ characters at a recursive edge. A conservative exact-source bound is therefore $O(n4^n)$ time, and returning many expressions already requires output-character work proportional to their total lengths.

The recursion depth is at most $n$, because every call consumes at least one digit. Under the conventional mutable-path analysis, the active recursion and expression buffer use $O(n)$ auxiliary space, matching the manifest.

The protected source passes immutable strings as `path`. Parent frames retain shorter path strings while a child owns a longer one, so the total lengths simultaneously retained along one deepest chain can sum to $O(n^2)$. A conservative exact-source auxiliary bound is therefore $O(n^2)$, excluding `ans`. The numeric state and loop variables use only constant space per frame.

If $R$ expressions are returned, each can contain up to $2n-1$ characters, so required output storage is $O(Rn)$. Output is normally excluded from auxiliary-space claims because the problem explicitly requires those strings.

## Alternatives and edge cases

- **Build every expression, then evaluate it:** This separates generation from evaluation but reparses every leaf and may rely on forbidden or unsafe `eval`-style functionality. Carrying `curr` and `prev` evaluates each branch incrementally.
- **Mutable expression buffer:** Append operand and operator fragments, recurse, then pop them. This avoids retaining a chain of immutable prefix strings and brings active path storage closer to the manifest's $O(n)$ auxiliary bound.
- **Dynamic programming by index and total:** The same index and current total can have different final multiplicative terms, so memoizing only those two values is incorrect. Including all required arithmetic state still does not naturally preserve every distinct expression string that must be returned.
- **No multiplication:** With only `+` and `-`, `curr` alone would suffice because both operators have equal precedence. `prev` exists specifically to revise the final term for `*`.
- **First operand:** It receives no leading operator. Treating it through the ordinary subtraction branch would generate unary-minus expressions that the insertion contract does not request.
- **Single digit:** The only complete expression is the digit itself. It is returned exactly when its value equals `target`.
- **Operand zero:** A single `0` is valid and participates normally in all three operator branches.
- **Leading-zero run:** When the next digit is zero, only that one digit may form the operand. Longer endpoints are pruned with `break`.
- **Negative intermediate totals:** They are valid. Subtraction can make `curr` negative, and later operations can still reach the target, so they must not be pruned.
- **Large intermediate products:** The target is 32-bit, but intermediate expression values are not promised to stay in that range. Python integers handle them without overflow; fixed-width implementations should use a sufficiently wide integer type.
- **Operator precedence:** The source supports the standard precedence of multiplication over addition and subtraction, with no parentheses. The signed-last-term update is valid precisely for this operator set.
- **All digits must be used:** Reaching the target before `u` reaches the end is not a solution; every digit must appear exactly once and in order.
- **Answer order:** DFS traversal determines the returned ordering. The contract asks for all possibilities and does not require a particular order.
- **No valid expression:** Exhaustive search leaves the result list empty, as in the third example.
