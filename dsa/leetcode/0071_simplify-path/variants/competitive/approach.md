## General

**Split once so every decision concerns a complete name**

The solution first computes `tokens = path.split("/")`. A Unix path assigns meaning to components between slashes, so whole-token processing avoids an important mistake: only tokens exactly equal to `.` and `..` are navigation instructions. A longer run such as `...` is a valid literal name.

Empty tokens are expected rather than erroneous. The initial slash creates an empty token at the beginning, a trailing slash can create one at the end, and repeated slashes create empty tokens between them. Later conditions deliberately refuse to append these empty strings, which collapses every separator run without needing a separate slash-normalization pass.

**Store only unresolved real components**

`stack` contains the canonical components produced by the processed prefix. Its last entry is the deepest current name, so a parent instruction can remove it in constant amortized time. This is the essential data-structure match: entering names occurs in input order, while `..` undoes the most recently entered surviving name.

Suppose the processed path is `/home/user/Documents`. The stack is `['home', 'user', 'Documents']`. If the next token is `..`, moving to the parent must discard `Documents`, and `stack.pop()` does exactly that. Earlier ancestors remain in their proper order.

**Understand the compact two-branch control flow**

The first branch is `if token == ".." and stack`. It pops only when the token requests a parent and a retained component exists. The `and stack` part is both a nonemptiness test and a safety guard against popping an empty list.

If the token is `..` while the stack is empty, that first condition is false. The `elif` also requires `token != ".."`, so it is false as well. The token is consequently ignored. This compact interaction implements the rule that an absolute path cannot ascend above root.

The second branch appends only when all three tests hold: the token is not `..`, is not `.`, and is nonempty. Thus a current-directory marker and every empty token are ignored, while every other sequence is accepted literally. In particular, `...` passes all three tests and remains a directory name. The branches are mutually exclusive, so a token can cause at most one stack operation.

**Trace the interaction between popping and literal periods**

For `/.../a/../b/c/../d/./`, the initial empty token is ignored. The token `...` is not a special marker and is appended. `a` is appended, then `..` pops it. Next `b` and `c` are appended, and the following `..` pops only `c`. The name `d` is appended. Finally `.` and the trailing empty token are ignored.

The resulting stack is `['...', 'b', 'd']`. The trace shows both reasons a period-containing token can behave differently: exact `..` reverses one retained descent, whereas exact `...` is just a name.

For `/a//b`, splitting produces empty tokens around the leading slash and between the doubled slashes. Only `a` and `b` satisfy the append condition, so reconstruction yields `/a/b` with exactly one separator.

**Why the stack always represents the simplified prefix**

Before processing a token, assume `stack` lists the canonical location reached by all earlier tokens. This is true initially because an empty stack represents root.

If the token is `..` and the stack is nonempty, popping moves to the represented parent. If it is `..` at root, both branches do nothing, which is the correct root behavior. If it is `.` or empty, the append condition fails and the represented location remains unchanged. Any other token is a valid literal name, and appending it moves to that child. Every possible input token therefore preserves the assumption.

By induction, after the loop the stack represents the same location as the entire absolute path and contains only the literal names that survive navigation. No future component is needed to interpret an earlier ordinary name except through a possible pop, which is exactly why stack state is sufficient.

**Build an absolute path without special casing root**

`"/".join(stack)` inserts one separator between retained names and none at either end. Prefixing `"/"` produces one leading separator. When the stack has names, the result is an absolute canonical path with no trailing slash. When the stack is empty, joining returns the empty string, so the expression naturally returns `"/"`.

The result cannot contain a navigation component because neither `.` nor `..` is appended. It cannot contain redundant separators because joining controls every separator. Together with the invariant, this proves that the returned spelling is canonical and denotes the same location as the input.

## Complexity detail

Let $n$ be `len(path)`. Splitting the path costs $O(n)$ time and space. Across the loop, the combined lengths of all tokens are $O(n)$; each token causes constant control work plus at most one amortized-constant append or pop. The final join writes $O(n)$ characters at most. Total time is $O(n)$, as declared by the manifest.

`tokens` retains the split representation, `stack` can retain all real components, and the result contains up to $O(n)$ characters. Their combined asymptotic storage is $O(n)$. A manual scanner could avoid the separate token list, but the stack and returned representation can still be linear.

## Alternatives and edge cases

- **Streaming token parser:** Scan characters and process a component whenever a slash is reached. It avoids `tokens` but requires explicit handling of the last component and repeated separators.
- **Single combined membership test:** Use a clearer sequence of explicit cases or test `token not in ('', '.')`. The selected branches are compact but require noticing how an unpoppable `..` falls through.
- **Filesystem library normalization:** A platform utility may have environment-specific behavior, while this problem defines a precise lexical contract and should be solved without consulting a real filesystem.
- **Repeated string rewrites:** Iteratively remove patterns such as `/name/..`; this can rescan large prefixes, mishandle root, and confuse literal period names.
- **Empty stack plus `..`:** Both conditions reject the token, correctly keeping the path at root.
- **One retained name plus `..`:** The pop empties the stack, so reconstruction returns `/`.
- **Consecutive `..` tokens:** They pop distinct retained names until root, after which extras are ignored.
- **Single `.` token:** It fails the append condition and has no effect.
- **`...` and longer names:** They are not equal to either special token and are appended unchanged.
- **Multiple slashes:** Their empty tokens fail the truthiness requirement.
- **Trailing slash:** The empty last token is ignored, and join adds no trailing separator.
- **Maximum input length:** Each character participates in splitting and reconstruction only a constant number of times.
- **Root-only input:** All tokens are empty and the prefixed empty join returns exactly `/`.
- **Input preservation:** The source path is unchanged; only the derived token and stack lists are mutated.
