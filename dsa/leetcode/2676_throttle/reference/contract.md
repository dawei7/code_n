## Function Contract

**Inputs**

- `fn`: The target function to throttle.
- `t`: The non-negative throttle interval in milliseconds ($0 \le t \le 1000$).

**Return value**

Return a throttled function that executes `fn` immediately on leading calls and coalesces intermediate calls into a single trailing execution per interval `t`.
