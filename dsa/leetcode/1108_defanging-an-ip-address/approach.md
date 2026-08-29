## General

**The transformation is purely local**

A valid IPv4 address contains four decimal components separated by exactly three period characters. Defanging does not parse, validate, reorder, or numerically interpret those components. It performs one literal transformation: every `.` becomes `[.]`, while every digit remains unchanged.

That means the problem does not need an IP-address parser. Splitting the address into components and joining them again could work, but it introduces extra concepts when Python already provides the exact whole-string replacement operation.

**Use immutable string replacement**

`address.replace('.', '[.]')` scans the string for every nonoverlapping occurrence of the period substring and constructs a new string in which each occurrence is replaced by the three-character text `[.]`.

Python strings are immutable, so `replace` does not alter the input object. The returned string is the transformed value. This matters because merely calling `replace` without returning or assigning its result would leave the original address unchanged from the caller’s perspective.

The first argument is a literal period, not a regular expression. A period has no wildcard meaning in `str.replace`, so no escaping is needed. The replacement text contains the original period inside square brackets, exactly matching the required defanged format.

**Why every required separator is transformed**

A valid IPv4 address has exactly three separators. `replace` processes all occurrences by default because no replacement-count argument is supplied. Therefore, each of the three separators becomes `[.]`.

Every other character is a decimal digit belonging to one of the four components. Since those digits do not match the search substring, `replace` copies them unchanged and in the same order.

For `"255.100.50.0"`, the digit runs `255`, `100`, `50`, and `0` remain intact. The three intervening periods each gain an opening and closing square bracket, producing `"255[.]100[.]50[.]0"`.

**Why no validation is required**

The contract guarantees that `address` is a valid IPv4 address. The method therefore does not need to check component count, numeric ranges, leading-zero rules, unexpected characters, or missing separators. Adding such validation would not improve the answer for any permitted input.

This guarantee also makes the output-size change exact. Replacing one character with three adds two characters per separator. With exactly three separators, the result is always six characters longer than the input.

**Complete correctness argument**

Consider any character position in the input. If it contains a period, `replace` substitutes `[.]`, exactly the rule required by defanging. If it contains a digit, it does not match the search text and is copied unchanged. These are the only two character categories in a valid IPv4 address.

Because replacement preserves left-to-right order and handles every occurrence, the output contains precisely the original four components separated by defanged periods. Therefore, the returned string is exactly the required defanged address.

## Complexity detail

The repository playbook classifies this package as a bounded-domain problem. A valid IPv4 address has at most fifteen characters: four components of at most three digits plus three separators. Its length is therefore bounded by a source-defined constant.

Under that legal domain, scanning and constructing the result take $O(1)$ time and $O(1)$ space, matching the package manifest. The result is at most twenty-one characters long, so even output storage is bounded.

For a generalized string of length $A$, Python must inspect $A$ characters and create an output proportional to $A$, giving $O(A)$ time and $O(A)$ result space. Stating both views prevents the constant bound from being mistaken for a claim that string replacement performs no work; it is constant only because the valid input domain is fixed.

The method uses no additional collection, parser state, or recursion. Apart from the newly returned immutable string, its auxiliary working storage is constant.

## Alternatives and edge cases

- **Split and join:** `'[.]'.join(address.split('.'))` also produces the result. It creates a temporary list of four components, making it more elaborate than direct replacement.
- **Character-by-character builder:** Append `[.]` for periods and the original character otherwise. This exposes the transformation explicitly but requires more code and a temporary list or repeated concatenation.
- **Regular expression replacement:** It is unnecessary and easier to misuse because a period is special in regex syntax. `str.replace` is literal and exact.
- **Manual three replacements:** Searching for separator indices individually couples the code to address structure and creates avoidable boundary logic.
- **Address with one-digit components:** `"1.1.1.1"` becomes `"1[.]1[.]1[.]1"`; component length does not affect separator handling.
- **Maximum-length address:** `"255.255.255.255"` still has only fifteen input characters and exactly three replacements.
- **Zero component:** Digits such as the final zero in `"255.100.50.0"` remain unchanged.
- **Input immutability:** The original string object is not edited; callers receive a separate transformed string.
- **Exactly three separators:** The validity guarantee is why replacing every period neither misses a separator nor transforms an unrelated punctuation mark.
- **Malformed input outside the contract:** The method would mechanically replace any periods without validating IPv4 semantics, which is acceptable because malformed addresses are not permitted.
- **Square brackets in output:** They are newly introduced around each period and are not interpreted as regex or indexing syntax inside the returned string.
- **No hidden numeric conversion:** Components such as `"100"` remain textually identical; no integer parsing can remove digits or change formatting.
