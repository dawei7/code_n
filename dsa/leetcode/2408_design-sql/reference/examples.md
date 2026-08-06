## Examples

**Example 1**

- **Input:** `["SQL", "ins", "sel", "ins", "exp", "rmv", "sel", "exp"]`, `[[["one", "two", "three"], [2, 3, 1]], ["two", ["first", "second", "third"]], ["two", 1, 3], ["two", ["fourth", "fifth", "sixth"]], ["two"], ["two", 1], ["two", 2, 2], ["two"]]`
- **Output:** `[null, true, "third", true, ["1,first,second,third", "2,fourth,fifth,sixth"], null, "fifth", ["2,fourth,fifth,sixth"]]`

**Example 2**

- **Input:** `["SQL", "ins", "sel", "rmv", "sel", "ins", "ins"]`, `[[["one", "two", "three"], [2, 3, 1]], ["two", ["first", "second", "third"]], ["two", 1, 3], ["two", 1], ["two", 1, 2], ["two", ["fourth", "fifth"]], ["two", ["fourth", "fifth", "sixth"]]]`
- **Output:** `[null, true, "third", null, "<null>", false, true]`

**Example 3**

- **Input:** `["SQL", "ins", "rmv", "ins", "exp"]`, `[[["data"], [1]], ["data", ["alpha"]], ["data", 1], ["data", ["beta"]], ["data"]]`
- **Output:** `[null, true, null, true, ["2,beta"]]`
