## General

**Use JavaScript's actual inheritance mechanism**

JavaScript inheritance is based on prototype links. An object has access to methods placed on a constructor's `prototype` when that exact prototype object occurs somewhere in the object's prototype chain.

Therefore, checking whether `obj` is an instance of `classFunction` reduces to:

1. obtain the prototype chain appropriate for `obj`;
2. obtain `classFunction.prototype` as the target;
3. walk upward until the target is found or the chain ends.

This directly implements the problem's definition in terms of access to class methods and naturally handles subclasses.

**Reject invalid inputs before reflection**

The first condition is:

`obj == null || typeof classFunction !== "function"`.

The intentionally loose comparison `obj == null` is true for both `null` and `undefined` and false for ordinary values. Neither null nor undefined can be boxed into an object that exposes a useful class prototype for this contract, so the function returns false.

The second check ensures the proposed class is callable as a JavaScript function or class value. Without it, accessing its prototype as a class target would not represent a meaningful instance relationship. Inputs such as numbers, strings, objects, or undefined in the class position return false instead of causing misleading behavior.

**Box primitive values**

Ordinary `instanceof` reports `5 instanceof Number` as false because five is a primitive rather than a `Number` object. The problem deliberately wants true because JavaScript lets the primitive access `Number.prototype` methods through temporary boxing.

`Object(obj)` performs this boxing:

- a number becomes a temporary Number wrapper;
- a string becomes a String wrapper;
- a Boolean becomes a Boolean wrapper;
- a symbol or bigint receives its corresponding wrapper;
- an existing object is returned as an object.

Then `Object.getPrototypeOf(Object(obj))` obtains the first prototype in the relevant chain. For numeric five, that first prototype is `Number.prototype`, so the requested relationship can be found.

The code handles null and undefined before `Object(obj)` because their special coercion behavior should not be interpreted as boxing them into valid instances.

**Walk one prototype link at a time**

`target` is set to `classFunction.prototype`. The loop compares the current `prototype` by identity:

`prototype === target`.

Identity is the correct test. Two prototype objects may contain similar methods while representing unrelated constructors; only the actual target object in the chain establishes inheritance.

If the current link is not the target, `Object.getPrototypeOf(prototype)` moves one level upward. Every normal chain eventually reaches `null`, which means there is no further inherited object. The function then returns false.

**Why subclasses work**

Suppose `Dog extends Animal` and `obj` is created by `new Dog()`. The chain begins:

$$
\texttt{Dog.prototype}
\to
\texttt{Animal.prototype}
\to
\texttt{Object.prototype}
\to
\texttt{null}.
$$

When the target is `Animal.prototype`, the first comparison fails at `Dog.prototype`, but the next step succeeds. The object is correctly recognized as an instance of both its direct class and its superclass.

This also shows why comparing only the immediate prototype would be insufficient.

**Why a constructor is not automatically its own instance**

For `checkIfInstanceOf(Date, Date)`, `obj` is the Date constructor function itself. Functions are objects whose prototype chain normally begins at `Function.prototype`, not at their own instance prototype.

The target is `Date.prototype`. Walking from the Date function reaches `Function.prototype` and then `Object.prototype`, never `Date.prototype`. The result is false, matching the example.

The fact that a function owns a property named `prototype` does not mean that prototype is in the function object's own chain. It is the prototype assigned to objects constructed by that function.

**Why prototype membership matches method access**

When JavaScript evaluates a missing property on `obj`, it checks the object and then repeatedly follows these same prototype links. If `classFunction.prototype` lies in the chain, methods defined there are visible unless shadowed by an own property. Shadowing changes which value a property lookup returns but does not remove the inheritance relationship.

The algorithm therefore checks structural access, not whether one particular method name happens to exist.

**Primitive and object examples**

For primitive `5` and constructor `Number`:

- `Object(5)` creates a Number wrapper;
- its prototype is `Number.prototype`;
- the first comparison succeeds.

For `"hello"` and `String`, the same steps succeed through `String.prototype`.

For a plain object and `Array`, the chain reaches `Object.prototype` without ever finding `Array.prototype`, so the result is false.

For an object created with `Object.create(null)`, the immediate prototype is null. The loop performs no comparisons and safely returns false for ordinary class targets.

**Why no recursion or allocation is needed**

Only one current prototype reference is maintained. Each step replaces it with its parent. The temporary wrapper for a primitive is created by the language, but no collection proportional to chain height is stored.

The chain cannot cycle under normal JavaScript prototype rules, so the walk terminates.

## Complexity detail

Let $h$ be the number of prototype links from the boxed object to null. The loop examines at most $h$ prototypes, so time complexity is $O(h)$.

The function stores only `prototype` and `target` plus fixed input references. It does not materialize the chain, so auxiliary space is $O(1)$.

In typical built-in and user-defined hierarchies, $h$ is small, but the asymptotic bound accurately describes arbitrarily deep inheritance.

## Alternatives and edge cases

- **Native `instanceof`:** Concise for objects, but it rejects primitives such as five against `Number` and therefore does not meet this contract.
- **Compare `constructor` properties:** A constructor property can be overwritten or inherited and does not reliably prove prototype-chain membership.
- **Recursive prototype walk:** Correct but uses $O(h)$ call-stack space without improving clarity.
- **`null` and `undefined` object input:** Both return false before boxing.
- **Non-function class input:** It returns false rather than attempting an invalid class relationship.
- **Primitive number, string, or Boolean:** `Object(obj)` exposes the wrapper prototype required by the problem.
- **Subclass instance:** Walking the complete chain finds superclass prototypes.
- **Constructor passed as object:** A constructor function follows `Function.prototype`, not its own instance prototype.
- **Null-prototype object:** Its chain ends immediately and returns false.
- **Prototype identity:** Structurally similar prototype objects are not interchangeable; strict identity is required.
