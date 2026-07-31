## General

JSON syntax is determined by the current value's type. `null` emits `null`; a string emits its characters between double quotes; a number or boolean emits `String(value)`. Arrays add brackets and serialize their elements in index order, separated by commas. Objects add braces and serialize each `Object.keys(value)` entry as a quoted key, a colon, and its recursively encoded value.

Append every piece to one shared `output` array rather than returning and repeatedly concatenating partial strings. After the complete value has been visited, join the token array once. The input guarantee that strings are alphanumeric means their contents and object keys cannot require escaping.

**Container punctuation follows position, not lookahead**

For either an array element or an object property, append a comma exactly when its index is greater than zero. This rule emits one comma between adjacent members and none before the first or after the last, including the empty-container cases `[]` and `{}`.

The recursive procedure emits the unique JSON representation for each primitive directly. Assuming recursive calls correctly encode nested values, the array branch places those encodings in original index order with valid separators, while the object branch places them in `Object.keys` order beside their corresponding keys. Wrapping those sequences with the correct delimiters therefore produces valid compact JSON for every container. By structural induction, the complete returned string represents the input exactly.

## Complexity detail

Let $S$ be the output length and $d$ the maximum nesting depth. Every output character is appended to the token buffer and copied into the joined result a constant number of times, giving $O(S)$ time. The tokens and returned string use $O(S)$ space, while recursion uses $O(d)$ stack space. Since every nested level contributes delimiters to the output, $d = O(S)$, so total space is $O(S)$.

## Alternatives and edge cases

- **Return concatenated strings recursively:** This is concise, but repeated rebuilding of growing prefixes can copy the same characters many times and degrade toward $O(S^2)$.
- **Iterative explicit stack:** Stack frames can be represented manually to avoid call-stack dependence while preserving $O(S)$ time, but the permitted depth of $1000$ is safe for the reviewed JavaScript runtime and recursion is clearer here.
- **Built-in `JSON.stringify`:** It supplies the desired behavior, but the problem explicitly forbids using it.
- **`null` before object handling:** JavaScript reports `typeof null === "object"`; test `null` first so it is not treated as a container.
- **Arrays before ordinary objects:** Arrays also have object type, so distinguish them with `Array.isArray` before enumerating object keys.
- **Empty containers:** Emit only their opening and closing delimiters, with no comma or member text.
- **Object key order:** Iterate the array returned by `Object.keys`; a `for...in` loop can include inherited enumerable properties.
- **Top-level primitives:** Strings, numbers, booleans, and `null` are complete valid inputs and must not be wrapped as an object or array.
- **String escaping:** The source contract restricts every string to alphanumeric characters. A general-purpose serializer would additionally escape quotes, backslashes, and control characters, but that behavior is outside this input domain.
