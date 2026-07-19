## General
**Replace only the separator character:** Apply a literal string replacement from `"."` to `"[.]"`. A valid IPv4 address uses periods only as the three octet separators, so every match must be replaced and no digit can be affected.

**Preserve octet spelling and order:** The transformation is textual. It does not convert octets to integers, normalize leading characters, reorder them, or add brackets around the entire address. For example, `address.replace(".", "[.]")` changes each separator independently while copying every other character exactly once.

The result is correct because each source period produces exactly one `"[.]"`, satisfying the definition of defanging, while every non-period character is copied unchanged. Those two cases cover every character in the valid input string.

## Complexity detail
A direct scan would take $O(n)$ time and return $n + 6$ characters because each of the three one-character separators gains two characters. Under the actual IPv4 contract, however, $7 \le n \le 15$, so both the work and returned storage are bounded constants. The contract-level bounds are therefore $O(1)$ time and $O(1)$ space.

## Alternatives and edge cases
- **Manual character scan:** Append `"[.]"` for a period and otherwise append the current character. It is equally correct but more verbose than literal replacement.
- **Split and join:** `"[.]".join(address.split("."))` also works because a valid IPv4 address has exactly four octets, though it creates an intermediate list.
- **Regular expression replacement:** It is unnecessary for a single literal character and requires escaping the period because `.` has special regex meaning.
- **Minimum-length address:** `"0.0.0.0"` still contains exactly three separators and becomes `"0[.]0[.]0[.]0"`.
- **Maximum-length address:** `"255.255.255.255"` remains within the fixed input domain and defangs all three periods.
- **Octet digits:** Digits such as the zero in `"10.0.0.1"` are copied verbatim; this task does not validate or numerically reinterpret the address.
