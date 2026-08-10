## General

**Replace repeated searching with fixed alphabet sweeps**

The required process repeatedly takes one copy of each available character in increasing order, then one copy of each available character in decreasing order. Since the input contains only lowercase English letters, there are just 26 possible choices. A frequency table is enough to represent the remaining multiset of characters; their original positions are irrelevant.

`Counter(s)` builds `cnt`, where `cnt[c]` is the number of unused copies of character `c`. Removing a character is simulated by appending it to `ans` and subtracting one from its counter. The original string never needs physical deletion.

The string `cs = ascii_lowercase + ascii_lowercase[::-1]` encodes one complete cycle. Its first half is `a` through `z`, exactly the increasing phase. Its second half is `z` through `a`, exactly the decreasing phase. The loop visits every possible character in that order and takes it if `cnt[c]` is positive.

**Why one alphabet visit implements “smallest greater”**

During the forward half, letters are examined from smallest to largest. The first available letter is therefore the smallest remaining character. After taking it, scanning continues strictly to later alphabet positions, so the next available letter is the smallest remaining character greater than the last appended one. Each letter position is visited only once in that half, preventing two equal copies from being taken during one increasing sweep.

The reverse half is symmetric. It begins at the largest letter and scans toward smaller letters. The first available letter is the largest remaining one, and every later chosen letter is the largest available character smaller than the preceding choice.

The two copies of `z` at the boundary of `cs` are deliberate. The forward phase may take one `z` as its final, largest choice. If another `z` remains, the decreasing phase is allowed to begin by taking one largest remaining character, which may also be `z`. Likewise, `a` appears at the end of the reverse half and again at the beginning of the next cycle. Consecutive equal letters across phase boundaries are valid even though equal letters cannot repeat inside one strictly increasing or decreasing phase.

**Why the outer loop stops at exactly the right time**

`ans` receives one character for every decrement of a counter. No character is invented and no available copy is used more than once. The loop condition `len(ans) < len(s)` therefore means some input copies remain. Every remaining lowercase character occurs somewhere in `cs`, so a traversal always appends at least one character until all counts reach zero. Once the two lengths match, every original copy has been emitted and the loop ends.

For `"aaaabbbbcccc"`, the first forward half takes `abc` and the reverse half takes `cba`, producing `"abccba"`. The counts are then two for each letter, so the next traversal repeats the same pattern and completes `"abccbaabccba"`.

**Why the result is correct**

At the beginning of each forward phase, scanning the alphabet from `a` to `z` chooses exactly one copy of each available distinct character in increasing order. This is precisely the repeated “smallest, then smallest greater” rule until no greater character remains. The reverse scan then chooses exactly one copy of each still-available distinct character in decreasing order, precisely implementing the corresponding largest-character rules.

Counter decrements make the remaining multiset after a phase identical to the multiset produced by physically removing the chosen occurrences. Repeating full forward-and-reverse traversals until the number emitted equals the input length therefore simulates every specified step and returns the required reordered string.

## Complexity detail

Let $n$ be the string length, $A=26$ the alphabet size, and $F$ the maximum frequency of any character. Building the counter and joining the answer each take $O(n)$ time. Every outer iteration scans the $2A$ characters in `cs`. No character can require more than roughly $F$ phase cycles before all of its copies are removed, so the scanning cost is $O(AF)$. Total time is

$$
O(n+AF),
$$

matching the manifest. With the fixed lowercase alphabet, $A$ is constant and $F\le n$, so this simplifies to $O(n)$.

The counter has at most $A$ entries and `cs` has length $2A$, giving $O(A)$ auxiliary state apart from the answer. `ans` stores $n$ output characters before joining; if output construction is included, total newly allocated space is $O(n+A)$, which simplifies to $O(n)$. The manifest's $O(A)$ convention excludes required output storage.

## Alternatives and edge cases

- **Repeatedly sort remaining characters:** It directly exposes the smallest and largest choices but wastes work by sorting after removals, potentially becoming much slower.
- **Ordered set plus frequencies:** Maintain the currently available letters in a balanced structure and traverse it both ways. This generalizes to a large alphabet but is unnecessary for 26 fixed letters.
- **Explicit two loops:** Scan `ascii_lowercase` and then its reverse in separate loops. It is equally correct and may make the phase boundary clearer; the exact solution concatenates them into `cs`.
- **One character:** The forward sweep takes it and the outer loop ends immediately.
- **All characters equal:** A cycle can take one copy in the forward occurrence and another in the reverse occurrence of that letter. The unchanged output is still the required result.
- **Missing alphabet ranges:** Zero counters are simply skipped, so gaps such as between `a` and `z` do not affect strict ordering.
- **Repeated maximum letter:** One copy may end the increasing phase and another may begin the decreasing phase, explaining adjacent equal maxima.
- **Repeated minimum letter:** One copy may end the decreasing phase and another begin the next increasing phase.
- **Input immutability:** Only `cnt` is changed. Strings are immutable, and `s` remains untouched.
- **Lowercase guarantee:** The traversal includes only lowercase English letters. Unexpected characters outside that alphabet would never be appended and would make the loop fail to finish.
- **Required names:** The environment must provide `Counter` and `ascii_lowercase`, normally from `collections` and `string` respectively.
