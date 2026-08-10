## General

**Carry moves from right to left through nines**

Adding one starts at the least significant digit, which is the final list entry. An original 9 cannot hold the increment; it becomes 0 and sends a carry left. Any digit from 0 through 8 can absorb the carry by increasing once, after which all more significant digits remain unchanged.

The reverse loop implements exactly this rule. It tests digits beginning at the end and stops on the first non-9.

**Explicitly handle the two digit cases**

If `digits[i] == 9`, the source writes zero and continues the loop. Continuing represents the unresolved carry.

Otherwise, it increments the digit and immediately returns the list. Since the original value was at most 8, the new value is at most 9 and creates no further carry.

For `[4,3,2,1]`, the 1 becomes 2 and the answer returns immediately. For `[4,3,9,9]`, the two trailing nines become zeros, 3 becomes 4, and the result is `[4,4,0,0]`.

**Why loop exhaustion means every digit was 9**

The only branch that does not return is the 9 branch. Therefore, reaching the code after the loop proves every position was visited and every original digit was 9. At that point, the list consists entirely of zeros.

Adding one to an $n$-digit run of nines produces a 1 followed by $n$ zeros. The source changes `digits[0]` from zero to 1 and appends one more zero. Before the append, the list has length $n$ and looks like `[1,0,...,0]` with only $n-1$ zeros after the 1. Appending supplies the required $n$th zero and grows the representation to length $n+1$.

This in-place repair may look less obvious than prepending 1, but it avoids constructing a separate concatenated list.

**Carry invariant**

Before processing index `i`, every digit to its right was a 9, is now zero, and a carry remains. Digits at or left of `i` retain their original values.

A non-9 absorbs the carry and makes the entire mutated list correct. A 9 becomes zero and preserves the invariant one position left. If the invariant passes beyond index 0, every original digit was 9 and the post-loop transformation creates the one extra decimal place.

**Why returned digits stay canonical**

In the ordinary branch, the original leading digit is unchanged unless the list has length one, so no leading zero can appear. In the all-nines branch, the source explicitly sets the first digit to 1. The result therefore has no leading zero.

Every entry remains between 0 and 9. The method never converts the whole sequence into a numeric type, so long inputs are safe from fixed-width overflow.

**Object identity and mutation**

This implementation always returns the original `digits` list. Ordinary cases update one or more entries. The all-nines case also appends to the same list, changing its length.

A caller holding the input reference therefore sees the complete returned result through that same object. The problem permits returning an array and does not require preserving the input.

Python may internally resize the list's storage during `append`, but its logical object identity remains unchanged. That memory-management detail does not create a second caller-visible digit array and does not alter the constant auxiliary-state algorithm.

**Selected class and the alternative**

`Solution2` creates reversed copies, uses an explicit carry, and reverses again. The harness selects `Solution`, whose direct reverse-index mutation uses constant auxiliary state and no proportional intermediate list.

## Complexity detail

The loop visits only the trailing run of nines plus at most one preceding digit. Its worst case is all $n$ digits, so time is $O(n)$. Appending is amortized constant time, though list resizing may copy internal references as an implementation detail.

Only the loop index is additional algorithmic state. Mutations occur in the input/output list, so auxiliary space is $O(1)$, matching the manifest. The returned list may grow by one required element.

## Alternatives and edge cases

- **Modulo update:** Increment each visited digit, take modulo 10, and use zero as the signal to continue carrying. It is algebraically equivalent under digit constraints.
- **Explicit carry and `divmod`:** More general for arbitrary addition but slightly more state than necessary for plus one.
- **Return a new list for all nines:** `[1] + digits` is simple but allocates and leaves the caller's original list zeroed if it was mutated first.
- **No trailing nine:** The last digit increments and the method returns in constant time.
- **Several trailing nines:** They become zeros until the first smaller digit absorbs the carry.
- **All nines:** The first zero is repurposed as leading 1, and one zero is appended.
- **Single 9:** After zeroing, setting index 0 to 1 and appending produces `[1,0]`.
- **Single 0:** The non-9 branch increments it to 1.
- **Maximum input length:** Work remains linear in digits and never depends on a machine integer width.
- **Input identity:** The same list object is returned in every branch.
