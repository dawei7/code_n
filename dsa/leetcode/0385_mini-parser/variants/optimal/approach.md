## General
**Treat an unbracketed input as one integer**

If the first character is not `[`, the entire valid serialization is a signed integer. Converting it directly also handles the only case in which no list stack is needed.

**Let the stack represent open lists**

For a list input, scan left to right. Each opening bracket creates a new list, appends it to its parent when one exists, and pushes it as the current container. A closing bracket finishes any number immediately before it and then pops the completed container. The stack therefore mirrors the unmatched opening brackets at every position.

**Recognize numbers by their source interval**

When a digit or minus sign begins a number, remember that character index. The next comma or closing bracket ends the token, so convert exactly that substring once and append it to the current list. Empty lists have no pending number and are closed without adding a value.

**Why every token reaches the correct parent**

An integer is appended while the stack top is precisely its innermost unmatched list. A nested list is attached to that same parent before becoming the new stack top. Closing brackets reverse only those nesting transitions. Consequently every scalar and list is added once at the depth encoded by the serialization, and the final completed outer list is the parsed result.

## Complexity detail
Let `n` be the serialization length and `d` its maximum nesting depth. The scan examines each delimiter once, and each number character belongs to one conversion, for $O(n)$ time. Excluding the returned structure, the stack holds at most one container per open level and uses $O(d)$ auxiliary space.

## Alternatives and edge cases
- **Recursive descent with one shared index:** also runs in $O(n)$ time and naturally follows the grammar, but recursion depth depends on the input nesting.
- **Recursively slice and rescan substrings:** is concise but deep singleton lists can make it $O(n^2)$ through repeated scans and copies.
- **General-purpose JSON parsing:** accepts this syntax in many languages but bypasses the intended parser construction and does not produce native `NestedInteger` objects.
- The input may be a single negative or nonnegative integer with no brackets.
- An empty list contains no pending numeric token.
- Multi-digit and negative numbers must remain one token.
- Deeply nested singleton lists require stack-safe handling.
