## General

The decision for one week depends only on the city occupied after Monday travel and the best total from the preceding week. This creates a dynamic program over weeks and cities.

Define `f[k][j]` as the maximum vacation days obtainable after completing the first `k` weeks while spending week `k - 1` in city `j`.

The table has `K + 1` rows. Before any week, the traveler is in city zero with total zero, so `f[0][0] = 0`. Every other city in row zero is initialized to negative infinity because it is unreachable before the first Monday.

Negative infinity is a safe impossible-state marker: it can never win a maximum against a reachable finite total, and adding vacation days leaves it impossible.

**Consider staying in the destination city.** For week `k` and destination `j`, the initial transition:

`f[k][j] = f[k - 1][j]`

represents staying in city `j`. Staying is always legal even though `flights[j][j]` is zero.

**Consider flying from every possible origin.** For each city `i`, if `flights[i][j]` is one, Monday travel from `i` to `j` is allowed. The method takes:

`max(f[k][j], f[k - 1][i])`.

This chooses the best previous total among staying and all direct incoming flights. Unreachable origins contribute negative infinity and cannot create a false route.

**Add vacation days in the destination.** After the best route into `j` is selected, the code adds:

`days[j][k - 1]`.

The week index is `k - 1` because DP row one represents source week zero. Vacation belongs to the city reached on Monday, exactly matching the contract.

For the first example, row one can reach cities zero, one, or two from initial city zero. City one supplies six days and becomes the best first-week choice. Later rows propagate totals through allowed flights and staying, eventually reaching twelve.

When no flights exist, only `f[k - 1][j]` can preserve a reachable city. Since only city zero starts reachable, every other state remains negative infinity and the answer sums city zero's allowances.

**Why one state per city is sufficient.** Future choices depend on the current city and accumulated score, not on the detailed earlier route. Among schedules ending the same week in the same city, only the one with maximum total can ever lead to an optimal continuation.

**Why every transition is legal.** A state comes either from the same city or from an origin with an explicit flight. It then adds only the allowance of the destination city for that week.

**Why every legal schedule is represented.** Read its weekly cities in order. Each consecutive pair is either equal or connected by a flight, so the corresponding DP transition exists. Induction shows its accumulated total is among the candidates for its ending state. Taking maxima cannot lose a better schedule.

After all weeks, the traveler may finish in any city. The method returns the maximum value in the final row.

For a small trace, suppose only flight `0 -> 1` exists and week-zero allowances are city zero: two, city one: six. Row zero is `[0, -inf]`. For week one, destination zero can stay and becomes two. Destination one can arrive from zero and becomes six. On week two, both destinations use their own prior stay values, while any available flight is considered again. The table never assumes a flight can be taken midweek or chained twice on one Monday.

Notice that the destination loop may temporarily add `days[j][k - 1]` to negative infinity. In Python floating-point arithmetic, negative infinity plus a finite allowance remains negative infinity. The unreachable marker is therefore stable without a separate conditional branch.

The DP also handles directed flights correctly. It tests `flights[i][j]`, the edge from prior city `i` into destination `j`; it never assumes `flights[j][i]` has the same value. This matters because the source matrix need not be symmetric.

## Complexity detail

There are $K$ weeks, $n$ destinations, and up to $n$ origins checked for each destination. Time is $O(Kn^2)$, matching the manifest.

The exact source allocates a full $(K+1)\times n$ table, using $O(Kn)$ space. This differs from the manifest's $O(n)$ bound, which is achievable because each row depends only on the previous row. The implementation does not perform that rolling-array compression.

The table is nevertheless useful pedagogically because each row preserves the best totals after a particular week and makes route evolution inspectable.

## Alternatives and edge cases

- **Rolling two DP rows:** It preserves the recurrence and reduces space to $O(n)$, matching the manifest.
- **Greedy highest allowance each week:** It may choose a city from which valuable later cities are unreachable.
- **Recursive search without memoization:** It explores exponentially many schedules.
- **No flights:** Only staying in city zero remains reachable.
- **Complete flight graph:** Every week can choose the city with best continuation.
- **Zero vacation allowance:** The city may still be strategically useful for later travel.
- **Stay transition:** It must be included separately because diagonal flight entries are zero.
- **Unreachable city:** Negative infinity prevents it from becoming reachable through arithmetic alone.
- **First Monday flight:** Row zero at city zero allows an immediate flight before week one.
- **Final city:** No return to city zero is required; maximum over all cities is correct.
