## Examples

**Example 1**

- **Input:** Sample `Drivers`, `Rides`, and `AcceptedRides` tables for 2020.
- **Output:**
  | month | working_percentage |
  | --- | --- |
  | 1 | 0.00 |
  | 2 | 0.00 |
  | 3 | 25.00 |
  | 4 | 0.00 |
  | 5 | 0.00 |
  | 6 | 0.00 |
  | 7 | 0.00 |
  | 8 | 0.00 |
  | 9 | 0.00 |
  | 10 | 0.00 |
  | 11 | 33.33 |
  | 12 | 0.00 |
- **Explanation:** In March (month 3), 4 drivers were active and 1 worked, giving 1/4 = 25.00%. In November (month 11), 6 drivers were active and 2 worked, giving 2/6 = 33.33%.

**Example 2**

- **Input:** One driver joined prior to 2020 completing 1 accepted ride in January.
- **Output:**
  | month | working_percentage |
  | --- | --- |
  | 1 | 100.00 |
- **Explanation:** January has 1 active driver and 1 working driver, giving 100.00%.

**Example 3**

- **Input:** Single driver completes multiple accepted rides in the same month.
- **Output:**
  | month | working_percentage |
  | --- | --- |
  | 1 | 100.00 |
- **Explanation:** Multiple rides by the same driver count as 1 distinct working driver.
