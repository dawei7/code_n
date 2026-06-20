# Run Length Encoding

| | |
|---|---|
| **ID** | `string_09` |
| **Category** | strings |
| **Complexity (required)** | $O(N)$ Time, $O(N)$ Space |
| **Difficulty** | 2/10 |
| **Interview relevance** | 4/10 |
| **GeeksForGeeks Equivalent** | [Run Length Encoding](https://www.geeksforgeeks.org/run-length-encoding/) |

## Problem statement

Given a string `s`, perform **Run Length Encoding** (RLE) on it.
RLE is a simple form of data compression where runs of data (sequences in which the same data value occurs in many consecutive data elements) are stored as a single data value and count.
For example, `"wwwwaaadexxxxxx"` should become `"w4a3d1e1x6"`.

**Input:** A string `s`.
**Output:** A compressed string.

## When to use it

- To heavily compress strings or arrays that contain massive, contiguous blocks of repeated identical values.
- As a foundational algorithmic warm-up question in entry-level interviews.

## Approach

**1. The Contiguous Block Counter:**
We need to iterate through the string and count how many times a character repeats consecutively.
We can maintain a pointer `i` that iterates from `0` to `N-1`.
We maintain a counter `count` initialized to `1`.
At every character `s[i]`, we look ahead to the next character `s[i+1]`.
- If `s[i] == s[i+1]`, it's part of the same run! We increment `count` and move `i` forward.
- If `s[i] != s[i+1]`, the run has mathematically ended! We take the character `s[i]`, convert the `count` to a string, append both to our output string, and safely reset `count` back to `1` for the next character's run!

**2. The End-of-String Edge Case:**
When `i` reaches the very last character (`N-1`), there is no `s[i+1]` to check! Attempting to access it will crash the program with an `IndexOutOfBounds` error.
To fix this, our `for` loop should only go up to `N-2` (the second to last character).
Wait, if the loop stops at `N-2`, how does the last run get added? We can just append the final character `s[N-1]` and whatever `count` remains immediately after the loop terminates!

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for string_09: Run-Length Encoding.

Walk the string, counting consecutive equal chars.
"""


def solve(s):
    if not s:
        return ""
    out = []
    cur = s[0]
    count = 1
    for c in s[1:]:
        if c == cur:
            count += 1
        else:
            out.append(cur + str(count))
            cur = c
            count = 1
    out.append(cur + str(count))
    return "".join(out)
```

</details>

## Walk-through

`s = "AABCCC"`
`n = 6`. Array `[]`. `count = 1`.

1. `i = 0`: `s[0] = 'A'`, `s[1] = 'A'`. Match!
   - `count = 2`.
2. `i = 1`: `s[1] = 'A'`, `s[2] = 'B'`. Mismatch!
   - Append `'A'` and `"2"`. Output `["A", "2"]`.
   - `count = 1`.
3. `i = 2`: `s[2] = 'B'`, `s[3] = 'C'`. Mismatch!
   - Append `'B'` and `"1"`. Output `["A", "2", "B", "1"]`.
   - `count = 1`.
4. `i = 3`: `s[3] = 'C'`, `s[4] = 'C'`. Match!
   - `count = 2`.
5. `i = 4`: `s[4] = 'C'`, `s[5] = 'C'`. Match!
   - `count = 3`.
6. Loop terminates (reached `n - 2`).
7. Execute post-loop boundary push:
   - Append `s[5]` (`'C'`) and `count` (`"3"`).
   - Output `["A", "2", "B", "1", "C", "3"]`.

Final string: `"A2B1C3"`. ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(N)$ | $O(N)$ |
| **Average** | $O(N)$ | $O(N)$ |
| **Worst** | $O(N)$ | $O(N)$ |

The array is traversed exactly once. Comparisons and array appends take $O(1)$ constant time. String joining at the end takes $O(N)$ time.
Time complexity is strictly $O(N)$.
Space complexity is $O(N)$ because strings are immutable in most languages (Python, Java, C#), so an auxiliary `encoded_chars` array of size up to 2N must be created to hold the intermediate result before joining it into the final returned string.

## Variants & optimizations

- **In-Place Modification:** If the language uses mutable strings (like C++ `std::string` or a pre-allocated `char[]`), you can technically do this in $O(1)$ space using Two Pointers (a read pointer and a write pointer), provided the compressed string is guaranteed to be shorter than the original string.
- **Decoding (String Compression II):** The reverse operation. Given `"A2B1C3"`, generate `"AABCCC"`. You iterate, read the character, parse the following integer, and execute a `for` loop to append the character that many times.

## Real-world applications

- **Fax Machines / Bitmaps:** Standard black-and-white fax transmission uses RLE. Instead of sending 1000 white pixels individually, it sends `[White, 1000]`. This reduces massive image files by 99% during transmission!
- **JPEG Encoding:** After Discrete Cosine Transform quantization, image data contains massive blocks of consecutive zeroes. RLE is applied before Huffman Coding to instantly squash the zeroes.

## Related algorithms in cOde(n)

- **[two_pointers_05 - Remove Duplicates from Sorted Array](../two_pointers/two_pointers_05_remove-duplicates.md)** — A functionally identical algorithm, but instead of counting the run, you just overwrite the array to delete the run entirely.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
