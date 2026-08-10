## General

**Every score ultimately comes from a primitive `()`**

The rule `AB -> score(A)+score(B)` means concatenated components contribute independently.

The rule `(A) -> 2*score(A)` means every surrounding pair of parentheses doubles the score inside.

At the bottom of every balanced structure are adjacent primitive pairs `()`, each with base score one. A primitive pair surrounded by `d` outer pairs contributes `2^d` to the total.

The solution scans once, tracks nesting depth, and adds this contribution whenever it recognizes an adjacent `()`.

**Depth meaning**

Variable `d` is the number of opening parentheses currently active after processing the current scan position's structural update:

- on `(`, increment `d`;
- on `)`, decrement `d` because that pair is closing.

For a closing parenthesis, the decremented value is the number of outer pairs surrounding the pair that just closed.

**Recognize only primitive pairs**

When current character is `)` and previous character `s[i-1]` is `(`, the two form an adjacent primitive `()`.

The code adds:

`1 << d`,

which equals `2^d`.

If the previous character is also `)`, the closing parenthesis ends a larger composite expression, not a new base primitive. Its score has already been accounted for through the primitives inside, so nothing is added.

**Why adding primitive contributions reproduces the recursive rules**

For plain `()`, closing reduces depth to zero and adds `2^0=1`.

For `(())`, the inner adjacent pair closes while one outer pair remains, so it contributes `2^1=2`. The outer closing is not adjacent to `(` and adds nothing. This matches doubling the inner score.

For `()()`, each primitive closes at depth zero and contributes one, totaling two. This matches concatenation's addition rule.

For deeper nesting, every surrounding layer increases `d` by one and therefore doubles that primitive's contribution, exactly matching repeated applications of `(A)`.

**Trace `"(()(()))"`**

The first primitive inner `()` occurs with one outer layer after closing, contributing 2.

The later inner `()` occurs with two outer layers after closing, contributing 4. Its surrounding component and the full outer close add no separate primitive.

Total score is 6, which agrees with recursive evaluation:

$$
(()(())) = 2\left(1+2\cdot1\right)=6.
$$

**Why `s[i-1]` is safe**

A balanced parentheses string cannot begin with `)`. Therefore, every time the code enters the closing branch, `i >= 1`, so the previous-character access is valid.

**Why constant space is possible**

We do not need to remember the score at every open parenthesis. Nesting affects a primitive only through its depth, and concatenated primitives can be added immediately to `ans`.

The scan converts the recursive grammar into weighted leaf counting.


Every primitive `()` corresponds to one leaf of the balanced-parentheses expression. If it has `d` surrounding pairs, recursive rules multiply its base score by two exactly `d` times, giving `2^d`.

Concatenation adds the scores of all leaves. The algorithm detects every primitive once, computes its outer depth at closing, and sums the exact leaf contribution. Therefore, `ans` equals the grammar-defined score.

**A scan invariant**

After processing any prefix of the balanced string, `d` equals the number of opening parentheses in that prefix whose matching closing parentheses have not yet been processed. Meanwhile, `ans` contains the final weighted contributions of every primitive pair whose closing parenthesis is already in the prefix. Future characters may close outer wrappers around a previously seen primitive, but that wrapper was already open when the primitive closed, so it was already included in that primitive's depth and weight. The contribution never needs later revision.

This explains why the algorithm can add immediately rather than postponing scores until an outer component closes. An opening parenthesis affects future primitives by increasing `d`. A nonprimitive closing parenthesis only removes one active wrapper; it creates no new leaf and therefore changes no accumulated score.

**Connection to the recursive definition**

Any balanced string has a parse tree whose internal nodes are concatenations or wrappers and whose leaves are primitive pairs. Concatenation nodes sum their descendant leaves, while each wrapper doubles every leaf below it. Distributing those multiplications down the tree gives one power of two per wrapper surrounding each leaf. The scan computes precisely this distributed form, so it is not a shortcut based only on examples; it is an algebraically equivalent evaluation of the full recursive definition.

## Complexity detail

Let `n = len(s)`. The loop examines each character once and performs constant work, so time is `O(n)`.

Only accumulator `ans`, depth `d`, and loop variables are stored. Auxiliary space is `O(1)`.

Bit shifting computes powers of two exactly as integers without floating-point exponentiation.

## Alternatives and edge cases

- **Stack of partial scores:** Push a frame for each opening parenthesis and combine on closing. It mirrors the grammar but uses `O(n)` worst-case space.

- **Divide and conquer:** Find top-level balanced components recursively. It is conceptually direct but can rescan ranges or use recursion.

- **One primitive `()`:** Depth after closing is zero, so score is one.

- **Pure nesting:** Only the deepest adjacent pair contributes, weighted by all outer levels.

- **Pure concatenation:** Every primitive occurs at depth zero, so the score is the number of pairs.

- **Mixed nesting and concatenation:** Each primitive independently receives its own depth weight.

- **Closing a composite:** Previous character is `)`, so no new base contribution is added.

- **Balanced guarantee:** Depth never becomes negative and ends at zero.

- **Maximum length 50:** Scores fit comfortably in Python integers; bit shifting remains exact.

- **Input immutability:** The string is read only.
