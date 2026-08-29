## General

**Wrap access rather than cloning the JSON value**

The function returns a Proxy around the supplied object or array. The proxy forwards reads but intercepts mutation attempts and throws the exact required string.

Nested objects are wrapped lazily when accessed. This provides deep protection without traversing the entire JSON structure at creation time.

The underlying value remains the proxy's target; the solution does not deep-clone or eagerly freeze it.

**Recognize values that need wrapping**

Helper `wrap(value)` returns `null` and primitive values directly.

Only non-null objects can contain writable JSON properties. Arrays also satisfy `typeof value === "object"`, so both objects and arrays enter the proxy path.

Functions obtained from normal property reads are not wrapped by this helper because their type is `"function"`. Mutating array methods are handled specially before that general read.

**Cache one proxy per target**

`proxies` is a `WeakMap` from an underlying object or array to the proxy already created for it.

Before creating a proxy, `wrap` checks this map. Reusing a cached proxy has two benefits:

- repeated access to the same nested value returns stable proxy identity;
- shared references do not create an unbounded series of wrappers.

JSON input has no cycles, but the same mechanism would also prevent recursive wrapping from duplicating proxy identity for repeated references. Weak keys do not by themselves keep discarded targets alive.

**Intercept direct assignment**

The proxy handler's `set` trap runs for syntax such as `obj.x = 5` or `arr[1] = value`.

It immediately throws the string returned by `modificationError`. The attempted value is never written to the target.

For an array target, the message is `Error Modifying Index: ${property}`. For an object target, it is `Error Modifying: ${property}`.

Even assigning the same value is still an attempt to modify and therefore throws.

**Protect nested values through the get trap**

For an ordinary property read, the handler uses `Reflect.get(target, property, receiver)` to perform standard JavaScript lookup semantics.

It then passes the result through `wrap`. A primitive comes back unchanged, while a nested object or array becomes its cached immutable proxy.

Therefore reading `proxy.user.settings` creates protection one level at a time, and a later assignment to `settings.theme` reaches the nested proxy's set trap.

**Block the specified mutating array methods**

The problem lists seven array methods that can mutate:

`pop`, `push`, `shift`, `unshift`, `splice`, `sort`, and `reverse`.

When the target is an array and the requested property belongs to this set, the `get` trap returns a replacement function. Calling it throws:

`Error Calling Method: ${property}`.

The original method is never invoked, so it cannot alter the array. The error is associated with method use rather than a lower-level index or length assignment, matching the required message category.

**Why method interception happens before `Reflect.get`**

Native methods such as `push` normally mutate through internal assignments to indices and `length`. Letting `push` run and merely relying on `set` would throw an index-style error.

The contract instead requires `Error Calling Method: push`. Detecting the property lookup and substituting a thrower produces the correct higher-level error.

**Also reject deletion and property definition**

The exact solution defines `deleteProperty` and `defineProperty` traps in addition to `set`.

They use the same object-versus-array modification message. These traps prevent alternate mutation syntax such as `delete proxy.x` or `Object.defineProperty(proxy, "x", ...)` from bypassing ordinary assignment protection.

This is stronger than the main examples while remaining consistent with immutability.

**A thrown string is intentional**

The problem explicitly requires a string literal, not an `Error` object.

The traps execute `throw modificationError(...)` or directly throw the method string. A surrounding validator can therefore receive exactly the specified text rather than a stack-bearing error instance with a different representation.

**Read-only operations continue to work**

Primitive property reads are returned normally. Operations such as `Object.keys` use default proxy behavior because no `ownKeys` trap changes enumeration.

Non-mutating array methods are not in `mutatingMethods` and are read normally. When they inspect array elements through the proxy, nested objects returned by indexed reads are still wrapped.

The contract identifies the complete set of mutating methods that must be blocked.


Any direct property write, deletion, or definition on the root or an accessed nested container encounters a proxy trap that throws before modifying its target.

Any listed mutating array method lookup yields a replacement that throws before the native method executes. Every nested object read is recursively wrapped, so depth does not open an unprotected path.

Thus no permitted mutation attempt through the returned structure can alter it, and every attempt produces the required category-specific string.

**Scope of the protection**

The returned proxy prevents mutation through that proxy graph. Because the exact function does not clone or freeze the original target, separate code that still holds the original `obj` reference could mutate it directly.

The challenge evaluates the immutable version's interface; this distinction is important when applying the pattern in a broader system.

## Complexity detail

Creating the top-level proxy is $O(1)$. Each ordinary property access, cache lookup, or intercepted operation takes expected $O(1)$ time, excluding whatever read-only method the caller deliberately executes.

If $p$ distinct object or array targets are actually accessed, the WeakMap and their proxies use $O(p)$ space. Laziness avoids space proportional to untouched parts of the input. Primitive reads use no new persistent wrapper.

## Alternatives and edge cases

- **`Object.freeze` only at the root:** Shallow freezing leaves nested objects mutable and does not provide the required custom strings.
- **Recursive deep freeze:** Can protect all descendants eagerly but costs a full traversal and still does not naturally classify errors.
- **Deep clone then freeze:** Uses more time and space and changes identity relationships unnecessarily.
- **Assignment to the same value:** Still throws because an attempted modification occurred.
- **Nested assignment:** The get trap supplies a nested proxy, whose set trap throws.
- **Array index assignment:** Uses the index-specific message.
- **Array `length` assignment:** The array target produces an index-category message with property `length`.
- **Listed mutating method:** The replacement function throws the method-category message before mutation.
- **Null value:** Returned directly and cannot expose deeper properties.
- **Repeated nested access:** WeakMap returns the same proxy.
- **Deletion and definition:** Explicit traps prevent these alternate writes.
- **Original external alias:** Direct mutation through the unwrapped original is not prevented by this proxy-only design.
