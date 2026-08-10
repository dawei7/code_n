## General

**Treat the input as a language with a cursor**

JSON values can be nested: an array element may be another array, an object property may hold an object, and so on. The exact solution uses a recursive-descent parser, meaning each JSON construct has a small function that recognizes it and returns the corresponding JavaScript value.

All parser functions share one variable, `index`. It always points to the first character not yet consumed. A helper does not need to return a new position because advancing this shared cursor records its progress for whichever parser called it. The central dispatcher, `parseValue`, skips whitespace, inspects the next token, and chooses the appropriate helper.

The reference guarantees that the input is valid JSON and contains no escape characters or invisible characters. Those guarantees allow the implementation to be deliberately smaller than a production JSON parser.

**Whitespace never changes a value**

`skipWhitespace` advances while the current character is one of space, newline, carriage return, or tab. `parseValue` calls it before examining a token. Arrays and objects also call it around separators and closing delimiters where whitespace is legal.

Because `index` only moves forward, whitespace is consumed once. It is not copied into any returned value. Whitespace inside a quoted string would be ordinary string content because `parseString`, rather than `skipWhitespace`, owns all characters between the quotes.

**Dispatching by the first token**

After whitespace, the first character uniquely identifies most JSON value types:

- A double quote begins a string.
- An opening bracket begins an array.
- An opening brace begins an object.
- Prefixes `true`, `false`, and `null` become their JavaScript primitive counterparts.
- Anything else must begin a valid JSON number under the input guarantee.

For the three keywords, the parser advances by the known literal length. It does not revalidate each character beyond `startsWith` because invalid input is excluded.

**Parsing strings under the stated restriction**

`parseString` skips the opening quote, remembers the content start, scans until the next quote, slices that content, and skips the closing quote. Ordinarily, a quote preceded by a backslash may belong to the string rather than end it, and escape sequences require decoding. The local description explicitly says escape characters do not occur. Therefore the next quote really is the terminator, and the simple scan is correct for this problem's domain.

That assumption should not be generalized into a claim that the function implements every possible JSON string. It implements the guaranteed subset exactly.

**Parsing the complete number shape used by valid input**

`parseNumber` remembers the starting position and advances through several optional or required regions:

1. An optional minus sign.
2. The integer part: a single zero, or a run of digits.
3. An optional decimal point followed by digits.
4. An optional exponent marker `e` or `E`, an optional exponent sign, and exponent digits.

It then slices the numeric token and passes it to `Number`. This handles integers, negative numbers, fractions, and scientific notation without manually implementing arithmetic. Valid JSON guarantees that malformed forms such as an empty exponent do not reach the parser.

**Parsing arrays**

After consuming `[`, `parseArray` skips whitespace and first checks for `]`, which represents an empty array. Otherwise it repeatedly calls `parseValue` and pushes the result.

After a value, it skips whitespace. A closing bracket finishes the array. If the next token is not a closing bracket, valid JSON guarantees it is a comma, so the parser advances one character and continues. This “advance without checking” is safe only because syntax validity is promised.

Recursion arises naturally: if an element starts with another bracket or brace, `parseValue` calls the corresponding nested parser. When that call returns, `index` already points immediately after the nested value.

**Parsing objects safely**

Object parsing follows the same delimiter pattern. Each member starts with a quoted key, followed by a colon and an arbitrary JSON value. The code parses the key, skips whitespace, advances over the guaranteed colon, recursively parses the value, and then handles either a closing brace or the guaranteed comma.

The assignment is made with `Object.defineProperty` rather than `result[key] = value`. This is a meaningful safety and correctness detail. A JSON key may literally be `"__proto__"`. On ordinary objects, direct assignment to that name can interact with the inherited prototype setter instead of creating a normal own data property. `Object.defineProperty` explicitly creates an enumerable, writable, configurable own property, so even that key is represented as data. Enumerable properties make the parsed object behave like a normal object during iteration and serialization.

**Why the recursive structure is correct**

Each helper begins with `index` at its construct's opening token, consumes exactly that construct, and returns its JavaScript value with `index` positioned immediately afterward. Primitive helpers satisfy this directly. Array and object helpers rely on the same property recursively for their children and then consume their own separators and closing delimiter. Thus, by structural induction on nesting, `parseValue` returns the value described by the input text. The top-level call begins at zero, so it reconstructs the complete JSON value.

## Complexity detail

Let `n` be `str.length` and `D` the maximum nesting depth. The cursor advances monotonically, so scanning tokens and whitespace accounts for `O(n)` character visits. String and number slicing plus JavaScript conversion also process token characters. Across disjoint tokens, their total content is `O(n)`, giving `O(n)` overall time under standard string-slice and conversion costs.

The returned arrays, objects, strings, and properties occupy `O(n)` space because they represent the parsed input. Excluding that required output, the parser's control state is `O(D)` for recursive array and object calls, plus `O(1)` shared cursor state and local variables per active call. Temporary token substrings can total `O(n)` over execution and have at most `O(n)` peak for one large token. It is therefore reasonable to state `O(n)` total space including output, while the key auxiliary recursion bound is `O(D)`.

On an extremely deeply nested valid input, JavaScript's call-stack limit can be reached even though the asymptotic bound is correct. An iterative parser would avoid that runtime-specific limitation at the cost of more explicit state.

## Alternatives and edge cases

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
