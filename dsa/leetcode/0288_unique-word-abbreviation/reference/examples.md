## Examples

**Example 1**

- Input: `operations = ["ValidWordAbbr","isUnique","isUnique","isUnique","isUnique","isUnique"], arguments = [[["deer","door","cake","card"]],["dear"],["cart"],["cane"],["make"],["cake"]]`
- Output: `[null,false,true,false,true,true]`
- Explanation: Construct the index from `['deer','door','cake','card']`. `isUnique("dear")` is false because the different word `"deer"` also abbreviates to `d2r`. `isUnique("cart")` is true because the dictionary has no word abbreviated as `c2t`. `isUnique("cane")` is false because the different word `"cake"` shares `c2e`. `isUnique("make")` is true because `m2e` is absent. Finally, `isUnique("cake")` is true because `"cake"` itself is the only dictionary word with abbreviation `c2e`.
