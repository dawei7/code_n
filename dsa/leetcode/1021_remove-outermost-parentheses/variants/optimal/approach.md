## General
**Use depth to identify primitive boundaries:** Maintain the number of unmatched opening parentheses before the current character. A `"("` seen at depth zero begins a primitive and is its outermost opening parenthesis, so skip it; append any opening parenthesis seen at positive depth.

**Handle closing parentheses after decreasing depth:** For `")"`, decrement depth first. If the new depth is zero, this character closes the primitive and is outermost, so skip it. Otherwise append it because it belongs inside the primitive.

**Preserve every inner character in order:** Depth returns to zero exactly at the end of each primitive component. The rules omit precisely the character that leaves zero and the character that returns to zero, while all characters at inner depths are appended unchanged.

Since `s` is valid, depth never becomes negative and finishes at zero. Each primitive therefore loses one matched boundary pair, and concatenating the retained characters produces exactly the requested result.

## Complexity detail
The scan examines each of the $N$ characters once, giving $O(N)$ time. The output-character list contains at most $N$ characters and uses $O(N)$ space, including the returned string.

## Alternatives and edge cases
- **Extract primitive slices:** Tracking each balanced interval and taking `primitive[1:-1]` is correct, but repeatedly copying the accumulated output can lead to $O(N^2)$ work.
- **Explicit stack:** A stack can track nesting, but an integer depth is sufficient because matching positions are not needed.
- **Primitive pair:** `"()"` contributes no characters.
- **Several adjacent primitives:** Depth zero separates them without a special delimiter.
- **Deep nesting:** Only the first opening and final closing parenthesis of that primitive are removed.
