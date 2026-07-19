## General
**Scan by index without rewriting the input**

Maintain an index into `code` and a stack of currently open tag names. Ordinary text advances one character; markup branches jump directly past the token they recognize.

**Recognize CDATA before ordinary opening tags**

When the current suffix begins with `<![CDATA[`, require at least one open tag, find the next `]]>`, and skip the entire region. Everything inside is opaque text, even strings that look like tags. An absent terminator makes the code invalid.

**Match closing tags against the stack top**

For $< / \ldots >$, locate the next `>`, validate the extracted name, and require it to equal the most recently opened tag. Pop on a match. This enforces both proper names and nesting.

**Validate and push opening tags**

For any other $< \ldots >$, extract the name, require 1 through 9 uppercase letters, and push it. Characters outside markup are allowed only while the stack is nonempty.

**Enforce exactly one root element**

The first meaningful token must open a tag. If the stack becomes empty before the index reaches the end, reject immediately, because trailing text or a second top-level tag would exist. At end of input, accept only when a root was opened and every tag has closed.

**Why the parser accepts exactly valid code**

The stack records the unmatched opening tags in nesting order. Each legal opening extends that state, each legal closing removes precisely its matching top, and CDATA cannot affect structure. Text and CDATA are admitted only inside the root. Consequently, an empty stack exactly at the final character means one complete, properly nested root; every rule violation is rejected at the token where it occurs.

## Complexity detail
The index advances monotonically and each delimiter search starts at the current position, so `n` characters are processed in $O(n)$ time. At most $O(n)$ tag names can be open, giving $O(n)$ stack space.

## Alternatives and edge cases
- **Recursive descent:** can mirror the grammar, but deeply nested tags consume call-stack depth.
- **Repeated suffix slicing:** can implement the same parser, yet removing one text character at a time repeatedly copies the remaining string and can take $O(n^2)$ time.
- **Regular expression alone:** cannot conveniently enforce arbitrary balanced nesting and CDATA scoping.
- **CDATA outside a tag:** is invalid.
- **Tag name length:** zero or more than nine characters is invalid.
- **Lowercase or nonletter tag character:** is invalid.
- **Mismatched closing order:** is invalid even when all names occur somewhere.
- **Two top-level elements:** are invalid because there must be one root.
- **Text before or after the root:** is invalid.
- **Angle brackets inside CDATA:** are opaque content.
- **Unclosed tag or CDATA:** is invalid at end of input.
