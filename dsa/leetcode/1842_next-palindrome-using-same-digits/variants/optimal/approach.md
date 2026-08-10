## General

**A palindrome is determined by its first half.** In an even-length palindrome, the second half is the mirror of the first. In an odd-length palindrome, the center digit stays between those mirrored halves. Because the input is already a palindrome, its digit counts have the required pairing structure. Rearranging the first-half digits and mirroring them generates every palindrome possible from those pairs; for odd length, the unique unpaired center digit remains fixed.

For equal-length digit strings, numeric order is determined by the first position where they differ. That position lies in the first half before its mirrored partner. Therefore, ordering the possible palindromes is exactly the same as lexicographically ordering their first halves. The smallest larger palindrome is obtained by finding the next lexicographic permutation of the first half.

**Operate on a mutable character list.** `nums = list(num)` copies the string into individual characters because Python strings cannot be modified in place. The nested helper receives the full list but sets its local `n = len(nums) // 2`. Inside that helper, `n` means the number of characters in the first half, not the full string length.

**Find the rightmost pivot that can increase.** Starting at `i = n - 2`, the code moves left while `nums[i] >= nums[i + 1]`. The skipped suffix is nonincreasing. If no index satisfies `nums[i] < nums[i + 1]`, the first half is already the greatest permutation of its multiset. No larger palindrome using the same digits exists, so the helper returns `False` and the method returns the empty string.

Choosing the rightmost possible pivot is what makes the increase minimal. Positions before `i` remain unchanged, preserving the longest possible prefix.

**Choose the smallest available digit greater than the pivot.** The helper begins `j` at `n - 1` and moves left while `nums[j] <= nums[i]`. Since the suffix is nonincreasing, the first value found from the right is the smallest suffix digit strictly greater than the pivot, accounting correctly for duplicates.

Swapping `nums[i]` and `nums[j]` makes the half larger at the latest possible position by the smallest possible amount.

**Minimize everything after the pivot.** Before the swap, the suffix was nonincreasing. After swapping with the rightmost greater element, reversing `nums[i + 1 : n]` puts the remaining suffix in nondecreasing order. This is the smallest possible continuation after the newly increased pivot, so the resulting half is the immediate next distinct permutation, not merely some larger one.

The exact assignment uses two slices and therefore creates temporary lists for the half suffix. Their total size is linear in the worst case, consistent with the method’s overall list storage.

**Mirror the new half.** After the helper succeeds, the outer method resets `n = len(nums)` to the full length. For every `i` below `n // 2`, it assigns

`nums[n - i - 1] = nums[i]`.

This overwrites the right half with the reverse of the new left half. In an odd-length string, the center index is not visited and remains unchanged. Finally, `"".join(nums)` builds the returned palindrome.

**Trace `"1221"`.** The first half is `"12"`. Pivot index zero contains one, and the suffix digit two is the smallest greater choice. Swapping produces `"21"`; there is no meaningful longer suffix to reorder. Mirroring gives `"2112"`, the next larger palindrome.

For `"32123"`, the first half `"32"` is nonincreasing and has no next permutation. The helper returns false, so the result is empty.

**Why only the next half permutation is needed.** Any larger palindrome must have a first half lexicographically larger than the original. The standard pivot, successor, and suffix reversal procedure returns the smallest such first half. Mirroring is order-preserving: if one first half is smaller than another, its palindrome is also smaller at their first differing position. Thus no valid larger palindrome lies between the returned one and the input.

**Why the same digits are preserved.** Next permutation only swaps and reverses first-half characters, preserving their multiset. Mirroring reproduces each half digit’s paired copy. The center digit, if present, is untouched. The full result therefore has exactly the original digit frequencies.

## Complexity detail

Let `n` be the full string length. Finding the pivot scans at most half the string, finding the successor scans at most half, suffix reversal is linear in the half length, and mirroring plus joining are linear. Total running time is `O(n)`.

The mutable `nums` list stores `n` characters, and slicing during reversal can allocate another linear-size temporary list. The joined output also has length `n`. Auxiliary space is therefore `O(n)`.

## Alternatives and edge cases

- **Generate every half permutation:** Sorting all possible palindromes is factorial and infeasible for 100,000 digits.
- **Frequency-based successor construction:** One can locate a pivot and rebuild the minimal suffix from digit counts, but the standard next-permutation reversal is simpler because the suffix is already ordered.
- **Even length:** Every digit belongs to a mirrored pair, and the entire palindrome is determined by the first half.
- **Odd length:** The middle digit is the only unpaired digit and remains unchanged.
- **Length one:** The half has no pivot, so no different palindrome exists and the method returns empty.
- **Length two palindrome:** Its first half has one character, so there is no alternative ordering.
- **Repeated digits:** The strict pivot and successor comparisons skip equal values and produce the next distinct permutation.
- **First half already nonincreasing:** It is the maximum arrangement, so no larger valid palindrome exists.
- **First half nondecreasing:** A next permutation exists unless every half digit is equal.
- **Leading zeros:** All candidates have equal length, so lexicographic comparison still matches their fixed-width digit-string order, though the local description does not separately define leading-zero inputs.
- **Input preservation:** Converting to a list creates a copy; the original string is immutable and unchanged.
- **Suffix slices:** The exact reversal syntax allocates temporary storage even though an in-place two-pointer reversal could avoid that extra slice.
