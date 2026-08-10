## General

**Only February depends on the year**

Month lengths follow a fixed calendar table. April, June, September, and November have thirty days. February has either twenty-eight or twenty-nine. Every other valid month has thirty-one.

Therefore, the only computation involving `year` is whether it is a Gregorian leap year. After that Boolean is known, a direct month-indexed lookup gives the answer.

**Apply the complete leap-year rule**

A year is a leap year when either:

- it is divisible by four but not divisible by one hundred, or
- it is divisible by four hundred.

The expression:

`(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)`

implements those clauses exactly.

The century exception matters. Year 1900 is divisible by four, but it is also divisible by one hundred and not by four hundred, so it is not a leap year. Year 2000 is divisible by four hundred, so the second clause makes it a leap year.

Ordinary years such as 1992 that are divisible by four and not by one hundred satisfy the first clause.

The rule can be understood as successive refinement. Divisibility by four supplies the normal extra-day pattern. Divisibility by one hundred removes that extra day for century years. Divisibility by four hundred restores it for every fourth century. The Boolean expression encodes those exceptions without needing nested conditionals.

Remainder zero is the exact test for divisibility. For example, `1900 % 100 == 0` activates the century exclusion, while `1900 % 400 != 0` prevents restoration. For 2000, both century tests are true but the four-hundred clause independently makes the entire `or` expression true.

**Build a one-based lookup table**

The list `days` begins with an unused zero at index zero. This aligns list indices directly with month numbers one through twelve, avoiding a repeated `month - 1` conversion.

February’s entry is `29 if leap else 28`. Every other entry is the fixed length for that month:

`[31, February, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]`.

Returning `days[month]` is safe because the contract guarantees `1 <= month <= 12`.

**Why table lookup is preferable to many branches**

A chain of conditionals could first detect February, then the four thirty-day months, and otherwise return thirty-one. The table makes the entire calendar mapping visible in month order and reduces the final selection to one indexed operation.

The leap calculation is still separated because February’s entry depends on the year. This keeps the static pattern and the one dynamic exception easy to audit.

**Complete correctness argument**

For February, the computed `leap` Boolean is true exactly for Gregorian leap years, so the table stores the required twenty-nine or twenty-eight. For each non-February month, the table entry matches its fixed calendar length.

Every valid input month selects exactly one of those verified entries. Therefore, the returned integer is the correct number of days for the requested month and year.

Notice that computing `leap` for a non-February month is harmless. The lookup entries for all other months ignore it, so July returns thirty-one in both leap and ordinary years. Keeping one uniform path avoids a separate early branch while still making February the only dynamic entry.

## Complexity detail

The repository playbook classifies this as a bounded-domain problem. Each call selects one of exactly twelve months and performs a fixed number of remainder, comparison, Boolean, list-construction, and indexing operations.

Time is therefore $O(1)$, and the thirteen-entry list has fixed size, so space is $O(1)$. Neither bound depends on the numeric magnitude of the year or on an input collection.

The list is constructed on every call, but it always contains the same constant number of entries. A class-level tuple could avoid repeated allocation as a constant-factor optimization without changing the asymptotic bound.

Even in a generalized setting with much larger year integers, the number of calendar cases remains fixed. Under ordinary machine-integer assumptions the modular operations are constant; for arbitrary-precision integers their bit cost could depend on the year’s representation, which is immaterial within the bounded source range.

## Alternatives and edge cases

- **Conditional branches:** Return thirty for months four, six, nine, and eleven; handle February separately; return thirty-one otherwise. It avoids list allocation but can be less visually systematic.
- **Calendar library:** A standard library can supply month lengths, but the leap rule is simple and the interview problem expects direct reasoning.
- **Store February as twenty-eight then add leap:** A fixed table plus `int(leap)` for month two is equivalent.
- **Year divisible by four:** It is not automatically leap if it is also a non-four-hundred century.
- **Year 1900:** Divisible by one hundred but not four hundred, so February has twenty-eight days.
- **Year 2000:** Divisible by four hundred, so February has twenty-nine days.
- **Thirty-day month:** April, June, September, and November map to thirty regardless of year.
- **January and December:** Both map to thirty-one.
- **Minimum and maximum years:** The modular rule applies uniformly throughout the stated range.
- **Valid month guarantee:** Index zero is never returned, and no out-of-range list access occurs.
- **One-based sentinel:** The initial zero is alignment padding, not a possible month length.
- **Boolean precedence:** Parentheses make the two leap-year clauses explicit and prevent misreading the mixture of `and` and `or`.
