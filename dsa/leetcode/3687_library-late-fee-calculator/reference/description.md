## Description

A library records in `daysLate` how many days late each returned book was. Calculate each book's fee independently from its delay, then return the sum of all fees.

A book returned exactly one day late costs 1. A delay from 2 through 5 days, inclusive, costs twice its number of late days. A delay greater than 5 days costs three times its number of late days. These ranges are separate, so the boundary values 1, 2, 5, and 6 must use their corresponding rules exactly.
