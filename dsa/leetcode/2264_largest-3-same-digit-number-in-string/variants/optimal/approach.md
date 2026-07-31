## General

**A good value is determined by one digit**

Every candidate has the form `ddd`, so comparing two candidates is equivalent
to comparing their repeated digit. There is no need to parse the three
characters as an integer, and `"000"` can be preserved without a special
numeric representation.

Scan each possible starting index and compare the three characters directly.
When all are equal, compare that digit with the best digit seen so far. At the
end, repeat the best digit three times; if no candidate was found, repeating
the empty string naturally returns `""`.

Every length-three substring is examined once, so every good integer is
considered. The stored digit is replaced only by a larger candidate digit and
therefore remains the maximum among all windows already visited. After the
final window it represents the globally largest good integer.

## Complexity detail

Let $n=\lvert\texttt{num}\rvert$. There are $n-2$ constant-size windows, so the
scan takes $O(n)$ time. Only the best digit and loop index are retained, using
$O(1)$ auxiliary space.

## Alternatives and edge cases

- **Search `"999"` through `"000"`:** Checking ten fixed patterns also has linear worst-case time, but may rescan the string repeatedly.
- **Regular expression runs:** A run matcher can identify repeated digits, but direct window comparisons are simpler and avoid regex machinery.
- **No qualifying window:** Return `""`.
- **Only zero qualifies:** Return `"000"`, not `"0"` or an empty result.
- **Several candidate digits:** Choose the largest digit, regardless of occurrence order.
- **Overlapping windows:** A run of four equal digits contains two good windows but yields the same result.
- **Exactly three characters:** The whole input is the only possible window.
- **Longer run:** Any three consecutive characters inside it form the same good integer.
