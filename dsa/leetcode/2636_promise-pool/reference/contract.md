## Function Contract

**Inputs**

- `functions`: An ordered array of $0 \le m \le 10$ no-argument asynchronous functions, each returning a resolving promise.
- `n`: An integer representing maximum allowed pending promises ($1 \le n \le 10$).

**Return value**

Return a promise that resolves when all $m$ functions have resolved, executing at most `n` functions concurrently.
