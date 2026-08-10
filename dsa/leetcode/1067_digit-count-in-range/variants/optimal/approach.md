## General

**Turn an inclusive range into two prefix counts**

The public method is:

```python
return self.f(high, d) - self.f(low - 1, d)
```

Let `f(n, d)` count how many written occurrences of digit `d` appear across all positive integers from one through `n`.

The prefix through `high` contains every occurrence wanted in the interval plus every occurrence below `low`. The prefix through `low - 1` contains exactly that unwanted earlier part. Subtracting leaves occurrences in the inclusive range from `low` through `high`.

Using `low - 1` is what keeps `low` itself included. The constraints guarantee `low >= 1`, so the smaller prefix argument is non-negative.

The helper computes a prefix count with digit dynamic programming. Rather than visiting every integer, it constructs all valid decimal representations position by position and combines equivalent suffix subproblems.

**Store the upper-bound digits from least significant to most significant**

Inside `f`, the array is filled as follows:

```python
a = [0] * 11
l = 0
while n:
    l += 1
    a[l] = n % 10
    n //= 10
```

`a[1]` receives the units digit, `a[2]` the tens digit, and so on. Thus `a[l]` is the most significant digit.

The recursive search starts at position `l` and decreases `pos`, so it still chooses digits from most significant to least significant. The reversed storage merely makes the current upper-bound digit available as `a[pos]`.

The fixed array length 11 is sufficient for the stated maximum `2 * 10^8`, which has nine digits. Unused cells remain zero.

The loop consumes the local `n` value, but the original prefix bound is no longer needed after its digits have been extracted.

If the argument is zero, the loop never runs and `l` remains zero. The recursive base case then returns zero. This makes `f(0, d) = 0`, exactly what the range subtraction needs when `low == 1`.

**Understand the four digit-DP state fields**

The cached function is:

```python
@cache
def dfs(pos, cnt, lead, limit):
```

Its state means:

- `pos` is the number of digit positions still to choose. The current upper-bound digit is `a[pos]`.
- `cnt` is the number of occurrences of `d` already chosen in the significant prefix.
- `lead` is true while every chosen digit has been a padding zero before the represented number begins.
- `limit` is true while the chosen prefix exactly matches the prefix of the upper bound. When true, the next digit cannot exceed `a[pos]`.

Memoization stores the total returned for each state. Different constructed prefixes that have the same remaining position, occurrence count, leading status, and tightness have identical possible suffixes, so they can reuse one result.

**Why the base case returns cnt**

The first condition is:

```python
if pos <= 0:
    return cnt
```

At that point, one complete number representation has been constructed. `cnt` is the number of target-digit occurrences in that number, so this branch contributes exactly that many to the aggregate total.

This DP differs from a common digit DP that returns the number of valid integers. Here every leaf returns an occurrence count. Internal states sum those leaf contributions, producing the total number of occurrences across all represented integers.

If one number contains the digit several times, its leaf returns a `cnt` greater than one. All appearances are therefore counted separately, as required.

**Respect the upper bound**

The maximum digit allowed at the current position is:

```python
up = a[pos] if limit else 9
```

If the chosen prefix still equals the bound's prefix, selecting anything larger than the bound's current digit would create a number greater than `n`. The range stops at `a[pos]`.

If a previous position was smaller, the constructed number is already below the bound. Every digit zero through nine is then legal.

The loop tries every allowed digit:

```python
for i in range(up + 1):
```

The next tightness flag is `limit and i == up`. When `limit` is true, `up` equals the bound digit, so tightness remains true only when `i` matches it. When `limit` is false, the expression remains false regardless of `i`.

This rule ensures a one-to-one correspondence between completed choices and zero-padded integers from zero through the prefix bound.

**Do not count padding zeros**

The crucial leading-zero branch is:

```python
if i == 0 and lead:
    ans += dfs(pos - 1, cnt, lead, limit and i == up)
```

Digit DP conceptually pads shorter numbers to the same length as the upper bound. For example, seven may be constructed as `007` when the bound has three digits. Those first two zeros are not written in the ordinary representation and must not count when `d == 0`.

While `lead` is true and another zero is selected:

- `cnt` does not change.
- `lead` remains true.

The code passes the existing `lead` value, which is true in this branch.

Once a nonzero digit is chosen, the represented number has begun. Any later zero is a real written zero and must be counted when zero is the target digit.

The all-zero padded choice represents the integer zero. It reaches the base case with `cnt == 0`, so the helper counts occurrences over positive integers one through `n` and gives zero no contribution. That is correct for this problem because every requested range begins at one.

**Count a significant chosen digit**

Every other digit choice uses:

```python
ans += dfs(
    pos - 1,
    cnt + (i == d),
    False,
    limit and i == up,
)
```

This branch includes a nonzero digit that starts the number and every digit after the number has started.

The expression `i == d` is a Boolean. Python adds false as zero and true as one, so `cnt` increases exactly when the chosen significant digit equals the target digit.

The next `lead` value is false because the number has started. It remains false even when a later chosen digit is zero.

**Sum every valid completion**

`ans` starts at zero inside each state. Every allowed current digit contributes the total occurrence count from all valid suffixes beneath that choice. After the loop:

```python
return ans
```

returns the aggregate for this state.

The initial call is:

```python
return dfs(l, 0, True, True)
```

No positions have been chosen, no target occurrences have been seen, the number has not begun, and its empty prefix exactly matches the bound. This root state therefore covers every number from zero through the original `n` exactly once.

**Why the prefix result is correct**

The tightness rule permits exactly the padded digit sequences numerically no greater than the bound. The leading flag distinguishes padding from written digits. The count state increases exactly once for every written occurrence of `d`, and the base case contributes that number's complete occurrence count.

Summing all leaves yields `f(n, d)`. Prefix subtraction then removes all numbers below `low` and retains every number from `low` through `high`, including both endpoints.

## Complexity detail

Let `D` be the number of decimal digits in the prefix bound.

The exact memoization state includes `pos` with `O(D)` values and `cnt` with up to `O(D)` values, plus two Boolean flags. This gives `O(D^2)` possible states. Each state tries at most ten digits, a constant alphabet size. The exact parameterized time complexity is `O(D^2)` and cache space is `O(D^2)`. Recursion depth and digit storage add `O(D)`.

The public function runs `f` twice, but multiplying by two does not change these bounds. Here `D = O(log H)`, where `H = high`.

Because the constraints cap `H` at `2 * 10^8`, `D` is at most nine and every state structure is absolutely small. Still, the exact source's count dimension means its general asymptotic form is not literally the manifest's `O(log H)` time and `O(1)` space.

The manifest bounds describe the standard positional arithmetic formula. For each decimal place value, count complete cycles of zero through nine and the partial cycle at the bound. Nonzero digits follow a direct full-cycle plus remainder formula. Digit zero needs a correction to exclude leading-zero positions. Processing one place at a time takes `O(log H)` time and uses a constant number of numeric variables, giving `O(1)` auxiliary space.

Another digit-DP optimization can remove `cnt` from the state by returning both the number of suffix completions and their total target-digit occurrences. That reduces the state count to `O(D)`, though recursion and memoization still use `O(D)` rather than strict constant space.

## Alternatives and edge cases

- **Positional counting for the manifest target:** Analyze units, tens, hundreds, and higher places independently with complete decimal cycles. Correct zero handling yields `O(log H)` time and `O(1)` auxiliary space.
- **Digit DP returning two aggregates:** Return a pair containing completion count and occurrence total instead of carrying `cnt` in the cache key. This reduces states from quadratic to linear in digit count.
- **Enumerate the range:** Convert every integer from `low` through `high` to text and count characters. This can take time proportional to the numeric interval and is infeasible near `2 * 10^8`.
- **Target digit zero:** Leading padding zeros must not count. The `lead` branch preserves that distinction, while zeros after the first nonzero digit do count.
- **Low equals one:** The second prefix is `f(0, d)`. Its zero-position call returns zero, so subtraction is correct.
- **Low equals high:** Prefix subtraction isolates the digit occurrences in that one number.
- **Repeated digit in one number:** The leaf returns the full `cnt`, so a number such as 11 contributes two occurrences of one.
- **Digit absent from the range:** Both prefix totals subtract to the same value and the result is zero.
- **Upper-bound digit choice:** When tight, choosing exactly `a[pos]` keeps the next state tight; choosing less releases the remaining positions.
- **Shorter numbers:** They are represented with padding zeros while `lead` is true, preventing those padding positions from contributing.
- **The integer zero:** The prefix helper intentionally gives the all-zero representation no written-digit contribution. This is safe because legal query ranges begin at one.
- **Maximum bound:** The fixed eleven-cell digit array is sufficient for the stated nine-digit maximum.
- **Cache lifetime:** `dfs` is defined inside `f`, so the cache is fresh for each prefix bound and target digit. Results from `high` cannot contaminate the `low - 1` computation.
- **Input preservation:** The local copy of `n` is divided during digit extraction, while the public arguments and target digit remain unchanged.
