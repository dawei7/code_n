## General

**Read one complete signed integer at a time**

When the cursor reaches a digit or minus sign, remember its position, consume the optional sign and full digit run,
and create one `TreeNode` from that slice. The app-local class is the direct equivalent of LeetCode's injected tree
model.

**Track each open ancestor and its next child slot**

Each stack frame contains an open node and a mutable slot number. A newly parsed node attaches to the left slot when
that number is zero and otherwise to the right slot. Attaching advances the parent's slot, and the child receives its
own frame so any following parentheses can describe its descendants.

**Use parentheses to enter and leave child contexts**

An opening parenthesis announces the next child expression. If the following character is immediately `)`, advance
the current parent's slot without creating a node; this records an absent left child before a possible right child.
Otherwise, the next signed integer starts a nonempty child. Its closing parenthesis pops that child's frame and
returns the parsing context to its parent.

Preorder encoding places every parent before its children, so the top frame is exactly the node awaiting the next
child expression. Slot advancement assigns child expressions in left-then-right order, including explicit empty
positions, and each closing parenthesis removes precisely the completed subtree. The monotonic cursor therefore
reconstructs every value and relationship once.

## Complexity detail

Let $n = \lvert s \rvert$ and let $h$ be the resulting tree height. The cursor advances monotonically, while all
integer slices cover disjoint character runs, so parsing takes $O(n)$ time. The stack stores one frame per open
ancestor and uses $O(h)$ auxiliary space, excluding the required tree nodes.

## Alternatives and edge cases

- **Recursive parser with one shared cursor:** also mirrors the grammar in $O(n)$ time, but a deeply skewed tree can
  exceed Python's call-stack limit.
- **Find matching parentheses and slice subtrees:** is intuitive but repeatedly rescans and copies nested suffixes,
  degrading to quadratic time on a skewed encoding.
- **Tokenize first:** separates lexical and structural parsing but stores $O(n)$ additional tokens.
- **Negative value:** consume `"-"` together with the complete following digit run.
- **Leaf node:** needs no child parentheses.
- **Right child without a left child:** `()` advances the left slot before the right subtree is parsed.
- **Empty string:** returns `None` before allocating a stack.
- **Multi-digit value:** the entire consecutive digit run creates one node.
