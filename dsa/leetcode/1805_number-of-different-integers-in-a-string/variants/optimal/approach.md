## General

**An integer is one maximal run of digits**

Letters act as separators. Each maximal consecutive digit run represents one integer, so the solution scans the string with indices rather than actually replacing letters with spaces.

A set `s` stores one canonical string for every distinct integer encountered. Canonicalization is necessary because `"1"`, `"01"`, and `"001"` represent the same numerical value.

**Skip leading zeros before capturing the run**

When index `i` points to a digit, the first inner loop advances `i` while the current character is `'0'`. After that:

- `i` points to the first nonzero digit of the same run;
- or `i` points to the separator after the run;
- or `i == n` when the all-zero run reaches the string's end.

The solution sets `j = i` and advances `j` through all remaining digits. It inserts slice `word[i:j]` into the set.

For a run such as `"000123"`, the slice is `"123"`. For `"45"`, no zero is skipped and the slice remains `"45"`.

**Why an all-zero integer becomes the empty string**

If a digit run contains only zeros, the leading-zero loop consumes the entire run. Then `j == i` and `word[i:j]` is `""`.

This is intentional and correct as a set key. Every all-zero representation—`"0"`, `"00"`, or `"0000"`—becomes the same empty string, while no positive integer becomes empty. The empty string therefore acts as the canonical representation of numerical zero.

Using `"0"` instead would also be understandable, but the exact protected code uses `""` and still produces the correct distinct count.

**Pointer movement avoids rescanning**

After inserting a digit run, the solution assigns `i = j`. At that moment, `i` is at the first following letter or at the end. The common `i += 1` at the bottom skips that separator.

If the current character is a letter from the beginning, no digit work occurs and the same bottom increment simply advances to the next character.

Digit runs and letters are therefore visited a constant number of times. No run is parsed twice.

**Following the examples**

For `"a123bc34d8ef34"`, the recorded canonical slices are `"123"`, `"34"`, `"8"`, and `"34"`. The set removes the repeated `"34"`, leaving size three.

For `"a1b01c001"`, the runs normalize to `"1"`, `"1"`, and `"1"` after leading zeros are skipped. Set size is one.

For a string such as `"a000b0c12"`, both zero runs add `""` and the positive run adds `"12"`. The answer is two distinct integers: zero and twelve.

**Why string normalization is preferable to integer conversion here**

The method never calls `int`. Comparing canonical decimal strings is enough: two nonnegative decimal integers are equal exactly when their representations after removing leading zeros are equal, with all-zero runs sharing one zero representation.

Avoiding numeric conversion also avoids dependence on fixed-width limits or language rules for extremely long digit strings. The stated input length is moderate, but the representation-level reasoning remains robust.

**Why the returned set size is correct**

Every maximal digit run is found once. Removing all leading zeros maps equal numerical values to the same canonical string. Different positive integers have different remaining decimal strings, and zero alone maps to empty.

Thus two runs produce the same set entry if and only if they represent the same integer. The number of set entries is therefore exactly the number of different integers.

## Complexity detail

Let $n$ be `len(word)`. Pointer scans cover disjoint portions of the string. Slicing and hashing a canonical run take time proportional to that run's retained length, and retained runs have total length at most $n$. Expected total time is $O(n)$.

The set and its stored string slices can contain $O(n)$ total characters in the worst case, so auxiliary space is $O(n)$. These bounds match the manifest.

Python's broader `isdigit` behavior is harmless because valid input contains only ASCII digits and lowercase letters.

## Alternatives and edge cases

- **Replace letters and split:** It is concise but creates another full string plus token lists; the pointer scan controls normalization directly.
- **Convert runs to integers:** It naturally removes leading zeros, but string normalization avoids large-integer parsing and is sufficient for equality.
- **Regular expression extraction:** It finds digit runs but adds regex machinery and still needs canonicalization.
- **Keep raw runs:** This incorrectly treats `"1"` and `"001"` as different.
- **All-zero run:** It becomes the empty-string key representing zero.
- **Several all-zero runs:** They all share one set entry and count once.
- **No digits:** No set entry is added, so the answer is zero.
- **Entire string is digits:** One run is normalized and counted once.
- **Digit at the end:** The scan reaches `n` safely and the bottom increment terminates the loop.
- **Adjacent letters:** Each is merely skipped; they do not create empty integers.
- **Repeated positive integer:** Identical canonical slices collapse in the set.
- **Different lengths after normalization:** They necessarily represent different positive integers.
- **Zero followed by nonzero digits in one run:** Leading zeros are discarded but the remaining digits stay together.
- **No signs or decimal points:** The input contract makes every digit run a nonnegative integer.
- **Input preservation:** Slices are read from `word`; the original string is unchanged.
