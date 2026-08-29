## General

**Composition applies the rightmost function first**

For functions listed as:

$$
[f_0,f_1,\ldots,f_{n-1}],
$$

their composition is:

$$
f_0(f_1(\cdots f_{n-1}(x)\cdots)).
$$

Although $f_0$ is written first in the mathematical expression, it executes last. Evaluation begins with the function at the final array index and proceeds backward.

The solution returns a new function that performs exactly this right-to-left evaluation whenever it is called.

**Capture the function array in a closure**

`compose(functions)` does not evaluate any supplied function immediately. It returns `function(x) { ... }`.

That returned function closes over `functions`, so it can use the list later when the caller supplies an input value. This separates composition construction from composition evaluation:

- construction chooses which functions participate;
- invocation chooses the initial value and runs the chain.

The exact closure holds a reference to the input array rather than copying it. Under normal challenge use the array is not changed after composition.

**Carry one current result**

At invocation time, `result` starts as `x`. The loop begins at `functions.length - 1` and decrements down to zero.

Each iteration performs:

`result = functions[index](result)`.

The output of the current function becomes the input to the next function on its left. Only one intermediate value is needed because once a function has consumed the previous result, that earlier value has no further role.

After index zero runs, `result` is the full nested expression and is returned.

**Trace the first example**

Let the list be:

- $f_0(x)=x+1$;
- $f_1(x)=x^2$;
- $f_2(x)=2x$.

For input four:

1. initialize `result = 4`;
2. apply $f_2$, obtaining eight;
3. apply $f_1$, obtaining 64;
4. apply $f_0$, obtaining 65.

The returned value is 65, matching $f_0(f_1(f_2(4)))$.

Applying the functions from index zero upward would instead compute $f_2(f_1(f_0(4)))$, generally a different value.

**Why order cannot be rearranged**

Function composition is usually neither commutative nor freely reorderable. Even simple operations demonstrate this:

$$
(x+1)^2 \ne x^2+1
$$

for most $x$.

The algorithm must preserve the array's specified order while reversing execution direction. Sorting functions, grouping them arbitrarily, or applying them left to right would violate the contract.

**The empty list becomes identity**

When `functions.length === 0`, initial loop index is `-1`, so the loop body never executes.

`result` remains equal to input `x` and is returned. Thus the exact same code implements:

$$
I(x)=x,
$$

the identity function required for an empty composition.

No special conditional branch is necessary. Initializing the accumulator with `x` provides the correct neutral behavior.

**A loop invariant proves correctness**

Before an iteration at index $i$, maintain:

> `result` equals the composition of functions from index $i+1$ through $n-1$ applied to $x$.

Before the first iteration, no function lies to the right of $n-1$, so that empty suffix acts as identity and `result = x`.

The iteration applies `functions[i]` to the existing suffix result, establishing the invariant for the next index to the left.

After index zero, `result` equals the composition of every function from zero through $n-1$, proving the returned value is correct.

**Each invocation starts fresh**

`result` is declared inside the returned function. Every call gets a new local accumulator initialized to that call's `x`.

Only the function list is shared through the closure. Calling the composed function once does not leave a previous result that contaminates the next call.

For example, invoking the same composition with four and then with ten evaluates two independent chains.

**Why reducer-style thinking applies**

This is a right fold over the function array, with the input value as the initial accumulator. A built-in `reduceRight` could express it, but the explicit loop shows the evaluation order directly and avoids creating an extra callback.

The functions all accept and return one integer, so every intermediate output is a valid input for the next function.

**Invocation context**

The exact implementation calls each entry as `functions[index](result)`. It does not forward the composed wrapper's `this` value.

That is correct for the contract's unary numeric functions, whose behavior depends only on their argument. A general-purpose composition utility for methods might choose `functions[index].call(this, result)` instead.

**Optimality of one pass**

Every supplied function may affect the output, so an invocation must generally execute all $n$ functions. The one reverse loop performs exactly those necessary calls and stores only the current value.

No precomputation at composition time can replace execution because the future input $x$ is not yet known and functions may be arbitrary.

## Complexity detail

Let $n=\texttt{functions.length}$. Each invocation calls every function once, so assuming each supplied function is $O(1)$, evaluation takes $O(n)$ time.

The loop uses one accumulator and one index, giving $O(1)$ auxiliary space. The returned closure retains one reference to the existing function array; it does not duplicate its $n$ entries.

Creating the composed wrapper itself takes $O(1)$ time.

## Alternatives and edge cases

- **`reduceRight`:** Naturally expresses right-to-left accumulation but adds a callback layer and is no clearer than the loop.
- **Recursive composition:** Mirrors the nested formula but uses $O(n)$ call-stack space.
- **Left-to-right loop:** Computes the reverse composition and is generally incorrect.
- **Empty function list:** The loop is skipped and input is returned unchanged.
- **Single function:** It is invoked once and its output is returned.
- **Noncommuting functions:** Their listed order must be preserved exactly.
- **Repeated invocation:** Each call initializes a fresh local result.
- **Function-array mutation:** Because the closure retains the original array reference, later external mutations would affect future calls.
- **Thrown error:** The wrapper does not catch it; an exception from a supplied function propagates immediately.
- **Method receiver:** The exact solution does not forward `this` because the challenge functions are argument-only.
