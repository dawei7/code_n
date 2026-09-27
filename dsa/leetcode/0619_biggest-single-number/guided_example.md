# Guided Example: Biggest Single Number

This lesson works one multiset of integers and reports the largest *single*
number in it, where a single number is a value occurring exactly once. The
instance below is the one that makes the problem interesting rather than trivial:
the largest value in the table is disqualified, and the answer is a smaller value
that only a correct reading of the definition can produce.

The whole input is one relation with a single attribute, and repeated values are
expected.

| `num` |
|:---:|
| $8$ |
| $8$ |
| $3$ |
| $3$ |
| $1$ |
| $4$ |
| $5$ |
| $6$ |

| `num` |
|:---:|
| $6$ |

Reading the table as a multiset $M = \{8, 8, 3, 3, 1, 4, 5, 6\}$ keeps the
duplicates visible. The answer is a single scalar, not a set of values and not a
row count.

---

## 1. Why the Maximum of the Raw Table Is the Wrong Answer

The most tempting move is to look at the largest stored value. That value is $8$,
and it is wrong twice over: it appears with multiplicity $2$, so it is not single
at all, and it is not even eligible to compete for the title. The problem asks for
the largest *single* number, so the qualification "appears exactly once" is a
precondition on candidacy, not a tie-breaker applied afterwards.

The distinction matters here more than in most instances, because the disqualified
value sits above every eligible one. In this table a procedure that ranks raw
values and takes the top one returns $8$; the correct answer is $6$. The instance
therefore separates two operations that are easy to conflate:

1. *filter by exact multiplicity*, which removes candidates and is not order
   preserving with respect to value; and
2. *select the maximum*, which is a pure order operation over whatever survives.

Order matters between them. Taking the maximum first and checking multiplicity
second gives $8$ and a failure, because the maximum has already discarded all
information about the other values. Filtering first and taking the maximum second
gives $6$. The candidate set must be reduced before the extremum is taken.

| Procedure | Value examined | Multiplicity of that value | Result |
|:---|:---:|:---:|:---:|
| Rank raw values, keep the largest | $8$ | $2$ | $8$ (not a single number) |
| Keep the largest value with multiplicity $1$ | $6$ | $1$ | $6$ (correct) |

## 2. The Multiplicity Invariant and the Singleton Supremum

The filter in the first step is a cardinality test on the multiset of occurrences
of each distinct value. The invariant it enforces is a sharp one: the candidate
set contains a value if and only if that value's multiplicity is exactly one, so
the set is closed under no value that appears twice and admits no value that
appears zero times. Writing $\text{mult}_{M}(x)$ for how many times the value
$x$ appears in $M$, the candidate set is

$$
T = \{\, x \in M : \text{mult}_{M}(x) = 1 \,\},
$$

and the required answer is the supremum of that set,

$$
\text{answer} = \sup T ,
$$

with the convention that the supremum of the empty set is reported as `null`
rather than as an error or as an absent row.

Two properties of $T$ drive the rest of the reasoning. First, $T$ is defined by
an exact equality on a count, so a value with multiplicity $3$ is excluded just
as firmly as a value with multiplicity $2$; there is no threshold to tune.
Second, the definition is about the *value*, not about the row. Two rows holding
the same number are one value with multiplicity two, and a table in which every
row is distinct is a table in which every value is single.

Grouping the relation by its value and keeping one count per distinct value is
all the state this filter needs: $|T| \le U \le N$, where $N$ is the number of
rows and $U$ the number of distinct values.

## 3. Frequency Census for the Representative Instance

Collapsing the eight rows by value gives six distinct values, and the counts
immediately show which ones survive the equality test and which are eliminated.

| Value $x$ | Multiplicity $\text{mult}_{M}(x)$ | Single? $\text{mult}_{M}(x) = 1$ | In $T$? | Position among singles |
|:---:|:---:|:---:|:---:|:---:|
| $8$ | $2$ | no | excluded | — |
| $3$ | $2$ | no | excluded | — |
| $1$ | $1$ | yes | included | smallest |
| $4$ | $1$ | yes | included | middle |
| $5$ | $1$ | yes | included | middle |
| $6$ | $1$ | yes | included | largest |

The census makes the exclusion of $8$ explicit and auditable: it holds the largest
raw value in the table and is nevertheless absent from the candidate set. The
candidate set is

$$
T = \{1, 4, 5, 6\},
$$

and its supremum is $6$, so the emitted relation is the single row containing
$6$.

| Step | Operation | Resulting collection | Size |
|:---:|:---|:---|:---:|
| $1$ | Collapse the eight rows by value and count | $\{(8,2), (3,2), (1,1), (4,1), (5,1), (6,1)\}$ | $6$ |
| $2$ | Keep groups whose count is exactly $1$ | $T = \{1, 4, 5, 6\}$ | $4$ |
| $3$ | Take the supremum of the survivors | $6$ | $1$ |

## 4. Why an Empty Candidate Set Must Produce `null`

The contract is unusual in the second official instance, where the table
$M = \{8, 8, 7, 7, 3, 3, 3\}$ has no single number at all. Every value appears at
least twice, so $T = \emptyset$, and the required output is still a one-row,
one-column relation whose only cell is `null`.

That requirement constrains which final operation is admissible. Ordering the
candidates by value and keeping the first row of that order yields the right cell
when $T$ is non-empty, but it yields *zero rows* when $T$ is empty, because there
is nothing to order. A scalar aggregate over the same candidate set instead
yields exactly one cell in both cases: the supremum when candidates exist, and
`null` when none do. The empty case is not an exception to be special-cased; it
falls out of the definition of an aggregate over an empty collection.

| Candidate set $T$ | Supremum of $T$ | Rows emitted by an ordering-and-limit plan | Rows emitted by a scalar aggregate |
|:---|:---:|:---:|:---:|
| $\{1, 4, 5, 6\}$ | $6$ | $1$ | $1$ |
| $\emptyset$ | undefined, reported as `null` | $0$ | $1$, holding `null` |

The aggregate form is therefore the one that matches the contract in both
branches, and it does so without any conditional logic about emptiness.

## 5. Traps This Instance Exposes

| Trap | Failure on this input |
|:---|:---|
| Reading "biggest" before "single" | Returns $8$, the maximum of the raw multiset, which is not a single number. |
| Testing the count with an inequality such as "at most once" | Treats a value with multiplicity $0$ as a candidate, which has no meaning for a stored value, and admits nothing extra here — but it signals that the equality test was not understood. |
| Admitting multiplicity $2$ or more | The candidate set becomes the full set of distinct values $\{1,3,4,5,6,8\}$ and the answer becomes $8$. |
| Ordering the candidates and taking the first one | Correct for this input, but returns an empty relation on the second official instance, where the contract requires one row holding `null`. |
| Assuming the answer must be positive | Negative values are legal. In a table of $-1, -1, -2, -3, -3$ the candidate set is $\{-2\}$ and the answer is $-2$. |
| Treating $0$ as an absent value | $0$ is an ordinary integer. A table of $5, 5, 0, -1, -1$ has candidate set $\{0\}$ and answer $0$, which is a real value and not a stand-in for emptiness. |
| Naming the output column anything other than `num` | The required schema is a single attribute called `num`. |

The negative-value and zero cases are worth stating together because they defeat
two different shortcuts. A falsy-value test would drop the correct answer $0$, and
a "largest means greatest magnitude" reading would pick $-3$ instead of $-2$ for
the negative table.

## 6. Complexity Derivation

Let $N$ be the number of rows in the table and $U$ the number of distinct values,
so $U \le N$. Let $K = |T|$ be the number of single numbers, so $K \le U \le N$.

The filtering stage has to establish, for every distinct value, how many times it
occurs. A hash grouping builds one counter per distinct value while scanning the
$N$ rows once, which costs $O(N)$ expected time. A sort-based grouping instead
orders the rows by value, costing $O(N \log N)$ time, and then walks the sorted
run to emit one group per distinct value. The equality test on each group's
counter is constant work, so the filtering stage costs at most $O(N \log N)$ and
$O(N)$ expected.

The final maximum scans only the surviving groups. That is at most $K \le U$
comparisons, which is dominated by the filtering stage in both plans. The output
is a single scalar, so no per-candidate output cost appears.

| Stage | Expected cost | Sort-based cost |
|:---|:---:|:---:|
| Group the $N$ rows by value and count | $O(N)$ | $O(N \log N)$ |
| Keep the groups whose count equals $1$ | $O(U)$ | $O(U)$ |
| Scan the $K$ survivors for the maximum | $O(K)$ | $O(K)$ |

The engine-independent bound is $O(N \log N)$ time, matching the conservative
sort-based plan; hash grouping makes the expected cost linear.

Auxiliary space is $O(U)$ and therefore $O(N)$ in the worst case. The grouping
structure stores one counter per distinct value, and a sort-based engine
additionally uses up to linear temporary storage for the ordering, which may spill
to disk without changing the asymptotic amount of working data. The final maximum
carries a single running value and therefore adds only $O(1)$ state, and the
result relation holds exactly one cell regardless of whether the candidate set is
empty.