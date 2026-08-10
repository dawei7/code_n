## General

**Influence JavaScript coercion rather than overloading `+`**

JavaScript does not let a class directly redefine the addition operator. It does let an object control how it converts to a primitive value.

When `+` receives object operands in this numeric situation, JavaScript asks each object for a primitive. A custom `valueOf` method can return the numeric meaning of an `ArrayWrapper`.

Likewise, `String(wrapper)` can use a custom `toString` method to obtain the required bracketed representation.

**Store the array and precompute its sum**

The constructor saves the supplied array reference as `this.nums`.

It also computes:

`this.sum = nums.reduce((total, value) => total + value, 0)`.

The initial value zero is important. It gives an empty array a sum of zero and makes `reduce` safe when there are no elements.

Computing once means future numeric coercions do not rescan the array.

**How `valueOf` drives addition**

`ArrayWrapper.prototype.valueOf` simply returns `this.sum`, which is already a primitive number.

For `obj1 + obj2`, JavaScript converts each wrapper. Their `valueOf` methods return the sums of their arrays, and the ordinary `+` operator then adds those two numbers.

If the arrays are `[1, 2]` and `[3, 4]`, coercion produces 3 and 7, so the final result is 10.

The operator itself has not changed; only the primitive meaning of each operand has been customized.

**Why a primitive return matters**

Object-to-primitive conversion needs `valueOf` or `toString` to produce a primitive.

Returning the array itself from `valueOf` would still be an object, causing JavaScript to try another conversion path and potentially concatenate strings instead of performing numeric addition.

Returning the precomputed number makes numeric intent unambiguous for the required operation.

**How `String` chooses the textual form**

`ArrayWrapper.prototype.toString` returns the equivalent of `"[" + this.nums.join(",") + "]"`.

`join(",")` converts each integer to text and places one comma between neighboring values. The surrounding concatenation supplies the opening and closing square brackets.

No spaces are inserted, matching examples such as `"[23,98,42,70]"`.

**Trace an empty array**

The constructor's reduction begins at zero and has no elements to process, so `sum` remains zero.

`valueOf` therefore makes an empty wrapper numerically equal to zero. Adding two empty wrappers yields zero.

For text, `[].join(",")` is the empty string. Surrounding it with brackets yields `"[]"`.

Both required behaviors emerge without special branches.

**Why the sum is precomputed**

The editorial's basic design may calculate the sum inside every `valueOf` call. The exact source moves that work into the constructor.

If one wrapper participates in many additions, construction pays one $O(n)$ scan and every later numeric conversion is $O(1)$.

This is worthwhile because the stored integers are treated as the wrapper's stable content under the challenge interface.

**The prototype holds shared behavior**

`valueOf` and `toString` are assigned to `ArrayWrapper.prototype` rather than recreated as own functions in each constructor call.

Every instance shares the same method objects, while `this.nums` and `this.sum` select that instance's data.

This saves per-instance method allocations and follows JavaScript's prototype-based class pattern.

**Addition of more than two wrappers**

Although examples show two objects, chained addition behaves naturally.

For `obj1 + obj2 + obj3`, the first two wrappers convert to numbers and produce a numeric subtotal. Adding the third converts it through `valueOf` and adds its sum.

Associativity of ordinary number addition gives the total of all contained elements, subject to standard JavaScript number semantics.

**The stored array reference and mutation caveat**

The constructor stores `nums` by reference rather than copying it. `toString` reads that array at the moment it is called, while `valueOf` returns the sum computed at construction.

If outside code later mutates `nums`, the string could reflect new elements while the numeric sum remains old. The challenge treats the supplied array as the wrapper's stable input, so the exact implementation is consistent in the intended use.

A general-purpose mutable wrapper would either copy the input or recompute or update the sum.


At construction, reduction adds every input integer exactly once starting from zero, so `this.sum` equals the mathematical array sum.

Numeric coercion returns exactly that sum for each wrapper. Adding two wrappers therefore adds all elements from both arrays.

String coercion joins every stored integer in order with commas and adds exactly one surrounding bracket pair, producing the required format. These two methods establish both requested features.

**Why this is optimal for repeated numeric use**

Reading all $n$ values once is necessary to know their sum. The constructor performs that unavoidable work.

Afterward, no numeric coercion can asymptotically beat the constant-time field return. String conversion must still inspect all values because the output itself contains them.

## Complexity detail

For an array of length $n$, construction takes $O(n)$ time to reduce all values. `valueOf` takes $O(1)$ time. `toString` takes $O(n)$ time plus the time proportional to the characters written in the returned string.

The constructor stores one array reference and one number, so auxiliary space is $O(1)$ beyond the supplied input. String conversion necessarily allocates its $O(n)$-scale output text; output space is normally excluded from the manifest's auxiliary-space bound.

## Alternatives and edge cases

- **Compute the sum inside `valueOf`:** Simpler state, but every addition rescans the array in $O(n)$ time.
- **Use `Symbol.toPrimitive`:** Can inspect the coercion hint and handle numeric and string cases in one hook, but two familiar methods are sufficient.
- **Use `JSON.stringify` for text:** Produces suitable integer-array syntax but does more general serialization work than `join`.
- **Empty array:** Numeric value is zero and string value is `"[]"`.
- **Single element:** Coerces to that element and formats with no comma.
- **Many elements:** `join` preserves their original order.
- **Repeated addition:** Reuses the precomputed sum in constant time.
- **No spaces:** The comma separator is exactly `","`.
- **External array mutation:** Can make cached sum and live string diverge; intended inputs are stable after construction.
- **Nonnegative integers:** Match the stated constraints, though the arithmetic also handles ordinary negative numbers.
- **Shared prototype methods:** Avoid allocating method functions per wrapper instance.
- **Standard number limits:** Extremely large accumulated sums would follow JavaScript's Number precision rules, but the challenge bounds remain safe.
