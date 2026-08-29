## General

Balanced parentheses create nested regions. The required processing order is innermost first, and a stack naturally exposes the most recently opened region when its closing parenthesis arrives.

The exact solution uses one list, `stk`, to hold opening-parenthesis markers and letters that have already been read. It scans `s` from left to right. Opening parentheses and ordinary letters are initially appended. A closing parenthesis triggers a local stack transformation instead of being stored.

**What the stack represents before a closing parenthesis**

At any scan position, `stk` contains the processed form of the input prefix, plus `"("` markers for regions that have opened but not closed. Any nested region that closed earlier has already been reversed and has had both of its parentheses removed.

Because parentheses are balanced, the marker for the current closing parenthesis exists somewhere below the stack’s top. Because matching is nested, the nearest opening marker on the stack is its matching one.

**Pop the current region in reverse order**

When `c == ")"`, the code creates an empty temporary list `t`. It repeatedly pops from `stk` until the new top is `"("`:

`t.append(stk.pop())`.

The stack yields the enclosed processed characters from right to left. Appending them to `t` in that pop order directly creates the reversal. There is no need to reverse `t` again.

Once the loop reaches the opening marker, `stk.pop()` discards that `"("`. The closing parenthesis was never appended, so both parentheses disappear from the eventual result. Finally, `stk.extend(t)` places the reversed characters back above the surrounding content.

**Why nested reversals occur in the required order**

An outer closing parenthesis cannot be encountered until every textual character and every nested closing parenthesis inside it has been scanned. Therefore, when an inner pair closes, its reversal is completed first. Its reversed letters then behave like ordinary processed content inside the outer region.

When the outer pair later closes, popping reverses the entire current interior, including the result of the inner reversal. This exactly simulates “reverse the innermost substring, remove its parentheses, then continue outward.”

Follow `"(u(love)i)"`. The stack first holds the outer marker, `u`, the inner marker, and the letters of `love`. At the inner close, the letters pop as `e`, `v`, `o`, `l` and are extended back in that order, giving processed inner text `evol`. The next letter `i` is appended. At the outer close, the current interior pops in reverse as `i`, `l`, `o`, `v`, `e`, `u`. The final joined text is `"iloveu"`.

Notice that the outer reversal reverses the already reversed sequence `"evol"` again as part of the larger region. That is not redundant from a semantic perspective; nested reversals can cancel direction for some letters, and the stack operations model those effects correctly.

**Why the final join contains exactly the answer**

For a pair with no nested parentheses, the pop loop plainly replaces its interior string by its reverse and removes the pair. For a nested pair, assume every pair closed earlier has already been transformed correctly. The current pop then reverses the fully processed interior and removes the current markers, so the larger region is also correct. This induction follows the closing-parenthesis order from innermost to outermost.

Ordinary letters outside parentheses are appended and never removed. Letters inside parentheses are popped and restored, so none are lost or duplicated. Every opening marker is discarded by its matching close, and closing markers are never stored. Balanced input ensures that after the scan there are no markers left. `"".join(stk)` therefore returns all input letters in the required transformed order and no parentheses.

**The exact implementation favors simplicity over the linear technique**

This stack transformation is direct and easy to trace, but the same letter can be moved more than once. A letter inside several nested pairs is popped and extended again at every enclosing close. That detail matters when describing the actual worst-case running time.

The editorial also describes pairing parentheses and changing traversal direction, which avoids physically reversing regions. That is a different implementation from the one stored here and has a different time bound.

## Complexity detail

Let $n$ be the length of `s`. The left-to-right scan itself has $n$ iterations, and ordinary append or marker operations are amortized $O(1)$.

At a closing parenthesis, however, the code may pop and re-append every processed letter in that region. With deeply nested parentheses around a long group of letters, the same letters can be moved once for each nesting level. Both the number of letters and nesting depth can be proportional to $n$, producing $O(n^2)$ total list operations in the worst case.

Thus the exact solution’s worst-case time complexity is $O(n^2)$, even though less nested inputs may behave close to linearly. The final join costs $O(n)$ and does not change the bound.

The main stack holds at most $O(n)$ characters and markers. A temporary list for one closing region can also hold $O(n)$ characters, but the two lists together still use $O(n)$ auxiliary space at any moment. The returned string requires $O(n)$ output space.

## Alternatives and edge cases

- **Paired-parenthesis direction traversal:** First link every matching pair. During a second pass, jump to the mate and reverse direction whenever a parenthesis is reached. This processes each position a constant number of times for $O(n)$ time and $O(n)$ space.
- **Recursive parsing:** A function can parse until a closing parenthesis and return the reversed nested result. It mirrors the grammar clearly but still needs attention to string-copying costs and recursion depth.
- **Repeated string slicing:** Finding an innermost textual pair and replacing slices is intuitive but can cause even more expensive immutable-string copying.
- **No parentheses:** Every letter is appended once, the closing branch never runs, and the original string is returned.
- **Empty parenthesized region:** If allowed by the balanced syntax, the top is immediately `"("` at close; the temporary list stays empty and both markers disappear.
- **Single pair:** All enclosed letters are popped once, producing their simple reversal.
- **Deep nesting:** Semantic processing remains correct, but repeated movement exposes the quadratic worst case.
- **Adjacent pairs:** Each pair is closed and transformed independently, and their resulting letter sequences remain adjacent in input order.
- **Balanced-input guarantee:** The loop safely reads `stk[-1]` because every closing parenthesis has a matching earlier opening marker. Malformed input would require explicit validation.
- **Parentheses removal:** The opening marker is explicitly popped, while the closing marker is never pushed. Joining the stack cannot include brackets.
- **Letters are not deduplicated:** Every pop is followed by exactly one append into `t` and one extension back into `stk`, preserving multiplicity.
