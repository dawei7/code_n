## General

**Intercept property access instead of defining methods**

An ordinary object can call only methods that exist somewhere on itself or its prototype chain. Defining infinitely many names in advance is impossible.

A JavaScript `Proxy` solves the problem by intercepting the operation that happens before every method call: property access.

`createInfiniteObject` returns a proxy around an empty target object. Its handler defines a `get` trap, so every expression such as `obj.abc123` or `obj["abc123"]` runs custom code.

**The property key is the method name**

The `get` trap receives two relevant arguments:

- `target` is the wrapped empty object;
- `property` is the key the caller requested.

For `obj.abc123`, `property` is string `"abc123"`. Bracket notation supports names that cannot be written with dot syntax, such as punctuation or the empty string.

The target itself is intentionally unused because no finite table of real methods is needed.

**Return a function from every lookup**

A method call has two stages:

1. evaluate the property access to obtain a value;
2. call that value as a function.

The trap must therefore return a callable, not the property string immediately.

It creates:

`function() { return property; }`.

Calling that generated function returns the key captured from the lookup. This closure is what makes each requested name behave like its own method.

**Why closure capture works**

Each invocation of the `get` trap has its own `property` parameter. The returned function retains access to that parameter after the trap finishes.

Thus the function produced for `abc123` keeps `"abc123"`, while a later function produced for `hello` keeps `"hello"`.

There is no shared mutable “last property” variable that could make one method overwrite another's result.

**Trace dot notation**

Evaluating `obj.abc123()` first triggers the trap with property `"abc123"`.

The trap returns a new zero-argument function. The trailing parentheses invoke it, and its only statement returns `property`.

The final result is `"abc123"`.

**Trace an unusual string key**

For method name `".-qw73n|^2It"`, dot notation would not be syntactically valid, but bracket notation is:

`obj[".-qw73n|^2It"]()`.

The proxy receives the exact bracket key as `property`. No parsing, validation, escaping, or normalization occurs, so the returned value is the same string.

An empty string key works for the same reason.

**Arguments and receiver do not matter**

The generated function declares no parameters and does not read `this`. JavaScript still permits callers to supply arguments, but they are ignored.

The method's result depends only on the property name captured at lookup time.

Calling a saved function separately, rather than through the proxy, also returns the same name because the closure does not depend on method receiver binding.

**Every access synthesizes a fresh function**

The implementation does not cache generated methods.

Two evaluations of `obj.x` produce two different function objects by identity, although invoking either returns `"x"`.

The contract cares about call results, not stable method identity. Avoiding a cache keeps persistent state constant.

**Existing-looking names are intercepted too**

The `get` trap does not ask whether a property exists on the empty target or its prototype.

Names such as `toString` or `constructor` are treated just like arbitrary names: lookup returns a closure that returns that key. This uniform interception is what gives the object its “infinite” behavior.

It also means the proxy does not act like a normal empty object for ordinary introspection-oriented property access.

**String keys versus symbol keys**

JavaScript property keys can be strings or symbols. The exact generated function returns `property` without calling `String(property)`.

Under the problem contract, method names are strings, so the return type is the required string. If outside code accesses a symbol property, the closure returns that symbol itself; that behavior is outside the stated string-method interface.


For any permitted method-name string $p$, accessing proxy property $p$ invokes the `get` trap with `property = p`. The trap returns a callable closure whose body returns that captured value.

Invoking the property therefore returns $p$ exactly, independent of arguments or prior accesses. Since the trap runs for every possible property string, the same proof applies to every permitted method name.

**Why a Proxy is the natural tool**

Without interception, one could add methods lazily only after learning their names through some separate API. The required syntax offers no such registration step.

Proxy lookup interception sees the arbitrary name at exactly the moment it is requested and can synthesize behavior on demand.

## Complexity detail

Creating the proxy and handler takes $O(1)$ time and persistent space. Each property access creates one small closure and each invocation returns its captured key, so both are $O(1)$ under the usual property-key model.

Only the proxy and handler remain persistently stored by the returned object. A caller that retains many generated method functions can itself accumulate $O(c)$ closures after $c$ accesses, but the implementation does not cache them. Per ordinary lookup, transient additional space is $O(1)$.

## Alternatives and edge cases

- **Predefine known methods:** Cannot support arbitrary future names and is not truly infinite.
- **Cache one closure per property:** Preserves method identity but grows storage with the number of distinct names.
- **Return the property directly from `get`:** Incorrect because `obj.name()` would try to call a string.
- **Use `Reflect.get` for existing properties:** Would break the uniform rule for names inherited from `Object.prototype`.
- **Empty method name:** Bracket access with `""` returns an empty string.
- **Punctuation and spaces:** Bracket notation passes the exact string key through the proxy.
- **Arguments:** They are accepted by JavaScript and ignored by the generated function.
- **Detached generated function:** Still returns its captured property because it does not use `this`.
- **Repeated lookup:** Produces different function objects with identical returned names.
- **Built-in-looking property:** The trap synthesizes a method rather than exposing inherited behavior.
- **Symbol property:** Exact code returns the symbol, while the challenge contract supplies string method names.
- **Assignments:** No `set` trap is defined; mutation behavior is not part of the requested interface, and lookups remain governed by `get`.
