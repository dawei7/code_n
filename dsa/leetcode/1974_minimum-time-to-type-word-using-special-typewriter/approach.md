## General

**Separate typing time from movement time**

Every character in `word` must be typed exactly once and typing the current character always costs one second. If the word length is $N$, the unavoidable typing cost is therefore $N$ seconds, regardless of the route taken by the pointer.

The source places this fixed cost into the answer immediately with `ans = len(word)`. The loop then adds only the minimum pointer movement required before each character. Keeping these costs separate makes it harder to forget the typing second, especially when the pointer is already on the next requested letter.

**Represent positions by character codes**

Lowercase English letters occupy consecutive code points. `ord("a")` is the numeric position used for the initial pointer, and `map(ord, word)` lazily converts each target character to its numeric position.

The variable `a` is not permanently the code for the letter a. It starts as `ord("a")` because that is the pointer's initial position, but after each iteration `a = c` changes it to the code of the character just typed. Thus, at the beginning of every iteration, `a` represents the current pointer location and `c` represents the next required location.

**There are two routes around the circle**

For two positions, the straight alphabetical distance is

`d = abs(c - a)`.

This is the number of one-step moves along the direct interval between the letters. Because the alphabet is a cycle containing 26 positions, traveling the other way uses the remaining edges and costs `26 - d`.

The least possible movement is therefore

$$
\min(d, 26-d).
$$

For example, moving from a to b has direct distance one and wraparound distance 25, so one step is optimal. Moving from a to z has direct distance 25 but wraparound distance one, so the counterclockwise move is optimal.

When the letters are the same, $d=0$. The formula chooses zero rather than 26, correctly adding no movement. The character still costs its already-counted one second to type.

**Why choosing the shortest route for each character is globally optimal**

The characters must be typed in the order given. After typing a particular target, the pointer is necessarily located on that target character, regardless of whether it arrived clockwise or counterclockwise. That means the choice of route for the current transition cannot improve or worsen the starting position for the next transition.

The total cost can be written as a fixed typing term plus independent transition terms:

$$
N+\sum_{i=0}^{N-1}\operatorname{dist}(p_i,w_i),
$$

where $p_0$ is a and, for $i>0$, $p_i$ is the previous character. Since one transition's route has no effect on any later transition endpoint, minimizing every term separately minimizes their sum. There is no hidden reason to take a longer route now to save time later.

**Trace `"bza"`**

The answer begins at 3 because three characters must be typed.

From a to b, $d=1$, so the loop adds one. The pointer state becomes b. From b to z, the direct distance is 24, while wrapping costs two through a; the loop adds two. From z to a, wrapping costs one, so it adds one more.

The movement total is four, and the fixed typing total is three, producing seven seconds.

**Trace a longer transition**

From p to c, the direct code difference is 13. The other direction also has length $26-13=13$. Either route is optimal. The formula does not need to choose an actual direction because the problem asks only for the minimum time, and both choices end at c.

This also explains why the answer can be calculated without simulating the pointer one letter at a time. Counting the edges on the shorter arc produces exactly the same movement cost.

**Read the loop invariant**

Before processing each loop character, `ans` equals the typing cost for the entire word plus the minimum movement cost for all previously processed transitions, and `a` is the position of the last processed character or the initial a.

The loop computes the exact shortest distance to `c`, adds it, and assigns `a = c`. The invariant is preserved. When all characters are processed, every required transition and every typing action has been counted, so `ans` is the minimum total time.

## Complexity detail

Let $N$ be `len(word)`. The loop visits each character once and performs constant-time arithmetic, so time is $O(N)$. Any correct solution must at least inspect the requested characters, making this asymptotically optimal.

`map(ord, word)` is lazy and does not construct a list of all codes. Apart from the returned integer and the scalar variables `ans`, `a`, `c`, and `d`, no storage grows with the input. Auxiliary space is $O(1)$.

## Alternatives and edge cases

- **Simulate one pointer step at a time:** It can produce the same answer, but it is more code and obscures the direct circular-distance formula.
- **Dynamic programming:** It is unnecessary because every typed character fixes the next pointer position; there are no competing states to retain.
- **Always move clockwise:** This fails badly near the a-z boundary, where counterclockwise may take one step instead of 25.
- **Always use absolute code difference:** This treats the alphabet as a line and misses the wraparound route; use `min(d, 26 - d)`.
- **First character is a:** No movement is needed, but its one-second typing cost is already included.
- **Repeated character:** Consecutive identical letters add zero movement and one typing second each.
- **a-to-z or z-to-a:** The circular distance is one.
- **Opposite letters:** When $d=13$, both directions are equally short and either is valid.
- **One-character word:** The initial `len(word)` handles typing, and the loop adds only its movement from a.
- **Maximum word length:** Linear work over at most 100 characters is easily bounded.
- **Lowercase guarantee:** Consecutive codes and a cycle length of 26 are valid because every input character is from a through z.
- **Input preservation:** The method iterates over the immutable string and does not alter it.
