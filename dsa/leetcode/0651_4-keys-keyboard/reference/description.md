## Description

Imagine you have a special keyboard with the following keys:

- A: Print one `'A'` on the screen.

- Ctrl-A: Select the whole screen.

- Ctrl-C: Copy selection to buffer.

- Ctrl-V: Print buffer on screen appending it after what has already been printed.

Given an integer n, return *the maximum number of *`'A'`* you can print on the screen with **at most** *`n`* presses on the keys*.
### Function Contract

`solve(n: int) -> int`

**Inputs**

- `n`: the maximum number of keyboard operations that may be performed.

The screen is initially empty. Every use of `A`, `Ctrl-A`, `Ctrl-C`, or `Ctrl-V` consumes one of the available keypresses and follows the operation semantics in the Description.

**Return value**

Return the maximum attainable number of `A` characters on the screen after at most `n` keypresses.

### Examples

#### Example 1

- **Input:** $n = 3$
- **Output:** `3`
- **Explanation:** We can at most get 3 A's on screen by pressing the following key sequence:
A, A, A
#### Example 2

- **Input:** $n = 7$
- **Output:** `9`
- **Explanation:** We can at most get 9 A's on screen by pressing following key sequence:
A, A, A, Ctrl A, Ctrl C, Ctrl V, Ctrl V
### Constraints

- $1 \le n \le 50$