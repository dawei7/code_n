## General

**What makes an integer fair**

An integer is fair when its decimal representation contains the same number of even and odd digits. Zero is an even digit. Because every digit belongs to exactly one of the two groups, a fair integer must have an even total number of digits. This observation explains the solution's important shortcut for an odd-length input.

The exact protected solution is a recursive candidate search with an odd-length jump. It does not implement the bounded digit-construction algorithm described by the variant summary, so its real behavior and costs must be understood from the code itself. Each call counts the odd digits in `a`, the even digits in `b`, and the number of digits in `k`. It does so by repeatedly inspecting `t % 10` and removing that last digit with `t //= 10`.

The test `(t % 10) & 1` is 1 precisely when the last digit is odd. In that case `a` increases; otherwise `b` increases. Since the input is positive, the loop runs once for every decimal digit. After it ends, `a + b = k`.

**Why an odd digit count permits a direct jump**

If `k` is odd, no `k`-digit number can be fair: splitting an odd number of digit positions into two equal integer counts is impossible. Therefore the answer must have more than `k` digits. The smallest possible next length is `k + 1`, which is even.

The code sets `x = 10**k`. Its decimal form is a leading `1` followed by `k` zeros, so it is the smallest number with `k + 1` digits. At this point it has one odd digit and `k` even digits. The code then constructs

`y = int('1' * (k >> 1) or '0')`.

Because `k` is positive and odd for every valid call reaching this branch, `k >> 1` is $\lfloor k/2 \rfloor$. Adding this suffix-sized number turns the last $\lfloor k/2 \rfloor$ zeros of `x` into ones without carrying. The result consists of a leading one, then $\lceil k/2 \rceil$ zeros, then $\lfloor k/2 \rfloor$ ones. Since $k$ is odd, the total number of ones is

$$
1 + \left\lfloor \frac{k}{2} \right\rfloor
= \frac{k+1}{2},
$$

and the number of zeros is also $(k+1)/2$. The constructed number is therefore fair.

It is also the smallest fair number of that new length. Every number with `k + 1` digits must begin with at least `1`. Choosing leading `1` is smallest. A fair result then needs $(k+1)/2 - 1$ additional odd digits and $(k+1)/2$ even digits. To minimize the remaining decimal positions lexicographically, all required even digits should be `0` and should appear as early as possible; the smallest usable odd digit is `1`, placed in the remaining suffix. Thus the returned pattern is minimal. For example, a three-digit candidate jumps to `1001`, the smallest fair four-digit integer.

**What happens when the length is even**

If `k` is even and `a == b`, the current `n` is already fair. Because the problem allows an answer equal to `n`, returning it is immediately optimal.

If the counts differ, the code calls `closestFair(n + 1)`. That recursive call performs the same digit count on the next integer. Repeating this operation tests consecutive values in strictly increasing order. Let `f` be the first fair integer at least as large as the original input. Every tested value before `f` is explicitly found not to be fair; when `f` is reached, the equality branch returns it. Hence no smaller valid candidate could have been skipped.

There is one transition worth following carefully. An even-length search can increment past a number made entirely of nines. The next value then has odd length. Rather than continuing through an entire digit-length range that contains no fair number, the odd-length branch jumps directly to the smallest fair number of the following even length. For instance, `99` is not fair. The recursion tests `100` next, recognizes its odd length, and returns `1001`.

The recursive search is therefore correct: the digit-count branch accepts exactly fair candidates; consecutive increments preserve minimality while the length is even; and the odd-length construction skips only numbers that cannot possibly be fair and lands on the smallest feasible number of the next length.

**A practical limitation of the exact implementation**

Although the reasoning above establishes mathematical correctness, recursion is a fragile way to perform the consecutive search in Python. Every non-fair even-length candidate adds another stack frame, and Python normally allows only around a thousand nested calls. A sufficiently long gap before the next fair number can therefore raise `RecursionError` even though a fair answer exists. This is an implementation limitation of the exact source, not a property of the problem.

It is also important not to describe this source as a direct $O(d^2)$ construction. It constructs only in the odd-length shortcut; otherwise it enumerates integers one at a time. A true digit-based construction is listed as an alternative below.

## Complexity detail

Let $d$ be the number of decimal digits of a candidate, and let $G$ be the number of consecutive non-fair even-length candidates examined before the search returns or reaches an odd-length shortcut. Counting one candidate's digits costs $O(d)$ time. The exact solution therefore takes $O(Gd)$ time in the search phase, plus $O(d)$ time to build the shortcut suffix. This is not the $O(d^2)$ time claimed in the local variant manifest.

The recursive call remains active while the next candidate is checked, so the recursion stack uses $O(G)$ space. Each frame otherwise stores only a constant number of integers, while the constructed string in the shortcut has $O(d)$ characters. Total auxiliary space is therefore $O(G + d)$, again differing from the manifest's $O(d^2)$ claim. An iterative version of the same enumeration would reduce stack usage to $O(1)$ apart from the constructed decimal string, but would retain the candidate-by-candidate running time.

The loose bound obtained by saying that at most an entire $d$-digit range is scanned is $O(d \cdot 10^d)$ time and $O(10^d)$ recursive depth. It is deliberately conservative; $G$ is the more informative parameter because the actual cost depends on the distance to the next fair integer.

## Alternatives and edge cases

- **Bounded digit construction:** Build the smallest decimal string at least `str(n)` with exactly half even and half odd digits, using a tight-prefix state and feasibility checks for the remaining counts. This avoids walking through the numeric gap and can achieve the intended polynomial-in-$d$ behavior, but it needs careful handling of the leading digit and backtracking when a chosen digit makes the suffix impossible.
- **Digit dynamic programming:** A memoized state such as position, remaining odd digits, and whether the prefix is still equal to the lower bound can determine feasibility, after which digits are greedily reconstructed from smallest to largest. This is more involved but matches the manifest's constructive description much better than the exact recursive enumeration.
- **Iterative enumeration:** A `while` loop that increments `n` until it is fair preserves the exact search logic while avoiding `RecursionError`. It still may inspect many candidates and therefore does not solve the time-complexity weakness.
- **Odd number of digits:** No value of that same length can be fair. The direct pattern of zeros followed by the required ones is both fair and the smallest feasible longer value.
- **Already fair:** The equality check returns `n` itself, which matters because the contract asks for greater than or equal to `n`, not strictly greater.
- **Digit zero:** Zero must count as even. The parity expression correctly classifies it that way whenever it occurs inside the positive integer.
- **One-digit input:** Every one-digit positive integer has one odd or one even digit and cannot be fair. The shortcut returns `10`, whose digits have opposite parity.
- **Carry across a power of ten:** Incrementing values such as `99` changes the digit count. The next recursive call recomputes all counts from scratch, so the odd-length shortcut is applied correctly.
- **Maximum stated input:** `10^9` has ten digits and is processed by the even-length branch. The answer may exceed the input constraint because the constraint limits only the argument, not the returned integer.
- **Manifest mismatch:** The local metadata says $O(d^2)$ time and space, but those bounds should not be used to reason about this exact Python file. Its candidate enumeration and recursive depth are observable parts of the implementation.
