## Description

Add a custom `forEach` method to `Array.prototype` so that every JavaScript array can invoke `array.forEach(callback, context)`. The method must call `callback` once for every array element in index order and must not return a value.

Each callback invocation receives the current element, its numeric index, and the array itself. It must also run with `this` bound to the supplied `context` object. The callback may use these arguments or its context to mutate the same array. Implement the traversal directly rather than delegating to built-in array iteration methods.
