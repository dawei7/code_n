## Examples

**Example 1**

- **Input:** `Ads = [[1,1,"Clicked"],[2,2,"Clicked"],[3,3,"Viewed"],[5,5,"Ignored"],[1,7,"Ignored"],[2,7,"Viewed"],[3,5,"Clicked"],[1,4,"Viewed"],[2,11,"Viewed"],[1,2,"Clicked"]]`

`Ads`:

| ad_id | user_id | action |
|---:|---:|---|
| 1 | 1 | Clicked |
| 2 | 2 | Clicked |
| 3 | 3 | Viewed |
| 5 | 5 | Ignored |
| 1 | 7 | Ignored |
| 2 | 7 | Viewed |
| 3 | 5 | Clicked |
| 1 | 4 | Viewed |
| 2 | 11 | Viewed |
| 1 | 2 | Clicked |

- **Output:** `[[1,66.67],[3,50.00],[2,33.33],[5,0.00]]`

Result:

| ad_id | ctr |
|---:|---:|
| 1 | 66.67 |
| 3 | 50.00 |
| 2 | 33.33 |
| 5 | 0.00 |

- **Explanation:** Advertisement `1` has two clicks and one view, so its CTR is $\frac{2}{2+1}\times100=66.67$. Advertisement `2` has one click and two views, giving $33.33$, while advertisement `3` has one of each and gives $50.00$. Advertisement `5` has neither a click nor a view, so its CTR is $0.00$. `Ignored` actions do not affect these calculations.
