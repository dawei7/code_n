## General

**Capture the original function**

`bindPolyfill` is called as a method of the function being bound. Inside that method, `this` is the target function.

The code saves it in `const target = this`. The returned regular function closes over both `target` and the supplied context object `obj`, so they remain available whenever the bound function is invoked later.

**Why ordinary method invocation sets this**

JavaScript determines a regular function's `this` from its call site. Calling:

`obj[key](...args)`

as a property of `obj` makes `obj` the receiver and therefore the `this` value inside that function.

The solution temporarily installs `target` as such a property, invokes it as a method, and then removes the property.

**Use a fresh Symbol key**

Every invocation creates `const key = Symbol()`. A Symbol is guaranteed unique, even if another symbol has the same description.

Using a normal string such as `"temp"` could overwrite an existing user property. A fresh symbol cannot collide with any existing string or symbol key unless that exact symbol reference was already used, which is impossible before creation.

Creating the symbol inside the returned function also makes simultaneous or nested calls use independent keys.

**Install and invoke**

`obj[key] = target` attaches the original function to the context object. Then:

`obj[key](...args)`

forwards every invocation argument in order and calls the target with `this === obj`.

The target's return value is returned unchanged. If it returns a number, object, promise, or any other value, the bound wrapper passes that value to its caller.

**Always remove the temporary property**

The invocation is inside `try` and cleanup is in `finally`:

`delete obj[key]`.

A `finally` block runs whether the target returns normally or throws. This prevents the temporary symbol property from leaking onto `obj` after either outcome.

If the target throws, the wrapper does not swallow or replace the exception. Cleanup runs, then the original exception continues to the caller.

This exact source improves on a simpler symbol polyfill that installs one permanent property when binding.

**Trace the multiplier example**

Calling `f.bindPolyfill({x: 10})` captures `f` and the object but does not call `f`.

Calling the returned wrapper with five creates a symbol, installs `f` under that symbol, and invokes `obj[key](5)`. Inside `f`, `this.x` is ten, so it returns fifty. The symbol property is deleted before the wrapper returns fifty.

**Why the returned function is regular**

The wrapper is declared with `function(...args)`, but it never relies on its own dynamic `this`. It always invokes the captured target through the captured `obj`. Calling the wrapper as a method of some other object cannot change the bound context.

This implements the core fixed-context behavior requested.

**Contract limitations compared with native bind**

Native `Function.prototype.bind` supports partial arguments and special constructor behavior with `new`. This task asks only for binding one non-null object and forwarding later arguments. The polyfill does not attempt full native constructor semantics.

It also assumes `obj` can accept and delete a temporary property. A frozen, sealed, or non-extensible object could reject assignment, but a normal object produced from the problem's JSON-style input is extensible.

**Reentrancy**

If the target indirectly calls the same bound function again before the outer invocation returns, the inner call creates a different Symbol property. Its cleanup deletes only its own key. The outer temporary method remains until its own finally block executes.


The closure preserves the exact target and fixed object. On every call, a collision-free symbol property temporarily makes target a method of that object. Method-call semantics bind `this` to `obj`, spread syntax forwards all arguments, and return or throw behavior is preserved. Finally cleanup removes the only temporary mutation. Therefore every wrapper invocation behaves with the requested context.

## Complexity detail

Let $a$ be the number of invocation arguments. Binding itself captures two references and creates one closure in $O(1)$ time and space.

Each invocation creates a rest-parameter array of $a$ arguments and spreads it into the target call, giving $O(a)$ forwarding time and $O(a)$ temporary argument storage. Symbol creation, property assignment, lookup, and deletion are expected $O(1)$.

The target function's own runtime and returned data are excluded. These bounds match the manifest's $O(a)$ time and space.

## Alternatives and edge cases

- **Function.call:** `target.call(obj, ...args)` is simpler if built-in context-setting methods are allowed.
- **Function.apply:** Naturally accepts the collected argument array but is likewise a built-in helper.
- **Permanent Symbol property:** Sets context correctly but leaves an unnecessary mutation on `obj`.
- **Normal string key:** Risks overwriting user data.
- **No arguments:** The rest array is empty and the target is called with only its bound context.
- **Many arguments:** Spread preserves their order exactly.
- **Target throws:** `finally` deletes the temporary key, then the exception propagates.
- **Target returns a promise:** The promise is returned; deleting the property does not change the already established call context.
- **Nested invocation:** Fresh symbols prevent key collisions.
- **Frozen object:** Temporary assignment may fail; such objects are outside the normal extensible-object assumption.
