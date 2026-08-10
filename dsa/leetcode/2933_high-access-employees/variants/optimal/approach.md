## General

Access records from different employees must be evaluated independently. The source first groups each employee's times, converting every four-digit clock string into minutes after midnight.

For time `t`:

`int(t[:2]) * 60 + int(t[2:])`

turns the hour portion into minutes and adds the minute portion. Numeric minutes make time differences ordinary subtraction and avoid incorrect lexicographic arithmetic.

**Group and sort each timeline**

`defaultdict(list)` maps each name to all of that employee's access minutes. The source sorts each list in ascending chronological order.

All records are from the same day, and the statement explicitly says not to wrap from the end of the day to the beginning. Therefore a normal linear order from minute $0$ through minute $1439$ is exactly what we need.

**Why checking consecutive triples is sufficient**

An employee is high-access if at least three accesses occur within a period shorter than 60 minutes. In a sorted timeline `ts`, inspect each consecutive triple ending at position $i$:

`ts[i - 2], ts[i - 1], ts[i]`.

All three fit inside a one-hour period exactly when

`ts[i] - ts[i - 2] < 60`.

The middle time automatically lies between the endpoints, so only the earliest-to-latest span matters.

If any three accesses—not necessarily originally chosen as consecutive—fit in such a period, then the sorted interval between their earliest and latest contains at least three records. Among the records in that interval, some three consecutive sorted entries also lie between the same endpoints and have span no larger. Thus testing all consecutive triples cannot miss a qualifying set.

Conversely, when a tested consecutive triple has span below 60, those three actual accesses themselves prove high-access status. The condition is both necessary and sufficient.

**Strictly less than sixty**

Times exactly one hour apart do not qualify. The source correctly uses `< 60`, not `<= 60`. For example, minutes 495 and 555 correspond to 08:15 and 09:15; a triple spanning those endpoints is rejected.

**Add each employee at most once**

`any(...)` stops when the first qualifying triple is found. The name is appended once after that Boolean succeeds, regardless of how many other qualifying windows exist.

Employees with fewer than three records produce an empty range in the generator, so `any` is false and they are not appended.

For times 05:32, 05:49, and 06:21, converted values are $332$, $349$, and $381$. Their span is $49<60$, so the employee qualifies. Times 10:25, 11:20, and 11:24 span $59$ minutes and also qualify.

**Why answer order needs no sorting**

The contract permits any order. Iterating `d.items()` uses dictionary insertion order in modern Python, but correctness does not depend on it. Sorting names would add work without satisfying an additional requirement.

## Complexity detail

Let $n$ be total records and let employee $q$ have $n_q$ records. Grouping and conversion take $O(n)$ time. Sorting costs

$$
\sum_q O(n_q\log n_q)\le O(n\log n).
$$

The consecutive-triple scans total $O(n)$. Overall time is $O(n\log n)$.

The dictionary and its lists store every converted access once, using $O(n)$ space. The answer contains at most the number of distinct employees and is output storage; including it still remains $O(n)$.

## Alternatives and edge cases

- **Check every triple:** It directly follows the definition but can take cubic time per employee. Sorting reduces the test to consecutive triples.
- **Sliding window with two pointers:** After sorting, maintain a left boundary less than 60 minutes behind and test window size. It is also correct but more state than needed for threshold three.
- **Compare `HHMM` integers directly:** Subtraction fails across hour boundaries; for example, 06:00 minus 05:30 is numerically 70 rather than 30.
- **Exactly 60 minutes:** Must be rejected by the strict inequality.
- **Midnight wrap:** 23:50 and 00:05 are not treated as close because all records share one day and wraparound is explicitly forbidden.
- **Duplicate timestamps:** Separate accesses at the same minute count separately. Three identical times produce span zero and qualify.
- **Fewer than three records:** No consecutive triple exists, so the employee cannot qualify.
- **Many qualifying triples:** `any` short-circuits, and the name is appended only once.
- **Unsorted input:** Group-local sorting restores chronological order regardless of record order.
- **Any output order:** No final sort is necessary.
- **Period may begin at the earliest access:** If three sorted times span less than 60 minutes, choosing the interval beginning at the first includes all three; no separate search over continuous start times is needed.
- **More than three accesses:** Any qualifying group of four or more contains a qualifying consecutive triple, so threshold-three checks also recognize larger bursts.
- **Hour parsing:** Leading zeros are safely accepted by `int`, so `"0002"` becomes minute two and `"0808"` becomes 488.
- **Same employee only:** Grouping before sorting prevents close times belonging to different employees from being combined.
- **Short-circuiting:** Once `any` finds one triple, later accesses cannot change the employee's already-true classification.
