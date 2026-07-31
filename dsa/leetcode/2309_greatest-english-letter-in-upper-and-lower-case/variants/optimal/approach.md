## General

**Record which characters occur**

Insert every character from `s` into a set. Uppercase and lowercase forms are
distinct entries, so presence queries preserve the case distinction required
by the contract.

**Search in the requested order**

Visit uppercase letters from `Z` down through `A`. For each `L`, test whether
both `L` and `L.lower()` are present. Return the first match. Descending order
makes that first match the greatest qualifying letter; if the scan finishes,
no letter has both forms and the correct result is empty.

The set exactly represents all observed forms. A returned letter therefore
qualifies, and every greater letter was tested and rejected first. If nothing
is returned during the scan, each of the 26 letters lacks at least one form.

## Complexity detail

Let $n=\lvert\texttt{s}\rvert$. Building the presence set takes $O(n)$ time.
The alphabet scan has 26 constant-time expected lookups, so total expected time
is $O(n)$. At most 52 English-letter characters are stored, giving $O(1)$
auxiliary space for the fixed alphabet.

## Alternatives and edge cases

- **Rescan for each letter:** Testing both forms with repeated string scans is correct but can take $O(26n)$ time; the fixed alphabet still makes it linear, though with more work.
- **Compare every character pair:** Searching for an opposite-case partner from each position can take $O(n^2)$ time.
- **Two bitmasks:** Separate 26-bit lowercase and uppercase masks also give $O(n)$ time and $O(1)$ space.
- **Only one case:** Repeated occurrences of one form do not qualify without the other form.
- **Several qualifying letters:** Alphabetical order, not position or frequency, decides the result.
- **Output case:** The returned character must be uppercase even if its lowercase occurrence appears later.
- **No match:** Return the empty string rather than a sentinel letter.
- **Repeated characters:** Duplicates do not change presence.
