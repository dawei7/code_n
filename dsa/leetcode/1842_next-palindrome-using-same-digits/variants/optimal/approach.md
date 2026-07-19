## General
**Reduce palindromes to their left halves**

In any palindrome, every position before the center determines its symmetric position after the center. Because `num` is already palindromic, each digit used on its left has a matching occurrence on its right. When $n$ is odd, the center is the only unpaired occurrence and cannot trade places with a paired digit without violating the digit multiplicities required by a palindrome.

Consequently, valid rearranged palindromes correspond one-to-one with permutations of the first $\lfloor n/2\rfloor$ digits. Mirroring a half always restores the correct complete multiset. Among equal-length digit strings, lexicographic and numeric order agree, and the first differing position lies in the left half. The smallest larger palindrome must therefore mirror the next lexicographic permutation of that half.

**Find the next half permutation in linear time**

Scan the half from right to left for the last pivot whose digit is smaller than the digit immediately after it. Everything to the pivot's right is non-increasing. If no pivot exists, the half is already its greatest permutation and the answer is empty.

Otherwise, scan backward within that suffix for the rightmost digit greater than the pivot. Since the suffix is non-increasing, this is the smallest available digit that can increase the pivot. Swap the two digits. The suffix remains non-increasing after that exchange, so reversing it puts the remaining digits in their least possible order.

The pivot change makes the half strictly larger. Choosing the rightmost greater successor makes the increase at the first changed position minimal, and reversing the suffix makes all later positions minimal. Thus this is exactly the next half permutation, not merely some larger one. Mirroring it produces a palindrome with the same digits; the half correspondence proves that no valid palindrome lies between it and `num`.

## Complexity detail
The pivot search, successor search, suffix reversal, and final mirroring each inspect at most $n$ positions, so the total time is $O(n)$. Converting the immutable input string to a mutable digit list and producing the result uses $O(n)$ space.

## Alternatives and edge cases
- **Sort every candidate suffix:** Sorting after the pivot swap is correct but costs $O(n\log n)$ rather than exploiting the suffix's known non-increasing order.
- **Enumerate digit permutations:** Generating permutations and filtering for palindromes is factorial and repeats symmetry work already determined by the half.
- **Increment and test numbers:** The value may contain up to $10^5$ digits, and unrelated intervening numbers do not preserve the digit multiset.
- **No pivot:** A non-increasing first half is the greatest palindromic arrangement, so return `""`.
- **Repeated digits:** The successor must be strictly greater than the pivot; equal digits do not create an increase.
- **Odd length:** Leave the center digit untouched and mirror only the first $\lfloor n/2\rfloor$ positions.
- **Lengths one and two:** Their half has fewer than two positions, so no distinct larger half permutation exists.
- **Strict comparison:** Returning the input itself is never valid, even when it is the only constructible palindrome.
- **Large input:** Operate on characters rather than converting the entire string to an integer.
