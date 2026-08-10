## General

**Tax only the slice belonging to each bracket**

Tax brackets are progressive. The rate for one bracket applies only to income above the preceding upper bound and at or below the current upper bound.

`prev` stores the previous bracket's upper bound, beginning at zero. For current `upper`, the nominal bracket width is `upper-prev`.

**Cap the taxable endpoint at income**

`min(income,upper)` is the highest earned dollar boundary that lies in this bracket or below. Subtracting `prev` gives the amount of income inside the current interval when income has reached it.

If income is already below `prev`, the subtraction is negative. `max(0,...)` clamps it to zero. The exact taxable width is therefore

`max(0,min(income,upper)-prev)`.

This one expression handles full, partial, and untouched brackets.

**Accumulate percentage numerators**

The code multiplies taxable dollars by the integer `percent` and adds the product to `ans`. At this stage, `ans` is measured in dollar-percent units, one hundred times the monetary tax.

Only after every bracket does the method return `ans/100`, converting the accumulated percentage numerator into the requested monetary value.

Delaying division avoids repeated floating operations inside the loop.

**Advance the previous boundary**

After processing a bracket, `prev=upper` prepares the lower boundary for the next sorted bracket.

Even after all income has been covered, the loop continues over later brackets. Their clamped taxable widths are zero, so they add nothing. An early break could save work but is not present in the exact source.

**Trace a partial final bracket**

For brackets `[3,50]`, `[7,10]`, `[12,25]` and income ten:

- first width is `min(10,3)-0=3`, contributing 150;
- second width is `min(10,7)-3=4`, contributing 40;
- third width is `min(10,12)-7=3`, contributing 75.

The accumulated numerator is 265. Dividing by 100 returns 2.65.

**Income below the first boundary**

If income is two and the first upper bound is three, the taxable width is two, not the full bracket width. Every later bracket sees income below `prev` and contributes zero.

If income is zero, every width is clamped to zero and the returned tax is zero.

**Why each dollar is taxed once**

The bracket intervals `(prev,upper]` are disjoint and consecutive because upper bounds are strictly increasing. Intersecting each with income range `[0,income]` yields the taxable slice formula.

The slices neither overlap nor leave a gap before income, and the final bracket reaches at least income. Multiplying each slice by its own rate and summing therefore applies exactly the progressive schedule.

**Why rates are not applied to total income**

A common mistake is to apply the highest reached rate to every earned dollar. The `prev` subtraction prevents this: only dollars newly entering the current bracket receive its percentage. Earlier dollars were already counted at earlier rates.

## Complexity detail

Let `b` be the number of brackets. The exact method visits all `b` rows and performs constant arithmetic for each, so time is `O(b)`.

`ans` and `prev` are the only persistent working values, giving `O(1)` auxiliary space. The final division produces a Python float accepted under the tolerance.

## Alternatives and edge cases

- **Break after reaching income:** Once `upper>=income`, later brackets contribute zero; an early return can reduce practical work.
- **Divide per bracket:** It is mathematically equivalent but introduces more floating-point operations.
- **Apply one marginal rate to all income:** That is not progressive taxation and overtaxes lower slices.
- **Zero income:** Every taxable width is zero.
- **Zero-percent bracket:** Its slice is processed but contributes zero.
- **Income exactly at an upper bound:** That bracket is fully taxed and the next has zero width.
- **Income inside a bracket:** `min` includes only the partial slice.
- **Income beyond several brackets:** Earlier bracket widths are fully included.
- **Last bracket guarantee:** It ensures all income is covered by the schedule.
- **Strictly increasing bounds:** They make every nominal width positive and prevent overlap.
- **Rates up to 100:** Multiplication remains direct; 100 percent taxes the full slice amount.
- **Input preservation:** Bracket rows are read in their supplied sorted order.
- **First bracket:** `prev=0` makes its taxable width begin at the first earned dollar boundary without a special case.
- **Later zero contributions:** Updating `prev` even after income is exhausted is harmless because `max(0,...)` continues to return zero.
- **Integer numerator:** Before the final division, `ans` is exact integer arithmetic, so no rounding accumulates between brackets.
- **Accepted tolerance:** Returning a float after one division satisfies the problem's numerical-output contract.
- **Income equals zero:** The loop may still visit every bracket, but it never creates a positive taxable slice.
- **Partial first bracket:** `min(income,upper)` taxes only the earned amount rather than the entire first upper bound.
- **No deductions or credits:** The source model contains only progressive slices; no other adjustment belongs in the computation.
- **Unsorted extension:** The formula assumes the guaranteed increasing bounds; arbitrary order could make `prev` invalid.
