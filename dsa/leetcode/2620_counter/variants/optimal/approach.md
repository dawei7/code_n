## General

The returned function must remember a value after `createCounter` has finished. A JavaScript closure provides exactly that lifetime: declare the current count in the outer function's lexical environment, then return an inner function that reads and updates it. Each created counter receives its own captured binding, so counters created from different starting values remain independent.

Post-increment expresses the required ordering directly. Evaluating `n++` produces the current value first and only then stores the value plus one. Thus the first call returns the original `n`, while the captured binding is ready with `n + 1` for the next call. Creation alone does not increment anything because the inner function has not yet executed.

After any $j \ge 0$ completed calls, the captured value is `n + j`. Therefore call $j + 1$ returns `n + j` and advances the binding to `n + j + 1`, preserving the required sequence for every invocation.

## Complexity detail

Creating the closure and each subsequent counter invocation take $O(1)$ time. The closure retains one numeric binding, so it uses $O(1)$ space. If a harness performs $k$ calls and collects every result, that harness necessarily spends $O(k)$ time and $O(k)$ output space; the counter operation itself remains constant-time per call.

The per-call bound is optimal because producing a return value already requires $\Omega(1)$ work.

## Alternatives and edge cases

- **Generator function:** A generator can retain state and yield successive values, but it changes the required call interface to repeated `.next()` operations.
- **Property on the returned function:** Storing a counter as a function property can work, but exposes mutable implementation state and is less direct than a private lexical binding.
- **Pre-increment:** Returning `++n` would make the first result `n + 1`, an off-by-one error.
- **Zero calls:** Merely creating the closure must not emit or advance a value.
- **Negative start:** Incrementing is arithmetic and continues correctly through negative values and zero.
- **Multiple counters:** Every call to `createCounter` creates an independent captured binding; state must not be shared globally.
