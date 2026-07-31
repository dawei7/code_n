## General

Every record uses the same fixed-width layout, so no delimiter parsing or search is necessary. The age is always the two-character slice `detail[11:13]`. Convert that slice to an integer and test it against the strict threshold 60 while scanning the list once.

Maintain a counter initialized to zero. For each record, add one exactly when its decoded age is greater than 60. Each record contributes independently, and the fixed field positions guarantee that the decoded value is that passenger's age. After all records have been examined, the counter therefore equals precisely the number of qualifying passengers.

## Complexity detail

Let $n$ be the number of passenger records. Extracting and converting a fixed two-character field takes constant time, so processing all records takes $O(n)$ time. The running count and current age use $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Compare the age substring lexicographically:** Because every age has exactly two decimal digits, `detail[11:13] > "60"` is valid and avoids conversion, though numeric comparison states the intent more directly.
- **Decode individual digits:** Computing the tens and ones digits manually also takes $O(n)$ time but is more verbose than parsing the two-character slice.
- **Repeated full scans:** Rechecking the entire list for each passenger can still produce the right count but wastes $O(n^2)$ time.
- **Strict boundary:** Age 60 must not be counted; the comparison is `> 60`, not `>= 60`.
- **Fixed positions:** Gender is at index 10, while age occupies indices 11 and 12. Reading from index 10 would mix a letter into the age field.
