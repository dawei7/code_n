## General

The solution separates the task into filtering and ordering. It scans the three parallel input arrays once, records the indices of coupons satisfying all validity rules, sorts those indices by the required two-part key, and finally converts the sorted indices back to coupon codes.

Keeping indices is useful because each coupon's code, business line, and active flag remain linked without copying records or building custom objects.

**Validating the code characters**

The nested helper `check(s)` first rejects an empty string. This is necessary because a loop over an empty string would otherwise finish successfully even though the statement explicitly requires a non-empty code.

For each character `c`, the helper accepts it only when at least one of these is true:

- `c.isalpha()`: it is a letter;
- `c.isdigit()`: it is a digit;
- `c == "_"`: it is an underscore.

The helper returns `False` immediately on the first invalid character, so it does not scan the unused suffix of an invalid code. If every character passes, it returns `True`.

Python's `isalpha` and `isdigit` recognize more Unicode characters than only `a-z`, `A-Z`, and `0-9`. However, the problem guarantees that `code[i]` consists of printable ASCII characters. Within that promised input domain, the helper accepts exactly the required alphanumeric characters and underscore.

**Checking all three validity conditions**

The allowed categories are stored in the constant-size set:

`{"electronics", "grocery", "pharmacy", "restaurant"}`.

For coupon index `i`, the condition:

`a and b in bs and check(c)`

checks that the coupon is active, that its business line is allowed, and that its code is valid.

Python evaluates `and` from left to right and stops after the first false condition. Therefore:

- an inactive coupon is rejected without looking up the business line or scanning the code;
- an active coupon with an invalid business line is rejected without scanning the code;
- the character scan runs only when the first two rules pass.

This ordering does not change correctness, but it can avoid unnecessary work.

The loop uses:

`enumerate(zip(code, businessLine, isActive))`.

`zip` supplies the three values at the same position, while `enumerate` recovers that position for `idx`. The contract guarantees all three arrays have the same length, so no entry is lost through `zip`'s usual shortest-input behavior.

**Why storing every valid index matters**

When a coupon is valid, its index is appended to `idx`. The solution does not use a set of codes. Consequently, two different valid coupons with identical code strings are both retained in the result. This matches processing the input coupons as rows rather than deduplicating identifiers without authorization.

The original arrays also remain the source of truth for sorting. For an index `i`, both `businessLine[i]` and `code[i]` are available without storing duplicate strings in a separate tuple list.

**The two-part sorting key**

The valid indices are sorted with:

`key=lambda i: (businessLine[i], code[i])`.

Python compares tuples lexicographically. It first compares the business-line strings. Only when those are equal does it compare the code strings. Thus all coupons in one category form a consecutive group, and codes within that category appear in ascending lexicographical order.

The problem gives a custom-looking category order:

1. electronics;
2. grocery;
3. pharmacy;
4. restaurant.

For these exact four strings, that order is already their normal ascending lexicographical order:

`"electronics" < "grocery" < "pharmacy" < "restaurant"`.

That coincidence is why the source does not need the explicit rank map shown in the local editorial. Sorting directly by `businessLine[i]` produces the required category order. If the required order changed, or if the category names did not happen to sort correctly, this key would need a rank mapping.

Within a category, Python compares code strings character by character. Since the input is printable ASCII, this is a case-sensitive ordering based on character code points. A shorter string sorts first when it is a prefix of a longer one.

**Producing only the requested codes**

After sorting, the list comprehension:

`[code[i] for i in idx]`

returns the code at each valid index in its new order. Business lines and active flags were necessary for validation and sorting but are not included in the requested output.

**Following the second example**

`"GROCERY15"` has an allowed category and valid characters, but its active flag is false, so short-circuit evaluation rejects it immediately.

`"ELECTRONICS_50"` is active, belongs to `"electronics"`, and contains only letters, digits, and an underscore, so its index is retained.

`"DISCOUNT10"` is active and its code is syntactically valid, but `"invalid"` is not in the category set, so it is rejected before `check` is called. Only the second code remains, making sorting trivial.

**Why the result is correct**

Every returned index was appended only after all three required predicates succeeded, so every returned code belongs to a valid coupon. Conversely, the scan visits every input position, and any coupon satisfying all three predicates is appended, so no valid coupon is omitted.

The tuple sort first orders by the category strings, whose alphabetical order equals the mandated category priority, and then orders equal-category entries by code. The final projection preserves that sorted index order. These facts prove both membership and ordering correctness.

**Difference from grouping by category**

The local editorial creates four separate code lists, sorts each, and concatenates them in rank order. The exact Optimal source uses a single valid-index list and one tuple sort. Both implement the same requested ordering, but the source's correctness depends on the four category labels already appearing in the desired lexicographical sequence.

## Complexity detail

Let `n` be the number of coupons, `v` the number that are valid, `S` the total number of characters inspected across code validation and category hashing, and `L` an upper bound on the number of characters compared for one sorting-key comparison.

Filtering costs `O(n + S)` time. The constant-size category set uses expected constant-time membership apart from hashing the business-line string. Code validation scans each examined code at most once and may stop early.

Sorting `v` indices performs `O(v\log v)` key comparisons in the comparison model. Comparing the business-line and code strings can require `O(L)` character work, so a safe bound is:

$$
O(S + vL\log v).
$$

The final list comprehension costs `O(v)` and is dominated. This matches the manifest.

`idx` holds `v` integers, and sorting creates `O(v)` key/reference workspace in Python. The returned list also has `v` references. Excluding output, auxiliary space is `O(v)`; the four-element category set is `O(1)`.

## Alternatives and edge cases

- **Four category buckets:** Use an explicit rank map, append codes to four lists, sort each list, and concatenate. This remains correct even if the category names' alphabetical order differs from their required priority.
- **Explicit numeric category rank:** Sort by `(rank[businessLine[i]], code[i])`. It makes the custom order obvious and is safer against future category renaming.
- **Regular expression validation:** A full match such as an ASCII-constrained alphanumeric/underscore pattern can be concise, but the character loop makes early rejection and the allowed symbols explicit.
- **Use `str.isalnum`:** Under the printable-ASCII guarantee, `c.isalnum() or c == "_"` is equivalent to the source's separate letter and digit checks.
- **Empty code:** `check` rejects it before entering the loop.
- **Underscore-only code:** A non-empty string such as `"_"` satisfies the stated character rule and is accepted.
- **Space, hyphen, or `@` in a code:** None is a letter, digit, or underscore, so the code is rejected.
- **Inactive but otherwise valid coupon:** The first condition rejects it, and its code is not scanned.
- **Invalid business line:** Set membership rejects it even when the code and active flag are valid.
- **Category capitalization:** `"Electronics"` is different from `"electronics"` and is not in the allowed set.
- **Duplicate valid codes:** Their separate indices are retained, so duplicate strings appear separately in the output.
- **Same code in different categories:** Category order determines which occurrence appears first.
- **Prefix codes:** Within one category, `"SAVE"` sorts before `"SAVE20"` because the shorter string is a prefix.
- **Uppercase and lowercase:** Python's ASCII-compatible lexicographical comparison is case-sensitive; uppercase letters sort before lowercase letters.
- **All coupons invalid:** `idx` stays empty, sorting does nothing, and the result is an empty list.
- **One valid coupon:** It is returned directly after a harmless one-element sort.
- **Equal-length-array contract:** The source relies on it; otherwise `zip` would silently ignore entries beyond the shortest array.
- **Future category changes:** Direct string sorting is correct only while the required order matches alphabetical order; an explicit rank map avoids that hidden dependency.
- **Input preservation:** The algorithm sorts only the index list. It never reorders or modifies `code`, `businessLine`, or `isActive`.
