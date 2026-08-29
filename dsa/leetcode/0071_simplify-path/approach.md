## General

**Read the path as components, not individual punctuation marks**

A slash separates path components. Calling `path.split('/')` exposes exactly those components so the algorithm can decide what each whole token means. This is important because the special rules apply only to the complete component `.` or the complete component `..`. A token such as `...`, `.hidden`, or `a..b` is an ordinary name and must not be interpreted one period at a time.

Splitting also turns structural slash cases into a simple representation. The leading slash of an absolute path produces an empty component before the first separator. Consecutive slashes produce empty components between them, and a trailing slash produces an empty final component. All such empty strings mean that there is no directory name at that position, so the code can ignore them uniformly.

**Let a stack represent the current canonical location**

The list `stk` holds the real directory or file-name components of the simplified path processed so far. Its order is root-to-leaf: `stk[0]` is immediately below the root, and the last element is the current deepest component. No empty token, `.` token, or `..` token is ever stored.

A stack is a natural fit because moving to a child directory appends a name, while moving to the parent reverses only the most recent unmatched child move. That is last-in, first-out behavior. For example, after reading `/a/b/c`, the stack is `['a', 'b', 'c']`. Reading `..` must remove `c`, not `a` or `b`, so `pop()` performs exactly the required change.

**Process each of the four token meanings**

An empty token or `.` has no effect. The condition `if not s or s == '.'` catches both and continues immediately. Empty tokens arise from redundant slashes; `.` explicitly denotes the current directory. Ignoring either one preserves the current location.

The token `..` requests the parent directory. If the stack is nonempty, `stk.pop()` removes its last real component. If the stack is empty, the current location is already the root. An absolute path cannot go above root, so the request is safely ignored. This is why the pop is guarded instead of being unconditional.

Every remaining nonempty token is a literal name and is appended. The ordering of the tests guarantees that `...` reaches this branch: it is neither `.` nor `..`. The algorithm does not normalize, trim, or otherwise reinterpret valid name characters.

**Trace a path with every important case**

Consider `/.../a/../b/c/../d/./`. The leading empty component is ignored. `...` is appended as a real name, followed by `a`. The first `..` removes `a`. Then `b` and `c` are appended; the next `..` removes `c`; `d` is appended; and `.` plus the empty component caused by the trailing slash are ignored.

The final stack is `['...', 'b', 'd']`. Notice that the three-period name remains because only exact token equality has special meaning. The operations also preserve the original order of all names that survive parent navigation.

For `/../`, both surrounding empty components are ignored. When `..` is read, the stack is empty, so nothing is popped. The final stack remains empty and correctly represents the root.

**A loop invariant that explains correctness**

After processing any prefix of the split components, `stk` is the canonical list of names reached by interpreting exactly that prefix from the root. It contains neither redundant separators nor navigation markers.

The invariant is initially true because no component has been processed and an empty stack represents root. Ignoring an empty token or `.` leaves the represented location unchanged. Popping for `..` moves to the parent when one exists and leaves root unchanged otherwise. Appending an ordinary token moves into precisely that named child. Each possible component therefore preserves the invariant.

After all tokens have been processed, the invariant says that `stk` represents the same location as the complete input path, already stripped of all navigation markers and redundant separators.

**Reconstruct the only canonical spelling**

`'/'.join(stk)` places exactly one slash between consecutive retained names and places none after the final name. Prefixing the result with `'/'` makes it absolute. If the stack is empty, the join is the empty string and the prefix alone yields `'/'`, so root is handled without a special return branch.

The constructed result starts with one slash, has exactly one slash between names, has no `.` or `..` navigation components, and has no trailing slash unless it is root. It is therefore the required simplified canonical path.

## Complexity detail

Let $n$ be the number of characters in `path`. Splitting examines the input once and creates components whose combined character count is $O(n)$. Each token is considered once, and every real component can be appended once and popped at most once. Joining the surviving components writes at most $O(n)$ characters. Total time is therefore $O(n)$, matching the manifest.

The split list and its component strings require $O(n)$ space. The stack can retain $O(n)$ characters in the worst case, and the returned string is also at most linear in the input length. Thus total and auxiliary construction space are $O(n)$. The list operations are amortized constant time per component.

## Alternatives and edge cases

- **Manual character scanner:** Build one token at a time without creating the complete split list. It can reduce temporary storage but introduces more boundary logic around slashes and the final token.
- **Deque as a stack:** It supports the same append and pop operations, but a Python list already provides efficient operations at its end and is simpler here.
- **Repeated textual replacement:** Replacing `//`, `/./`, or name-plus-`/..` patterns is fragile because changes interact, root has special behavior, and periods may be valid names.
- **Leading slash:** Splitting produces an empty token, which is ignored; reconstruction adds exactly one leading slash.
- **Repeated slashes:** Every extra separator creates an empty token, and ignoring all empty tokens collapses any run to one canonical separator.
- **Trailing slash:** Its empty final token is ignored, and joining names does not append a slash.
- **Current-directory marker:** A component exactly equal to `.` changes nothing.
- **Parent at root:** An empty stack cannot be popped, so `/..` remains `/`.
- **Several parent markers:** Each one removes at most one retained component; any excess markers at root are ignored.
- **Three or more periods:** Only exact `.` and `..` matches are special, so `...` and `....` remain literal names.
- **Names containing periods:** Tokens such as `.config` or `a..b` are ordinary names.
- **Root result:** An empty stack joins to an empty suffix, making `'/' + ''` exactly `/`.
- **Input mutation:** The input string is immutable and only read; the stack stores derived component strings.
