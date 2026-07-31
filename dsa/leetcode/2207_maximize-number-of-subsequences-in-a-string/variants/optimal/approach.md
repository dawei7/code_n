## General

**Count the subsequences already present**

Scan `text` from left to right while tracking how many copies of `pattern[0]` have appeared. Whenever `pattern[1]` is encountered, it completes one subsequence with every earlier first character, so add the current first-character count to the answer.

Process a second-character match before a first-character match. This order matters when the two pattern letters are equal: the current occurrence may finish pairs with earlier occurrences, but it cannot pair with itself. Track the total occurrences of both pattern characters during the same scan.

**Move the inserted character to an endpoint**

If `pattern[0]` is inserted before all existing text, it precedes every existing `pattern[1]` and creates exactly `second_count` new subsequences. No later insertion of that character can create more, because moving it right only removes possible second characters after it.

Symmetrically, inserting `pattern[1]` after the complete text creates exactly `first_count` new subsequences, and no earlier position can do better. The best insertion therefore adds `max(first_count, second_count)` to the existing count. These two endpoint choices attain both candidate gains, and every allowed insertion is bounded by its corresponding endpoint, which proves the maximum.

## Complexity detail

Let $n$ be the length of `text`. The algorithm performs one constant-work pass, so its time complexity is $O(n)$.

Only the existing subsequence total and two character counts are stored, giving $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Try every insertion position:** Constructing or evaluating all $n+1$ modified strings is correct but can require $O(n^2)$ time.
- **Suffix counts:** Precomputing how many second characters follow every position also counts existing subsequences in $O(n)$ time, but uses unnecessary $O(n)$ space.
- **Equal pattern letters:** Processing the completion contribution before incrementing the first count ensures one occurrence is never paired with itself.
- **Only first characters present:** Insert `pattern[1]` at the end so every existing first character contributes.
- **Only second characters present:** Insert `pattern[0]` at the beginning for the symmetric maximum.
- **Unrelated letters:** Characters matching neither pattern position do not affect any counter or subsequence.
