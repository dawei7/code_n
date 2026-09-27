# Guided Example: Curry

## 1. The instance and the value to derive

A curried form of a function accepts parameters in several instalments. Each call may carry any number of arguments up to the function's declared parameter count, and while the total number of arguments gathered so far falls short of that count, the call returns another curried function. The moment the total reaches the count, the underlying function runs with every argument gathered so far, concatenated in arrival order.

The instance traced here has declared parameter count $a = 4$ and an underlying function that assembles its four arguments into the four-digit number $F(w, x, y, z) = 1000w + 100x + 10y + z$. Four calls arrive with the batches

| Call | Batch received | Size of the batch |
|---|---|---|
| 1 | `1, 2` | 2 |
| 2 | no arguments at all | 0 |
| 3 | `3` | 1 |
| 4 | `4` | 1 |

and the required value is the single number `1234`. This instance is chosen because it separates the two quantities that a careless curried function conflates: the number of calls is four, but the number of accumulated arguments only reaches four on the fourth call, and the empty second call changes nothing at all. It also fixes the concatenation order, since reassembling the batches newest-first would produce `4321`.

The statement bounds the instance by $1 \le \text{inputs.length} \le 1000$, $0 \le \text{inputs}[i][j] \le 10^{5}$, $0 \le \text{fn.length} \le 1000$, and the guarantee $\text{inputs.flat}().length = \text{fn.length}$, so the flattened arguments supply exactly enough values to satisfy the declared count. Two further guarantees matter for the traps: when $a > 0$ the last batch is never empty, and when $a = 0$ there is exactly one call.

## 2. The trigger rule: count accumulated arguments, not calls

Write the batches as $B_1, B_2, \dots, B_m$ with sizes $b_k = \lvert B_k \rvert$, and let $c_k = b_1 + b_2 + \cdots + b_k$ be the accumulated argument count after call $k$.

| Quantity | Meaning | What it decides |
|---|---|---|
| $a$, the declared parameter count | how many parameters the underlying function declares, known before it is ever invoked | the threshold that ends currying |
| $c_k$, the accumulated count | how many argument values have been gathered through call $k$ | whether the threshold has been reached |
| the pending argument sequence | $B_1$ followed by $B_2$ and so on, in arrival order | the exact argument list the underlying function will receive |
| the returned value of call $k$ | another curried function while $c_k < a$, otherwise the computed result | the shape the caller observes at each step |

The rule is therefore: return a further curried function while $c_k < a$, and evaluate at the first call whose accumulated count satisfies $c_k \ge a$. Every one of the four calling styles in the statement collapses onto this single rule, which the following equivalence table makes explicit for a three-parameter sum.

| Calling style | Batch sizes | Accumulated counts | Evaluates on call |
|---|---|---|---|
| one argument per call | 1, 1, 1 | 1, 2, 3 | third |
| two then one | 2, 1 | 2, 3 | second |
| one then two | 1, 2 | 1, 3 | second |
| all at once | 3 | 3 | first |
| two empty calls then all three | 0, 0, 3 | 0, 0, 3 | third |

## 3. Step-by-step trace of the instance

| Call | Batch | Accumulated count before | Accumulated count after | Is the count at least $a = 4$? | Returned to the caller | Pending argument sequence |
|---|---|---|---|---|---|---|
| 1 | `1, 2` | 0 | 2 | no | another curried function | `1, 2` |
| 2 | none | 2 | 2 | no | another curried function | `1, 2` |
| 3 | `3` | 2 | 3 | no | another curried function | `1, 2, 3` |
| 4 | `4` | 3 | 4 | yes | the result of evaluating the underlying function | `1, 2, 3, 4` |

The fourth call is the only one that computes anything; the value it produces is $F(1, 2, 3, 4) = 1000 + 200 + 30 + 4 = 1234$, exactly the required number. The second call is the informative one: it added a call without adding an argument, so the count stayed at two and currying continued.

```text
call 1   batch (1,2)   count 0 -> 2   pending: 1 2
call 2   batch ()      count 2 -> 2   pending: 1 2          (empty batch advances nothing)
call 3   batch (3)     count 2 -> 3   pending: 1 2 3
call 4   batch (4)     count 3 -> 4   count reached 4  ->  evaluate F(1,2,3,4) = 1234
```

An implementation that keeps one record per call rather than one growing list, linking each record backwards to its predecessor, has to reverse that chain when the threshold is finally reached, because the newest record is the one nearest the hand:

| Record | Batch it holds | Points backwards to | Position in the assembled argument list |
|---|---|---|---|
| 1 | `1, 2` | nothing | first and second |
| 2 | none | record 1 | contributes nothing |
| 3 | `3` | record 2 | third |
| 4 | `4` | record 3 | fourth |

Walking the chain from record 4 back to record 1 visits the batches in the reverse of arrival order, so they must be replayed from the oldest record forward; otherwise the underlying function would receive `4, 3, 1, 2` and return `4312`.

## 4. The accumulation invariant and why the single trigger is correct

**Invariant.** After call $k$ has returned another curried function, that function is equivalent to one that already holds the argument sequence $B_1 B_2 \cdots B_k$ and has recorded the count $c_k$; when it is later called with further batches, it will evaluate the underlying function with $B_1 B_2 \cdots B_k$ followed by those later arguments, as soon as the running count reaches $a$.

**Maintenance.** A call carrying batch $B_{k+1}$ appends its values after the retained sequence and adds $b_{k+1}$ to the retained count. Appending keeps arrival order, because the retained sequence is exactly the earlier arrival order by the invariant and the new values arrived after all of them. Adding the batch size keeps the count equal to the length of the retained sequence, which is the fact the trigger tests. Nothing else in the accumulator changes, so no earlier argument is lost or reordered.

**Correctness of the trigger.** Two directions have to hold for every call. If $c_k < a$, the underlying function must not run, because it declares $a$ parameters and fewer than $a$ arguments have arrived; returning a further curried function is the only permitted behaviour, and the invariant guarantees the retained prefix is right. If $c_k \ge a$, the function must run with the gathered arguments, and it must do so exactly once: the evaluation returns a value rather than a function, so there is no curried function left to call again with the same prefix. Induction over the calls shows the first time the threshold is reached, the gathered sequence is $B_1$ followed by every later batch in order, which is precisely the argument list the uncurried call would have received.

**Why the pending state must be immutable.** Every intermediate curried function is a value the caller may keep and reuse. If all of them shared one mutable argument buffer, then evaluating the prefix `1, 2` and later approaching the same prefix again would find the buffer already polluted by the arguments of the first evaluation, and the second evaluation would compute a different value. Branch independence is therefore part of correctness: each call builds a new record referring to its predecessor instead of editing shared state.

**Zero declared parameters.** With $a = 0$ the count reaches the threshold before any argument arrives, so the very first call evaluates immediately, even with no arguments. That is consistent with the rule rather than an exception to it, and the guarantee that $a = 0$ comes with exactly one call is what makes the resulting invocation well defined.

## 5. Boundary and trap analysis

| Situation | Concrete plan | Required value | The trap it exposes |
|---|---|---|---|
| Zero declared parameters | count 0, one call with no arguments, underlying work producing 42 | 42 | the threshold is satisfied at the first call; evaluating eagerly when the curried form is created would run the work before any call and hand back a value where a function is required |
| All parameters in one call | count 4, one batch `2, 3, 4, 5` multiplying to the required product | 120 | the rule must allow a batch that already satisfies the threshold; no minimum number of calls exists |
| Empty batches | count 2, batches `()`, `10`, `()`, `()`, `20` summing to the required value | 30 | a call with no arguments adds nothing to the count, so the threshold is still reached only by the values |
| A zero argument | count 3, batches `5` then `0, 7`, assembling a three-digit number | 507 | a zero is a legitimate argument value, not an absent one; skipping arguments that are numerically zero would assemble `57` |
| Order across batches | count 4, batches `1, 2`, `()`, `3`, `4` | 1234 | concatenation follows arrival order, so the newest batch goes last even though it is nearest in the retained chain |
| Empty final batch | excluded by the guarantee that a positive-arity plan ends with values | not applicable | if the last batch were empty, the threshold would never be reached and no value could be returned, which is exactly why the statement forbids it |
| Very long plan | up to 1000 calls with one argument each and a declared count of 1000 | the value of the fully gathered argument list | the number of retained records grows with the number of calls, not only with the number of arguments |

## 6. Alternatives this instance eliminates

| Alternative | Behaviour on this instance | Why it is eliminated |
|---|---|---|
| Triggering after a fixed number of calls | would evaluate on the second call with only two of four arguments | the threshold counts arguments, so the two-then-one and one-then-one styles must agree |
| Triggering when any call happens | would evaluate on the first call with `1, 2` | currying must return a function until the declared count is satisfied |
| Skipping batches that are empty when counting | harmless for the count, but skipping empty *values* inside a batch is not | the distinction is between a batch that carries nothing and an argument whose value is zero |
| Assembling the batches newest-first | would compute `4312` | the argument order of the original call must be reproduced exactly |
| Sharing one mutable argument buffer across all intermediate functions | a re-used intermediate prefix would see arguments from a previous evaluation | every intermediate curried function must stay independently reusable |
| Evaluating the underlying function eagerly when the curried form is created | would run the work before the caller asks and return a value instead of a function | the contract returns a curried function, and only the call that satisfies the threshold produces a value |
| Appending each call's arguments by copying the whole accumulated list | correct results, but repeated copying as the count grows | a retained record per call keeps the per-call cost proportional to the batch it carries |

## 7. Time and auxiliary space complexity

Let $a$ be the declared parameter count, $m$ the number of calls before the threshold is reached, and $G$ the total number of argument values gathered, so $G = a$ under the statement's guarantee that the flattened input length equals the declared count. Each call performs work proportional to the batch it carries — reading the argument values and recording them — so the calls together cost $O(G)$ time, and the threshold test itself is a single comparison against the retained count, hence $O(1)$ per call. When the threshold is reached, assembling the argument list visits one retained record per call, which costs $O(m)$ and yields the gathered values in arrival order, so the total time to produce the final value is $O(G + m)$. Nothing in the process depends on the magnitude of the argument values.

The auxiliary space is the retained state of the pending chain: one record per call, each holding the batch it carried plus a link to its predecessor, so the chain occupies $O(G + m)$ space overall — $O(G)$ for the argument values themselves and $O(m)$ for the links. With $\text{inputs.length} \le 1000$ and $\text{fn.length} \le 1000$, both terms are bounded by a thousand. The working memory of a single call beyond the stored batch is $O(1)$: it compares a running count and creates one record. A design that copies the whole accumulated list on every call would instead cost $O(G)$ time per call and reach $O(G \cdot m)$ in the worst case, which the record-per-call form avoids.
