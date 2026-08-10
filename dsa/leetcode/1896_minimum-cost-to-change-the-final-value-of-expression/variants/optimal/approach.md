## General

**Store the cost of forcing either Boolean result.** For every parsed subexpression, the algorithm keeps tuple `(cost_to_0, cost_to_1)`. This is more useful than storing only its current value. A parent operator may need either child to become zero or one, and the cheapest way to flip the whole expression can involve changing a child, changing the operator, or both.

A literal zero has state `(0, 1)`: leaving it zero costs nothing, while changing it to one costs one operation. A literal one has state `(1, 0)`. These leaf states already include every legal way to force their two possible values.

**Combine two complete subexpressions exhaustively but constantly.** Helper `combine(left, right, operator)` begins both result costs at a large sentinel. It enumerates desired `left_value` and `right_value` from zero and one, then enumerates chosen operator `"&"` and `"|"`. The operand cost is `left[left_value] + right[right_value]`. Keeping the original operator adds zero; replacing it adds one through `chosen_operator != operator`.

The chosen Boolean operation determines `result`. The candidate cost updates `costs[result]` if it is smaller. There are only $2\cdot2\cdot2=8$ combinations, so this complete local search is constant time. It covers retaining or flipping each operand through its already-optimal state and retaining or flipping the connecting operator.

**Why local cost tuples compose globally.** Once a child subexpression is required to produce a particular Boolean value, only its minimum cost for that value matters to the parent. Its internal edit choices do not affect the other child or the connecting operator because characters occupy disjoint portions of the expression. Therefore child costs add independently, and minimizing over the finite value/operator combinations finds the optimal parent tuple.

**Parse non-parenthesized operations left to right.** The statement gives `&` and `|` equal precedence. Variable `current` stores the value-cost tuple for the expression accumulated at the current parenthesis depth, and `operator` stores the pending connector. On a digit, the source either initializes `current` or calls `combine(current, term, operator)`. Combining immediately makes a sequence such as `1|0&1` evaluate as `(1|0)&1`, exactly the required left-to-right rule rather than ordinary language precedence.

**Use a stack for parentheses.** On `(`, the parser saves tuple `(current, operator)` and resets both variables to begin the inner expression. On `)`, the completed inner `current` becomes `term`, and the saved outer state is popped. If no outer value preceded the parentheses, the parenthesized term becomes the current value directly. Otherwise, it is combined with the saved outer value and operator. Parentheses therefore form one atomic term while their contents still follow left-to-right evaluation.

The optional types reflect legitimate parser moments: an expression can begin with parentheses, leaving the saved outer value absent. The fallback `term or (0, 0)` and empty operator fallback are defensive; valid input guarantees a real inner term and a connector whenever an outer value must be combined.

**Recover the cost to change the actual final value.** For the unedited expression, exactly one component of the final tuple is zero: the cost of producing its current value. If `current[0] == 0`, the original result is zero and the requested answer is `current[1]`. Otherwise, the original result is one and `current[0]` is returned. The method asks for the opposite value, not merely the cheaper of the two costs.

**Trace a simple operator choice.** For `1&(0|1)`, literals zero and one inside parentheses combine under `|`. Their cost tuple records both leaving the result one and the cheapest way to force zero, which can be achieved by changing the operator. That inner tuple then combines with the outer literal one under `&`. The final tuple has zero cost to remain one and cost one to become zero, so the method returns one.

**Why the parser never needs an explicit syntax tree.** Each completed term is summarized immediately by two numbers. A parenthesis stack retains only the unfinished outer aggregate and its connector. This is equivalent to evaluating a syntax tree bottom-up but avoids constructing node objects. Maximum stack depth is the nesting depth.

**Why the result is optimal.** Leaf tuples are exact. Assuming two child tuples are exact, `combine` enumerates every possible child result and both legal states of their operator, so its tuple is exact. Immediate combination respects left associativity, while stack boundaries respect parentheses. Structural induction over the parsed expression therefore makes the final tuple exact, and selecting the nonzero opposite-value component returns the minimum edit count.

## Complexity detail

Let $N$ be the expression length. Every token is processed once. Each literal that joins an existing aggregate invokes one constant-size eight-case `combine`, so total time is $O(N)$.

The stack stores one pair of optional states per unmatched opening parenthesis. In the worst case nesting depth is $O(N)$, giving $O(N)$ auxiliary space. Outside the stack, only constant-size tuples and scalars are retained. This matches the manifest.

Costs cannot exceed the number of editable literal and operator tokens, so the `10**9` sentinel is safely larger for $N\le10^5$. Python Boolean values used in arithmetic behave as zero or one.

## Alternatives and edge cases

- **Build a syntax tree first:** A tree plus postorder DP uses the same state and asymptotic bounds, but allocates explicit nodes that the streaming stack avoids.
- **Track only current value and flip cost:** A specialized recurrence can store these two facts, but the two-target cost tuple is more symmetric and makes operator changes easy to verify.
- **Apply normal operator precedence:** That would be incorrect. `&` and `|` must combine left to right unless parentheses intervene.
- **Single literal:** Its tuple is `(0, 1)` or `(1, 0)`, and changing the final value costs exactly one.
- **Deep parentheses:** The iterative parser avoids Python recursion depth, though its explicit stack grows linearly with nesting.
- **Parenthesized leading term:** The saved outer value is `None`, so closing parentheses installs the inner tuple directly without inventing an operator.
- **Changing an operator only:** `combine` adds one when the chosen operator differs, allowing cases where no literal edit is needed.
- **Changing both operands and operator:** The exhaustive eight combinations include mixed edit strategies and choose them when cheaper globally.
- **Valid-input assumption:** Empty parentheses, unmatched delimiters, or missing operators are outside the contract. Defensive fallbacks do not define meaningful behavior for invalid syntax.
