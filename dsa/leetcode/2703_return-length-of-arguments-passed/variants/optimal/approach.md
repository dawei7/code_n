## General

**Count calls, not values inside a container**

The requested result is the number of arguments supplied in one function invocation.

For `argumentsLength({}, null, "3")`, three separate expressions occur between the call parentheses, so the answer is three.

This is different from accepting one array and returning that array's length. A call `argumentsLength([1, 2, 3])` supplies one argument, even though that argument contains three elements.

**Use a rest parameter to capture every argument**

The function signature is `function(...args)`.

JavaScript rest syntax gathers all positional arguments supplied after the function name into a real array:

- zero supplied arguments create `[]`;
- one supplied value creates a one-element array;
- several supplied values preserve their order in a longer array.

The name `args` is local to this invocation.

**Array length stores exactly the desired count**

JavaScript arrays maintain a `length` property equal to one more than their greatest present index. A rest array is densely created with one element for every supplied argument.

Therefore `args.length` is exactly the call's arity at runtime.

No loop, type test, serialization, or inspection of argument contents is needed.

**Null still counts**

`null` is a value and occupies one argument position.

The function does not use truthiness, so it never confuses null, false, zero, or an empty string with absence. Each supplied position contributes one regardless of its value.

This is why counting truthy elements would be incorrect.

**Objects and arrays each count once**

An object argument can contain any number of keys, and an array argument can contain any number of elements. Both are still one value in the outer call.

The rest array stores a reference to that object or array in one slot. `length` counts the slot rather than recursively examining the value.

**Trace zero arguments**

Calling `argumentsLength()` gives the rest parameter no values.

`args` is an empty array and `args.length` is zero. This satisfies the allowed lower bound without a special condition.

**Trace mixed arguments**

For `argumentsLength({}, null, "3")`:

- `args[0]` is the object reference;
- `args[1]` is null;
- `args[2]` is the string.

The array length is three, which is returned directly.

The order is preserved even though order is irrelevant to the count.

**Arguments are evaluated before the function**

As with every JavaScript call, argument expressions are evaluated before `argumentsLength` begins.

The function counts resulting values, not source-code tokens. A spread at the call site can contribute several arguments, while an expression that returns an array still contributes one unless that array is spread.

For example, `argumentsLength(...[1, 2])` receives two arguments, whereas `argumentsLength([1, 2])` receives one.

**The return value is an ordinary number**

`args.length` is a nonnegative integer. With the challenge bound of at most 100 arguments, it is exactly representable as a JavaScript Number.

The result does not depend on argument types, values, equality, or mutability.

**Rest syntax versus the legacy `arguments` object**

A non-arrow function also has an array-like `arguments` object whose `length` could be returned.

The exact source chooses a rest parameter. A rest value is a true array, has clearer syntax, and works naturally with modern JavaScript.

For this method, only its length is used.

**Why the body is already complete**

The JavaScript runtime has already performed all bookkeeping necessary to know how many values were passed.

Recounting with a loop would merely rediscover `args.length` and introduce more code paths. Returning the stored metadata is both simpler and less error-prone.


Rest-parameter semantics create one array element for each positional argument supplied to the invocation and no elements for omitted positions beyond the call's actual argument list.

The array's length is therefore equal to the number of supplied arguments. Returning that property gives the required result for every permitted call.

**Bounded versus general complexity**

The manifest states constant time and space under the explicit constraint that at most 100 JSON arguments are supplied.

At the language-mechanics level, constructing a rest array with $a$ references requires $O(a)$ time and space before the constant-time `length` access. Both descriptions are useful when their model is stated.

## Complexity detail

Reading `args.length` and returning it take $O(1)$ time. Under the challenge's fixed maximum of 100 arguments, total call overhead is treated as $O(1)$ and stored rest space as $O(1)$.

In an unbounded parameterized model, materializing the rest array costs $O(a)$ time and $O(a)$ space for $a$ supplied arguments. The function creates no other growing structure.

## Alternatives and edge cases

- **Return `arguments.length`:** Avoids naming a rest array and reports the same count in a normal function.
- **Loop over `args`:** Correct but unnecessary because the array already stores its length.
- **Count truthy values:** Incorrect because falsy supplied values still count.
- **No arguments:** Returns zero.
- **One array argument:** Returns one, not the array's internal length.
- **Spread call-site array:** Counts each spread element as a separate argument.
- **Null:** Counts as one supplied value.
- **False, zero, and empty string:** Each counts normally.
- **Object argument:** Its number of keys is irrelevant.
- **Repeated references:** Every supplied position counts even if several positions reference the same object.
- **Return type:** Always a nonnegative integer Number.
