## General

**Reduce the sentence to word boundaries**

A sentence is circular when every word's last character matches the next word's first character, including the connection from the final word back to the first. Characters inside a word do not affect this condition.

The exact solution calls `sentence.split()` to create the word list `ss`. Under the stated input format, words are separated by one space with no spaces at either end, so this produces exactly the intended words.

For each pair consisting of index `i` and word `s`, the generator checks

`s[-1] == ss[(i+1)%n][0]`.

Here `s[-1]` is the last character of the current word, while index zero selects the first character of the next word.

**Modulo makes the last edge wrap around**

For every index except the last, `i+1` is the ordinary next word index. At `i=n-1`, the expression `(i+1)%n` becomes `n%n=0`, selecting the first word.

This treats the words as vertices arranged on a cycle. There are exactly `n` required directed connections:

$$
0\to1,\ 1\to2,\ \ldots,\ n-2\to n-1,\ n-1\to0.
$$

The modulo expression covers all of them with one uniform rule and no separate final comparison.

**Why `all` expresses the contract**

Python's `all` returns true only if every Boolean produced by the generator is true. Therefore, the method returns true precisely when all neighboring boundary comparisons succeed.

If one comparison fails, `all` short-circuits immediately and returns false; later comparisons cannot repair a broken circular link. If every comparison succeeds, each required link in the definition has been verified, so the sentence is circular.

This gives a direct correctness argument in both directions. A true return means each current word passed its equality with the next word, including wraparound. A genuinely circular sentence makes every generated equality true, so `all` returns true.

**Trace the circular indexing**

For `"leetcode exercises sound delightful"`, the word list is:

`["leetcode","exercises","sound","delightful"]`.

The comparisons are `e==e`, `s==s`, `d==d`, and finally `l==l` from `"delightful"` back to `"leetcode"`. All succeed.

For `"Leetcode is cool"`, the first comparison is the final `e` of `"Leetcode"` against the initial `i` of `"is"`. It fails, so the result is false without needing to inspect the remaining links.

**A one-word sentence still has one circular edge**

When there is one word, `n=1` and the next index for `i=0` is also zero. The word is compared with itself, but specifically its last character against its first.

Thus `"eetcode"` is circular because both boundary characters are `e`. `"Leetcode"` is not because its last character is `e` and its first is uppercase `L`. A one-word sentence is not automatically circular.

**Case is significant**

The contract treats uppercase and lowercase letters as different. Python string equality already has that behavior, so no lowercasing or normalization should be applied. `'A'` does not equal `'a'`.

**What splitting costs and changes**

The manifest summary mentions checking spaces in one scan with constant extra space, but the exact implementation takes a different route. It materializes a list of words and uses their boundary characters. This is conceptually simple and fully correct, but it allocates storage proportional to the sentence.

Calling `split()` without an explicit delimiter also tolerates repeated whitespace and leading or trailing whitespace, even though the problem guarantees those cases do not occur. That extra tolerance does not alter behavior on valid inputs.

The input length is at least one and valid sentences contain at least one word, so `n` is never zero. The modulo operation therefore cannot divide by zero, and every indexed word has at least one character.

## Complexity detail

Let $L$ be the number of characters in `sentence` and $w$ the number of words. Splitting scans the sentence in $O(L)$ time. The generator checks $w$ word boundaries, so its work is $O(w)$ and is bounded by $O(L)$. Total time is $O(L)$.

The list and substring objects created by `split()` occupy $O(L)$ total auxiliary space in the exact Python implementation. The generator itself is lazy and uses constant additional state. The manifest's $O(1)$ space claim corresponds to a direct character scan, not to this stored word list.

Short-circuiting can reduce comparisons on a failing sentence, but splitting has already scanned the complete input, so the asymptotic worst case remains linear.

## Alternatives and edge cases

- **Direct space scan:** Check the character before each space against the character after it, plus the final-to-first comparison. This avoids the word list and achieves $O(1)$ auxiliary space.
- **Explicit word loop:** A regular loop can return false at the first mismatch and true afterward; it is equivalent to `all`.
- **Single word:** Compare its last and first characters; do not automatically return true.
- **Case difference:** Uppercase and lowercase characters must compare unequal.
- **Wraparound link:** Forgetting the last-word-to-first-word comparison accepts non-circular chains.
- **No leading or trailing spaces:** The contract ensures every word extracted from valid input is non-empty.
- **Short-circuit:** One failed boundary is sufficient to return false.
- **All boundaries equal:** Then every required edge is present and true is returned.
- **Input mutation:** `split()` creates new objects but does not modify the original string.
- **Manifest mismatch:** Space complexity must follow the materialized `ss` list in the actual source.
