## General

**Generate syntax while traversing the JSON tree**

A valid JSON value is one of:

- null;
- string;
- number;
- Boolean;
- array;
- object.

Each category has a different textual representation. The helper `write(value)` identifies the category, appends the required tokens to one shared buffer, and recursively writes container children.

After the root value is complete, `output.join('')` combines all tokens exactly once into the final compact string.

**Why a shared token buffer matters**

Repeatedly building a string with recursive expressions such as:

`result = result + nextPart`

can copy the entire prefix many times because JavaScript strings are immutable. Depending on runtime optimizations, deeply or broadly nested output can risk superlinear copying.

The solution instead pushes small pieces into `output`:

- punctuation;
- keys;
- primitive text.

Appending array entries is amortized constant time, and one final join performs output assembly proportional to the final serialized length.

**Handle null before the object branch**

JavaScript's historical behavior reports:

`typeof null === "object"`.

Therefore, null must be tested first. The solution appends literal `"null"` and returns from that branch implicitly.

If null reached the ordinary object branch, `Object.keys(null)` would fail. The category order prevents this.

**Write strings under the contract's character restriction**

For a string, the solution pushes:

`'"', value, '"'`.

This surrounds the content with JSON double quotes.

In general JSON serialization, quote, backslash, newline, control characters, and certain Unicode characters require escaping. The package constraint says all strings contain only alphanumeric characters, so no escape transformation is needed here.

The same restriction covers object keys, which are also strings in valid JSON. The exact implementation can safely place each key between double quotes unchanged.

**Write numbers and Booleans**

For any non-object value that was not null or a string, the solution appends `String(value)`.

Under valid JSON inputs, this branch handles finite numbers and Booleans:

- true becomes `"true"`;
- false becomes `"false"`;
- numbers receive their ordinary decimal representation.

Values such as undefined, functions, symbols, `NaN`, and Infinity are not valid JSON inputs and therefore need no special behavior.

**Serialize arrays in order**

For an array, the helper appends opening bracket `[`. It then visits indices from zero through length minus one.

Before every element except the first, it appends a comma. This rule produces:

- no comma for an empty array;
- no leading comma;
- no trailing comma;
- exactly one comma between adjacent serialized elements.

Each element is passed recursively to `write`, so arbitrarily nested arrays and objects use their own correct syntax. Finally, the helper appends closing bracket `]`.

Array order is preserved because indices are processed in increasing order.

**Serialize objects in `Object.keys` order**

For an object, the helper appends opening brace `{` and obtains `const keys = Object.keys(value)`.

The loop follows that key array in order, satisfying the explicit requirement. For each key:

1. append a separating comma except before the first member;
2. append a quoted key and colon;
3. recursively serialize `value[key]`.

After all members, append `}`.

An empty object has zero loop iterations and becomes `{}`.

**Trace a nested object**

For:

`{"key":{"a":1,"b":[{},null,"Hello"]}}`,

the buffer grows conceptually as:

- outer opening brace;
- quoted `key` and colon;
- inner opening brace;
- quoted `a`, colon, and one;
- comma;
- quoted `b` and colon;
- array opening bracket;
- empty object tokens;
- comma and null;
- comma and quoted Hello;
- array closing bracket;
- inner and outer closing braces.

Joining without a separator yields the exact compact JSON text, with no extra spaces.

**Structural correctness proof**

Use induction on maximum nesting depth.

At depth zero, the value is primitive or null. Each base branch emits exactly its valid JSON literal under the input restrictions.

Assume `write` correctly serializes children of smaller depth. For an array, brackets delimit the container, commas separate recursively correct child strings, and iteration preserves order. For an object, braces delimit members, each key receives quotes and a colon, commas separate members, and recursive calls correctly serialize values in `Object.keys` order.

Thus every category emits valid and exact JSON at its depth. The root call consequently produces the desired representation.

**Why output length is unavoidable**

If the final JSON string has length $S$, any solution must produce $S$ characters. Even a perfect algorithm therefore needs $\Omega(S)$ time and $O(S)$ output storage.

The token-buffer method meets this lower bound asymptotically by traversing each input component and emitting each output character a constant number of times.

**Recursion depth**

The helper uses one call frame per active nested container. Maximum depth can be 1000. This mirrors the structure cleanly, though a runtime with a strict stack limit could use an explicit stack of write actions.

The exact source assumes the challenge runtime accepts the allowed nesting.

## Complexity detail

Let $S$ be the length of the returned JSON string. Traversal visits each key, primitive representation, and delimiter once, and final joining copies the tokens into an $S$-character string. Time is $O(S)$.

The token buffer and returned string each require $O(S)$ storage. The recursive call stack adds $O(D)$ for nesting depth $D$, and $D\le S$, so total space is $O(S)$.

## Alternatives and edge cases

- **Repeated string concatenation:** Correct in principle but can cause repeated prefix copying; a shared buffer gives a clear linear bound.
- **Explicit action stack:** Avoids recursion-depth limits while emitting the same token sequence.
- **Built-in `JSON.stringify`:** Exactly suited to the task but explicitly forbidden.
- **Null:** Must be handled before checking general object type.
- **Empty array:** Emits `[]` with no comma.
- **Empty object:** Emits `{}` with no member syntax.
- **Nested containers:** Recursive calls choose syntax independently at every level.
- **Object key order:** Iterating the `Object.keys` result preserves the required order.
- **String escaping:** The exact code relies on the alphanumeric-only constraint; general JSON strings would require escapes.
- **No extra spaces:** Only structural punctuation and value tokens are appended.
