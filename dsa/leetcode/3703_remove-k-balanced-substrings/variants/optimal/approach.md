## General

Process the string from left to right while storing the unreduced prefix as run-length encoded blocks `[character, count]`. Equal adjacent characters share one block, so the only possible removable suffix after reading a closing parenthesis consists of the final opening-parenthesis block followed by the final closing-parenthesis block.

**Remove a pattern as soon as it is completed.** Each closing parenthesis increments the final `)` run. When that run reaches exactly `k` and the preceding `(` run contains at least `k` characters, those last `k` openings followed by the `k` closings form one k-balanced substring. Delete the closing run and subtract `k` from the opening run, deleting it too if its count becomes zero.

Processing one character at a time means a removable closing run is detected at the moment its count first reaches `k`; it never needs to grow beyond `k` while a qualifying opening run precedes it. Removing the suffix immediately has the same effect as one of the required rounds. Any earlier characters exposed by that removal are already represented at the stack boundary, and future characters can form newly created occurrences with them.

After every input prefix, the stack therefore represents exactly the fixed-point reduction of that prefix. The update either appends a character that completes no pattern or removes the unique pattern ending at that character. By induction, after the final character the stack contains no removable occurrence and preserves precisely the characters left by repeated global rounds. Expanding its runs produces the required final string.

## Complexity detail

Let $n=\lvert s\rvert$. Each input character is added once, and each run is removed at most once, so reduction takes $O(n)$ time. Expanding the surviving runs also takes at most $O(n)$ time. The run stack and returned string use $O(n)$ space in the worst case.

## Alternatives and edge cases

- **Repeated string replacement:** Removing the pattern from a freshly rebuilt string in every round is simple but can rescan long nested inputs $O(n)$ times, leading to $O(n^2)$ work.
- **Character stack plus suffix slicing:** Checking the last `2 * k` characters after every append can take $O(k)$ per character and therefore $O(nk)$ time.
- **No occurrence:** Every run remains in the stack and the original string is returned unchanged.
- **Cascade after joining:** A removal can expose another match, such as `"(())"` with `k = 1`; immediate stack reduction handles the cascade without restarting a scan.
- **Pattern size matters:** A substring such as `"()"` is not removable when `k > 1`.
- **Complete deletion:** If all runs cancel, joining the empty run stack correctly returns `""`.
