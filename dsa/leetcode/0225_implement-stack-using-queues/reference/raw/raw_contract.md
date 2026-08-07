## Function Contract

**Inputs**

- `operations`: App-local commands `["push", x]`, `["pop"]`, `["top"]`, and `["empty"]`, processed against one initially empty stack.

**Return value**

Return the result of each `pop`, `top`, and `empty` command in command order; `push` produces no result.
