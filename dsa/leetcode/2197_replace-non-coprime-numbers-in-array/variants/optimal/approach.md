## General

The process repeatedly merges adjacent values whose greatest common divisor is greater than one. A merge can create a new least common multiple that is non-coprime with the value immediately to its left, so one replacement may need to propagate backward.

The exact solution uses a stack representing the fully reduced prefix. Each new input value is pushed, then the top two values are merged repeatedly until they are coprime or only one remains.

**Maintain a reduced-prefix invariant**

Before processing the next input value, every adjacent pair already inside `stk` is coprime. This means the stack is the final reduced form of the input prefix seen so far.

Appending a new `x` cannot affect relationships between older interior pairs. The only possible new violation is at the boundary between the previous stack top and the newly appended value.

That localization is why a stack is sufficient.

**Test the newest adjacent pair**

After pushing, the loop reads `x, y = stk[-2:]` and computes `g = gcd(x, y)`.

If `g == 1`, the pair is coprime. The stack invariant already covers every earlier adjacent pair, so the entire stack is reduced and the loop can stop for this input element.

If `g > 1`, the pair is non-coprime and must be replaced.

**Compute the least common multiple**

For positive integers,

$$
\operatorname{lcm}(x,y)=\frac{xy}{\gcd(x,y)}.
$$

The code pops the top value `y` and overwrites the preceding `x` entry with `x * y // g`. Two adjacent stack items become one at the same relative position.

Python integers prevent overflow during `x * y`. In a fixed-width language, dividing one operand by `g` before multiplying is often safer.

**Propagate a merge to the left**

The new LCM contains prime factors from both merged values. It may share a factor with the element now immediately before it, even if that earlier element was coprime with old `x`.

Therefore the while-loop repeats rather than appending the result and moving on. Every repeated merge pops another stack item and moves the combined component left.

Once the new boundary is coprime, all older boundaries are still reduced and the invariant is restored.

For `[6,4,3,2]`, pushing four merges it with six into twelve. Pushing three then merges with twelve and remains twelve; pushing two merges again. The backward propagation produces one reduced component 12.

**Why processing left to right is allowed**

The problem guarantees that choosing non-coprime adjacent pairs in any order produces the same final array. The stack implements one particular valid order: always resolve the newest right boundary completely before reading another input value.

Every stack merge is an operation allowed by the problem, so the produced reduced array is reachable. When the scan finishes, every adjacent stack pair is coprime, so the process has reached a terminal array. Order independence guarantees it is the required unique final result.

**Why no necessary merge is missed**

Assume the stack was reduced before a push. Older pairs remain adjacent with unchanged values until a boundary merge reaches them. Thus they cannot spontaneously become invalid except when one member is replaced by a propagated LCM.

The loop tests exactly that newly formed boundary after every replacement. It continues until the boundary is coprime. By induction, no non-coprime adjacent pair remains anywhere in the stack after each input prefix.

**Why elements are processed efficiently**

Every input value is pushed once. A successful merge pops one stack element, and a popped element never returns as a separate stack item.

Although one new value can trigger many iterations, the total number of successful merges across the whole scan is at most $n-1$. There is also at most one final failed gcd test per pushed value. This amortized view prevents the nested while-loop from becoming quadratic.

Values equal to one never merge with anything because their gcd with every positive integer is one. They act as permanent separators between independently reducible regions.

## Complexity detail

Let $n$ be the input length and $V$ bound the values encountered during gcd computations. There are $O(n)$ total gcd calls by the push/pop amortization. Euclid's algorithm takes $O(\log V)$ time per call, so total time is $O(n\log V)$.

The stack may retain all $n$ values when every adjacent pair is already coprime, giving $O(n)$ space. The stack is also the returned result. Excluding output storage, only constant scalar variables are used.

The final-value guarantee bounds completed merged values by $10^8$; intermediate merged components belong to eventual components and remain within the same practical bound. The manifest's time and space match the exact stack implementation.

## Alternatives and edge cases

- **Repeated full-array scans:** Finding and replacing one pair at a time is direct but can shift arrays and revisit long prefixes, leading to quadratic behavior.
- **Linked list simulation:** Deletions are cheaper than array shifts, but finding newly invalid neighbors still needs careful management; the stack is simpler.
- **Recursive reduction:** Recursively merge with the previous result, but deep chains risk call-stack limits.
- **All adjacent pairs coprime:** Every value remains on the stack and the output equals the input.
- **All values merge:** Repeated pops leave one LCM component.
- **Value one:** It is coprime with every neighbor and blocks propagation across it.
- **Equal values greater than one:** Their LCM is the same value, so duplicates collapse.
- **New LCM shares a left factor:** The while-loop immediately catches and merges it.
- **GCD exactly one:** The loop breaks without changing either value.
- **Positive inputs:** LCM and gcd formulas need no zero special case.
- **Order-independent guarantee:** It justifies using this deterministic left-to-right merge order.
- **Potential multiplication overflow elsewhere:** Python is safe; fixed-width implementations should compute `x // g * y`.
- **Input preservation:** The exact source reads `nums` and builds a separate stack, leaving the input list unchanged.
