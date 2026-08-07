## Function Contract

**Inputs**

- `fn`: A function whose parameters are explicitly declared ($0 \le \text{fn.length} \le 1000$).

**Return value**

Return a curried function that collects arguments over multiple calls and evaluates `fn` with all collected arguments once `fn.length` arguments have been accumulated.
