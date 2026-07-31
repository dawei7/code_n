## General

**Why one merge can expose another**

An adjacent pair may initially be coprime but become mergeable after the value on its right absorbs another number. For example, in `[6, 35, 10]`, the last two values first become `70`; that new value then shares a factor with `6`. A single left-to-right pass that never revisits a boundary would therefore stop too early.

Keep a stack representing the fully reduced prefix. Append each input value. While the top two stack values have greatest common divisor $g > 1$, remove the right value and replace the left value by their least common multiple:

$$
\operatorname{lcm}(a,b)=\frac{a}{\gcd(a,b)}b.
$$

Check the new top boundary again after every merge. Dividing before multiplying avoids an unnecessarily large intermediate product.

**Why the stack produces the final array**

Before a new value is appended, every adjacent pair already in the stack is coprime. Consequently, the only possible violation is at the new top boundary. Merging that pair preserves the order of all remaining values, but the resulting least common multiple may violate the boundary immediately to its left; the loop examines exactly that boundary next. When the loop stops, the enlarged prefix is reduced again.

Every stack merge is one of the operation's permitted adjacent replacements. After the last input is processed, the stack contains no adjacent non-coprime pair, so it is a terminal array reachable by valid operations. The problem guarantees that every permitted replacement order has the same terminal result; therefore this terminal stack is the required array.

## Complexity detail

Each input value is pushed once. Every successful merge removes one stack entry, so fewer than $n$ merges occur and there are $O(n)$ greatest-common-divisor calls. Euclid's algorithm costs $O(\log V)$ per call, where $V$ is the largest value involved in such a call. The total time is $O(n \log V)$.

The stack can retain all $n$ input values when every adjacent pair is already coprime, so the auxiliary space is $O(n)$.

## Alternatives and edge cases

- **Repeated full-array rescanning:** Rebuilding or rescanning the entire current array after each replacement is correct, but repeated merges can make it quadratic.
- **Prime-factor bookkeeping:** Factoring every value can detect shared factors, but it adds more machinery and does not remove the need to propagate merged values leftward.
- **Values equal to one:** Since $\gcd(1,x)=1$, a `1` never participates in a replacement and acts as a permanent separator.
- **Cascading merges:** A least common multiple can merge through several earlier stack entries, so the top-boundary check must be a loop rather than a single condition.
- **Already reduced input:** If all adjacent pairs are coprime, every value remains in its original order.
