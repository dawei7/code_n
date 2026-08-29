# Guided Example: Create Object from Two Arrays

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"keysArr": ["a", "b", "c"], "valuesArr": [1, 2, 3]}`
- **Required output:** `{"a": 1, "b": 2, "c": 3}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given two arrays `keysArr` and `valuesArr`, return a new object `obj`. Each key-value pair in `obj` should come from $\text{keysArr}[i]$ and $\text{valuesArr}[i]$.

The objective is to compute `{"a": 1, "b": 2, "c": 3}` from `{"keysArr": ["a", "b", "c"], "valuesArr": [1, 2, 3]}` while avoiding redundant calculations and unnecessary overhead.

A naive or brute-force exploration risks evaluating infeasible states or repeating subproblem computations. The optimal method establishes a clear invariant that advances deterministically toward the goal.

---

## 2. Conceptual Foundation & Invariants

We maintain the core conceptual parameters and state variables:

| State Parameter | Role & Purpose | Initial State |
|---|---|---|
| Primary State | Tracks active elements, frontier indices, or DP table cells | Initialized at boundary |
| Accumulator | Preserves confirmed optimal sub-answers or counts | Empty / Neutral |

> **Invariant.** At every processing step, all previously evaluated subproblems strictly satisfy the problem constraints, and no viable candidate solution has been omitted.

---

## 3. Step-by-Step Worked Execution

### Step 1: Pair corresponding indices in one pass

The two arrays have equal length. The exact solution creates `ans = {}` and loops `i` from zero through `keysArr.length - 1`. At each index, it converts the key and, if that converted property appears unused according to its test, stores `valuesArr[i]`.

Because indices are visited in increasing order, accepting a key only while it is absent implements “first occurrence wins” for ordinary non-colliding properties. Later converted duplicates are skipped.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"keysArr": ["a", "b", "c"], "valuesArr": [1, 2, 3]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Convert before checking duplicates

The source computes:

`const k = keysArr[i] + '';`

Adding an empty string invokes JavaScript primitive conversion and string concatenation. For the JSON-domain key values in the contract, this produces the same familiar property strings expected from `String(value)`:

- number `1` becomes `"1"`;
- Boolean `false` becomes `"false"`;
- `null` becomes `"null"`;
- an existing string remains its own contents;
- JSON arrays and objects follow their ordinary JavaScript string coercion.

Conversion occurs before duplicate detection. Therefore string `"1"` and number `1` collide as one key, and the earlier index supplies the value.

The written contract specifically says to call `String()`. The exact source uses concatenation instead. For ordinary JSON values these usually agree, but they are not universally interchangeable for every possible JavaScript value, especially values such as Symbols or objects with custom coercion. Those are outside a strict JSON-value model, yet the distinction belongs in an exact explanation.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: How the source decides whether a key is unused

The condition is:

`if (ans[k] === undefined)`.

For a normal own property previously assigned a JSON value, reading `ans[k]` returns that defined value, so the condition is false and the duplicate is skipped. For a new ordinary property not found anywhere on the object or its prototype chain, the read returns undefined, so the first value is assigned.

The values array is a valid JSON array. JSON has no undefined value, so an accepted own property cannot legitimately store undefined under the stated domain. This makes undefined usable as an absence sentinel for ordinary own keys. Outside the contract, if the first value were undefined, a later duplicate would be treated as absent and overwrite it.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"a": 1, "b": 2, "c": 3}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"keysArr": ["a", "b", "c"], "valuesArr": [1, 2, 3]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"a": 1, "b": 2, "c": 3}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Null-prototype object:** `Object.create(null)` removes inherited-name collisions. Direct assignment then treats `"toString"` and `"__proto__"` as ordinary data keys.
- **Separate `Set` of converted keys:** Test `seen.has(k)`, add on first occurrence, and define the property. This matches the manifest and makes duplicate detection independent of stored values.
- **`Object.hasOwn(ans, k)`:** It distinguishes own properties from inherited ones, fixing ordinary prototype-name skips; safe definition is still preferable for `"__proto__"`.
- **`Object.defineProperty`:** Defining an enumerable writable configurable own data property safely handles `"__proto__"` without invoking the inherited setter.
- **Use `String(keysArr[i])` exactly:** It follows the written conversion contract rather than relying on empty-string concatenation.
- **String and numeric duplicate:** Both convert to the same property string, so the first should win.
- **Boolean and null keys:** They convert to `"true"`, `"false"`, and `"null"`.
- **Empty arrays:** The loop runs zero times and returns an empty ordinary object.
- **First value is null, false, zero, or empty string:** These are defined JSON values; lookup is not undefined, so later duplicates are correctly skipped.
- **First value is undefined outside the contract:** The sentinel test mistakes it for absence and allows a later overwrite.
- **Prototype-colliding key:** The exact code incorrectly skips first occurrences such as `"toString"` and `"constructor"`.
- **`"__proto__"` key:** The exact code does not create the required own property and needs safe definition or a null prototype.
- **Nested value:** The output stores the same reference rather than deep-copying it.
- **Manifest mismatch:** No Set and no safe property-definition API appear in the source; the approach must disclose that difference.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(1)$. Let `n` be the number of pairs and let `K` be the total length of all converted key strings. String conversion takes time proportional to produced key length, and ordinary property lookup/assignment is expected `O(1)` per key after hashing. Expected time is `O(n + K)`.
- **Auxiliary Space Complexity:** $O(n + K)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
