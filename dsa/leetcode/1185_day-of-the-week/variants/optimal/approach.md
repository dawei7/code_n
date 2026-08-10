## General

The exact Optimal solution delegates Gregorian calendar arithmetic to Python’s standard `datetime` library. It constructs a date object from the supplied year, month, and day, then asks the library to format that date using its full weekday name.

The entire implementation is one return expression:

`datetime.date(year, month, day).strftime('%A')`.

Although compact, the expression contains two logically distinct operations. Understanding both makes it clear why no manual leap-year or month-offset code is required.

**Construct a calendar date, not a text approximation**

`datetime.date(year, month, day)` creates an object representing that exact civil date in the proleptic Gregorian calendar used by Python’s date type. The constructor understands the varying month lengths, including February, and the Gregorian leap-year rules.

A Gregorian year is normally a leap year when divisible by four. A year divisible by 100 is not a leap year unless it is also divisible by 400. Thus 2000 was a leap year, while 2100 is not. Those details are common sources of errors in hand-written date calculations, but they are already implemented and thoroughly exercised in the standard library.

The problem guarantees that every supplied triple is a valid date between 1971 and 2100. Therefore, the constructor will not encounter an impossible day such as February 30 or a month outside one through twelve. In a general application, invalid input would cause `datetime.date` to raise `ValueError`, but no recovery branch is needed under this contract.

The code assumes the execution environment has made the `datetime` module available, as the solution refers to `datetime.date` directly rather than importing it inside the method. The package harness supplies the surrounding execution context for the solution.

**Turn the date’s weekday into the required name**

The method `strftime` converts date information to formatted text. The directive `%A` requests the full weekday name, as opposed to `%a`, which requests an abbreviated name. For example, the full-name directive yields `"Saturday"` rather than an abbreviation such as `"Sat"`.

The seven expected outputs are full English names with initial capital letters. In the judge’s English execution environment, `%A` produces exactly that form. This is shorter and less error-prone than obtaining a numeric weekday and manually indexing a name list.

The formatter uses the weekday already associated with the constructed date. It does not infer the answer from the textual order of the arguments. Passing the constructor arguments as `year, month, day` is essential because that is the order required by `datetime.date`, even though the problem’s method parameters are listed as `day, month, year`.

**Why the library’s answer matches the calendar**

A weekday advances by one when the date advances by one day, with the seven names repeating cyclically. Correct calendar arithmetic must also account for every full month and year before the target date and insert February 29 in the appropriate leap years. Python’s date object represents the date according to those Gregorian rules, so its stored weekday is the result of exactly that progression.

The supplied note that January 1, 1971 was Friday is a reference point that a manual solution could use. The standard library’s calendar agrees with that reference. From there, counting the correct number of elapsed days modulo seven leads to the same weekday that `strftime('%A')` names.

For August 31, 2019, the constructor creates the corresponding valid date and the formatter returns `"Saturday"`. For July 18, 1999, it returns `"Sunday"`. There is no special-case table for these examples; they follow from the same calendar implementation used for every valid input.

**Why using a standard calendar primitive is an optimal approach**

The task asks only for the weekday of one date. A library date type already encapsulates the precise rules, keeps the method readable, and avoids duplicating delicate date logic. The operation does not iterate once per day since 1971. Internally, calendar components can be converted with fixed arithmetic, so the amount of work is bounded and independent of the distance from the reference date within the supported range.

Reliability here comes from selecting the correct abstraction. The solution creates exactly the semantic object described by the input—a calendar date—and requests exactly the semantic attribute required by the output—a full weekday name.

## Complexity detail

The method processes one fixed-size date triple. Constructing a `date` object and determining its weekday use a bounded number of arithmetic operations. Formatting one of seven constant-length names also takes bounded work. The time complexity is therefore $O(1)$.

The date object and formatted result contain a fixed amount of information. No storage grows with the numerical year or with the number of days since 1971. Auxiliary-space complexity is $O(1)$, and the returned weekday string has constant bounded length.

These bounds describe the standard computational model for fixed-width calendar fields. The solution does not loop across years, months, or elapsed days.

## Alternatives and edge cases

- **Manual elapsed-day counting:** Sum complete years since 1971, add complete months in the target year, add `day - 1`, and take the total modulo seven from Friday. This can be correct but requires careful leap-year and indexing logic.
- **Zeller-style congruence:** A closed-form weekday formula avoids library use and remains constant time, but its month transformations and century terms are less beginner-friendly and easier to implement incorrectly.
- **Numeric weekday plus name list:** `date.weekday()` could return a number that indexes a manually supplied array. That approach must respect Python’s Monday-first numbering, whereas `%A` directly produces the full name.
- **Leap day:** February 29 is valid only in a leap year. The date constructor applies the century exceptions correctly without a special branch in this method.
- **Century boundary:** The year 2000 is divisible by 400 and therefore leap, while 2100 is not. Library calendar logic handles both rules.
- **January and December:** Month transitions and year boundaries do not need special handling because the constructor represents the complete date directly.
- **Argument order:** The method receives `day, month, year` but the constructor requires `year, month, day`. Passing them in the incoming order would create an invalid or incorrect date.
- **Full versus abbreviated weekday:** `%A` is required. Using `%a` would produce abbreviations that do not match the allowed output values.
- **Locale dependence:** Weekday names produced by `strftime` are locale-sensitive in general. The judge environment must provide English names for this exact implementation to match the English-only contract.
- **Invalid dates outside this problem:** `datetime.date` would raise an exception for an impossible date. The stated validity guarantee makes explicit validation unnecessary here.
