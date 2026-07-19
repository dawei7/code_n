## General
**Generate all twelve months.** A recursive common table expression creates the fixed month spine from 1 through 12. Starting from it ensures that months with no drivers or rides remain present.

**Aggregate distinct working drivers by request month.** Join `AcceptedRides` to `Rides` by `ride_id`, restrict requests to 2020, group by the numeric request month, and count distinct `driver_id` values. The request date controls the month because the acceptance table has no separate completion date. Distinct counting prevents several rides by one driver from inflating the percentage.

**Use the month-end active population as denominator.** For month $m$, count driver rows whose `join_date` is earlier than the first day of month $m+1$. This exclusive cutoff correctly includes every join date in month $m$ and all earlier drivers. Divide the month's working count by that active count, guarding a zero denominator, round, and order the month spine.

The two aggregates match the numerator and denominator definitions independently. Their fixed twelve-month join therefore produces every required month exactly once, including zero-activity months.

## Complexity detail
The month spine has constant size. With ordinary join and grouping support, the driver relation and the ride/acceptance join require $O(d+r+a)$ total input processing. The accepted-ride grouping can retain up to $O(a)$ state for distinct driver/month combinations; the twelve month rows use constant space.

## Alternatives and edge cases
- **Count accepted rides:** Counting rows rather than distinct drivers overstates months in which one driver completes multiple rides.
- **Divide by all drivers:** Drivers who join after a month ends are not yet active and must not enter that month's denominator.
- **Group only months with rides:** This omits required zero rows; use a complete month relation and left join.
- Drivers who joined before 2020 are active in every 2020 month.
- A driver joining on a month's last day is active in that month.
- Rejected requests never contribute because they have no `AcceptedRides` row.
- Accepted rides requested outside 2020 do not contribute to any reported month.
- A zero active-driver count produces 0 rather than division by zero.
