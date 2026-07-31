# Find All Possible Recipes from Given Supplies

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2115 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, String, Graph Theory, Topological Sort |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/) |

## Problem Description
### Goal

There are $n$ named recipes. Recipe `recipes[i]` can be prepared only when
every item in `ingredients[i]` is available. An ingredient may itself be the
name of another recipe, allowing a prepared recipe to unlock later recipes.

The strings in `supplies` are available initially, with an unlimited quantity
of each. Prepared recipes can likewise be used wherever their names occur as
ingredients. A dependency may name something that is never available, and
recipes may participate in cycles, including two recipes that require each
other.

Return every recipe that can eventually be prepared from the initial supplies
and other preparable recipes. The result may list those recipe names in any
order.

### Function Contract
**Inputs**

- `recipes`: A list of $n$ distinct recipe names.
- `ingredients`: A list of $n$ ingredient lists;
  `ingredients[i]` contains the distinct items required by `recipes[i]`.
- `supplies`: A nonempty list of distinct names available from the start.

Recipe names and initial supply names are mutually distinct. Let $V$ be the
number of distinct names appearing anywhere in the three inputs, and let $E$
be the total number of recipe requirements:

$$
E = \sum_{i=0}^{n-1} \lvert\texttt{ingredients}[i]\rvert.
$$

**Return value**

Return a list containing each preparable recipe exactly once, in any order.

### Examples
**Example 1**

- Input: `recipes = ["bread"], ingredients = [["yeast", "flour"]], supplies = ["yeast", "flour", "corn"]`
- Output: `["bread"]`

Both required ingredients are initially available.

**Example 2**

- Input: `recipes = ["bread", "sandwich"], ingredients = [["yeast", "flour"], ["bread", "meat"]], supplies = ["yeast", "flour", "meat"]`
- Output: `["bread", "sandwich"]`

Preparing `bread` makes the final ingredient of `sandwich` available.

**Example 3**

- Input: `recipes = ["bread", "sandwich", "burger"], ingredients = [["yeast", "flour"], ["bread", "meat"], ["sandwich", "meat", "bread"]], supplies = ["yeast", "flour", "meat"]`
- Output: `["bread", "sandwich", "burger"]`

The dependency chain can unlock several recipes in succession.
