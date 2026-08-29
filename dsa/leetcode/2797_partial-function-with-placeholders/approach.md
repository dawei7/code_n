## General

**The merge rule.** The input contains a function `fn` and a partially prepared argument array `args`. Ordinary elements of `args` already occupy their final positions. Each literal string `"_"` is a placeholder that must consume the next value supplied when the returned function is called. After every placeholder has consumed one value, any remaining call-time values are appended to the end. The wrapper then invokes `fn` with that completed sequence.

For instance, suppose `args` is logically `[2, "_", 4, "_"]` and the wrapper receives `[7, 9, 11]`. The first underscore takes `7`, the second takes `9`, and the unused `11` is appended. The resulting invocation is therefore equivalent to passing `[2, 7, 4, 9, 11]`.

**Capture the partial argument array.** The outer `partial` call returns an inner function. JavaScript closures allow this inner function to retain references to `fn` and `args` after `partial` itself has returned. Nothing is merged at creation time because the values that replace the placeholders do not exist yet.

The returned wrapper declares a rest parameter, `...restArgs`. At each invocation, JavaScript collects all arguments supplied to the wrapper into the array `restArgs`. The variable `i` is the index of the next unconsumed element of that array.

**Scan fixed positions from left to right.** The `for` loop visits every current element of `args` by index `j`. Whenever `args[j] === '_'`, it assigns `restArgs[i]` into that position and increments `i`. Strict equality is useful here: only the exact primitive string underscore is treated as a placeholder. Other strings and values remain ordinary pre-filled arguments.

The contract guarantees that the number of placeholders does not exceed the number of supplied rest arguments. Therefore every placeholder reads a real call-time value. After the loop, `i` equals the number of placeholder values consumed. The relative order is correct because both `j` and `i` move only forward: the leftmost placeholder takes the first call-time value, the next placeholder takes the second, and so on.

**Append values that found no placeholder.** The `while` loop handles the rest of `restArgs`. Each remaining value is pushed onto `args` in its original order. At termination, every call-time value has been used exactly once: the prefix of `restArgs` filled placeholders and the suffix was appended. No fixed non-placeholder entry was moved.

These two loops establish correctness. Every position originating as an ordinary argument is preserved. Every placeholder is replaced exactly once by the next unused rest value. Every rest value not used for a placeholder appears exactly once at the end. Those are precisely the three rules in the required partial-application transformation.

**Call the original function with the wrapper's receiver.** The last statement uses `fn.apply(this, args)`. `apply` passes the array elements as individual positional arguments, rather than passing `args` itself as one argument. It also forwards the wrapper's dynamic `this` to `fn`. Thus, if the partial function is installed as an object method and called through that object, a receiver-sensitive `fn` observes the same object.

An arrow function would not be appropriate for the returned wrapper because arrows do not receive their own dynamic `this`. The ordinary returned function is what makes this receiver forwarding possible.

**A crucial stateful detail in the exact implementation.** The wrapper modifies the captured `args` array in place. Filling a placeholder destroys the underscore at that position, and pushing unused values permanently lengthens the same array. This is harmless for a single invocation, which is the usage exercised by the stated challenge. It is not a reusable, purely functional partial application.

If the example wrapper above is called a second time, the original underscore positions are no longer visible. The scan finds no placeholders, so all new call-time arguments are appended after the arguments produced by the first call. The second result is based on accumulated state rather than a fresh merge with the original template. The source must be explained honestly: it satisfies the one-shot contract but has this material limitation if callers reuse the returned function.

Mutation is also visible to code that retained the original `args` array passed into `partial`. After invocation, that caller will see the replacements and appended values. A defensive implementation would clone the template inside each wrapper call, but the exact solution does not.

## Complexity detail

Let $a$ be the length of `args` at the start of the first wrapper invocation and let $r$ be the number of call-time arguments. The `for` loop examines $a$ positions. The `while` loop appends at most $r$ values, and together placeholder replacement plus appending consumes exactly $r$ rest values under the contract. The merge work is therefore $O(a + r)$ time. Calling `fn` may perform arbitrary additional work; that cost belongs to the supplied function and is normally excluded from the wrapper's own complexity.

The rest parameter creates a `restArgs` array containing $r$ values, so the invocation uses $O(r)$ call-specific space. The captured `args` array already contains $a$ entries and may grow by up to $r$ entries. Since the implementation mutates that existing array, its newly retained growth is $O(r)$ on the first call. Describing the completed argument representation as $O(a + r)$ space is also reasonable; the wrapper's auxiliary storage beyond those arrays is only the two integer indices.

On later calls, let $A$ be the captured array's current, possibly enlarged length. The scan takes $O(A)$ even though no original placeholders may remain, and new arguments can enlarge it again. Repeated use can therefore make both running time and retained memory grow across invocations. The manifest's linear bound accurately describes one merge, but it should not be interpreted as stateless behavior.

## Alternatives and edge cases

- **Fresh array on every call:** Map over the original template into a new argument list and then append leftovers. This avoids mutating caller-owned data and makes the returned partial safely reusable, at the cost of allocating $O(a + r)$ fresh space per invocation.
- **Single output pass:** Build a new result array while scanning `args`, selecting either the fixed value or the next rest value. This makes the correctness rule especially explicit and has the same asymptotic bounds.
- **Bind-based approaches:** `Function.prototype.bind` can pre-fill a prefix of arguments, but it does not natively understand placeholders in arbitrary positions, so additional merging logic is still required.
- **No placeholders:** The scan changes nothing, and every call-time argument is appended. On the first invocation this behaves like fixing a prefix of arguments.
- **Every position is a placeholder:** The first $a$ call-time arguments replace the template, and any further arguments are appended. The final ordering is exactly the original call ordering.
- **Exact underscore matching:** Only `"_"` is special. Values such as `"__"`, an object whose string form is underscore, or an omitted value are ordinary arguments.
- **Extra call-time arguments:** The contract deliberately allows them; the `while` loop preserves all of them rather than discarding them.
- **Too few call-time arguments outside the contract:** A placeholder could receive `undefined` because `restArgs[i]` would be out of range. The stated placeholder-count guarantee prevents this case.
- **Repeated invocation:** The captured template has already been overwritten and extended, so later calls do not repeat the advertised transformation independently. Use a fresh-copy implementation when reusable partial functions are required.
- **Receiver forwarding:** Calling the wrapper as `obj.wrapper(...)` sends `obj` to `fn`. Calling it as a plain function supplies the ordinary strict- or non-strict-mode receiver dictated by the environment.
- **Exceptions from `fn`:** The merge has already mutated `args` before `fn` is invoked. If `fn` throws, the mutation is not rolled back.
