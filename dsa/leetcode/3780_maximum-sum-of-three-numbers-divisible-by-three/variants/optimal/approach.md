## General

**Classify values by their remainder**

A sum is divisible by three exactly when the sum of its remainders is congruent to zero modulo three. Every value belongs to one of three groups:

- remainder 0;
- remainder 1;
- remainder 2.

The source first sorts `nums` and then appends each value to `g[x % 3]`. Because the input was sorted globally, every residue list is also nondecreasing. Its final element is the largest currently available value in that class.

**Reduce infinitely many values to nine residue choices**

The outer loops choose residue `a` for the first element and residue `b` for the second. The third residue is forced:

`c = (3 - (a + b) % 3) % 3`.

This is the unique member of `{0,1,2}` satisfying

$$
(a+b+c)\bmod 3=0.
$$

There are only nine ordered pairs $(a,b)$, so every valid residue multiset appears in at least one loop ordering. For example, three remainder-one values arise from $a=1,b=1,c=1$, while one value of each class arises from orderings such as $a=0,b=1,c=2$.

**Temporarily remove chosen occurrences**

For a nonempty first class, `x = g[a].pop()` takes its largest value and removes that occurrence. For each nonempty second class, `y = g[b].pop()` does the same in the temporarily reduced groups.

If `a==b`, the second pop obtains the second-largest distinct occurrence rather than reusing `x`. If the required third class equals `a` or `b`, its list has already had the appropriate one or two occurrences removed.

When `g[c]` remains nonempty, `z = g[c][-1]` is the largest third occurrence still available. The candidate `x+y+z` therefore uses three distinct array positions even when their values or remainders are equal.

After testing a second choice, `g[b].append(y)` restores it. After all second classes are tried, `g[a].append(x)` restores the first. Since each removed item was the current last and largest item, appending it restores the original sorted order.

**Why the largest available values are sufficient**

Fix a valid ordered remainder pattern $(a,b,c)$. All values are positive, and choosing a larger value within the same residue class does not change divisibility.

Therefore the best triplet for this pattern uses the largest available occurrence from each required class, using the top two or three distinct occurrences when a class repeats. The pop-and-peek procedure does exactly that.

Any valid triplet has some remainder pattern that the loops enumerate. For that pattern, the constructed candidate is at least as large as the triplet because every selected occurrence is replaced by the largest legal occurrence of the same residue multiplicity. Taking the maximum across candidates therefore reaches the global optimum.

Every evaluated candidate is also sound: its remainder sum is zero and the temporary removals ensure three positions are distinct.

**Trace a mixed-remainder choice**

For `[4,2,3,1]`, sorting gives `[1,2,3,4]`. Residue groups are:

- `g[0]=[3]`;
- `g[1]=[1,4]`;
- `g[2]=[2]`.

Choosing `a=1` pops 4, choosing `b=2` pops 2, and the required `c` is zero. Peeking 3 yields $4+2+3=9$.

Another valid pattern chooses 2, 3, and 1 for sum six, but `ans` retains nine.

**Use zero only as the no-triplet result**

`ans` begins at zero. All input values are positive, so every valid triplet has a positive sum and replaces zero. If no residue pattern has enough remaining occurrences for three positions, no candidate is evaluated and zero is returned exactly as required.

**The manifest describes a different optimization**

The manifest says the method retains only the three largest values per residue and therefore runs in $O(N)$ time with $O(1)$ space. The exact source sorts all values and stores every value in a residue list.

Its actual general time is $O(N\log N)$ and its additional storage is $O(N)$. The constant nine-pattern enumeration does not remove the sorting and grouping costs.

## Complexity detail

Sorting $N$ values takes $O(N\log N)$ time. Distributing them into residue groups takes $O(N)$. The nested residue loops have only $3\cdot3=9$ combinations, and every pop, append, or final-element access is $O(1)$.

Total actual time is $O(N\log N)$.

The three group lists together store all $N$ values, using $O(N)$ auxiliary space. Python's sort may also use $O(N)$ temporary memory. The input `nums` is mutated into sorted order.

## Alternatives and edge cases

- **Keep only three maxima per residue:** This is sufficient because a triplet uses at most three occurrences from one class and achieves the manifest's intended $O(N)$ time and $O(1)$ bounded storage, but it is not the exact source.
- **Enumerate all triplets:** It is direct but costs $O(N^3)$.
- **Dynamic programming by selected count and remainder:** A small DP can solve the problem in $O(N)$ time, but the source uses sorted residue groups.
- **Choose one maximum from each class only:** Valid patterns also include three values from one class and patterns such as residues 1,1,1.
- **Reuse the same occurrence:** Temporary pops are essential when residue classes repeat.
- **Three equal numeric values at different indices:** They are valid distinct selections and remain as three list occurrences.
- **Insufficient class multiplicity:** A required empty `g[c]` causes that pattern to be skipped.
- **Exactly three inputs:** The sole triplet is returned if divisible by three, otherwise zero.
- **All values remainder zero:** The source pops the three largest distinct occurrences from `g[0]`.
- **No valid triplet:** Positive inputs ensure the untouched zero sentinel is unambiguous.
- **Restoration order:** Popped maxima are appended back, preserving sorted residue lists for later patterns.
- **Input mutation:** The initial `nums.sort()` changes caller-visible order.
- **Source/manifest mismatch:** This implementation stores and sorts the complete input rather than maintaining three bounded top-value buffers.
