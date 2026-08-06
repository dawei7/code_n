## Function Contract

**Inputs**

- `flights`: the square directed-flight matrix. `flights[i][j]` indicates whether city `j` can be reached directly
  from city `i` on a Monday.
- `days`: the per-city, per-week vacation allowances. `days[i][w]` is the maximum vacation time in city `i` during
  week `w`.

Let $n = \lvert\texttt{flights}\rvert$ be the city count and let $k = \lvert\texttt{days[0]}\rvert$ be the week
count. Staying in the current city is always permitted even though the flight-matrix diagonal is zero. A location
chosen for one week becomes the origin for the next Monday.

**Return value**

Return the maximum total vacation days across all $k$ weeks. The result counts only the allowances in the cities
where the traveler spends each week; flight time and work days add nothing.
