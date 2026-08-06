## Examples

**Example 1**

- **Input:** Three files contain valid `bull` occurrences; the second and third also contain valid `bear` occurrences.
- **Output:**
  | word | count |
  | --- | --- |
  | bull | 3 |
  | bear | 2 |
- **Explanation:** Each qualifying file contributes once to the corresponding count.

**Example 2**

- **Input:** `Files = [("one.txt", " a bull bull bear bear z ")]`
- **Output:**
  | word | count |
  | --- | --- |
  | bull | 1 |
  | bear | 1 |
- **Explanation:** Repetition inside one file does not increase the number of matching files.

**Example 3**

- **Input:** `Files = [("edges.txt", "bull starts while bears and bull. fail bear")]`
- **Output:**
  | word | count |
  | --- | --- |
  | bull | 0 |
  | bear | 0 |
- **Explanation:** Targets at text boundaries, embedded in words, or adjacent to punctuation fail the space-enclosed rule.
