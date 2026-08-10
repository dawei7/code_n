## General

**Create one promise that represents the whole group**

Each input element is a function rather than an already-created promise. To run the operations in parallel, the solution must invoke every function without waiting for an earlier result. It also needs one returned promise whose eventual state summarizes the group.

The code returns `new Promise((resolve, reject) => { ... })`. The executor runs synchronously, setting up all of the asynchronous work before `promiseAll` returns.

**Start every function immediately**

`functions.forEach((fn, index) => { ... })` walks through the array. For each function, `fn()` is called immediately, and handlers are attached to its returned promise.

There is no `await` inside this loop and no chain from one input promise to the next. Invocation of function at index one does not wait for index zero to fulfill. By the end of the synchronous loop, every input operation has been started. Their asynchronous portions can then make progress concurrently according to the JavaScript runtime.

“Parallel” here describes overlapping asynchronous lifetimes, not necessarily simultaneous JavaScript execution on several CPU cores. JavaScript callbacks still run through the host's event loop, but timers, network work, and other promise-producing operations are all initiated without artificial serialization.

**Reserve result positions before anything finishes**

The array `results` is created with the same length as `functions`. A fulfillment handler stores each value at its original `index`:

`results[index] = value`.

This is crucial because completion order can differ from input order. If the third promise fulfills first, its value belongs at index two, not at the beginning of the result. Appending values as they arrive would produce completion order and violate the contract.

Sparse slots in the initially allocated array are filled as promises fulfill. The aggregate promise is resolved only after every slot has received its value.

**Count successful completions**

`completed` starts at zero. Every fulfillment handler increments it exactly once. When it becomes equal to `functions.length`, all input promises have fulfilled, so `resolve(results)` settles the returned promise with the fully populated array.

No earlier fulfillment may resolve the aggregate because at least one result would still be unknown. Conversely, when the count reaches the array length, there can be no missing promise: each input promise has one fulfillment handler, and a promise settles only once.

**Reject as soon as an input rejects**

Each chain ends with `.catch(reject)`. Passing the outer `reject` function directly means that an input rejection attempts to reject the aggregate promise with exactly the same reason.

A JavaScript promise is immutable after settlement. Therefore, whichever rejection handler runs first determines the aggregate rejection. Later fulfillments may still write their array positions, and later rejections may call `reject` again, but those attempts cannot change the already rejected outer promise.

The solution does not cancel the remaining asynchronous operations; ordinary promises do not provide universal cancellation. “Fail fast” means the returned promise rejects promptly, not that all underlying work stops.

**Trace out-of-order fulfillment**

Suppose three functions resolve after 50, 150, and 100 milliseconds with values 4, 10, and 16.

At roughly 50 milliseconds, index zero stores four and `completed` becomes one. At roughly 100 milliseconds, index two stores sixteen and `completed` becomes two. Nothing resolves yet because one task remains. At roughly 150 milliseconds, index one stores ten and the count becomes three, so the aggregate resolves with `[4, 10, 16]`.

The array order follows function indices even though the completion order was zero, two, one.

**Trace a rejection**

If one promise is scheduled to resolve after 200 milliseconds and another rejects after 100 milliseconds, both are started during the initial loop. At about 100 milliseconds, the rejection handler calls the outer `reject`. The returned promise rejects with that reason immediately. The first operation may still finish later, but its fulfillment cannot reverse the rejection.

**Synchronous exceptions**

The call `fn()` occurs inside the executor passed to the outer `Promise` constructor. If an input function unexpectedly throws before returning a promise, the constructor converts that uncaught executor exception into rejection of the outer promise. The loop stops at that throw, so later functions would not start. The stated contract says the functions return promises, so the intended path attaches handlers to all of them.

**Why the construction is correct**

Every function is invoked in the same synchronous pass, establishing concurrent execution. For every fulfillment, its value is stored at the matching input index. The outer promise fulfills only after the number of successful settlements equals the number of inputs, so its result is complete and correctly ordered. Any rejection is forwarded to the outer reject function, and promise settlement rules preserve the first rejection that reaches it. These are exactly the required success and failure behaviors.

## Complexity detail

Let $n$ be the number of functions. The aggregation layer invokes each function once, attaches handlers once, and processes one settlement callback per input, for $O(n)$ bookkeeping time excluding work performed inside the supplied functions.

The `results` array contains $n$ entries, and the attached closures retain an index and handler state for each promise, so auxiliary aggregation space is $O(n)$. The returned result itself also has $n$ values.

Wall-clock completion time is not the sum of all durations. When all fulfill, it is governed by the last input promise to fulfill, plus scheduling overhead. On rejection, it is governed by the first rejection observed. Asymptotic $O(n)$ describes the solution's management work, not elapsed timer duration or the internal complexity of user functions.

## Alternatives and edge cases

- **Built-in `Promise.all`:** Has the desired semantics but is explicitly forbidden by the problem.
- **Sequential `await` loop:** Preserves order easily but delays invocation of later functions, violating the required parallel start.
- **Append values on fulfillment:** Produces completion order rather than input order and is therefore incorrect.
- **Use `Promise.allSettled`:** Waits for every rejection and fulfillment and returns status objects, which does not match fail-fast behavior.
- **One function:** Its fulfillment becomes a one-element result, and its rejection is forwarded directly.
- **Out-of-order completion:** Indexed assignment keeps the output in input order.
- **Multiple rejections:** The first rejection handler to settle the outer promise determines its reason; later attempts are ignored.
- **Work after rejection:** Already-started operations continue unless they implement their own cancellation mechanism.
- **Empty array:** The constraints require at least one function. This exact code would leave the returned promise pending forever for an empty array because `completed === functions.length` is never checked before the loop.
- **Synchronous throw:** The outer Promise constructor rejects, although later functions after the throwing call are not invoked.
