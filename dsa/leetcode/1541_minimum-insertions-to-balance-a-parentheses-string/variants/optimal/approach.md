## General
**Track required closing characters rather than a stack**

Scan from left to right while `needed` records how many closing-parenthesis characters the openings already seen still require. Each `(` adds two to `needed`. Each `)` satisfies one requirement and subtracts one.

The count encodes both nesting and the special paired-close rule. A completed valid prefix has `needed = 0`, while a positive value describes exactly how many future `)` characters would finish all pending openings if no new opening appeared.

**Finish an odd closing requirement before a new opening**

When a new `(` arrives while `needed` is odd, the previous closing token has consumed only its first `)`. The required pair must be consecutive, so the second `)` has to be inserted before this new opening. Count that insertion and decrease `needed` by one, making it even, before adding the new opening's two requirements.

This repair is forced: placing the missing `)` anywhere after the encountered `(` would separate the two characters of the previous closing token and could not fix that prefix.

**Supply an opening for an excess close**

When processing `)` makes `needed` negative, no earlier opening exists for it. Insert `(` immediately before this close. That new opening needs two closing characters; the current `)` supplies the first, so reset `needed` to one and count one insertion.

After the scan, every remaining requirement can only be fulfilled by appending `)` characters. Adding `needed` to the insertions is both sufficient and necessary. Every repair made during the scan addresses a prefix violation at the first point it becomes unavoidable, so postponing it cannot use fewer characters.

## Complexity detail
The scan performs constant work for each of the $n$ input characters, taking $O(n)$ time. The insertion count and outstanding-close count use $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Literal list insertion:** can repair the string in place and obtain the same minimum, but repeated middle insertions can take $O(n^2)$ time.
- **Explicit stack of openings:** works, but stores up to $O(n)$ indices even though only the number and parity of outstanding closes matter.
- A single `(` needs two appended `)` characters, while a single `)` needs an inserted `(` and one additional `)`.
- The string `))` needs only one opening parenthesis inserted before it.
- A lone `)` immediately before `(` forces the missing second `)` to be inserted before that new opening.
- Already balanced strings such as `())` require no insertion.
- Long runs of openings leave two required closing characters per opening at the end.
