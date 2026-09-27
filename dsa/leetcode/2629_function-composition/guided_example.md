# Guided Example: Function Composition

## 1. The instance and the value to derive

Composition turns an array of single-argument integer functions into one function that applies them in sequence. For the array $[f_1, f_2, \dots, f_n]$ the composed function is

$$
F(x) = f_1\bigl(f_2\bigl(\cdots f_n(x)\cdots\bigr)\bigr),
$$

so the **rightmost** function touches the original input first and the **leftmost** function produces the final answer. The composition of an empty array is the identity: $F(x) = x$.

The instance traced here is the three-function case with $f(x) = x + 1$ (position 1), $g(x) = x^{2}$ (position 2), and $h(x) = 2x$ (position 3), evaluated at $x = 4$. The required value is $65$. This instance is chosen because its three functions belong to three different families — a translation, a power, and a scaling — so any accidental reordering shows up immediately as a different number, and because $4$ passes through two intermediate values that are easy to verify by hand.

The statement bounds the instance: $-1000 \le x \le 1000$ and $0 \le \text{functions.length} \le 1000$, with every function accepting and returning a single integer. The intermediate values are not required to stay inside the input range, so no clamping is implied anywhere in the fold.

## 2. The direction of travel

Reading the array from left to right gives the order of *nesting*, not the order of *execution*. The table below separates the two.

| Array position | Function | Role in the composed expression | When it runs | Where its input comes from |
|---|---|---|---|---|
| 1 | $f(x) = x + 1$ | outermost application | last | the value produced by positions 2 and 3 |
| 2 | $g(x) = x^{2}$ | middle application | second | the value produced by position 3 |
| 3 | $h(x) = 2x$ | innermost application | first | the original input $x$ |

So the evaluation order is the reverse of the array order: position $n$, then $n-1$, and so on down to position 1. The next section makes that concrete on the instance.

## 3. Step-by-step trace of the instance

The method keeps a single running value, the *accumulator*, and folds the functions into it from the right end of the array.

| Step | Function applied | Input to that function | Output, stored in the accumulator | What the accumulator now means |
|---|---|---|---|---|
| 0 | none | not applicable | 4 | the untouched input |
| 1 | $h$, the doubling at position 3 | 4 | $2 \cdot 4 = 8$ | positions 3 through 3 have been applied |
| 2 | $g$, the squaring at position 2 | 8 | $8^{2} = 64$ | positions 2 through 3 have been applied |
| 3 | $f$, the increment at position 1 | 64 | $64 + 1 = 65$ | all three positions have been applied |

The accumulator ends at $65$, which is the required value, and the three arithmetic facts of the official trace are reproduced in the same right-to-left order: doubling $4$ gives $8$, squaring $8$ gives $64$, incrementing $64$ gives $65$.

```text
array order          position 1        position 2        position 3
                     f: add one        g: square         h: double
evaluation order     third             second            first
value flow           4  ->  8  ->  64  ->  65
                          h(4)   g(8)      f(64)
```

## 4. The fold invariant and correctness

Write $A_k$ for the function that applies positions $k$ through $n$ in nesting order, that is $A_k = f_k \circ f_{k+1} \circ \cdots \circ f_n$, and let $A_{n+1}$ be the identity function.

**Invariant.** Immediately after the step that applies position $k$, the accumulator holds $A_k(x)$. Before any function has been applied the accumulator holds $A_{n+1}(x) = x$, and after the final step it holds $A_1(x) = F(x)$, which is the required answer.

The invariant is maintained by one algebraic identity: because nesting is associative in the sense that applying the outer function to the result of the inner ones is the same as composing them, we have

$$
A_k(x) = f_k\bigl(A_{k+1}(x)\bigr).
$$

So each step reads the accumulator, which by the invariant is $A_{k+1}(x)$, feeds it to $f_k$, and stores $f_k(A_{k+1}(x)) = A_k(x)$. Induction from $k = n$ down to $k = 1$ proves that the final accumulator is exactly the composed value, and no function is ever applied to a value it should not see.

**Why the direction cannot be reversed.** Applying the array left to right would compute $f_n(\cdots f_1(x)\cdots)$, a different function whenever the family does not commute. On this instance it produces $f(4) = 5$, then $g(5) = 25$, then $h(25) = 50$, and $50 \ne 65$. The reversal is therefore part of the specification, not an implementation detail.

**Why the empty array is the identity.** With $n = 0$ there is no function to apply, so the accumulator is never updated and holds the original input. That is exactly the stated convention $F(x) = x$, so the empty case needs no special branch — the initial value of the accumulator *is* the identity.

## 5. Boundary analysis

| Instance | Required value | What it shows |
|---|---|---|
| $[g]$ with $x = -9$, where $g(x) = x^{2}$ | 81 | one position means one application; there is nothing to reverse, and the sign of the input disappears through squaring |
| $[f, \text{negate}]$ with $x = -7$: negate the input, then increment | 8 | the rightmost function consumes the raw input $-7$, producing $7$; the increment then gives $8$ |
| $[f, g, z]$ with $x = 999$, where $z$ is the constant-zero function at position 3 | 5 | the rightmost function erases the input before any other step: $z(999) = 0$, $g(0) = 0$, $f(0) = 5$ |
| $[\;]$ with $x = 42$ | 42 | the empty composition is the identity, so the answer is the input itself |
| three copies of the scaling $x \mapsto 10x$ with $x = 1$ | 1000 | identical functions are still applied once each; repetition is not collapsed into a single step |
| $[p, q]$ against $[q, p]$ with $x = 2$, where $p(x) = x + 5$ and $q(x) = 3x$ | 11 against 21 | the same two functions in swapped positions give different answers, so a position is semantic information rather than a container slot |

## 6. Alternatives this instance eliminates

| Alternative | Result on this instance | Why it is eliminated |
|---|---|---|
| Applying the functions left to right | 50 instead of 65 | the order of execution is the reverse of the array order |
| Sorting or otherwise reordering the array for convenience | 50 or 21 depending on the order chosen | functions are not interchangeable; reordering changes the composed function |
| Treating the empty array as an error or as a null result | fails the case that requires 42 | the composition of zero functions is defined to be the identity |
| Assuming the functions commute, so that either direction works | 50 instead of 65 | addition, squaring, and doubling do not commute; the counterexample is this very instance |
| Memoizing or deduplicating repeated functions | 1000 in both approaches, but no work is saved | every position is applied exactly once, so there is no repeated subproblem to reuse |
| Building the answer by wrapping the input in nested deferred calls | the same 65 | correct but allocates one retained frame per function for the lifetime of the composed function, where a single accumulator suffices |

## 7. Time and auxiliary space complexity

Let $n = \text{functions.length}$. The fold performs exactly $n$ function applications: one per array position, each preceded by a constant amount of bookkeeping that reads the accumulator, calls the current function, and stores the result. The running time is therefore $\Theta(n)$ with no dependence on the magnitude of $x$ and no possibility of an early exit, because every function must be applied even when a later one would ignore its input. With $n \le 1000$ the composed function performs at most a thousand integer operations per call.

The auxiliary space is $O(1)$: one accumulator holds the entire intermediate state, and the fold is iterative, so no stack of pending applications grows with $n$. A recursive variant would instead consume $O(n)$ stack frames, which is why the iterative form is the safer one against the bound $n \le 1000$. The composed function itself retains the original array so that it can replay the positions when it is finally called, so the retained input is $O(n)$, but that is the caller's array rather than extra working memory.
