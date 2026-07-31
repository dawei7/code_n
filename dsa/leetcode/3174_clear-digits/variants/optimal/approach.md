## General

Scan the original string from left to right while storing the non-digit characters that have survived so far in a stack. When the next character is a letter, append it. When the next character is a digit, remove the stack's top letter.

At the moment a digit is processed, every earlier digit has already been removed because the required operation always selects the first remaining digit. The stack therefore contains exactly the still-present non-digits to this digit's left, in their original order. Its top is the closest such character, so popping the top performs precisely the required pair deletion. The validity guarantee ensures the stack is nonempty at every digit.

After the complete scan, every digit has triggered one pop and is itself omitted. The stack consequently holds exactly the characters remaining after all operations, and joining it gives the required string.

## Complexity detail

Let $n$ be the length of `s`. Each character is examined once, and each letter is pushed at most once and popped at most once, so the time complexity is $O(n)$. The stack can hold up to $n$ letters, giving $O(n)$ auxiliary space. Constructing the returned string also takes $O(n)$ space in the worst case.

## Alternatives and edge cases

- **Literal repeated deletion:** Find the first digit and rebuild or shift the remaining string after each operation. This follows the statement directly but can take $O(n^2)$ time.
- **Mark deleted indices:** Track the nearest unmarked letter to the left of each digit, then construct the result from unmarked positions. This can be linear with an additional index stack, but storing the surviving letters directly is simpler.
- **No digits:** Every letter is pushed and never popped, so the original string is returned unchanged.
- **Consecutive digits:** Earlier digit operations expose earlier surviving letters; each following digit pops the next closest one.
- **Empty result:** The number of digits may equal the number of letters, in which case all characters disappear.
- **Digits are values only syntactically:** The particular digit character does not affect the operation; every decimal digit performs one deletion.
