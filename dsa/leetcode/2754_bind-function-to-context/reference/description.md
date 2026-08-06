## Description

Extend every JavaScript function with a method named `bindPolyfill`. Calling that method with one non-null object `obj` must return a new function whose later invocations always execute the original target with `obj` as its `this` context.

The returned function receives between zero and 100 arguments. Forward every argument in its original order and return the target function's result without alteration. Reads and writes through `this` must affect the supplied object itself.

Do not use the built-in `Function.bind`. A basic solution may use another invocation helper, while the follow-up asks for a solution that does not use built-in context-binding methods.
