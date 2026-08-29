## General

**Fix the array from right to left**

A pancake flip reverses only a prefix. The strategy places the largest remaining value into its final position, then never touches that position again.

For target index `i`, required value is `i + 1` because the input is a permutation of one through `n`.

The outer loop runs `i` from `n - 1` down to one. Positions greater than `i` are already correct, and every new flip length is at most `i + 1`, so that suffix remains untouched.

**Find the required value**

The code begins `j = i` and scans left until `arr[j] == i + 1`.

The permutation guarantee ensures the value exists exactly once. Because larger values were placed beyond `i`, the current target lies within prefix zero through `i`.

If `j == i`, it is already correct and no flip is needed.

**First flip: bring the target to the front**

If `j > 0`, flipping prefix length `j + 1` moves the target from the end of that prefix to index zero.

Helper `reverse(arr, j)` treats `j` as an inclusive endpoint. Two pointers swap symmetric entries while left is less than right.

The recorded problem flip length is therefore `j + 1`.

If `j == 0`, the target is already at the front and this flip is skipped.

**Second flip: send the target to position `i`**

Once target is at zero, reversing prefix zero through `i` moves it to index `i`.

The solution records `i + 1` and calls `reverse(arr, i)`.

That position is final. Later iterations use shorter prefixes and cannot move it.

**Trace**

For `[3, 2, 4, 1]`, first target is four for index three, currently at index two.

- Flip length three: `[4, 2, 3, 1]`.
- Flip length four: `[1, 3, 2, 4]`.

Four is fixed. Target three for index two is at index one:

- Flip length two: `[3, 1, 2, 4]`.
- Flip length three: `[2, 1, 3, 4]`.

Target two for index one is already at front, so flip length two yields `[1, 2, 3, 4]`.

The exact sequence need not match an example because many valid answers exist.

**Why two flips suffice**

A prefix reversal cannot always move an arbitrary interior value directly to arbitrary index `i` in one step. The front serves as a staging position:

1. interior target to front;
2. front target to final index.

If target is already at front or final position, one or both flips disappear.


At iteration `i`, assume suffix `i + 1` through `n - 1` is sorted and final. The process places `i + 1` at `i` using only prefix `i + 1`, so the suffix stays unchanged.

This establishes the invariant for the next smaller index. When the loop ends, positions one through `n - 1` are correct, and the remaining value at zero must be one.

**Flip-limit guarantee**

There are `n - 1` iterations and at most two flips each. The result contains at most `2(n - 1)` flips, safely under `10n`.

**Why reversing disrupts only unfinished work**

The two flips may scramble smaller values inside the current prefix. That is harmless because none has been declared final yet. Subsequent iterations deliberately sort that remaining prefix from its right boundary inward.

This separation between fixed suffix and unfinished prefix is the central invariant.

**How the reversal helper implements one legal flip**

For inclusive endpoint `j`, the helper begins with left pointer zero. It swaps positions zero and `j`, then one and `j - 1`, moving inward until pointers meet or cross.

Every position inside the prefix moves to its mirror location, while positions after `j` are never accessed. This is exactly reversal of `arr[0:j + 1]` and therefore exactly one allowed pancake operation.

**Why the search never crosses into the fixed suffix**

At iteration `i`, values greater than `i + 1` already occupy their correct suffix positions. Because the input is a permutation, target `i + 1` cannot be among those larger fixed values.

The leftward search starts at `i` and is guaranteed to find the target before index becomes negative. This also explains why the code needs no failure branch.

**Why returning flips is enough**

The problem's judge applies or validates the recorded `k` values. It does not require the method to return the sorted array.

The implementation mutates `arr` internally so each later choice reflects prior flips, while `ans` provides a reproducible certificate of the same operations.

## Complexity detail

For each `i`, locating the target may scan `O(i)` positions and flips may reverse `O(i)` elements. Summed over all indices, time is `O(N^2)`.

The answer has at most `2N` integers, so space including output is `O(N)`. Reversal uses `O(1)` working space and mutates `arr`.

## Alternatives and edge cases

- **Ordinary sorting:** It does not provide a legal flip sequence.
- **Shortest-sequence BFS:** Exponential and unnecessary because any answer within the limit is accepted.
- **Already sorted:** Every target is already final, so answer is empty.
- **Target at front:** Skip the first flip.
- **Target already final:** Skip both flips.
- **One element:** No outer iteration or flip.
- **Inclusive endpoint:** Helper endpoint plus one is the recorded `k`.
- **Permutation guarantee:** Ensures every target is found exactly once.
- **Input mutation:** The method sorts the actual array.
- **Multiple answers:** Minimum flip count is not required.
