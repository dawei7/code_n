## General
**Turn every rotation into a substring**

Write two copies of `s` consecutively. Every length-`n` cyclic rotation starts somewhere among the first `n` positions of $s + s$: the suffix after a chosen cut is followed immediately by the prefix before that cut. Therefore, after confirming equal lengths, the task is to find `goal` inside $s + s$.

**Search without restarting comparisons**

Build the Knuth-Morris-Pratt prefix table for `goal`. At each pattern position, the table records the length of the longest proper prefix that is also a suffix. When a mismatch occurs, this table moves the pattern to the longest alignment that could still match instead of rescanning text characters.

If KMP matches all of `goal`, its starting position in the doubled text describes a valid cut of `s`, so the target is a rotation. Conversely, every legal sequence of front-to-back moves chooses one such cut, and that rotation appears contiguously in $s + s$. Thus the substring test accepts exactly the reachable targets.

## Complexity detail
Let `n` be the length of `s`. Building the prefix table and scanning the doubled string each take $O(n)$ time. The doubled text and prefix table use $O(n)$ auxiliary space.

## Alternatives and edge cases
- **Built-in substring search:** Checking `goal in s + s` is concise and usually highly optimized, but an explicit KMP implementation makes the worst-case linear bound independent of library behavior.
- **Generate every rotation:** Constructing and comparing all `n` rotations is correct but can take $O(n^2)$ time because each constructed string has length `n`.
- **Repeated deque shifts:** Simulating one move at a time still compares up to `n` full states and has the same quadratic worst case.
- **Different lengths:** Rotation never changes length, so unequal lengths must return `False` before searching.
- **No shifts:** Equal strings are valid rotations because applying the operation zero times is permitted.
- **Repeated characters:** Several cuts may produce the same string; finding any one matching alignment is sufficient.
- **Single character:** Its only rotation is itself.
