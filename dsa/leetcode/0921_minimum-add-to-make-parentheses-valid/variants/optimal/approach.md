## General
**Match each closing parenthesis as it arrives**

Scan from left to right while maintaining `open_count`, the number of unmatched opening parentheses available to close. An opening parenthesis increases this balance. A closing parenthesis consumes one available opening when the balance is positive.

If a closing parenthesis arrives with balance zero, no later character can precede it, so it can never be matched by an existing opening parenthesis. One inserted opening parenthesis is therefore unavoidable; count that insertion and continue with balance zero.

**Account for openings left at the end**

After the scan, every unit of `open_count` is an opening parenthesis that never found a closing partner. Each requires one inserted closing parenthesis. The answer is the number of forced openings inserted during the scan plus this remaining balance.

Every counted insertion is necessary: unmatched closing parentheses require earlier openings, and unmatched opening parentheses require later closings. Adding exactly those characters produces a valid nesting, so the lower bound is achievable and the count is minimal.

## Complexity detail
Let $n$ be the length of `s`. The scan processes each character once, giving $O(n)$ time. The balance and insertion count use $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Explicit stack:** Pushing openings and popping them for closings is correct and linear, but stores up to $O(n)$ characters when a counter is sufficient.
- **Repeatedly remove matched pairs:** Removing every occurrence of `"()"` until none remain leaves exactly the unmatched characters, but nested input can require $O(n)$ full-string passes and $O(n^2)$ time.
- **All openings:** Every character needs a closing parenthesis appended, so the answer is $n$.
- **All closings:** Every character needs an opening parenthesis inserted before it, so the answer is $n$.
- **Already valid input:** The scan ends with no forced insertion and zero balance.
- **Balanced counts are insufficient:** A string such as `")("` has equal numbers of each character but still needs two insertions because prefix order matters.
