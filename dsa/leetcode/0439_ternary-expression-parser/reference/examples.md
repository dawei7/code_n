## Examples

**Example 1**

- **Input:** `expression = "T?2:3"`

- **Output:** `"2"`

- **Explanation:** The condition is true, so the expression selects `2` rather than `3`.

**Example 2**

- **Input:** `expression = "F?1:T?4:5"`

- **Output:** `"4"`

- **Explanation:** Right-to-left grouping makes the expression `(F ? 1 : (T ? 4 : 5))`. One evaluation view first reduces the inner conditional:

`(F ? 1 : (T ? 4 : 5)) -> (F ? 1 : 4) -> 4`

Equivalently, the false outer condition selects its false branch before that branch is reduced:

`(F ? 1 : (T ? 4 : 5)) -> (T ? 4 : 5) -> 4`

**Example 3**

- **Input:** `expression = "T?T?F:5:3"`

- **Output:** `"F"`

- **Explanation:** Right-to-left grouping makes the expression `(T ? (T ? F : 5) : 3)`. Reducing the inner conditional first gives:

`(T ? (T ? F : 5) : 3) -> (T ? F : 3) -> F`

Equivalently, the true outer condition first selects the nested true branch:

`(T ? (T ? F : 5) : 3) -> (T ? F : 5) -> F`
