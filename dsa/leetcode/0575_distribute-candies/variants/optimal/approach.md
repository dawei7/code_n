## General

At first, the story sounds like a selection problem: perhaps we must decide exactly which candies Alice should eat. The key simplification is that the answer asks only for the *number of different types*, not the actual candies. That turns the problem into comparing two independent limits.

Let $n$ be the number of candies and let $u$ be the number of distinct values in `candyType`. Alice must eat exactly $n/2$ candies because $n$ is even. Her number of different eaten types can never exceed either of these quantities:

- it cannot exceed $u$, because no type outside the input exists;
- it cannot exceed $n/2$, because every represented type requires eating at least one candy and she may eat only $n/2$ candies.

Therefore, every valid answer is at most

$$
\min\left(u,\frac{n}{2}\right).
$$

The important step is proving that this upper bound is always achievable. Once that is established, the expression is not merely a bound—it is the exact answer.

**Why the smaller limit can always be reached**

Suppose first that $u \le n/2$. Alice can choose one candy from each of the $u$ types. That uses $u$ candy slots and represents all available types. If $u < n/2$, she fills the remaining slots with any duplicate candies. Those extra candies do not reduce the number of represented types, so she finishes with exactly $u$ different types.

Now suppose that $u > n/2$. There are more available types than eating slots. Alice chooses one candy from any $n/2$ distinct types. That uses every allowed slot and gives her exactly $n/2$ different types. Thus, in both possible relationships between $u$ and $n/2$, Alice reaches the smaller value. This two-case construction proves that the answer is exactly their minimum.

**How the exact code obtains the two limits**

The solution is one expression:

```python
return min(len(candyType) >> 1, len(set(candyType)))
```

`set(candyType)` inserts every type value into a set. A set stores each distinct value only once, so repeated candies collapse into one entry. Consequently, `len(set(candyType))` is $u$, the number of available types.

`len(candyType)` is $n$. The operator `>> 1` shifts the nonnegative integer $n$ one binary position to the right. For a nonnegative integer, this equals floor division by two:

$$
n \mathbin{\text{>>}} 1 = \left\lfloor \frac{n}{2} \right\rfloor.
$$

The contract says $n$ is even, so the floor has no effect and the value is exactly $n/2$. Writing `len(candyType) // 2` would communicate the story more directly to many beginners, but the bit shift in the exact solution computes the same number under this contract.

Finally, `min` returns the tighter of the capacity limit and the availability limit. There is no need to construct Alice’s chosen subset because the proof above guarantees that a choice achieving this count exists.

**Tracing the examples**

For `[1, 1, 2, 2, 3, 3]`, $n=6$, so Alice has three slots. The set is `{1, 2, 3}` and has size three. The minimum of three and three is three; choosing one of each type realizes it.

For `[1, 1, 2, 3]`, $n=4$, so there are two slots, while the set has three values. The slot limit is tighter, and choosing any two distinct types gives the answer two.

For `[6, 6, 6, 6]`, there are two slots but only one distinct type. Eating a second candy cannot introduce a new type, so the availability limit gives one.

Negative type labels cause no complication. Values such as `-7` are ordinary hashable integers, and the set distinguishes them just as it distinguishes positive values. Their numeric magnitude and ordering do not matter; only equality matters.

**Why the algorithm is correct**

Let an arbitrary valid selection represent $d$ different types. It contains only types present in `candyType`, so $d \le u$. It contains $n/2$ individual candies and needs at least one selected candy per represented type, so $d \le n/2$. Hence $d \le \min(u,n/2)$ for every selection.

If $u \le n/2$, selecting one candy of every type and then arbitrary duplicates achieves $u=\min(u,n/2)$. If $u>n/2$, selecting one candy from each of any $n/2$ types achieves $n/2=\min(u,n/2)$. The returned value is thus both an upper bound on every solution and attainable by some solution. It must be the maximum possible number of types.

## Complexity detail

Let $n$ be the length of `candyType` and $u$ its number of distinct values. Constructing `set(candyType)` visits all $n$ candies. Hash-set insertion and membership handling take $O(1)$ expected time per integer, so the total expected time is $O(n)$. Computing the two lengths, shifting by one bit, and taking the minimum are constant-time operations at this scale. The declared time complexity is therefore $O(n)$.

The set stores exactly $u$ values, giving $O(u)$ auxiliary space. In the worst case every candy has a different type, so $u=n$ and the declared worst-case space complexity is $O(n)$. The one-line expression creates the full set before taking its length; Python can release that temporary after the expression is evaluated, but its peak space still includes all distinct types.

The $O(1)$ hash operation is an expected, amortized model. Pathological hash collisions can worsen a generic hash table’s theoretical worst case, but Python integers have well-defined hashing and the standard interview analysis uses expected $O(n)$ time. The input list itself is not modified and is not counted as auxiliary space.

## Alternatives and edge cases

- **Sort and count adjacent changes:** Sorting makes equal types consecutive, so one scan can count distinct runs. It needs $O(n \log n)$ time and may modify the input; its extra memory depends on the language’s sorting implementation.
- **Boolean presence array:** Because the constraints bound type values, an offset-indexed boolean array could mark seen types. It can run in $O(n+R)$ initialization time and $O(R)$ space for value range $R$, but a hash set is simpler and stores only types that occur.
- **Manual hash-set loop with early stopping:** Insert values until the set reaches $n/2$ types, then return immediately. This can save work on favorable inputs, though its worst-case time and space remain $O(n)$.
- **Frequency map:** A dictionary of type-to-count also reveals how many types exist, but the counts are unnecessary. A set records exactly the information the answer needs.
- **Trying every subset:** Enumerating choices of $n/2$ candies repeats equivalent decisions and grows combinatorially. The two-limit proof removes the need to search.
- **All candies distinct:** Then $u=n$, but Alice has only $n/2$ slots, so the result is $n/2$.
- **All candies identical:** Then $u=1$, so the answer is one even though Alice eats multiple candies.
- **Exactly enough types:** When $u=n/2$, both limits agree and Alice chooses one candy of each type.
- **Smallest valid input:** With $n=2$, Alice eats one candy, so the answer is always one. The bit shift correctly produces one.
- **Even-length guarantee:** The exact code would compute floor division for an odd length. The problem promises even $n$, so no policy for a fractional half is needed.
- **Bit-shift readability:** `n >> 1` is correct for this nonnegative length, but `n // 2` is often clearer when explaining the domain rule. This is a readability distinction, not an algorithmic one.
