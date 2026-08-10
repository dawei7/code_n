## General

**Interpret one answer as a complete color-group size**

If a rabbit answers `x`, it claims that exactly `x` other rabbits share its color. Including the rabbit that spoke, that color must contain

$$
g = x + 1
$$

rabbits in total.

For example, an answer of two describes a color group of three rabbits. Some of those three may not be among the questioned rabbits, but they must still exist in the forest and must be counted in the answer.

**Rabbits with different answers cannot share a color**

Every rabbit of one color sees the same number of other rabbits of that color. Therefore all members of a color group would give the same answer.

A rabbit answering one belongs to a two-rabbit color, while a rabbit answering two belongs to a three-rabbit color. They cannot be describing the same color. This lets the algorithm handle each distinct answer value independently and add the resulting minimum group sizes.

**Rabbits with the same answer can share groups, but each group has a capacity**

Suppose `v` questioned rabbits all answered `x`. A single color group for that answer has size `g = x + 1`, so at most `g` of those respondents can share one color.

Packing as many respondents as possible into each group minimizes the total number of implied rabbits. If `v <= g`, all `v` respondents can belong to one color, but the forest must still contain the full `g` rabbits of that color. If `v > g`, at least two colors with that same group size are needed, and so on.

The minimum number of groups is

$$
\left\lceil \frac{v}{g} \right\rceil.
$$

Each group contributes all `g` rabbits, whether or not every member answered the survey. Thus this answer class contributes

$$
\left\lceil \frac{v}{g} \right\rceil g.
$$

**Compute the ceiling using integer arithmetic**

For positive integers, the ceiling quotient can be written without floating-point arithmetic:

`(v + group - 1) // group`.

Adding `group - 1` ensures that any nonzero remainder pushes the integer division into the next group. When `v` is already divisible by `group`, the quotient remains exact.

The implementation multiplies that quotient by `group` and adds it to `ans`.

**Why partially filled respondent groups still count as full color groups**

Consider five rabbits that answer two. Each described color has exactly three members. The first three respondents may all share one color. The remaining two cannot join that color because it would then have at least five members, contradicting their answer of two.

The last two respondents can share a second color, but that color still needs a third rabbit who was not questioned. Therefore five identical answers of two imply two groups of three and contribute six rabbits, not five.

This is why ordinary frequency counting alone is insufficient: the algorithm rounds each frequency upward to a multiple of its required group size.

**Trace `answers = [1, 1, 2]`**

The counter contains frequency two for answer one and frequency one for answer two.

For `x = 1`, the group size is two. The two respondents fill exactly one group, contributing two rabbits.

For `x = 2`, the group size is three. The single respondent requires one entire group of three, contributing three rabbits. Two of those rabbits were simply not questioned.

Adding the independent contributions gives five, which is the minimum possible forest size.

**Trace repeated large answers**

For `answers = [10, 10, 10]`, all respondents can belong to one color group of size eleven. The group has eight unquestioned members, so the minimum is eleven.

If there were twelve answers of ten, one eleven-rabbit color could contain at most eleven respondents. The twelfth response would force a second eleven-rabbit color, making the minimum twenty-two.

**Why the construction proves minimality**

For a fixed answer `x`, every compatible color has exactly `g = x + 1` members. Since one such color can account for at most `g` of the `v` respondents, any valid forest needs at least `ceil(v / g)` distinct colors for that answer. This establishes a lower bound of `ceil(v / g) * g` rabbits.

That lower bound is achievable: partition the `v` respondents into groups of at most `g`, assign each partition a different color, and add enough unquestioned rabbits to make every partition contain exactly `g` members. Every rabbit's answer is then consistent.

Different answer values require different colors, so these independently achievable minimum constructions can be combined without conflict. Summing their contributions is therefore both feasible and globally minimal.

**Why a counter is the right summary**

The order of responses carries no information. Only the number `v` of occurrences of each answer `x` affects how many full groups are needed. `Counter(answers)` produces exactly those frequencies in one pass, after which every distinct answer is processed once.

## Complexity detail

Let $n$ be the number of responses and $u$ the number of distinct answer values. Building the counter takes $O(n)$ expected time. Iterating over its $u$ entries takes $O(u)$ time, and $u \le n$, so total time is $O(n)$.

The counter stores one entry for each distinct answer, requiring $O(u)$ auxiliary space. All arithmetic variables use constant additional space.

## Alternatives and edge cases

- **Sort the answers:** Equal values become consecutive and can be grouped in $O(n \log n)$ time with little extra storage, but hashing reaches linear expected time.

- **Track remaining capacity online:** A map can remember open spots in the current color group for each answer. It is valid but more stateful than rounding a final frequency.

- **Count only respondents:** Incorrect whenever a color group is not filled by questioned rabbits, because unquestioned members still exist.

- **Answer zero:** The group size is one, so each such rabbit has a unique color and contributes exactly one.

- **Frequency smaller than group size:** It still requires one complete group.

- **Frequency exactly divisible by group size:** No extra group is created by the ceiling formula.

- **Frequency one above a multiple:** That single extra response forces another entire color group.

- **Same answer, multiple colors:** This is allowed and becomes necessary when the response count exceeds one group's capacity.

- **Different answers:** They must never be packed into the same color group because members of one color must report the same value.
