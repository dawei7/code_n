## General

A JSON value is identifiable from its first non-whitespace character. A quote starts a string, `[` starts an array, `{` starts an object, the initial letters `t`, `f`, and `n` identify the three fixed literals, and every remaining valid token is a number. This makes recursive descent a natural match for the grammar.

Maintain one shared cursor `index` into the input. `parseValue` inspects the current token and dispatches to the matching routine. Each routine consumes exactly its own representation and leaves the cursor on the first character after that value, so its caller never needs to search for a matching delimiter or reparse a substring.

**Strings and numbers.** A string routine skips the opening quote, scans to the closing quote, and returns that slice. This is safe under the contract that string contents contain no escape sequences. The number routine consumes the JSON number components in order: an optional minus sign, the integer part, an optional fractional part, and an optional exponent with its own sign. Converting the single completed slice with `Number` preserves integers, decimals, exponents, and negative zero.

**Arrays and objects.** After an opening bracket, parse complete values until the matching closing bracket, consuming commas between them. Object parsing follows the same pattern but reads a quoted key, consumes its colon, parses one complete value, and installs the property. Defining properties explicitly makes keys such as `"__proto__"` ordinary own data properties rather than accidentally invoking the legacy prototype setter.

This cursor discipline also explains correctness. Primitive routines consume precisely one primitive token. Assuming recursive calls correctly consume nested values, an array routine appends exactly the values between its brackets in order, and an object routine associates every parsed key with exactly the value after its colon. Therefore `parseValue` reconstructs the complete value described by the valid input.

## Complexity detail

Let $n = \lvert\texttt{str}\rvert$. The cursor only moves forward, and every input character is examined a constant number of times. String and number slices cover disjoint tokens, so their total copied length is also $O(n)$. The time complexity is therefore $O(n)$.

The returned arrays, objects, strings, and primitive values collectively require $O(n)$ space in the worst case. In addition, recursive calls use $O(d)$ stack space for nesting depth $d$, where $d \leq n$. Thus the total and worst-case auxiliary bound are $O(n)$.

## Alternatives and edge cases

- **Use `eval` or the `Function` constructor:** Executing input text is unsafe, accepts JavaScript syntax beyond JSON, and avoids implementing the requested parser just as surely as `JSON.parse` does.
- **Split on commas or colons:** Delimiters can occur inside quoted strings or nested containers, so flat splitting loses the grammar's nesting and quoting context.
- **Repeated substring recursion:** Passing a shrinking suffix or repeatedly searching for matching brackets can copy and rescan the same characters, degrading to $O(n^2)$ on deeply nested inputs.
- **Empty containers:** Check for `]` or `}` immediately after opening a container so `[]` and `{}` do not attempt to parse a nonexistent first element.
- **Numeric forms:** Negative values, fractional parts, exponent notation, and `-0` must all remain numbers rather than strings.
- **Quoted punctuation:** Commas, colons, and brackets inside strings are data; only the closing quote ends the token because escape sequences are excluded.
- **Prototype-like keys:** Object keys such as `"__proto__"` must become enumerable own properties with their parsed values.

