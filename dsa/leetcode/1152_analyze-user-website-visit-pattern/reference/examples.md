## Examples

**Example 1**

- Input: `username = ["joe","joe","joe","james","james","james","james","mary","mary","mary"], timestamp = [1,2,3,4,5,6,7,8,9,10], website = ["home","about","career","home","cart","maps","home","home","about","career"]`
- Output: `["home","about","career"]`

- Explanation: Interpreting each record as `(username, website, timestamp)`, Joe's visits are `("joe", "home", 1)`, `("joe", "about", 2)`, and `("joe", "career", 3)`. James's visits are `("james", "home", 4)`, `("james", "cart", 5)`, `("james", "maps", 6)`, and `("james", "home", 7)`. Mary's visits are `("mary", "home", 8)`, `("mary", "about", 9)`, and `("mary", "career", 10)`.

The pattern `("home", "about", "career")` has score $2$ because Joe and Mary both match it. James gives each of `("home", "cart", "maps")`, `("home", "cart", "home")`, `("home", "maps", "home")`, and `("cart", "maps", "home")` a score of $1$. The pattern `("home", "home", "home")` has score $0$ because no user visited `"home"` three times. The unique highest score is therefore achieved by `["home","about","career"]`.

**Example 2**

- Input: `username = ["ua","ua","ua","ub","ub","ub"], timestamp = [1,2,3,4,5,6], website = ["a","b","a","a","b","c"]`
- Output: `["a","b","a"]`
