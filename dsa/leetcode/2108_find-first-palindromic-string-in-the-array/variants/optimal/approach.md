## General

**Preserve array order**

The output is not any palindrome but the first one. Process `words` from left to right and return immediately when the current word qualifies. If the scan ends without a match, return `""`.

**Check mirrored pairs in place**

For one word, place `left` at its first character and `right` at its last. While `left < right`, unequal characters prove that word is not palindromic; stop checking it and continue with the next array element. When they match, move both pointers inward.

If the pointers meet or cross without a mismatch, every mirrored pair is equal, so reading the word forward and backward yields the same sequence. Returning at that moment preserves the required first-match ordering.

The scan rejects every non-palindrome at a concrete unequal pair and accepts only after verifying all necessary pairs. Since words are considered in input order, the first accepted word is exactly the requested result.

## Complexity detail

Across all inspected words, at most their characters are examined, so the worst-case time is $O(S)$. The two indices use $O(1)$ auxiliary space. Early return may inspect less than $S$ when an earlier palindrome exists.

## Alternatives and edge cases

- **Compare with a reversed copy:** `word == word[::-1]` is concise and still takes $O(S)$ total time, but allocates a temporary string proportional to the current word length.
- **Build reverses by front insertion:** Explicitly shifting accumulated characters right before inserting each new character at the front takes quadratic time per word and unnecessary extra space.
- Every one-character string is palindromic because it has no unequal mirrored pair.
- Even-length words finish when their two central characters have been compared; odd-length words need not compare the center with itself.
- A later palindrome must not replace an earlier one, so collecting all matches before choosing is unnecessary.
- If every word has a mismatch, the required result is the empty string.
