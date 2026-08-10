## General

**One object exposes three operations on shared private state**

`createCounter(init)` must return an object with methods that all observe and change the same current value.

The solution declares:

`let current = init`

inside the factory and returns three functions that close over both `current` and `init`.

Even after `createCounter` returns, those lexical bindings remain alive because the methods reference them.

**Keep initial and current values conceptually separate**

`init` is the permanent reset target. `current` is the mutable state after operations.

Increment and decrement change only `current`. Reset assigns `init` back into `current` but never changes `init` itself.

If the implementation mutated the sole initial binding without retaining its original value, reset would no longer know where to return.

**Increment before returning**

The increment method executes:

`current += 1`

then returns `current`.

This matches “increases the current value by one and then returns it.” With initial five, the first increment returns six, not five.

Using postfix `return current++` would return the old value and violate this version of the counter contract.

**Decrement before returning**

Decrement similarly executes:

`current -= 1`

before returning.

The operation applies to the state left by every prior method. After two increments from zero, current is two; decrement changes it to one and returns one.

**Reset is a state transition too**

Reset performs:

`current = init`

and returns the restored value.

Calling reset repeatedly is valid. Every call assigns the same initial value and returns it, even if current was already equal to init.

Reset does not create a new counter object or new closure. The same three methods continue sharing the restored binding.

**Trace the first example**

Create with five:

- initial hidden state is five;
- `increment()` changes current to six and returns six;
- `reset()` changes it back to five and returns five;
- `decrement()` changes it to four and returns four.

The result sequence is `[6,5,4]`.

**All three methods share one binding**

The functions are created in the same lexical environment. They do not each receive a copy of `current`.

When increment writes six, reset and decrement see six on later calls. This shared closure state is the central design requirement.

If each method declared its own local current value, operations would not compose into one counter history.

**Separate counter objects remain independent**

Calling `createCounter(0)` twice creates two lexical environments and two distinct `current` bindings.

Incrementing the first object does not affect the second. The methods may have identical source code, but their closures point to different state.

A global variable would break this independence.

**Private state and encapsulation**

The returned object exposes only functions. It does not expose `current` as a writable property.

Code can change state only through the defined operations. Assigning some unrelated property such as `counter.current = 100` would not alter the captured lexical variable.

This is a simple example of closures providing encapsulation without a class.

**A state invariant**

After any operation sequence, `current` equals:

- `init` if the most recent relevant reset occurred after all later increments/decrements;
- otherwise, that reset or initial value plus number of subsequent increments minus subsequent decrements.

Each method applies exactly its stated transition and returns the resulting state. Induction over calls proves every returned value is correct.

**Why method `this` is unnecessary**

The methods reference lexical variables directly and never read `this`.

They can be detached:

`const inc = counter.increment`

and called as `inc()` without losing access to state. A class method using `this.current` would require preserving its receiver.

**No history array is needed**

The next operation depends only on current value and immutable init, not the full sequence of past calls.

Two numbers summarize all relevant history, so storage stays constant no matter how many operations occur.

**Negative values**

Both initialization and later state may be negative. Ordinary integer addition and subtraction cross zero without special cases.

The bounded call count keeps values small, and JavaScript Number arithmetic is exact for these integers.

## Complexity detail

Creating a counter allocates one result object, three function closures, and two captured numeric bindings, all $O(1)$.

Each method performs at most one assignment and one arithmetic operation, so time is $O(1)$ per call and retained space is $O(1)$.

Across $q$ calls, total time is $O(q)$ without growing state.

## Alternatives and edge cases

- **Class with a field:** Models the same state but exposes or requires receiver-based access unless private fields are used.
- **Object with public `current`:** Simpler but allows external mutation and weaker encapsulation.
- **Postfix increment:** Returns the old value and is wrong for this contract unless rewritten.
- **Repeated reset:** Always returns the original `init`.
- **Increment after reset:** Starts from `init` again.
- **Negative initial value:** Arithmetic behavior remains unchanged.
- **No calls:** The object is created with hidden state but produces no outputs.
- **Detached method:** Still works because it closes over state rather than relying on `this`.
- **Multiple counters:** Each factory call has independent bindings.
- **Shared methods:** Within one object, all three closures reference the same mutable `current`.
