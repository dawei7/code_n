## General
**Translate the rule key into one column**

The item schema fixes type at index `0`, color at index `1`, and name at index `2`. Map `ruleKey` to that index once before scanning instead of checking the key separately for every row.

**Inspect exactly the selected attribute**

For each item, compare `item[field_index]` with `ruleValue` using exact string equality. Add one to the count when they match. The other two fields are deliberately ignored, so a requested value appearing in the wrong attribute cannot cause a false match.

**Accumulate one complete count**

Each row is visited once and contributes either zero or one according to the rule's definition. The fixed mapping selects the contractually correct field, so the final sum includes every matching item and no nonmatching item.

## Complexity detail
The scan performs one constant-time field access and bounded-length string comparison for each of the $n$ items, giving $O(n)$ time. Apart from the returned integer, the field index and running count use $O(1)$ space.

## Alternatives and edge cases
- **Branch on `ruleKey` inside the loop:** This is correct but repeats the same three-way decision for every item.
- **Build dictionaries for every item:** Named fields may improve readability, but allocating transformed rows adds unnecessary $O(n)$ space.
- **Value in the wrong field:** A name equal to `ruleValue` does not match a type rule.
- **No matches:** The accumulator remains zero.
- **Every item matches:** The result equals the number of item rows.
- **Repeated identical rows:** Each row is a separate item and contributes independently.
- **Exact string comparison:** Prefixes, substrings, and different attribute values do not match.
- **Single item:** The same field mapping and comparison apply without a special case.
