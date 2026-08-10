## General

**Capture the actual value in a tiny expectation object**

Calling `expect(val)` returns an object with two methods.

Both methods are closures: they retain access to the original `val` even after `expect` has returned.

The caller then supplies an `expected` value to either `toBe` or `notToBe`. The methods implement opposite assertions over the same captured actual value.

**`toBe` requires strict equality**

The condition is `val !== expected`.

If that inequality is true, the assertion failed and the method throws `new Error("Not Equal")`.

Otherwise strict equality holds and the method returns true.

There is no false return path: a failed assertion throws, while a successful assertion returns true.

**`notToBe` requires strict inequality**

The second method checks `val === expected`.

Equality means the negative assertion failed, so it throws `new Error("Equal")`. If the values differ strictly, it returns true.

Together, the two methods are logical complements with different required failure messages.

**Why strict equality matters**

JavaScript `===` compares without type coercion.

For example:

- `5 === 5` is true;
- `5 === "5"` is false;
- `0 === false` is false;
- `null === undefined` is false.

Using loose equality would incorrectly make some values of different types pass `toBe`.

**Objects compare by identity**

Two separately created objects with identical keys are not strictly equal:

`{} === {}` is false.

The same object reference compared with itself is true. The expectation helper does not perform deep structural comparison because the contract specifically asks for `===`.

Arrays follow the same reference-identity rule.

**Important JavaScript numeric cases**

`NaN === NaN` is false, so `expect(NaN).toBe(NaN)` would throw while `notToBe` would return true.

Positive zero and negative zero compare strictly equal, so `expect(0).toBe(-0)` returns true.

These are consequences of the required operator, not special branches in the implementation.

**Throw an Error object with the exact message**

The source uses `throw new Error("Not Equal")` and `throw new Error("Equal")`.

The thrown value is an Error object whose `message` field contains the required text. Test harnesses typically catch it and report that message.

This differs from throwing the bare string, even though both can display similar text.

**Trace successful `toBe`**

`expect(5)` creates an object whose closures capture number 5.

Calling `.toBe(5)` compares the captured value with the new argument. They are strictly equal, so the throw branch is skipped and true is returned.

**Trace failed `toBe`**

`expect(5).toBe(null)` compares different types and values.

`5 !== null` is true, so the method constructs and throws an Error with message `"Not Equal"`. It never reaches the success return.

**Trace `notToBe`**

`expect(5).notToBe(null)` sees strict equality false. That is exactly the desired condition for a negative assertion, so it returns true.

`expect(5).notToBe(5)` sees equality true and throws message `"Equal"`.

**Each expectation is independent**

Every `expect` call returns a new object and new closures capturing that call's `val`.

One expectation cannot overwrite another's actual value. There is no global state, counter, or mutable shared result.

**Why both methods are created together**

The returned object represents one expectation about one captured actual value. Supplying both operations on that object lets the caller choose a positive or negative assertion without repeating the actual expression. Neither method calls the other, so their error messages remain explicit and cannot be accidentally exchanged. Creating the pair also makes the interface predictable: after `expect(val)`, both named operations are immediately available and each evaluates only the newly supplied expected value.

**Captured objects are references**

If `val` is an object, the closure captures its reference rather than a deep snapshot.

Mutating the object later does not change its identity, so comparison with the same reference still succeeds. Comparing with a newly constructed lookalike still fails.

This is consistent with strict equality semantics.


`toBe` returns true exactly when strict inequality is false, which is exactly when `val === expected`. In every other case it throws the required failure message.

`notToBe` returns true exactly when strict equality is false and throws its required message otherwise.

The closures preserve the original actual value for both comparisons, so the returned object implements the complete requested interface.

## Complexity detail

Creating the expectation object and two closures takes $O(1)$ time and space. Each method performs one strict comparison and either returns or creates one Error, all $O(1)$ under the ordinary fixed-size value/reference model.

No traversal occurs for objects or arrays because comparison is by identity, not content. Each expectation object stores only the captured reference or primitive.

## Alternatives and edge cases

- **Loose equality:** Incorrect because it coerces types such as number 5 and string `"5"`.
- **Deep equality:** Answers a different question for objects and arrays.
- **Return false on failure:** Incorrect because the contract requires throwing.
- **Throw a string:** Produces a different thrown type from the exact `Error` source.
- **Different primitive types:** Strict comparison treats them as unequal.
- **Same object reference:** `toBe` succeeds.
- **Structurally equal different objects:** `toBe` throws because identity differs.
- **`NaN`:** Is not strictly equal to itself.
- **Positive and negative zero:** Are strictly equal.
- **Null and undefined:** Are strictly unequal.
- **Repeated method calls:** Use the same captured actual value and have no internal state changes.
- **Exact messages:** `toBe` uses `Not Equal` and `notToBe` uses `Equal`.
