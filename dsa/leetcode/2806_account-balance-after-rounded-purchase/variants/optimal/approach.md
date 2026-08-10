## General

**Separate the rounded purchase from the remaining balance.** The account begins with one hundred dollars. The purchase amount must first be rounded to the nearest multiple of ten, with a value ending in five rounded upward. If the rounded purchase is $x$, the required answer is simply $100-x$.

The implementation searches for $x$ explicitly rather than using the arithmetic formula described in the Optimal manifest. It initializes `diff = 100` as a safely large best distance and `x = 0` as the current chosen multiple. It then examines every multiple of ten from one hundred down to zero.

**Enumerate every legal rounded value.** The loop `for y in range(100, -1, -10)` produces

`100, 90, 80, ..., 10, 0`.

These are all and only the possible rounded purchase amounts for an input between zero and one hundred. There are always eleven candidates, independent of the particular purchase amount.

For each candidate `y`, the expression `t := abs(y - purchaseAmount)` computes its distance from the original amount and stores it in `t` using Python's assignment expression. A smaller distance means that `y` is a better rounding result.

**Update only for a strict improvement.** The condition is `t < diff`, not `t <= diff`. When a candidate is strictly closer, the code records both its distance and its value. When two candidates are equally close, it keeps whichever one was encountered earlier.

The descending iteration order is what turns that “keep the first tie” rule into rounding upward. Consider an amount ending in five, such as thirty-five. Candidate forty is visited before candidate thirty. Its distance five becomes the best. When thirty is later examined, its distance is also five, but it is not strictly smaller, so forty remains selected. For any other final digit, exactly one adjacent multiple of ten is closer, so traversal order does not affect the choice.

This interaction between order and strict comparison is the most important subtlety in the exact source. If the loop ran upward with the same strict comparison, ties would round down. If the comparison used `<=` while still running downward, a later smaller candidate would replace the larger one and again round down.

**Why checking distant multiples is harmless.** Mathematically, only the multiples immediately below and above the input can be nearest. The source nevertheless checks all eleven. The first candidate may set an imperfect provisional best, but every closer candidate replaces it. Because the final stored value minimizes absolute distance over the complete legal set, it is the nearest multiple of ten.

The tie rule then selects the greater minimizer. Therefore, after the loop, `x` is exactly the required rounded purchase amount. Returning `100 - x` consequently gives the correct account balance.

For example, with `purchaseAmount = 64`, the loop eventually records seventy with distance six and then replaces it with sixty with distance four. No later candidate is closer, so it returns forty. With `purchaseAmount = 65`, seventy is recorded with distance five and sixty cannot replace it on the tie, so it returns thirty-five.

**Boundary inputs are included directly.** Zero and one hundred are candidates in the enumeration. For zero, candidate zero eventually achieves distance zero and must be the unique optimum. For one hundred, the first candidate already has distance zero, and no update can improve it. The final balances are one hundred and zero respectively.

**The exact algorithm differs from the manifest summary.** The manifest describes adding five and performing integer division, commonly written as `((purchaseAmount + 5) // 10) * 10`. That formula is a valid constant-time alternative, but it does not appear in this solution. The shipped source is a fixed eleven-candidate exhaustive search. Its asymptotic complexity is still constant because the input domain and candidate set are fixed, but a faithful explanation must teach its enumeration and tie behavior.

## Complexity detail

The loop always performs exactly eleven iterations. Each iteration uses a subtraction, absolute value, comparison, and at most two assignments. Therefore, with the stated purchase range, running time is $O(1)$. It is also $\Theta(1)$ because the exact code runs all eleven iterations even when the first candidate is already an exact match.

Only the scalar variables `diff`, `x`, `y`, and `t` are used. Auxiliary space is $O(1)$.

If the problem were generalized to balances up to $B$ while retaining this enumeration of every multiple of ten, the loop would visit $B/10+1$ candidates and take $O(B/10)=O(B)$ time in terms of the numeric range. The constant-time claim relies on the fixed maximum of one hundred in this contract. Complexity analysis should name that distinction rather than pretending the loop has no work.

The arithmetic rounding formula would also be $O(1)$ for an unbounded machine-word value, with the usual caveat that arithmetic cost changes for arbitrarily large integers. Under the current small constraints, both approaches have the same asymptotic label even though the formula uses fewer operations.

## Alternatives and edge cases

- **Add-five formula:** Compute `rounded = ((purchaseAmount + 5) // 10) * 10` and return `100 - rounded`. This directly exploits decimal rounding and is shorter, but it is not the exact implemented method.
- **Use quotient and remainder:** Divide by ten, round the quotient up when the remainder is at least five, and multiply back. This makes the tie rule explicit without enumerating candidates.
- **Floating-point `round`:** Python's built-in rounding uses ties-to-even in relevant forms, not the required always-up rule. It can therefore give the wrong result for amounts ending in five.
- **Amount ending in zero:** The exact matching candidate has distance zero and is selected.
- **Final digit one through four:** The lower multiple is uniquely closer, so the balance reflects rounding down.
- **Final digit five:** Adjacent multiples tie; descending enumeration plus strict improvement retains the higher one.
- **Final digit six through nine:** The higher multiple is uniquely closer.
- **Purchase amount zero:** It rounds to zero and leaves the entire one-hundred-dollar balance.
- **Purchase amount one hundred:** It rounds to one hundred and leaves zero.
- **Changing traversal direction:** An ascending loop would need a non-strict update on ties, or another explicit rule, to continue rounding upward.
- **Changing `<` to `<=`:** With the present descending order, this would make the lower equal-distance multiple overwrite the higher one and violate the tie rule.
- **Inputs outside zero through one hundred:** The candidate set would no longer cover every possible nearest multiple, so the proof and constant bound depend on the stated range.
