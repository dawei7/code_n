## General

**Convert letters into positions once**

The keyboard string is a permutation of all 26 lowercase English letters. Its index is the physical position of each key. To type quickly, the algorithm needs to answer “where is this character?” for every character of `word`.

Searching `keyboard` from the beginning for each typed character would repeatedly scan up to 26 positions. Although 26 is fixed, a direct position table is clearer and avoids repeated lookup work.

The dictionary comprehension

`{c: i for i, c in enumerate(keyboard)}`

creates a mapping from each letter `c` to its index `i`. Because every lowercase letter appears exactly once, every key has one unambiguous position and no dictionary entry is overwritten by a duplicate.

**Track the finger's current position**

The assignment `ans = i = 0` initializes both the accumulated time and the current finger position to zero. The starting position is an index, not necessarily the key `a`; whichever character appears at `keyboard[0]` is under the finger initially.

For each target character `c`, `pos[c]` is the destination key index. The movement time is the absolute distance

`abs(pos[c] - i)`.

This value is added to `ans`. Then `i = pos[c]` updates the current position because the finger remains on the key just typed and starts the next movement there.

No separate time is charged for pressing a key. The contract defines cost only as movement distance.

**Why absolute difference is exact**

All keys lie in one row at integer positions zero through 25. Moving from index `i` to index `j` requires crossing exactly `|i - j|` adjacent position gaps.

There is only one dimension and no shorter route around the row, so the absolute difference is both a lower bound and an achievable movement cost. The solution applies precisely the metric provided by the problem.

**Trace the first example**

On the alphabetically ordered keyboard, the finger begins at index zero.

Typing `c` moves from zero to two and costs two. Typing `b` then moves from two to one and costs one. Typing `a` moves from one back to zero and costs one. The accumulated time is four.

If two consecutive word characters are equal, the first leaves the finger on that key. The second has destination equal to `i`, so its movement cost is zero.

**Why summing local movements is globally correct**

The word's character order is fixed, and each character has exactly one keyboard position. After typing character `t`, the finger must be at that character's key; there is no alternative endpoint that could trade a longer current move for a shorter future route.

Therefore, the complete typing path is uniquely determined:

`0 -> pos[word[0]] -> pos[word[1]] -> ...`.

The total time is the sum of the distances of its consecutive moves. The loop accumulates exactly those terms and updates the start of each term to the preceding destination. When all characters have been processed, `ans` is the exact typing time.

**Why the preprocessing matches the constraints**

Every word character is lowercase, and the keyboard contains each lowercase letter once. Thus `pos[c]` always exists. The code needs no missing-key branch and no handling for multiple locations of one character.

The fixed 26-key layout also matters for complexity: building the position dictionary is bounded work and bounded storage independent of word length.

**Repository-designated complexity context**

This problem is listed in the repository's original complexity-blocker playbook. The current task is limited to teaching the existing optimal approach, so it does not inspect, modify, or make new claims about the package's benchmark or certificate artifacts.

The algorithmic explanation remains straightforward: after a fixed-size keyboard preprocessing step, every required word character must be read and contributes one distance calculation.

## Complexity detail

Let `m = len(word)`. Enumerating the keyboard always processes exactly 26 characters, which is `O(1)` under the fixed lowercase alphabet. The typing loop processes each of the `m` word characters once with expected constant-time dictionary lookup and arithmetic. Total time is `O(m)`.

The `pos` dictionary holds exactly 26 entries, and all other state consists of a few integers and the loop character. Its size does not grow with `m`, so auxiliary space is `O(1)`.

The input strings are read but not copied or modified.

The linear time is also information-theoretically natural: changing the last word character can change the result, so a correct general algorithm must inspect the word through its final position.

## Alternatives and edge cases

- **Call `keyboard.index(c)` for every character:** This is correct and each scan is bounded by 26, so it is still `O(m)` under the fixed alphabet. The position map avoids repeated scans and makes the data flow explicit.
- **Use a 26-element integer array:** Store positions at `ord(c) - ord("a")`. This has the same bounds and may have lower lookup overhead than a dictionary.
- **Simulate one adjacent step at a time:** It reproduces the distance but performs unnecessary per-position updates. Absolute difference computes the same cost directly.
- **Finger begins at index zero:** It does not begin at the position of `a` unless `a` happens to be the first keyboard character.
- **First word character is already at index zero:** Its first movement contributes zero.
- **Repeated consecutive characters:** Every repeat after the first costs zero movement.
- **Word of length one:** The result is simply the distance from position zero to that key.
- **Arbitrary keyboard permutation:** The dictionary captures the supplied layout; no alphabetical-order assumption is made.
- **Every word key exists:** The permutation and lowercase-word guarantees make dictionary lookup safe.
- **Maximum word length:** The algorithm retains constant state and performs one arithmetic update per character.
