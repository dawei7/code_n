# Guided Example: Array Prototype Last

## 1. The instance and the required outcome

The instance to work through is the array `nums = [null, {}, 3]`, and the required outcome is the number `3`. That looks trivial, and the arithmetic is — but the problem is not asking for a way to read a final element once. It asks for a *capability*: after the enhancement, **any** array must answer a call to a method named `last`, and an array with no elements must answer `-1`.

| aspect of the contract | requirement |
|---|---|
| who gains the capability | every array, not one chosen array |
| name of the capability | `last` |
| result for a non-empty array | its final element, unchanged |
| result for an empty array | the sentinel `-1` |
| assumption about inputs | the array is the output of `JSON.parse`, with $0 \le \text{arr.length} \le 1000$ |

Reading the array as a table of positions makes the whole task concrete:

| position | 0 | 1 | 2 |
|---|---|---|---|
| stored value | `null` | an empty object | `3` |

The final position is the only one that matters, and its index is one less than the length. Two side conditions ride along with that observation: the positions before the end must not influence the result even when they hold falsy values such as `null`, and the empty array has no final position at all, so the sentinel has to come from a length test rather than from a failed read.

## 2. Where the method has to live

An array that can answer `last` has been given access to one more method, and the runtime grants method access by delegation along the prototype chain. Every array delegates to one shared array prototype object, so adding a single method there gives the capability to every existing array, every array created later, and arrays nested inside other values — with no per-instance work.

| entity | role in the delegation | consequence for this problem |
|---|---|---|
| the shared array prototype | holds the method once | one definition serves all arrays |
| an individual array such as `nums` | delegates lookups upward | the call resolves without the array owning the method |
| the receiver of the call | the array the method was invoked on | the method must operate on whichever array calls it, never on a captured one |
| nested array elements | delegates to the same prototype | a nested array can answer the same call |

The receiver point is the one that carries risk. The method is shared, so it cannot use a fixed array captured from the surrounding scope; it must read the current receiver's own length and its own final position. This is precisely why the capability is described as living on the prototype instead of being copied onto instances.

## 3. Turning a length into an index

In a dense array of length $L$, the elements occupy exactly the positions $0, 1, \dots, L-1$, so the final element sits at index

$$
L - 1 .
$$

| length $L$ | valid indices | index of the final element | what the method must answer |
|---|---|---|---|
| 0 | none | none exists | the sentinel `-1` |
| 1 | 0 | 0 | the single element, whatever it is |
| 2 | 0, 1 | 1 | the element at position 1 |
| 3 | 0, 1, 2 | 2 | the element at position 2 |

Two conclusions follow. The index is *derived* from the length rather than fixed, so the method must read the receiver's length on each call — caching a length from an earlier call, or hard-coding an offset, breaks as soon as a different array calls the method. And the empty case cannot be handled by computing an index at all, because $L - 1 = -1$ is not a position of a length-0 array; probing it would yield "no such property" rather than the required sentinel.

## 4. Executing the call on `[null, {}, 3]`

Take the method installed on the shared prototype and traced on the receiver `nums`, whose three elements are `null`, an empty object, and `3`.

| step | action | value observed | decision |
|---|---|---|---|
| 1 | receive the call on `nums` | the receiver is the three-element array | operate on this array |
| 2 | read the receiver's length | $L = 3$ | the length is not zero |
| 3 | apply the empty test | $L = 0$ is false | do not return the sentinel |
| 4 | compute the final index | $L - 1 = 2$ | position 2 is the target |
| 5 | read the value at position 2 | `3` | answer `3` |

Positions 0 and 1 — the falsy `null` and the empty object — are never inspected, and this is the point of the instance: the decision depends only on the length and on the single stored value at the final position. The answer is the element itself, not a copy, a wrapper, or a formatted rendering of it. The method also returns rather than stores, so calling it does not modify the array, and calling it repeatedly on an unchanged array gives the same answer.

## 5. Invariant and correctness

Let the receiver be an array of length $L$ whose final element, when it exists, is $x$.

**Invariant.** Before the answer is produced, the procedure has established the receiver's current length $L$ and has not read any position other than $L - 1$.

*Base.* The length is read directly from the receiver, so it reflects the array as it is at the moment of the call, not as it was when the method was installed.

*Case $L = 0$.* A length-0 array has no positions, so there is no final element to return. The contract specifies the sentinel `-1` for exactly this situation, and the procedure returns it without reading any position. The answer is total: it is defined for every array, including the empty one.

*Case $L \ge 1$.* Because the input is the output of `JSON.parse`, the array is dense: its elements occupy precisely the positions $0$ through $L - 1$, with no holes and no `undefined` values, since neither is representable in JSON. Therefore position $L - 1$ holds an element, that element is the final one, and no other position is later in the ordering. The procedure reads it and returns it unmodified.

*Why the element's own value cannot interfere.* The only test performed is on the length, so a final element that is falsy — `false`, `0`, an empty string, `null` — is returned exactly as stored instead of being mistaken for absence. A procedure that tested the element for truthiness, or that treated a missing value as the empty case, would fail on such inputs; the length test is what makes the empty case and the falsy case disjoint.

*Why the capability is complete.* Once the method exists on the shared array prototype, method lookup from any array reaches it by delegation, so every array in the program gains the capability without individual installation, and the receiver-based length read keeps distinct arrays independent of one another.

One residual property of the design deserves to be stated rather than hidden: the sentinel `-1` is also a legal JSON number. An array whose final element is literally `-1` therefore answers `-1`, and that answer is indistinguishable from the empty-array answer. The contract accepts this collision, so the correct behaviour is to return the final element unchanged in both cases — the ambiguity belongs to the chosen sentinel, not to the procedure.

## 6. Traps this instance exposes

| trap | concrete symptom | correct handling |
|---|---|---|
| Testing the final element for truthiness | an array ending in `false`, `0`, `null` or an empty string must return that value, but a truthiness test reports the sentinel | Test the length, then return the element as found |
| Guarding with `undefined` instead of a length check | an empty array has no position to read, so a failed read yields `undefined`, not the required `-1` | Detect emptiness from the length |
| Computing the index as $L$ rather than $L - 1$ | positions run from $0$, so position $L$ does not exist | Derive the index as length minus one |
| Return the value for the wrong array | a shared method that captured one array, or that cached a length, misbehaves when another array calls it | Read the receiver's length at call time |
| Attaching the method to instances rather than the prototype | arrays created after the enhancement, and nested arrays, would not answer the call | Install it once on the shared array prototype |
| Returning a copy, a slice, or a serialization | a nested array or object must come back intact and by reference | Return the stored element itself |
| Assuming holes or `undefined` can appear | JSON has neither elisions nor an `undefined` literal, so the input array is always dense | Rely on density; do not add hole-scanning logic |
| Treating `-1` as proof of emptiness | an array ending in the number `-1` returns the same value as an empty array | Accept the documented sentinel collision and return the element unchanged |
| Scanning the whole array to find the end | a full traversal costs time proportional to the length for no benefit | Index the final position directly |
| Defining the method as an enumerable property | it then appears when the array's properties are enumerated, surprising unrelated loops | Prefer a non-enumerable definition; the requirement is only that arrays can call it |

## 7. Complexity

**Time.** The method reads the length, compares it with zero, computes $L - 1$, and reads one position. Array indexing by a numeric position is constant-time, so the work is independent of the array's length:

$$
O(1)
$$

per call. The stated bound $\text{arr.length} \le 1000$ is therefore not a resource limit for this method at all — the answer costs the same for an array of one element and an array of a thousand. A traversal that walked from the front to find the end would cost $O(L)$ and would be strictly worse for the same result. Using a built-in indexing helper that counts backwards from the end is also constant-time, but it answers "no element" with a different absent value, so the explicit length guard would still be required for the empty case.

**Auxiliary space.** No temporary structure is created: the method holds the length and the final index, and returns the stored element without copying it. The auxiliary space is $O(1)$, and the array is left unmodified, so repeated calls are free of side effects.
