# Guided Example: Convert JSON String to Object

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"str": "{\"a\":2,\"b\":[1,2,3]}"}`
- **Required output:** `{"a": 2, "b": [1, 2, 3]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given a string `str`, return parsed JSON `parsedStr`. You may assume the `str` is a valid JSON string hence it only includes strings, numbers, arrays, objects, booleans, and null. `str` will not include invisible characters and escape characters.

The objective is to compute `{"a": 2, "b": [1, 2, 3]}` from `{"str": "{\"a\":2,\"b\":[1,2,3]}"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Treat the input as a language with a cursor

JSON values can be nested: an array element may be another array, an object property may hold an object, and so on. The exact solution uses a recursive-descent parser, meaning each JSON construct has a small function that recognizes it and returns the corresponding JavaScript value.

All parser functions share one variable, `index`. It always points to the first character not yet consumed. A helper does not need to return a new position because advancing this shared cursor records its progress for whichever parser called it. The central dispatcher, `parseValue`, skips whitespace, inspects the next token, and chooses the appropriate helper.

The reference guarantees that the input is valid JSON and contains no escape characters or invisible characters. Those guarantees allow the implementation to be deliberately smaller than a production JSON parser.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"str": "{\"a\":2,\"b\":[1,2,3]}"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Whitespace never changes a value

`skipWhitespace` advances while the current character is one of space, newline, carriage return, or tab. `parseValue` calls it before examining a token. Arrays and objects also call it around separators and closing delimiters where whitespace is legal.

Because `index` only moves forward, whitespace is consumed once. It is not copied into any returned value. Whitespace inside a quoted string would be ordinary string content because `parseString`, rather than `skipWhitespace`, owns all characters between the quotes.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Dispatching by the first token

After whitespace, the first character uniquely identifies most JSON value types:

- A double quote begins a string.
- An opening bracket begins an array.
- An opening brace begins an object.
- Prefixes `true`, `false`, and `null` become their JavaScript primitive counterparts.
- Anything else must begin a valid JSON number under the input guarantee.

For the three keywords, the parser advances by the known literal length. It does not revalidate each character beyond `startsWith` because invalid input is excluded.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"a": 2, "b": [1, 2, 3]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"str": "{\"a\":2,\"b\":[1,2,3]}"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"a": 2, "b": [1, 2, 3]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Use `JSON.parse`:** That is the production-standard choice, but the challenge asks for parsing without it. The recursive-descent structure supplies the needed behavior directly.
- **Regular-expression-only parsing:** Nested arrays and objects require balanced recursive structure, which a simple flat token replacement cannot reliably model.
- **Iterative explicit stack:** It can avoid call-stack overflow for extreme nesting, but it requires more bookkeeping for container state, keys, commas, and completed child values.
- **Direct object assignment:** `result[key] = value` is shorter but mishandles special names such as `"__proto__"` on ordinary objects. Defining an own data property preserves the JSON member faithfully.
- **Empty array or object:** The immediate check for `]` or `}` returns the empty container without trying to parse a nonexistent first member.
- **Top-level primitive:** The entry point is `parseValue`, not an object-only parser, so strings, numbers, booleans, and `null` work as complete inputs.
- **Negative, fractional, and exponent numbers:** `parseNumber` recognizes all of these regions before calling `Number`.
- **Leading zero rules:** Valid JSON is guaranteed. The parser consumes a lone initial zero rather than an arbitrary digit run beginning with zero.
- **Whitespace around separators:** Calls to `skipWhitespace` allow legal spacing before values and around commas, colons, and closing delimiters.
- **Escaped quote or backslash:** The exact string scanner does not support escapes. This is correct only because the reference explicitly excludes escape characters.
- **Malformed input:** Missing delimiters or invalid literals could run the cursor incorrectly. Validation and useful syntax errors are intentionally omitted under the valid-input guarantee.
- **Deep nesting:** Recursive calls mirror the data and use `O(D)` stack frames; an adversarial depth may exceed the JavaScript engine's call-stack limit.
- **Duplicate object keys:** Each later `defineProperty` call redefines the configurable own property, so the last occurrence wins, consistent with ordinary practical parsing behavior.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let `n` be `str.length` and `D` the maximum nesting depth. The cursor advances monotonically, so scanning tokens and whitespace accounts for `O(n)` character visits. String and number slicing plus JavaScript conversion also process token characters. Across disjoint tokens, their total content is `O(n)`, giving `O(n)` overall time under standard string-slice and conversion costs.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
