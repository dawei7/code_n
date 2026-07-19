## General
**Tokenize by separators, then interpret navigation components**

Split on `/`. Repeated separators create empty components, which do nothing. A component exactly equal to `.` also preserves the current location. A component exactly equal to `..` pops the most recent stored directory when one exists; at root, it has no effect. Push every other nonempty component unchanged.

The comparisons must be exact. Names such as `...`, `.hidden`, and `..data` are ordinary directory names, not navigation instructions.

**The stack already is the canonical component sequence**

Join the remaining stack with single separators and prepend `/`. An empty stack naturally produces the root path `/`.

**Root is an unpoppable lower boundary**

After each component, the stack is the canonical sequence of directories reached by the processed prefix. It contains neither separators nor `.`/`..` navigation markers. Ignoring `..` when the stack is empty models the rule that an absolute path cannot move above root.

**Trace repeated separators and parent navigation**

For `/home/user/Documents/../Pictures`, push `home`, `user`, and `Documents`; `..` removes `Documents`; then push `Pictures`. Joining yields `/home/user/Pictures`.

**The stack mirrors every directory transition**

Empty and `.` components leave the current location unchanged. An ordinary name descends one level and is pushed; `..` ascends one level by popping when possible, while an empty stack correctly keeps the path at root.

After each component, the stack therefore lists exactly the directory names from root to the current destination. Joining that list with single separators removes all redundant syntax and yields the unique canonical absolute path.

## Complexity detail
Splitting, classifying, and joining process $O(n)$ total characters. The component stack and returned path use $O(n)$ space.

## Alternatives and edge cases
- **Repeated string replacement:** becomes brittle for interacting `//`, `.`, and `..` patterns and can copy the path many times.
- **Regular expressions alone:** can collapse separators but do not naturally model parent-directory state.
- **Manual character tokenizer:** avoids the split list and can reduce temporary allocations, but uses the same stack logic with more parsing code.
- `/../` simplifies to `/`, while `/.../` remains `/...`. A trailing separator never appears in the result unless the result is root.
- The input is absolute. Relative paths would need different behavior for leading unresolved `..` components.
