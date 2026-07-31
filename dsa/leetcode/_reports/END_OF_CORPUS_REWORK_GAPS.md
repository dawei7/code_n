# End-of-Corpus Rework Gaps

Generated: 2026-07-31

This generated inventory records every known remaining package and repository gap. Regenerate it from the live worktree instead of hand-editing counts or package rows.

## Summary

| Gap | Packages |
|---|---:|
| Not fully complete | 283 |
| Active verified-solution queue | 0 |
| Deferred documentation-only failures | 283 |
| Other completion failures | 0 |
| Source-fidelity unverified | 3285 |
| Source-fidelity invalid | 0 |
| Known repository-regression packages | 15 |

## Required end-of-corpus order

1. repair deferred documentation-completeness failures
2. review every unverified or invalid source-fidelity manifest
3. clear the repository-wide regression debt and rerun the full suite

## Active verified-solution queue

These packages still lack a remotely verified Optimal submission. Their rows show every completion gate currently missing.

| ID | Title | Missing gates | Cases | Submission | Variant errors | Package |
|---:|---|---|---:|---|---|---|

## Deferred documentation-only failures

These packages already pass cases, complexity, variant, app-source, and remote-submission gates. Their only local-completion failure is the current narrative-depth requirement.

| ID | Title | Words | Required | Paragraphs | Required | Section mode | Package |
|---:|---|---:|---:|---:|---:|---|---|
| 3 | Longest Substring Without Repeating Characters | 49 | 60 | 2 | 2 | reference/ | `dsa/leetcode/0003_longest-substring-without-repeating-characters` |
| 5 | Longest Palindromic Substring | 51 | 60 | 2 | 2 | reference/ | `dsa/leetcode/0005_longest-palindromic-substring` |
| 9 | Palindrome Number | 37 | 60 | 2 | 2 | reference/ | `dsa/leetcode/0009_palindrome-number` |
| 10 | Regular Expression Matching | 54 | 60 | 3 | 2 | reference/ | `dsa/leetcode/0010_regular-expression-matching` |
| 14 | Longest Common Prefix | 36 | 60 | 2 | 2 | reference/ | `dsa/leetcode/0014_longest-common-prefix` |
| 15 | 3Sum | 57 | 60 | 3 | 2 | reference/ | `dsa/leetcode/0015_3sum` |
| 16 | 3Sum Closest | 43 | 60 | 2 | 2 | reference/ | `dsa/leetcode/0016_3sum-closest` |
| 19 | Remove Nth Node From End of List | 56 | 60 | 3 | 2 | reference/ | `dsa/leetcode/0019_remove-nth-node-from-end-of-list` |
| 20 | Valid Parentheses | 55 | 60 | 3 | 2 | reference/ | `dsa/leetcode/0020_valid-parentheses` |
| 21 | Merge Two Sorted Lists | 38 | 60 | 2 | 2 | reference/ | `dsa/leetcode/0021_merge-two-sorted-lists` |
| 22 | Generate Parentheses | 38 | 60 | 2 | 2 | reference/ | `dsa/leetcode/0022_generate-parentheses` |
| 23 | Merge k Sorted Lists | 33 | 60 | 2 | 2 | reference/ | `dsa/leetcode/0023_merge-k-sorted-lists` |
| 24 | Swap Nodes in Pairs | 34 | 60 | 2 | 2 | reference/ | `dsa/leetcode/0024_swap-nodes-in-pairs` |
| 25 | Reverse Nodes in k-Group | 57 | 60 | 2 | 2 | reference/ | `dsa/leetcode/0025_reverse-nodes-in-k-group` |
| 26 | Remove Duplicates from Sorted Array | 55 | 60 | 2 | 2 | reference/ | `dsa/leetcode/0026_remove-duplicates-from-sorted-array` |
| 27 | Remove Element | 59 | 60 | 2 | 2 | reference/ | `dsa/leetcode/0027_remove-element` |
| 28 | Find the Index of the First Occurrence in a String | 26 | 60 | 2 | 2 | reference/ | `dsa/leetcode/0028_find-the-index-of-the-first-occurrence-in-a-string` |
| 29 | Divide Two Integers | 46 | 60 | 2 | 2 | reference/ | `dsa/leetcode/0029_divide-two-integers` |
| 32 | Longest Valid Parentheses | 42 | 60 | 2 | 2 | reference/ | `dsa/leetcode/0032_longest-valid-parentheses` |
| 34 | Find First and Last Position of Element in Sorted Array | 46 | 60 | 2 | 2 | reference/ | `dsa/leetcode/0034_find-first-and-last-position-of-element-in-sorted-array` |
| 35 | Search Insert Position | 41 | 60 | 2 | 2 | reference/ | `dsa/leetcode/0035_search-insert-position` |
| 40 | Combination Sum II | 34 | 60 | 2 | 2 | reference/ | `dsa/leetcode/0040_combination-sum-ii` |
| 41 | First Missing Positive | 33 | 60 | 2 | 2 | reference/ | `dsa/leetcode/0041_first-missing-positive` |
| 42 | Trapping Rain Water | 39 | 60 | 2 | 2 | reference/ | `dsa/leetcode/0042_trapping-rain-water` |
| 43 | Multiply Strings | 19 | 60 | 1 | 2 | reference/ | `dsa/leetcode/0043_multiply-strings` |
| 44 | Wildcard Matching | 46 | 60 | 3 | 2 | reference/ | `dsa/leetcode/0044_wildcard-matching` |
| 46 | Permutations | 22 | 60 | 1 | 2 | reference/ | `dsa/leetcode/0046_permutations` |
| 47 | Permutations II | 25 | 60 | 1 | 2 | reference/ | `dsa/leetcode/0047_permutations-ii` |
| 48 | Rotate Image | 37 | 60 | 2 | 2 | reference/ | `dsa/leetcode/0048_rotate-image` |
| 49 | Group Anagrams | 21 | 60 | 1 | 2 | reference/ | `dsa/leetcode/0049_group-anagrams` |
| 50 | Pow(x, n) | 20 | 60 | 1 | 2 | reference/ | `dsa/leetcode/0050_powx-n` |
| 51 | N-Queens | 52 | 60 | 2 | 2 | reference/ | `dsa/leetcode/0051_n-queens` |
| 52 | N-Queens II | 30 | 60 | 2 | 2 | reference/ | `dsa/leetcode/0052_n-queens-ii` |
| 53 | Maximum Subarray | 17 | 60 | 1 | 2 | reference/ | `dsa/leetcode/0053_maximum-subarray` |
| 54 | Spiral Matrix | 12 | 60 | 1 | 2 | reference/ | `dsa/leetcode/0054_spiral-matrix` |
| 55 | Jump Game | 34 | 60 | 2 | 2 | reference/ | `dsa/leetcode/0055_jump-game` |
| 56 | Merge Intervals | 34 | 60 | 2 | 2 | reference/ | `dsa/leetcode/0056_merge-intervals` |
| 58 | Length of Last Word | 28 | 60 | 2 | 2 | reference/ | `dsa/leetcode/0058_length-of-last-word` |
| 59 | Spiral Matrix II | 22 | 60 | 1 | 2 | reference/ | `dsa/leetcode/0059_spiral-matrix-ii` |
| 60 | Permutation Sequence | 53 | 60 | 4 | 2 | reference/ | `dsa/leetcode/0060_permutation-sequence` |
| 61 | Rotate List | 16 | 60 | 1 | 2 | reference/ | `dsa/leetcode/0061_rotate-list` |
| 64 | Minimum Path Sum | 32 | 60 | 1 | 2 | reference/ | `dsa/leetcode/0064_minimum-path-sum` |
| 66 | Plus One | 54 | 60 | 2 | 2 | reference/ | `dsa/leetcode/0066_plus-one` |
| 67 | Add Binary | 14 | 60 | 1 | 2 | reference/ | `dsa/leetcode/0067_add-binary` |
| 69 | Sqrt(x) | 46 | 60 | 2 | 2 | reference/ | `dsa/leetcode/0069_sqrtx` |
| 70 | Climbing Stairs | 34 | 60 | 2 | 2 | reference/ | `dsa/leetcode/0070_climbing-stairs` |
| 72 | Edit Distance | 34 | 60 | 3 | 2 | reference/ | `dsa/leetcode/0072_edit-distance` |
| 73 | Set Matrix Zeroes | 33 | 60 | 2 | 2 | reference/ | `dsa/leetcode/0073_set-matrix-zeroes` |
| 74 | Search a 2D Matrix | 54 | 60 | 3 | 2 | reference/ | `dsa/leetcode/0074_search-a-2d-matrix` |
| 75 | Sort Colors | 49 | 60 | 2 | 2 | reference/ | `dsa/leetcode/0075_sort-colors` |
| 76 | Minimum Window Substring | 51 | 60 | 2 | 2 | reference/ | `dsa/leetcode/0076_minimum-window-substring` |
| 77 | Combinations | 28 | 60 | 2 | 2 | reference/ | `dsa/leetcode/0077_combinations` |
| 78 | Subsets | 31 | 60 | 2 | 2 | reference/ | `dsa/leetcode/0078_subsets` |
| 82 | Remove Duplicates from Sorted List II | 34 | 60 | 2 | 2 | reference/ | `dsa/leetcode/0082_remove-duplicates-from-sorted-list-ii` |
| 83 | Remove Duplicates from Sorted List | 26 | 60 | 2 | 2 | reference/ | `dsa/leetcode/0083_remove-duplicates-from-sorted-list` |
| 84 | Largest Rectangle in Histogram | 26 | 60 | 2 | 2 | reference/ | `dsa/leetcode/0084_largest-rectangle-in-histogram` |
| 85 | Maximal Rectangle | 23 | 60 | 1 | 2 | reference/ | `dsa/leetcode/0085_maximal-rectangle` |
| 86 | Partition List | 39 | 60 | 2 | 2 | reference/ | `dsa/leetcode/0086_partition-list` |
| 90 | Subsets II | 31 | 60 | 2 | 2 | reference/ | `dsa/leetcode/0090_subsets-ii` |
| 92 | Reverse Linked List II | 31 | 60 | 2 | 2 | reference/ | `dsa/leetcode/0092_reverse-linked-list-ii` |
| 94 | Binary Tree Inorder Traversal | 28 | 60 | 1 | 2 | reference/ | `dsa/leetcode/0094_binary-tree-inorder-traversal` |
| 95 | Unique Binary Search Trees II | 31 | 60 | 2 | 2 | reference/ | `dsa/leetcode/0095_unique-binary-search-trees-ii` |
| 96 | Unique Binary Search Trees | 25 | 60 | 1 | 2 | reference/ | `dsa/leetcode/0096_unique-binary-search-trees` |
| 98 | Validate Binary Search Tree | 54 | 60 | 3 | 2 | reference/ | `dsa/leetcode/0098_validate-binary-search-tree` |
| 99 | Recover Binary Search Tree | 23 | 60 | 1 | 2 | reference/ | `dsa/leetcode/0099_recover-binary-search-tree` |
| 100 | Same Tree | 33 | 60 | 2 | 2 | reference/ | `dsa/leetcode/0100_same-tree` |
| 101 | Symmetric Tree | 26 | 60 | 1 | 2 | reference/ | `dsa/leetcode/0101_symmetric-tree` |
| 102 | Binary Tree Level Order Traversal | 32 | 60 | 1 | 2 | reference/ | `dsa/leetcode/0102_binary-tree-level-order-traversal` |
| 103 | Binary Tree Zigzag Level Order Traversal | 38 | 60 | 1 | 2 | reference/ | `dsa/leetcode/0103_binary-tree-zigzag-level-order-traversal` |
| 104 | Maximum Depth of Binary Tree | 36 | 60 | 2 | 2 | reference/ | `dsa/leetcode/0104_maximum-depth-of-binary-tree` |
| 105 | Construct Binary Tree from Preorder and Inorder Traversal | 31 | 60 | 1 | 2 | reference/ | `dsa/leetcode/0105_construct-binary-tree-from-preorder-and-inorder-traversal` |
| 106 | Construct Binary Tree from Inorder and Postorder Traversal | 31 | 60 | 1 | 2 | reference/ | `dsa/leetcode/0106_construct-binary-tree-from-inorder-and-postorder-traversal` |
| 107 | Binary Tree Level Order Traversal II | 32 | 60 | 1 | 2 | reference/ | `dsa/leetcode/0107_binary-tree-level-order-traversal-ii` |
| 108 | Convert Sorted Array to Binary Search Tree | 41 | 60 | 2 | 2 | reference/ | `dsa/leetcode/0108_convert-sorted-array-to-binary-search-tree` |
| 109 | Convert Sorted List to Binary Search Tree | 44 | 60 | 2 | 2 | reference/ | `dsa/leetcode/0109_convert-sorted-list-to-binary-search-tree` |
| 110 | Balanced Binary Tree | 32 | 60 | 2 | 2 | reference/ | `dsa/leetcode/0110_balanced-binary-tree` |
| 111 | Minimum Depth of Binary Tree | 28 | 60 | 2 | 2 | reference/ | `dsa/leetcode/0111_minimum-depth-of-binary-tree` |
| 112 | Path Sum | 34 | 60 | 2 | 2 | reference/ | `dsa/leetcode/0112_path-sum` |
| 113 | Path Sum II | 58 | 60 | 2 | 2 | reference/ | `dsa/leetcode/0113_path-sum-ii` |
| 114 | Flatten Binary Tree to Linked List | 54 | 60 | 2 | 2 | reference/ | `dsa/leetcode/0114_flatten-binary-tree-to-linked-list` |
| 115 | Distinct Subsequences | 47 | 60 | 2 | 2 | reference/ | `dsa/leetcode/0115_distinct-subsequences` |
| 117 | Populating Next Right Pointers in Each Node II | 53 | 60 | 2 | 2 | reference/ | `dsa/leetcode/0117_populating-next-right-pointers-in-each-node-ii` |
| 120 | Triangle | 51 | 60 | 2 | 2 | reference/ | `dsa/leetcode/0120_triangle` |
| 121 | Best Time to Buy and Sell Stock | 59 | 60 | 3 | 2 | reference/ | `dsa/leetcode/0121_best-time-to-buy-and-sell-stock` |
| 123 | Best Time to Buy and Sell Stock III | 29 | 60 | 2 | 2 | reference/ | `dsa/leetcode/0123_best-time-to-buy-and-sell-stock-iii` |
| 125 | Valid Palindrome | 47 | 60 | 2 | 2 | reference/ | `dsa/leetcode/0125_valid-palindrome` |
| 128 | Longest Consecutive Sequence | 24 | 60 | 2 | 2 | reference/ | `dsa/leetcode/0128_longest-consecutive-sequence` |
| 131 | Palindrome Partitioning | 39 | 60 | 2 | 2 | reference/ | `dsa/leetcode/0131_palindrome-partitioning` |
| 132 | Palindrome Partitioning II | 40 | 60 | 2 | 2 | reference/ | `dsa/leetcode/0132_palindrome-partitioning-ii` |
| 133 | Clone Graph | 49 | 60 | 2 | 2 | reference/ | `dsa/leetcode/0133_clone-graph` |
| 135 | Candy | 58 | 60 | 4 | 2 | reference/ | `dsa/leetcode/0135_candy` |
| 136 | Single Number | 36 | 60 | 2 | 2 | reference/ | `dsa/leetcode/0136_single-number` |
| 137 | Single Number II | 38 | 60 | 2 | 2 | reference/ | `dsa/leetcode/0137_single-number-ii` |
| 139 | Word Break | 26 | 60 | 1 | 2 | reference/ | `dsa/leetcode/0139_word-break` |
| 140 | Word Break II | 29 | 60 | 1 | 2 | reference/ | `dsa/leetcode/0140_word-break-ii` |
| 144 | Binary Tree Preorder Traversal | 27 | 60 | 1 | 2 | reference/ | `dsa/leetcode/0144_binary-tree-preorder-traversal` |
| 145 | Binary Tree Postorder Traversal | 28 | 60 | 1 | 2 | reference/ | `dsa/leetcode/0145_binary-tree-postorder-traversal` |
| 148 | Sort List | 21 | 60 | 1 | 2 | reference/ | `dsa/leetcode/0148_sort-list` |
| 149 | Max Points on a Line | 33 | 60 | 1 | 2 | reference/ | `dsa/leetcode/0149_max-points-on-a-line` |
| 150 | Evaluate Reverse Polish Notation | 23 | 60 | 1 | 2 | reference/ | `dsa/leetcode/0150_evaluate-reverse-polish-notation` |
| 151 | Reverse Words in a String | 42 | 60 | 2 | 2 | reference/ | `dsa/leetcode/0151_reverse-words-in-a-string` |
| 152 | Maximum Product Subarray | 34 | 60 | 2 | 2 | reference/ | `dsa/leetcode/0152_maximum-product-subarray` |
| 157 | Read N Characters Given Read4 | 23 | 60 | 1 | 2 | reference/ | `dsa/leetcode/0157_read-n-characters-given-read4` |
| 158 | Read N Characters Given read4 II - Call Multiple Times | 31 | 60 | 1 | 2 | reference/ | `dsa/leetcode/0158_read-n-characters-given-read4-ii-call-multiple-times` |
| 159 | Longest Substring with At Most Two Distinct Characters | 17 | 60 | 1 | 2 | reference/ | `dsa/leetcode/0159_longest-substring-with-at-most-two-distinct-characters` |
| 161 | One Edit Distance | 59 | 60 | 3 | 2 | reference/ | `dsa/leetcode/0161_one-edit-distance` |
| 164 | Maximum Gap | 44 | 60 | 2 | 2 | reference/ | `dsa/leetcode/0164_maximum-gap` |
| 166 | Fraction to Recurring Decimal | 52 | 60 | 2 | 2 | reference/ | `dsa/leetcode/0166_fraction-to-recurring-decimal` |
| 168 | Excel Sheet Column Title | 32 | 60 | 3 | 2 | reference/ | `dsa/leetcode/0168_excel-sheet-column-title` |
| 169 | Majority Element | 35 | 60 | 2 | 2 | reference/ | `dsa/leetcode/0169_majority-element` |
| 170 | Two Sum III - Data structure design | 56 | 60 | 3 | 2 | reference/ | `dsa/leetcode/0170_two-sum-iii-data-structure-design` |
| 171 | Excel Sheet Column Number | 35 | 60 | 3 | 2 | reference/ | `dsa/leetcode/0171_excel-sheet-column-number` |
| 172 | Factorial Trailing Zeroes | 12 | 60 | 1 | 2 | reference/ | `dsa/leetcode/0172_factorial-trailing-zeroes` |
| 175 | Combine Two Tables | 42 | 60 | 2 | 2 | reference/ | `dsa/leetcode/0175_combine-two-tables` |
| 176 | Second Highest Salary | 24 | 60 | 1 | 2 | reference/ | `dsa/leetcode/0176_second-highest-salary` |
| 177 | Nth Highest Salary | 23 | 60 | 1 | 2 | reference/ | `dsa/leetcode/0177_nth-highest-salary` |
| 178 | Rank Scores | 49 | 60 | 3 | 2 | reference/ | `dsa/leetcode/0178_rank-scores` |
| 179 | Largest Number | 39 | 60 | 2 | 2 | reference/ | `dsa/leetcode/0179_largest-number` |
| 180 | Consecutive Numbers | 24 | 60 | 2 | 2 | reference/ | `dsa/leetcode/0180_consecutive-numbers` |
| 181 | Employees Earning More Than Their Managers | 31 | 60 | 2 | 2 | reference/ | `dsa/leetcode/0181_employees-earning-more-than-their-managers` |
| 182 | Duplicate Emails | 38 | 60 | 2 | 2 | reference/ | `dsa/leetcode/0182_duplicate-emails` |
| 183 | Customers Who Never Order | 26 | 60 | 2 | 2 | reference/ | `dsa/leetcode/0183_customers-who-never-order` |
| 184 | Department Highest Salary | 28 | 60 | 2 | 2 | reference/ | `dsa/leetcode/0184_department-highest-salary` |
| 185 | Department Top Three Salaries | 40 | 60 | 2 | 2 | reference/ | `dsa/leetcode/0185_department-top-three-salaries` |
| 186 | Reverse Words in a String II | 40 | 60 | 2 | 2 | reference/ | `dsa/leetcode/0186_reverse-words-in-a-string-ii` |
| 187 | Repeated DNA Sequences | 42 | 60 | 2 | 2 | reference/ | `dsa/leetcode/0187_repeated-dna-sequences` |
| 188 | Best Time to Buy and Sell Stock IV | 41 | 60 | 2 | 2 | reference/ | `dsa/leetcode/0188_best-time-to-buy-and-sell-stock-iv` |
| 189 | Rotate Array | 17 | 60 | 1 | 2 | reference/ | `dsa/leetcode/0189_rotate-array` |
| 190 | Reverse Bits | 19 | 60 | 1 | 2 | reference/ | `dsa/leetcode/0190_reverse-bits` |
| 191 | Number of 1 Bits | 23 | 60 | 1 | 2 | reference/ | `dsa/leetcode/0191_number-of-1-bits` |
| 192 | Word Frequency | 17 | 60 | 1 | 2 | reference/ | `dsa/leetcode/0192_word-frequency` |
| 193 | Valid Phone Numbers | 53 | 60 | 2 | 2 | reference/ | `dsa/leetcode/0193_valid-phone-numbers` |
| 194 | Transpose File | 11 | 60 | 1 | 2 | reference/ | `dsa/leetcode/0194_transpose-file` |
| 195 | Tenth Line | 11 | 60 | 1 | 2 | reference/ | `dsa/leetcode/0195_tenth-line` |
| 196 | Delete Duplicate Emails | 18 | 60 | 1 | 2 | reference/ | `dsa/leetcode/0196_delete-duplicate-emails` |
| 197 | Rising Temperature | 26 | 60 | 2 | 2 | reference/ | `dsa/leetcode/0197_rising-temperature` |
| 198 | House Robber | 43 | 60 | 2 | 2 | reference/ | `dsa/leetcode/0198_house-robber` |
| 199 | Binary Tree Right Side View | 52 | 60 | 2 | 2 | reference/ | `dsa/leetcode/0199_binary-tree-right-side-view` |
| 201 | Bitwise AND of Numbers Range | 27 | 60 | 2 | 2 | reference/ | `dsa/leetcode/0201_bitwise-and-of-numbers-range` |
| 203 | Remove Linked List Elements | 33 | 60 | 2 | 2 | reference/ | `dsa/leetcode/0203_remove-linked-list-elements` |
| 204 | Count Primes | 18 | 60 | 1 | 2 | reference/ | `dsa/leetcode/0204_count-primes` |
| 206 | Reverse Linked List | 16 | 60 | 1 | 2 | reference/ | `dsa/leetcode/0206_reverse-linked-list` |
| 209 | Minimum Size Subarray Sum | 40 | 60 | 2 | 2 | reference/ | `dsa/leetcode/0209_minimum-size-subarray-sum` |
| 214 | Shortest Palindrome | 30 | 60 | 2 | 2 | reference/ | `dsa/leetcode/0214_shortest-palindrome` |
| 215 | Kth Largest Element in an Array | 56 | 60 | 3 | 2 | reference/ | `dsa/leetcode/0215_kth-largest-element-in-an-array` |
| 216 | Combination Sum III | 51 | 60 | 3 | 2 | reference/ | `dsa/leetcode/0216_combination-sum-iii` |
| 217 | Contains Duplicate | 23 | 60 | 1 | 2 | reference/ | `dsa/leetcode/0217_contains-duplicate` |
| 219 | Contains Duplicate II | 39 | 60 | 2 | 2 | reference/ | `dsa/leetcode/0219_contains-duplicate-ii` |
| 220 | Contains Duplicate III | 56 | 60 | 4 | 2 | reference/ | `dsa/leetcode/0220_contains-duplicate-iii` |
| 221 | Maximal Square | 26 | 60 | 1 | 2 | reference/ | `dsa/leetcode/0221_maximal-square` |
| 223 | Rectangle Area | 43 | 60 | 2 | 2 | reference/ | `dsa/leetcode/0223_rectangle-area` |
| 224 | Basic Calculator | 20 | 60 | 1 | 2 | reference/ | `dsa/leetcode/0224_basic-calculator` |
| 225 | Implement Stack using Queues | 56 | 60 | 2 | 2 | reference/ | `dsa/leetcode/0225_implement-stack-using-queues` |
| 226 | Invert Binary Tree | 14 | 60 | 1 | 2 | reference/ | `dsa/leetcode/0226_invert-binary-tree` |
| 227 | Basic Calculator II | 44 | 60 | 2 | 2 | reference/ | `dsa/leetcode/0227_basic-calculator-ii` |
| 229 | Majority Element II | 20 | 60 | 1 | 2 | reference/ | `dsa/leetcode/0229_majority-element-ii` |
| 230 | Kth Smallest Element in a BST | 23 | 60 | 1 | 2 | reference/ | `dsa/leetcode/0230_kth-smallest-element-in-a-bst` |
| 231 | Power of Two | 31 | 60 | 2 | 2 | reference/ | `dsa/leetcode/0231_power-of-two` |
| 232 | Implement Queue using Stacks | 57 | 60 | 2 | 2 | reference/ | `dsa/leetcode/0232_implement-queue-using-stacks` |
| 233 | Number of Digit One | 24 | 60 | 1 | 2 | reference/ | `dsa/leetcode/0233_number-of-digit-one` |
| 234 | Palindrome Linked List | 22 | 60 | 1 | 2 | reference/ | `dsa/leetcode/0234_palindrome-linked-list` |
| 235 | Lowest Common Ancestor of a Binary Search Tree | 50 | 60 | 2 | 2 | reference/ | `dsa/leetcode/0235_lowest-common-ancestor-of-a-binary-search-tree` |
| 236 | Lowest Common Ancestor of a Binary Tree | 50 | 60 | 2 | 2 | reference/ | `dsa/leetcode/0236_lowest-common-ancestor-of-a-binary-tree` |
| 238 | Product of Array Except Self | 55 | 60 | 3 | 2 | reference/ | `dsa/leetcode/0238_product-of-array-except-self` |
| 239 | Sliding Window Maximum | 50 | 60 | 2 | 2 | reference/ | `dsa/leetcode/0239_sliding-window-maximum` |
| 240 | Search a 2D Matrix II | 49 | 60 | 3 | 2 | reference/ | `dsa/leetcode/0240_search-a-2d-matrix-ii` |
| 242 | Valid Anagram | 34 | 60 | 1 | 2 | reference/ | `dsa/leetcode/0242_valid-anagram` |
| 243 | Shortest Word Distance | 38 | 60 | 2 | 2 | reference/ | `dsa/leetcode/0243_shortest-word-distance` |
| 244 | Shortest Word Distance II | 58 | 60 | 3 | 2 | reference/ | `dsa/leetcode/0244_shortest-word-distance-ii` |
| 245 | Shortest Word Distance III | 49 | 60 | 2 | 2 | reference/ | `dsa/leetcode/0245_shortest-word-distance-iii` |
| 246 | Strobogrammatic Number | 30 | 60 | 2 | 2 | reference/ | `dsa/leetcode/0246_strobogrammatic-number` |
| 247 | Strobogrammatic Number II | 42 | 60 | 2 | 2 | reference/ | `dsa/leetcode/0247_strobogrammatic-number-ii` |
| 248 | Strobogrammatic Number III | 37 | 60 | 2 | 2 | reference/ | `dsa/leetcode/0248_strobogrammatic-number-iii` |
| 250 | Count Univalue Subtrees | 28 | 60 | 2 | 2 | reference/ | `dsa/leetcode/0250_count-univalue-subtrees` |
| 252 | Meeting Rooms | 57 | 60 | 3 | 2 | reference/ | `dsa/leetcode/0252_meeting-rooms` |
| 253 | Meeting Rooms II | 33 | 60 | 2 | 2 | reference/ | `dsa/leetcode/0253_meeting-rooms-ii` |
| 254 | Factor Combinations | 56 | 60 | 3 | 2 | reference/ | `dsa/leetcode/0254_factor-combinations` |
| 255 | Verify Preorder Sequence in Binary Search Tree | 26 | 60 | 1 | 2 | reference/ | `dsa/leetcode/0255_verify-preorder-sequence-in-binary-search-tree` |
| 257 | Binary Tree Paths | 23 | 60 | 2 | 2 | reference/ | `dsa/leetcode/0257_binary-tree-paths` |
| 258 | Add Digits | 33 | 60 | 2 | 2 | reference/ | `dsa/leetcode/0258_add-digits` |
| 259 | 3Sum Smaller | 35 | 60 | 3 | 2 | reference/ | `dsa/leetcode/0259_3sum-smaller` |
| 260 | Single Number III | 50 | 60 | 3 | 2 | reference/ | `dsa/leetcode/0260_single-number-iii` |
| 261 | Graph Valid Tree | 46 | 60 | 2 | 2 | reference/ | `dsa/leetcode/0261_graph-valid-tree` |
| 263 | Ugly Number | 32 | 60 | 2 | 2 | reference/ | `dsa/leetcode/0263_ugly-number` |
| 264 | Ugly Number II | 28 | 60 | 2 | 2 | reference/ | `dsa/leetcode/0264_ugly-number-ii` |
| 266 | Palindrome Permutation | 26 | 60 | 1 | 2 | reference/ | `dsa/leetcode/0266_palindrome-permutation` |
| 267 | Palindrome Permutation II | 34 | 60 | 2 | 2 | reference/ | `dsa/leetcode/0267_palindrome-permutation-ii` |
| 268 | Missing Number | 29 | 60 | 2 | 2 | reference/ | `dsa/leetcode/0268_missing-number` |
| 270 | Closest Binary Search Tree Value | 34 | 60 | 1 | 2 | reference/ | `dsa/leetcode/0270_closest-binary-search-tree-value` |
| 272 | Closest Binary Search Tree Value II | 53 | 60 | 2 | 2 | reference/ | `dsa/leetcode/0272_closest-binary-search-tree-value-ii` |
| 273 | Integer to English Words | 9 | 60 | 1 | 2 | reference/ | `dsa/leetcode/0273_integer-to-english-words` |
| 274 | H-Index | 45 | 60 | 2 | 2 | reference/ | `dsa/leetcode/0274_h-index` |
| 275 | H-Index II | 54 | 60 | 3 | 2 | reference/ | `dsa/leetcode/0275_h-index-ii` |
| 276 | Paint Fence | 51 | 60 | 3 | 2 | reference/ | `dsa/leetcode/0276_paint-fence` |
| 279 | Perfect Squares | 44 | 60 | 2 | 2 | reference/ | `dsa/leetcode/0279_perfect-squares` |
| 280 | Wiggle Sort | 28 | 60 | 3 | 2 | reference/ | `dsa/leetcode/0280_wiggle-sort` |
| 282 | Expression Add Operators | 44 | 60 | 2 | 2 | reference/ | `dsa/leetcode/0282_expression-add-operators` |
| 283 | Move Zeroes | 33 | 60 | 2 | 2 | reference/ | `dsa/leetcode/0283_move-zeroes` |
| 285 | Inorder Successor in BST | 45 | 60 | 2 | 2 | reference/ | `dsa/leetcode/0285_inorder-successor-in-bst` |
| 287 | Find the Duplicate Number | 40 | 60 | 3 | 2 | reference/ | `dsa/leetcode/0287_find-the-duplicate-number` |
| 291 | Word Pattern II | 57 | 60 | 2 | 2 | reference/ | `dsa/leetcode/0291_word-pattern-ii` |
| 294 | Flip Game II | 51 | 60 | 2 | 2 | reference/ | `dsa/leetcode/0294_flip-game-ii` |
| 298 | Binary Tree Longest Consecutive Sequence | 59 | 60 | 2 | 2 | reference/ | `dsa/leetcode/0298_binary-tree-longest-consecutive-sequence` |
| 300 | Longest Increasing Subsequence | 40 | 60 | 1 | 2 | reference/ | `dsa/leetcode/0300_longest-increasing-subsequence` |
| 301 | Remove Invalid Parentheses | 41 | 60 | 2 | 2 | reference/ | `dsa/leetcode/0301_remove-invalid-parentheses` |
| 303 | Range Sum Query - Immutable | 54 | 60 | 3 | 2 | reference/ | `dsa/leetcode/0303_range-sum-query-immutable` |
| 306 | Additive Number | 57 | 60 | 2 | 2 | reference/ | `dsa/leetcode/0306_additive-number` |
| 307 | Range Sum Query - Mutable | 53 | 60 | 3 | 2 | reference/ | `dsa/leetcode/0307_range-sum-query-mutable` |
| 309 | Best Time to Buy and Sell Stock with Cooldown | 46 | 60 | 2 | 2 | reference/ | `dsa/leetcode/0309_best-time-to-buy-and-sell-stock-with-cooldown` |
| 311 | Sparse Matrix Multiplication | 36 | 60 | 1 | 2 | reference/ | `dsa/leetcode/0311_sparse-matrix-multiplication` |
| 313 | Super Ugly Number | 46 | 60 | 2 | 2 | reference/ | `dsa/leetcode/0313_super-ugly-number` |
| 314 | Binary Tree Vertical Order Traversal | 43 | 60 | 2 | 2 | reference/ | `dsa/leetcode/0314_binary-tree-vertical-order-traversal` |
| 315 | Count of Smaller Numbers After Self | 28 | 60 | 1 | 2 | reference/ | `dsa/leetcode/0315_count-of-smaller-numbers-after-self` |
| 316 | Remove Duplicate Letters | 31 | 60 | 1 | 2 | reference/ | `dsa/leetcode/0316_remove-duplicate-letters` |
| 318 | Maximum Product of Word Lengths | 33 | 60 | 1 | 2 | reference/ | `dsa/leetcode/0318_maximum-product-of-word-lengths` |
| 322 | Coin Change | 43 | 60 | 2 | 2 | reference/ | `dsa/leetcode/0322_coin-change` |
| 323 | Number of Connected Components in an Undirected Graph | 42 | 60 | 2 | 2 | reference/ | `dsa/leetcode/0323_number-of-connected-components-in-an-undirected-graph` |
| 324 | Wiggle Sort II | 32 | 60 | 3 | 2 | reference/ | `dsa/leetcode/0324_wiggle-sort-ii` |
| 325 | Maximum Size Subarray Sum Equals k | 28 | 60 | 1 | 2 | reference/ | `dsa/leetcode/0325_maximum-size-subarray-sum-equals-k` |
| 326 | Power of Three | 31 | 60 | 2 | 2 | reference/ | `dsa/leetcode/0326_power-of-three` |
| 327 | Count of Range Sum | 47 | 60 | 2 | 2 | reference/ | `dsa/leetcode/0327_count-of-range-sum` |
| 334 | Increasing Triplet Subsequence | 50 | 60 | 3 | 2 | reference/ | `dsa/leetcode/0334_increasing-triplet-subsequence` |
| 338 | Counting Bits | 40 | 60 | 1 | 2 | reference/ | `dsa/leetcode/0338_counting-bits` |
| 340 | Longest Substring with At Most K Distinct Characters | 23 | 60 | 1 | 2 | reference/ | `dsa/leetcode/0340_longest-substring-with-at-most-k-distinct-characters` |
| 342 | Power of Four | 34 | 60 | 3 | 2 | reference/ | `dsa/leetcode/0342_power-of-four` |
| 343 | Integer Break | 36 | 60 | 2 | 2 | reference/ | `dsa/leetcode/0343_integer-break` |
| 344 | Reverse String | 27 | 60 | 2 | 2 | reference/ | `dsa/leetcode/0344_reverse-string` |
| 345 | Reverse Vowels of a String | 37 | 60 | 2 | 2 | reference/ | `dsa/leetcode/0345_reverse-vowels-of-a-string` |
| 347 | Top K Frequent Elements | 25 | 60 | 1 | 2 | reference/ | `dsa/leetcode/0347_top-k-frequent-elements` |
| 349 | Intersection of Two Arrays | 30 | 60 | 1 | 2 | reference/ | `dsa/leetcode/0349_intersection-of-two-arrays` |
| 350 | Intersection of Two Arrays II | 38 | 60 | 1 | 2 | reference/ | `dsa/leetcode/0350_intersection-of-two-arrays-ii` |
| 354 | Russian Doll Envelopes | 56 | 60 | 2 | 2 | reference/ | `dsa/leetcode/0354_russian-doll-envelopes` |
| 356 | Line Reflection | 48 | 60 | 2 | 2 | reference/ | `dsa/leetcode/0356_line-reflection` |
| 357 | Count Numbers with Unique Digits | 25 | 60 | 3 | 2 | reference/ | `dsa/leetcode/0357_count-numbers-with-unique-digits` |
| 358 | Rearrange String k Distance Apart | 49 | 60 | 2 | 2 | reference/ | `dsa/leetcode/0358_rearrange-string-k-distance-apart` |
| 360 | Sort Transformed Array | 35 | 60 | 3 | 2 | reference/ | `dsa/leetcode/0360_sort-transformed-array` |
| 363 | Max Sum of Rectangle No Larger Than K | 40 | 60 | 2 | 2 | reference/ | `dsa/leetcode/0363_max-sum-of-rectangle-no-larger-than-k` |
| 366 | Find Leaves of Binary Tree | 43 | 60 | 3 | 2 | reference/ | `dsa/leetcode/0366_find-leaves-of-binary-tree` |
| 367 | Valid Perfect Square | 39 | 60 | 2 | 2 | reference/ | `dsa/leetcode/0367_valid-perfect-square` |
| 368 | Largest Divisible Subset | 50 | 60 | 3 | 2 | reference/ | `dsa/leetcode/0368_largest-divisible-subset` |
| 369 | Plus One Linked List | 34 | 60 | 2 | 2 | reference/ | `dsa/leetcode/0369_plus-one-linked-list` |
| 370 | Range Addition | 58 | 60 | 3 | 2 | reference/ | `dsa/leetcode/0370_range-addition` |
| 371 | Sum of Two Integers | 14 | 60 | 1 | 2 | reference/ | `dsa/leetcode/0371_sum-of-two-integers` |
| 372 | Super Pow | 27 | 60 | 3 | 2 | reference/ | `dsa/leetcode/0372_super-pow` |
| 373 | Find K Pairs with Smallest Sums | 46 | 60 | 2 | 2 | reference/ | `dsa/leetcode/0373_find-k-pairs-with-smallest-sums` |
| 377 | Combination Sum IV | 48 | 60 | 2 | 2 | reference/ | `dsa/leetcode/0377_combination-sum-iv` |
| 382 | Linked List Random Node | 50 | 60 | 3 | 2 | reference/ | `dsa/leetcode/0382_linked-list-random-node` |
| 383 | Ransom Note | 38 | 60 | 2 | 2 | reference/ | `dsa/leetcode/0383_ransom-note` |
| 384 | Shuffle an Array | 48 | 60 | 3 | 2 | reference/ | `dsa/leetcode/0384_shuffle-an-array` |
| 385 | Mini Parser | 50 | 60 | 2 | 2 | reference/ | `dsa/leetcode/0385_mini-parser` |
| 386 | Lexicographical Numbers | 40 | 60 | 2 | 2 | reference/ | `dsa/leetcode/0386_lexicographical-numbers` |
| 387 | First Unique Character in a String | 28 | 60 | 2 | 2 | reference/ | `dsa/leetcode/0387_first-unique-character-in-a-string` |
| 389 | Find the Difference | 32 | 60 | 2 | 2 | reference/ | `dsa/leetcode/0389_find-the-difference` |
| 391 | Perfect Rectangle | 54 | 60 | 2 | 2 | reference/ | `dsa/leetcode/0391_perfect-rectangle` |
| 392 | Is Subsequence | 45 | 60 | 2 | 2 | reference/ | `dsa/leetcode/0392_is-subsequence` |
| 395 | Longest Substring with At Least K Repeating Characters | 37 | 60 | 2 | 2 | reference/ | `dsa/leetcode/0395_longest-substring-with-at-least-k-repeating-characters` |
| 397 | Integer Replacement | 41 | 60 | 3 | 2 | reference/ | `dsa/leetcode/0397_integer-replacement` |
| 400 | Nth Digit | 39 | 60 | 3 | 2 | reference/ | `dsa/leetcode/0400_nth-digit` |
| 402 | Remove K Digits | 47 | 60 | 2 | 2 | reference/ | `dsa/leetcode/0402_remove-k-digits` |
| 404 | Sum of Left Leaves | 34 | 60 | 2 | 2 | reference/ | `dsa/leetcode/0404_sum-of-left-leaves` |
| 405 | Convert a Number to Hexadecimal | 36 | 60 | 2 | 2 | reference/ | `dsa/leetcode/0405_convert-a-number-to-hexadecimal` |
| 407 | Trapping Rain Water II | 40 | 60 | 2 | 2 | reference/ | `dsa/leetcode/0407_trapping-rain-water-ii` |
| 3701 | Compute Alternating Sum | 42 | 60 | 3 | 2 | reference/ | `dsa/leetcode/3701_compute-alternating-sum` |
| 3702 | Longest Subsequence With Non-Zero Bitwise XOR | 35 | 60 | 2 | 2 | reference/ | `dsa/leetcode/3702_longest-subsequence-with-non-zero-bitwise-xor` |
| 3704 | Count No-Zero Pairs That Sum to N | 43 | 60 | 3 | 2 | reference/ | `dsa/leetcode/3704_count-no-zero-pairs-that-sum-to-n` |
| 3706 | Maximum Distance Between Unequal Words in Array II | 53 | 60 | 2 | 2 | reference/ | `dsa/leetcode/3706_maximum-distance-between-unequal-words-in-array-ii` |
| 3708 | Longest Fibonacci Subarray | 48 | 60 | 3 | 2 | reference/ | `dsa/leetcode/3708_longest-fibonacci-subarray` |
| 3712 | Sum of Elements With Frequency Divisible by K | 42 | 60 | 2 | 2 | reference/ | `dsa/leetcode/3712_sum-of-elements-with-frequency-divisible-by-k` |
| 3713 | Longest Balanced Substring I | 37 | 60 | 3 | 2 | reference/ | `dsa/leetcode/3713_longest-balanced-substring-i` |
| 3714 | Longest Balanced Substring II | 43 | 60 | 3 | 2 | reference/ | `dsa/leetcode/3714_longest-balanced-substring-ii` |
| 3718 | Smallest Missing Multiple of K | 37 | 60 | 2 | 2 | reference/ | `dsa/leetcode/3718_smallest-missing-multiple-of-k` |
| 3719 | Longest Balanced Subarray I | 36 | 60 | 2 | 2 | reference/ | `dsa/leetcode/3719_longest-balanced-subarray-i` |
| 3721 | Longest Balanced Subarray II | 36 | 60 | 2 | 2 | reference/ | `dsa/leetcode/3721_longest-balanced-subarray-ii` |
| 3722 | Lexicographically Smallest String After Reverse | 52 | 60 | 3 | 2 | reference/ | `dsa/leetcode/3722_lexicographically-smallest-string-after-reverse` |
| 3725 | Count Ways to Choose Coprime Integers from Rows | 50 | 60 | 2 | 2 | reference/ | `dsa/leetcode/3725_count-ways-to-choose-coprime-integers-from-rows` |
| 3726 | Remove Zeros in Decimal Representation | 22 | 60 | 1 | 2 | reference/ | `dsa/leetcode/3726_remove-zeros-in-decimal-representation` |
| 3732 | Maximum Product of Three Elements After One Replacement | 48 | 60 | 4 | 2 | reference/ | `dsa/leetcode/3732_maximum-product-of-three-elements-after-one-replacement` |
| 3734 | Lexicographically Smallest Palindromic Permutation Greater Than Target | 48 | 60 | 2 | 2 | reference/ | `dsa/leetcode/3734_lexicographically-smallest-palindromic-permutation-greater-than-target` |
| 3735 | Lexicographically Smallest String After Reverse II | 57 | 60 | 4 | 2 | reference/ | `dsa/leetcode/3735_lexicographically-smallest-string-after-reverse-ii` |
| 3783 | Mirror Distance of an Integer | 58 | 60 | 4 | 2 | reference/ | `dsa/leetcode/3783_mirror-distance-of-an-integer` |
| 3784 | Minimum Deletion Cost to Make All Characters Equal | 58 | 60 | 3 | 2 | reference/ | `dsa/leetcode/3784_minimum-deletion-cost-to-make-all-characters-equal` |
| 3826 | Minimum Partition Score | 59 | 60 | 4 | 2 | reference/ | `dsa/leetcode/3826_minimum-partition-score` |
| 3827 | Count Monobit Integers | 34 | 60 | 3 | 2 | reference/ | `dsa/leetcode/3827_count-monobit-integers` |

## Source-fidelity backlog

Verified: 720; unverified: 3285; invalid: 0. A missing manifest means no live-source review has been claimed; it is not evidence that the existing prose is wrong. Structural values below are triage signals, not substitutes for live review.

### Overlap with completion work

| Bucket | Source-fidelity gaps |
|---|---:|
| Active verified-solution queue | 0 |
| Deferred documentation-only queue | 0 |
| Otherwise locally complete | 3285 |

### Unverified triage signals

| Signal | Packages |
|---|---:|
| No local Constraints heading | 3285 |
| No locally marked example explanation | 1664 |
| Has local images | 0 |
| Has non-metadata tables | 84 |
| Has local diagrams | 0 |

### Package inventory

| ID | Status | Reason | Constraints | Examples | Explained | Images | Tables | Diagrams | Package |
|---:|---|---|---|---:|---:|---:|---:|---:|---|
| 408 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0408_valid-word-abbreviation` |
| 409 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0409_longest-palindrome` |
| 410 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0410_split-array-largest-sum` |
| 411 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0411_minimum-unique-word-abbreviation` |
| 412 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0412_fizz-buzz` |
| 413 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0413_arithmetic-slices` |
| 414 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0414_third-maximum-number` |
| 415 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0415_add-strings` |
| 416 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0416_partition-equal-subset-sum` |
| 417 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0417_pacific-atlantic-water-flow` |
| 418 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0418_sentence-screen-fitting` |
| 419 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0419_battleships-in-a-board` |
| 420 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0420_strong-password-checker` |
| 421 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0421_maximum-xor-of-two-numbers-in-an-array` |
| 422 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0422_valid-word-square` |
| 423 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0423_reconstruct-original-digits-from-english` |
| 424 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0424_longest-repeating-character-replacement` |
| 425 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0425_word-squares` |
| 426 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0426_convert-binary-search-tree-to-sorted-doubly-linked-list` |
| 427 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0427_construct-quad-tree` |
| 428 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0428_serialize-and-deserialize-n-ary-tree` |
| 429 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0429_n-ary-tree-level-order-traversal` |
| 430 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0430_flatten-a-multilevel-doubly-linked-list` |
| 431 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0431_encode-n-ary-tree-to-binary-tree` |
| 432 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0432_all-oone-data-structure` |
| 433 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0433_minimum-genetic-mutation` |
| 434 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0434_number-of-segments-in-a-string` |
| 435 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0435_non-overlapping-intervals` |
| 436 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0436_find-right-interval` |
| 437 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0437_path-sum-iii` |
| 438 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0438_find-all-anagrams-in-a-string` |
| 439 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0439_ternary-expression-parser` |
| 440 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0440_k-th-smallest-in-lexicographical-order` |
| 441 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0441_arranging-coins` |
| 442 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0442_find-all-duplicates-in-an-array` |
| 443 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0443_string-compression` |
| 444 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0444_sequence-reconstruction` |
| 445 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0445_add-two-numbers-ii` |
| 446 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0446_arithmetic-slices-ii-subsequence` |
| 447 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0447_number-of-boomerangs` |
| 448 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0448_find-all-numbers-disappeared-in-an-array` |
| 449 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0449_serialize-and-deserialize-bst` |
| 450 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0450_delete-node-in-a-bst` |
| 451 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0451_sort-characters-by-frequency` |
| 452 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0452_minimum-number-of-arrows-to-burst-balloons` |
| 453 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0453_minimum-moves-to-equal-array-elements` |
| 454 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0454_4sum-ii` |
| 455 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0455_assign-cookies` |
| 456 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0456_132-pattern` |
| 457 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0457_circular-array-loop` |
| 458 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0458_poor-pigs` |
| 459 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0459_repeated-substring-pattern` |
| 460 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0460_lfu-cache` |
| 461 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0461_hamming-distance` |
| 462 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0462_minimum-moves-to-equal-array-elements-ii` |
| 463 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0463_island-perimeter` |
| 464 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0464_can-i-win` |
| 465 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0465_optimal-account-balancing` |
| 466 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0466_count-the-repetitions` |
| 467 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0467_unique-substrings-in-wraparound-string` |
| 468 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0468_validate-ip-address` |
| 469 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0469_convex-polygon` |
| 470 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0470_implement-rand10-using-rand7` |
| 471 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0471_encode-string-with-shortest-length` |
| 472 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0472_concatenated-words` |
| 473 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0473_matchsticks-to-square` |
| 474 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0474_ones-and-zeroes` |
| 475 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0475_heaters` |
| 476 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0476_number-complement` |
| 477 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0477_total-hamming-distance` |
| 478 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0478_generate-random-point-in-a-circle` |
| 479 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0479_largest-palindrome-product` |
| 480 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0480_sliding-window-median` |
| 481 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0481_magical-string` |
| 482 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0482_license-key-formatting` |
| 483 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0483_smallest-good-base` |
| 484 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0484_find-permutation` |
| 485 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0485_max-consecutive-ones` |
| 486 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0486_predict-the-winner` |
| 487 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0487_max-consecutive-ones-ii` |
| 488 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0488_zuma-game` |
| 489 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0489_robot-room-cleaner` |
| 490 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0490_the-maze` |
| 491 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0491_non-decreasing-subsequences` |
| 492 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0492_construct-the-rectangle` |
| 493 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0493_reverse-pairs` |
| 494 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0494_target-sum` |
| 495 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0495_teemo-attacking` |
| 496 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0496_next-greater-element-i` |
| 497 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0497_random-point-in-non-overlapping-rectangles` |
| 498 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0498_diagonal-traverse` |
| 499 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0499_the-maze-iii` |
| 500 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0500_keyboard-row` |
| 501 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0501_find-mode-in-binary-search-tree` |
| 502 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0502_ipo` |
| 503 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0503_next-greater-element-ii` |
| 504 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0504_base-7` |
| 505 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0505_the-maze-ii` |
| 506 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0506_relative-ranks` |
| 507 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0507_perfect-number` |
| 508 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0508_most-frequent-subtree-sum` |
| 509 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0509_fibonacci-number` |
| 510 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0510_inorder-successor-in-bst-ii` |
| 511 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0511_game-play-analysis-i` |
| 512 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0512_game-play-analysis-ii` |
| 513 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0513_find-bottom-left-tree-value` |
| 514 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0514_freedom-trail` |
| 515 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0515_find-largest-value-in-each-tree-row` |
| 516 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0516_longest-palindromic-subsequence` |
| 517 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0517_super-washing-machines` |
| 518 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0518_coin-change-ii` |
| 519 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0519_random-flip-matrix` |
| 520 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0520_detect-capital` |
| 521 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0521_longest-uncommon-subsequence-i` |
| 522 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0522_longest-uncommon-subsequence-ii` |
| 523 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0523_continuous-subarray-sum` |
| 524 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0524_longest-word-in-dictionary-through-deleting` |
| 525 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0525_contiguous-array` |
| 526 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0526_beautiful-arrangement` |
| 527 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0527_word-abbreviation` |
| 528 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0528_random-pick-with-weight` |
| 529 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0529_minesweeper` |
| 530 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0530_minimum-absolute-difference-in-bst` |
| 531 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0531_lonely-pixel-i` |
| 532 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0532_k-diff-pairs-in-an-array` |
| 533 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0533_lonely-pixel-ii` |
| 534 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0534_game-play-analysis-iii` |
| 535 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0535_encode-and-decode-tinyurl` |
| 536 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0536_construct-binary-tree-from-string` |
| 537 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0537_complex-number-multiplication` |
| 538 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0538_convert-bst-to-greater-tree` |
| 539 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0539_minimum-time-difference` |
| 540 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0540_single-element-in-a-sorted-array` |
| 541 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0541_reverse-string-ii` |
| 542 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0542_01-matrix` |
| 543 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0543_diameter-of-binary-tree` |
| 544 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0544_output-contest-matches` |
| 545 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0545_boundary-of-binary-tree` |
| 546 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0546_remove-boxes` |
| 547 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0547_number-of-provinces` |
| 548 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0548_split-array-with-equal-sum` |
| 549 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0549_binary-tree-longest-consecutive-sequence-ii` |
| 550 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0550_game-play-analysis-iv` |
| 551 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0551_student-attendance-record-i` |
| 552 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0552_student-attendance-record-ii` |
| 553 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0553_optimal-division` |
| 554 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0554_brick-wall` |
| 555 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0555_split-concatenated-strings` |
| 556 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0556_next-greater-element-iii` |
| 557 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0557_reverse-words-in-a-string-iii` |
| 558 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0558_logical-or-of-two-binary-grids-represented-as-quad-trees` |
| 559 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0559_maximum-depth-of-n-ary-tree` |
| 560 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0560_subarray-sum-equals-k` |
| 561 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0561_array-partition` |
| 562 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0562_longest-line-of-consecutive-one-in-matrix` |
| 563 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0563_binary-tree-tilt` |
| 564 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0564_find-the-closest-palindrome` |
| 565 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0565_array-nesting` |
| 566 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0566_reshape-the-matrix` |
| 567 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0567_permutation-in-string` |
| 568 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0568_maximum-vacation-days` |
| 569 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0569_median-employee-salary` |
| 570 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0570_managers-with-at-least-5-direct-reports` |
| 571 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0571_find-median-given-frequency-of-numbers` |
| 572 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0572_subtree-of-another-tree` |
| 573 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0573_squirrel-simulation` |
| 574 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0574_winning-candidate` |
| 575 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0575_distribute-candies` |
| 576 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0576_out-of-boundary-paths` |
| 577 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0577_employee-bonus` |
| 578 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0578_get-highest-answer-rate-question` |
| 579 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0579_find-cumulative-salary-of-an-employee` |
| 580 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0580_count-student-number-in-departments` |
| 581 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0581_shortest-unsorted-continuous-subarray` |
| 582 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0582_kill-process` |
| 583 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0583_delete-operation-for-two-strings` |
| 584 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0584_find-customer-referee` |
| 585 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0585_investments-in-2016` |
| 586 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0586_customer-placing-the-largest-number-of-orders` |
| 587 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0587_erect-the-fence` |
| 588 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0588_design-in-memory-file-system` |
| 589 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0589_n-ary-tree-preorder-traversal` |
| 590 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0590_n-ary-tree-postorder-traversal` |
| 591 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0591_tag-validator` |
| 592 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0592_fraction-addition-and-subtraction` |
| 593 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0593_valid-square` |
| 594 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0594_longest-harmonious-subsequence` |
| 595 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0595_big-countries` |
| 596 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0596_classes-with-at-least-5-students` |
| 597 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0597_friend-requests-i-overall-acceptance-rate` |
| 598 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0598_range-addition-ii` |
| 599 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0599_minimum-index-sum-of-two-lists` |
| 600 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0600_non-negative-integers-without-consecutive-ones` |
| 601 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0601_human-traffic-of-stadium` |
| 602 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0602_friend-requests-ii-who-has-the-most-friends` |
| 603 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0603_consecutive-available-seats` |
| 604 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0604_design-compressed-string-iterator` |
| 605 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0605_can-place-flowers` |
| 606 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0606_construct-string-from-binary-tree` |
| 607 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0607_sales-person` |
| 608 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0608_tree-node` |
| 609 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/0609_find-duplicate-file-in-system` |
| 610 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/0610_triangle-judgement` |
| 611 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0611_valid-triangle-number` |
| 612 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/0612_shortest-distance-in-a-plane` |
| 613 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/0613_shortest-distance-in-a-line` |
| 614 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/0614_second-degree-follower` |
| 615 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/0615_average-salary-departments-vs-company` |
| 616 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/0616_add-bold-tag-in-string` |
| 617 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/0617_merge-two-binary-trees` |
| 618 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/0618_students-report-by-geography` |
| 619 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/0619_biggest-single-number` |
| 620 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/0620_not-boring-movies` |
| 621 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0621_task-scheduler` |
| 622 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/0622_design-circular-queue` |
| 623 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/0623_add-one-row-to-tree` |
| 624 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/0624_maximum-distance-in-arrays` |
| 625 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0625_minimum-factorization` |
| 626 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/0626_exchange-seats` |
| 627 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/0627_swap-sex-of-employees` |
| 628 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0628_maximum-product-of-three-numbers` |
| 629 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0629_k-inverse-pairs-array` |
| 630 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0630_course-schedule-iii` |
| 631 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0631_design-excel-sum-formula` |
| 632 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0632_smallest-range-covering-elements-from-k-lists` |
| 633 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0633_sum-of-square-numbers` |
| 634 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0634_find-the-derangement-of-an-array` |
| 635 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0635_design-log-storage-system` |
| 636 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0636_exclusive-time-of-functions` |
| 637 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0637_average-of-levels-in-binary-tree` |
| 638 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0638_shopping-offers` |
| 639 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0639_decode-ways-ii` |
| 640 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0640_solve-the-equation` |
| 641 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0641_design-circular-deque` |
| 642 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0642_design-search-autocomplete-system` |
| 643 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0643_maximum-average-subarray-i` |
| 644 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0644_maximum-average-subarray-ii` |
| 645 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0645_set-mismatch` |
| 646 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0646_maximum-length-of-pair-chain` |
| 647 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0647_palindromic-substrings` |
| 648 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0648_replace-words` |
| 649 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0649_dota2-senate` |
| 650 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0650_2-keys-keyboard` |
| 651 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0651_4-keys-keyboard` |
| 652 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0652_find-duplicate-subtrees` |
| 653 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0653_two-sum-iv-input-is-a-bst` |
| 654 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0654_maximum-binary-tree` |
| 655 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0655_print-binary-tree` |
| 656 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0656_coin-path` |
| 657 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0657_robot-return-to-origin` |
| 658 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0658_find-k-closest-elements` |
| 659 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0659_split-array-into-consecutive-subsequences` |
| 660 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0660_remove-9` |
| 661 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0661_image-smoother` |
| 662 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0662_maximum-width-of-binary-tree` |
| 663 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0663_equal-tree-partition` |
| 664 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0664_strange-printer` |
| 665 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0665_non-decreasing-array` |
| 666 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0666_path-sum-iv` |
| 667 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0667_beautiful-arrangement-ii` |
| 668 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0668_kth-smallest-number-in-multiplication-table` |
| 669 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0669_trim-a-binary-search-tree` |
| 670 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0670_maximum-swap` |
| 671 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0671_second-minimum-node-in-a-binary-tree` |
| 672 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0672_bulb-switcher-ii` |
| 673 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0673_number-of-longest-increasing-subsequence` |
| 674 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0674_longest-continuous-increasing-subsequence` |
| 675 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0675_cut-off-trees-for-golf-event` |
| 676 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0676_implement-magic-dictionary` |
| 677 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0677_map-sum-pairs` |
| 678 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0678_valid-parenthesis-string` |
| 679 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0679_24-game` |
| 680 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0680_valid-palindrome-ii` |
| 681 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0681_next-closest-time` |
| 682 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0682_baseball-game` |
| 683 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0683_k-empty-slots` |
| 684 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0684_redundant-connection` |
| 685 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0685_redundant-connection-ii` |
| 686 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0686_repeated-string-match` |
| 687 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0687_longest-univalue-path` |
| 688 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0688_knight-probability-in-chessboard` |
| 689 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0689_maximum-sum-of-3-non-overlapping-subarrays` |
| 690 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0690_employee-importance` |
| 691 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0691_stickers-to-spell-word` |
| 692 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0692_top-k-frequent-words` |
| 693 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/0693_binary-number-with-alternating-bits` |
| 694 | unverified | source_fidelity.json is missing | no | 3 | 2 | 0 | 0 | 0 | `dsa/leetcode/0694_number-of-distinct-islands` |
| 695 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0695_max-area-of-island` |
| 696 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0696_count-binary-substrings` |
| 697 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0697_degree-of-an-array` |
| 698 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0698_partition-to-k-equal-sum-subsets` |
| 699 | unverified | source_fidelity.json is missing | no | 3 | 1 | 0 | 0 | 0 | `dsa/leetcode/0699_falling-squares` |
| 700 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0700_search-in-a-binary-search-tree` |
| 701 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0701_insert-into-a-binary-search-tree` |
| 702 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0702_search-in-a-sorted-array-of-unknown-size` |
| 703 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0703_kth-largest-element-in-a-stream` |
| 704 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0704_binary-search` |
| 705 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0705_design-hashset` |
| 706 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0706_design-hashmap` |
| 707 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0707_design-linked-list` |
| 708 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0708_insert-into-a-sorted-circular-linked-list` |
| 709 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0709_to-lower-case` |
| 710 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0710_random-pick-with-blacklist` |
| 711 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/0711_number-of-distinct-islands-ii` |
| 712 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0712_minimum-ascii-delete-sum-for-two-strings` |
| 713 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0713_subarray-product-less-than-k` |
| 714 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0714_best-time-to-buy-and-sell-stock-with-transaction-fee` |
| 715 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0715_range-module` |
| 716 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0716_max-stack` |
| 717 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0717_1-bit-and-2-bit-characters` |
| 718 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0718_maximum-length-of-repeated-subarray` |
| 719 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0719_find-k-th-smallest-pair-distance` |
| 720 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0720_longest-word-in-dictionary` |
| 721 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0721_accounts-merge` |
| 722 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0722_remove-comments` |
| 723 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0723_candy-crush` |
| 724 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0724_find-pivot-index` |
| 725 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0725_split-linked-list-in-parts` |
| 726 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0726_number-of-atoms` |
| 727 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0727_minimum-window-subsequence` |
| 728 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0728_self-dividing-numbers` |
| 729 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0729_my-calendar-i` |
| 730 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0730_count-different-palindromic-subsequences` |
| 731 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0731_my-calendar-ii` |
| 732 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0732_my-calendar-iii` |
| 733 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0733_flood-fill` |
| 734 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0734_sentence-similarity` |
| 735 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0735_asteroid-collision` |
| 736 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0736_parse-lisp-expression` |
| 737 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0737_sentence-similarity-ii` |
| 738 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0738_monotone-increasing-digits` |
| 739 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0739_daily-temperatures` |
| 740 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0740_delete-and-earn` |
| 741 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0741_cherry-pickup` |
| 742 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0742_closest-leaf-in-a-binary-tree` |
| 743 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0743_network-delay-time` |
| 744 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0744_find-smallest-letter-greater-than-target` |
| 745 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0745_prefix-and-suffix-search` |
| 746 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/0746_min-cost-climbing-stairs` |
| 747 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/0747_largest-number-at-least-twice-of-others` |
| 748 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/0748_shortest-completing-word` |
| 749 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/0749_contain-virus` |
| 750 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/0750_number-of-corner-rectangles` |
| 751 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/0751_ip-to-cidr` |
| 752 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/0752_open-the-lock` |
| 753 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/0753_cracking-the-safe` |
| 754 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/0754_reach-a-number` |
| 755 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/0755_pour-water` |
| 756 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/0756_pyramid-transition-matrix` |
| 757 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/0757_set-intersection-size-at-least-two` |
| 758 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/0758_bold-words-in-string` |
| 759 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/0759_employee-free-time` |
| 760 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/0760_find-anagram-mappings` |
| 761 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/0761_special-binary-string` |
| 762 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/0762_prime-number-of-set-bits-in-binary-representation` |
| 763 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/0763_partition-labels` |
| 764 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/0764_largest-plus-sign` |
| 765 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/0765_couples-holding-hands` |
| 766 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/0766_toeplitz-matrix` |
| 767 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/0767_reorganize-string` |
| 768 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/0768_max-chunks-to-make-sorted-ii` |
| 769 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/0769_max-chunks-to-make-sorted` |
| 770 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/0770_basic-calculator-iv` |
| 771 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/0771_jewels-and-stones` |
| 772 | unverified | source_fidelity.json is missing | no | 3 | 2 | 0 | 0 | 0 | `dsa/leetcode/0772_basic-calculator-iii` |
| 773 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/0773_sliding-puzzle` |
| 774 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/0774_minimize-max-distance-to-gas-station` |
| 775 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/0775_global-and-local-inversions` |
| 776 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/0776_split-bst` |
| 777 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/0777_swap-adjacent-in-lr-string` |
| 778 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/0778_swim-in-rising-water` |
| 779 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/0779_k-th-symbol-in-grammar` |
| 780 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/0780_reaching-points` |
| 781 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/0781_rabbits-in-forest` |
| 782 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/0782_transform-to-chessboard` |
| 783 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/0783_minimum-distance-between-bst-nodes` |
| 784 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/0784_letter-case-permutation` |
| 785 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/0785_is-graph-bipartite` |
| 786 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/0786_k-th-smallest-prime-fraction` |
| 787 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/0787_cheapest-flights-within-k-stops` |
| 788 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/0788_rotated-digits` |
| 789 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/0789_escape-the-ghosts` |
| 790 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/0790_domino-and-tromino-tiling` |
| 791 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/0791_custom-sort-string` |
| 792 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/0792_number-of-matching-subsequences` |
| 793 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/0793_preimage-size-of-factorial-zeroes-function` |
| 794 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/0794_valid-tic-tac-toe-state` |
| 795 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/0795_number-of-subarrays-with-bounded-maximum` |
| 796 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/0796_rotate-string` |
| 797 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/0797_all-paths-from-source-to-target` |
| 798 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/0798_smallest-rotation-with-highest-score` |
| 799 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/0799_champagne-tower` |
| 800 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/0800_similar-rgb-color` |
| 801 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/0801_minimum-swaps-to-make-sequences-increasing` |
| 802 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/0802_find-eventual-safe-states` |
| 803 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/0803_bricks-falling-when-hit` |
| 804 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/0804_unique-morse-code-words` |
| 805 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/0805_split-array-with-same-average` |
| 806 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/0806_number-of-lines-to-write-string` |
| 807 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/0807_max-increase-to-keep-city-skyline` |
| 808 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/0808_soup-servings` |
| 809 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/0809_expressive-words` |
| 810 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/0810_chalkboard-xor-game` |
| 811 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/0811_subdomain-visit-count` |
| 812 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/0812_largest-triangle-area` |
| 813 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/0813_largest-sum-of-averages` |
| 814 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/0814_binary-tree-pruning` |
| 815 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/0815_bus-routes` |
| 816 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/0816_ambiguous-coordinates` |
| 817 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/0817_linked-list-components` |
| 818 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/0818_race-car` |
| 819 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/0819_most-common-word` |
| 820 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/0820_short-encoding-of-words` |
| 821 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0821_shortest-distance-to-a-character` |
| 822 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/0822_card-flipping-game` |
| 823 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/0823_binary-trees-with-factors` |
| 824 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/0824_goat-latin` |
| 825 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/0825_friends-of-appropriate-ages` |
| 826 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/0826_most-profit-assigning-work` |
| 827 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/0827_making-a-large-island` |
| 828 | unverified | source_fidelity.json is missing | no | 3 | 2 | 0 | 0 | 0 | `dsa/leetcode/0828_count-unique-characters-of-all-substrings-of-a-given-string` |
| 829 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/0829_consecutive-numbers-sum` |
| 830 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/0830_positions-of-large-groups` |
| 831 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/0831_masking-personal-information` |
| 832 | unverified | source_fidelity.json is missing | no | 3 | 2 | 0 | 0 | 0 | `dsa/leetcode/0832_flipping-an-image` |
| 833 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0833_find-and-replace-in-string` |
| 834 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0834_sum-of-distances-in-tree` |
| 835 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0835_image-overlap` |
| 836 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0836_rectangle-overlap` |
| 837 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0837_new-21-game` |
| 838 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0838_push-dominoes` |
| 839 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0839_similar-string-groups` |
| 840 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0840_magic-squares-in-grid` |
| 841 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0841_keys-and-rooms` |
| 842 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0842_split-array-into-fibonacci-sequence` |
| 843 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/0843_guess-the-word` |
| 844 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0844_backspace-string-compare` |
| 845 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0845_longest-mountain-in-array` |
| 846 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0846_hand-of-straights` |
| 847 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0847_shortest-path-visiting-all-nodes` |
| 848 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0848_shifting-letters` |
| 849 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0849_maximize-distance-to-closest-person` |
| 850 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0850_rectangle-area-ii` |
| 851 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0851_loud-and-rich` |
| 852 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0852_peak-index-in-a-mountain-array` |
| 853 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0853_car-fleet` |
| 854 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0854_k-similar-strings` |
| 855 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0855_exam-room` |
| 856 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0856_score-of-parentheses` |
| 857 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0857_minimum-cost-to-hire-k-workers` |
| 858 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0858_mirror-reflection` |
| 859 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0859_buddy-strings` |
| 860 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0860_lemonade-change` |
| 861 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0861_score-after-flipping-matrix` |
| 862 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0862_shortest-subarray-with-sum-at-least-k` |
| 863 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0863_all-nodes-distance-k-in-binary-tree` |
| 864 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0864_shortest-path-to-get-all-keys` |
| 865 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0865_smallest-subtree-with-all-the-deepest-nodes` |
| 866 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0866_prime-palindrome` |
| 867 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0867_transpose-matrix` |
| 868 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0868_binary-gap` |
| 869 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0869_reordered-power-of-2` |
| 870 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0870_advantage-shuffle` |
| 871 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0871_minimum-number-of-refueling-stops` |
| 872 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0872_leaf-similar-trees` |
| 873 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0873_length-of-longest-fibonacci-subsequence` |
| 874 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0874_walking-robot-simulation` |
| 875 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0875_koko-eating-bananas` |
| 876 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0876_middle-of-the-linked-list` |
| 877 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0877_stone-game` |
| 878 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0878_nth-magical-number` |
| 879 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0879_profitable-schemes` |
| 880 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0880_decoded-string-at-index` |
| 881 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0881_boats-to-save-people` |
| 882 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0882_reachable-nodes-in-subdivided-graph` |
| 883 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0883_projection-area-of-3d-shapes` |
| 884 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0884_uncommon-words-from-two-sentences` |
| 885 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0885_spiral-matrix-iii` |
| 886 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0886_possible-bipartition` |
| 887 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0887_super-egg-drop` |
| 888 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0888_fair-candy-swap` |
| 889 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0889_construct-binary-tree-from-preorder-and-postorder-traversal` |
| 890 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0890_find-and-replace-pattern` |
| 891 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0891_sum-of-subsequence-widths` |
| 892 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0892_surface-area-of-3d-shapes` |
| 893 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0893_groups-of-special-equivalent-strings` |
| 894 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0894_all-possible-full-binary-trees` |
| 895 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0895_maximum-frequency-stack` |
| 896 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0896_monotonic-array` |
| 897 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0897_increasing-order-search-tree` |
| 898 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0898_bitwise-ors-of-subarrays` |
| 899 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0899_orderly-queue` |
| 900 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0900_rle-iterator` |
| 901 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0901_online-stock-span` |
| 902 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0902_numbers-at-most-n-given-digit-set` |
| 903 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0903_valid-permutations-for-di-sequence` |
| 904 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0904_fruit-into-baskets` |
| 905 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/0905_sort-array-by-parity` |
| 906 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/0906_super-palindromes` |
| 907 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/0907_sum-of-subarray-minimums` |
| 908 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0908_smallest-range-i` |
| 909 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/0909_snakes-and-ladders` |
| 910 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0910_smallest-range-ii` |
| 911 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0911_online-election` |
| 912 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/0912_sort-an-array` |
| 913 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/0913_cat-and-mouse` |
| 914 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/0914_x-of-a-kind-in-a-deck-of-cards` |
| 915 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/0915_partition-array-into-disjoint-intervals` |
| 916 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0916_word-subsets` |
| 917 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0917_reverse-only-letters` |
| 918 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/0918_maximum-sum-circular-subarray` |
| 919 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0919_complete-binary-tree-inserter` |
| 920 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/0920_number-of-music-playlists` |
| 921 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0921_minimum-add-to-make-parentheses-valid` |
| 922 | unverified | source_fidelity.json is missing | no | 3 | 1 | 0 | 0 | 0 | `dsa/leetcode/0922_sort-array-by-parity-ii` |
| 923 | unverified | source_fidelity.json is missing | no | 3 | 1 | 0 | 0 | 0 | `dsa/leetcode/0923_3sum-with-multiplicity` |
| 924 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0924_minimize-malware-spread` |
| 925 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/0925_long-pressed-name` |
| 926 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/0926_flip-string-to-monotone-increasing` |
| 927 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0927_three-equal-parts` |
| 928 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0928_minimize-malware-spread-ii` |
| 929 | unverified | source_fidelity.json is missing | no | 2 | 1 | 0 | 0 | 0 | `dsa/leetcode/0929_unique-email-addresses` |
| 930 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/0930_binary-subarrays-with-sum` |
| 931 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/0931_minimum-falling-path-sum` |
| 932 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/0932_beautiful-array` |
| 933 | unverified | source_fidelity.json is missing | no | 1 | 1 | 0 | 0 | 0 | `dsa/leetcode/0933_number-of-recent-calls` |
| 934 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0934_shortest-bridge` |
| 935 | unverified | source_fidelity.json is missing | no | 3 | 1 | 0 | 0 | 0 | `dsa/leetcode/0935_knight-dialer` |
| 936 | unverified | source_fidelity.json is missing | no | 2 | 1 | 0 | 0 | 0 | `dsa/leetcode/0936_stamping-the-sequence` |
| 937 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/0937_reorder-data-in-log-files` |
| 938 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/0938_range-sum-of-bst` |
| 939 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/0939_minimum-area-rectangle` |
| 940 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/0940_distinct-subsequences-ii` |
| 941 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0941_valid-mountain-array` |
| 942 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0942_di-string-match` |
| 943 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/0943_find-the-shortest-superstring` |
| 944 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0944_delete-columns-to-make-sorted` |
| 945 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/0945_minimum-increment-to-make-array-unique` |
| 946 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/0946_validate-stack-sequences` |
| 947 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0947_most-stones-removed-with-same-row-or-column` |
| 948 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0948_bag-of-tokens` |
| 949 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/0949_largest-time-for-given-digits` |
| 950 | unverified | source_fidelity.json is missing | no | 2 | 1 | 0 | 0 | 0 | `dsa/leetcode/0950_reveal-cards-in-increasing-order` |
| 951 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0951_flip-equivalent-binary-trees` |
| 952 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0952_largest-component-size-by-common-factor` |
| 953 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/0953_verifying-an-alien-dictionary` |
| 954 | unverified | source_fidelity.json is missing | no | 3 | 1 | 0 | 0 | 0 | `dsa/leetcode/0954_array-of-doubled-pairs` |
| 955 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/0955_delete-columns-to-make-sorted-ii` |
| 956 | unverified | source_fidelity.json is missing | no | 3 | 2 | 0 | 0 | 0 | `dsa/leetcode/0956_tallest-billboard` |
| 957 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/0957_prison-cells-after-n-days` |
| 958 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/0958_check-completeness-of-a-binary-tree` |
| 959 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0959_regions-cut-by-slashes` |
| 960 | unverified | source_fidelity.json is missing | no | 3 | 1 | 0 | 0 | 0 | `dsa/leetcode/0960_delete-columns-to-make-sorted-iii` |
| 961 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0961_n-repeated-element-in-size-2n-array` |
| 962 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/0962_maximum-width-ramp` |
| 963 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0963_minimum-area-rectangle-ii` |
| 964 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/0964_least-operators-to-express-number` |
| 965 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/0965_univalued-binary-tree` |
| 966 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/0966_vowel-spellchecker` |
| 967 | unverified | source_fidelity.json is missing | no | 2 | 1 | 0 | 0 | 0 | `dsa/leetcode/0967_numbers-with-same-consecutive-differences` |
| 968 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/0968_binary-tree-cameras` |
| 969 | unverified | source_fidelity.json is missing | no | 2 | 1 | 0 | 0 | 0 | `dsa/leetcode/0969_pancake-sorting` |
| 970 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/0970_powerful-integers` |
| 971 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0971_flip-binary-tree-to-match-preorder-traversal` |
| 972 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0972_equal-rational-numbers` |
| 973 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/0973_k-closest-points-to-origin` |
| 974 | unverified | source_fidelity.json is missing | no | 2 | 1 | 0 | 0 | 0 | `dsa/leetcode/0974_subarray-sums-divisible-by-k` |
| 975 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/0975_odd-even-jump` |
| 976 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/0976_largest-perimeter-triangle` |
| 977 | unverified | source_fidelity.json is missing | no | 2 | 1 | 0 | 0 | 0 | `dsa/leetcode/0977_squares-of-a-sorted-array` |
| 978 | unverified | source_fidelity.json is missing | no | 3 | 2 | 0 | 0 | 0 | `dsa/leetcode/0978_longest-turbulent-subarray` |
| 979 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/0979_distribute-coins-in-binary-tree` |
| 980 | unverified | source_fidelity.json is missing | no | 3 | 1 | 0 | 0 | 0 | `dsa/leetcode/0980_unique-paths-iii` |
| 981 | unverified | source_fidelity.json is missing | no | 2 | 1 | 0 | 0 | 0 | `dsa/leetcode/0981_time-based-key-value-store` |
| 982 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/0982_triples-with-bitwise-and-equal-to-zero` |
| 983 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/0983_minimum-cost-for-tickets` |
| 984 | unverified | source_fidelity.json is missing | no | 2 | 1 | 0 | 0 | 0 | `dsa/leetcode/0984_string-without-aaa-or-bbb` |
| 985 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/0985_sum-of-even-numbers-after-queries` |
| 986 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/0986_interval-list-intersections` |
| 987 | unverified | source_fidelity.json is missing | no | 3 | 2 | 0 | 0 | 0 | `dsa/leetcode/0987_vertical-order-traversal-of-a-binary-tree` |
| 988 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/0988_smallest-string-starting-from-leaf` |
| 989 | unverified | source_fidelity.json is missing | no | 3 | 1 | 0 | 0 | 0 | `dsa/leetcode/0989_add-to-array-form-of-integer` |
| 990 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/0990_satisfiability-of-equality-equations` |
| 991 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/0991_broken-calculator` |
| 992 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/0992_subarrays-with-k-different-integers` |
| 993 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/0993_cousins-in-binary-tree` |
| 994 | unverified | source_fidelity.json is missing | no | 3 | 2 | 0 | 0 | 0 | `dsa/leetcode/0994_rotting-oranges` |
| 995 | unverified | source_fidelity.json is missing | no | 3 | 2 | 0 | 0 | 0 | `dsa/leetcode/0995_minimum-number-of-k-consecutive-bit-flips` |
| 996 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/0996_number-of-squareful-arrays` |
| 997 | unverified | source_fidelity.json is missing | no | 3 | 1 | 0 | 0 | 0 | `dsa/leetcode/0997_find-the-town-judge` |
| 998 | unverified | source_fidelity.json is missing | no | 3 | 1 | 0 | 0 | 0 | `dsa/leetcode/0998_maximum-binary-tree-ii` |
| 999 | unverified | source_fidelity.json is missing | no | 3 | 2 | 0 | 0 | 0 | `dsa/leetcode/0999_available-captures-for-rook` |
| 1000 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1000_minimum-cost-to-merge-stones` |
| 1001 | unverified | source_fidelity.json is missing | no | 3 | 1 | 0 | 0 | 0 | `dsa/leetcode/1001_grid-illumination` |
| 1002 | unverified | source_fidelity.json is missing | no | 3 | 1 | 0 | 0 | 0 | `dsa/leetcode/1002_find-common-characters` |
| 1003 | unverified | source_fidelity.json is missing | no | 3 | 1 | 0 | 0 | 0 | `dsa/leetcode/1003_check-if-word-is-valid-after-substitutions` |
| 1004 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1004_max-consecutive-ones-iii` |
| 1005 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1005_maximize-sum-of-array-after-k-negations` |
| 1006 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1006_clumsy-factorial` |
| 1007 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1007_minimum-domino-rotations-for-equal-row` |
| 1008 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1008_construct-binary-search-tree-from-preorder-traversal` |
| 1009 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1009_complement-of-base-10-integer` |
| 1010 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1010_pairs-of-songs-with-total-durations-divisible-by-60` |
| 1011 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1011_capacity-to-ship-packages-within-d-days` |
| 1012 | unverified | source_fidelity.json is missing | no | 3 | 2 | 0 | 0 | 0 | `dsa/leetcode/1012_numbers-with-repeated-digits` |
| 1013 | unverified | source_fidelity.json is missing | no | 3 | 2 | 0 | 0 | 0 | `dsa/leetcode/1013_partition-array-into-three-parts-with-equal-sum` |
| 1014 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1014_best-sightseeing-pair` |
| 1015 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1015_smallest-integer-divisible-by-k` |
| 1016 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1016_binary-string-with-substrings-representing-1-to-n` |
| 1017 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1017_convert-to-base-2` |
| 1018 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1018_binary-prefix-divisible-by-5` |
| 1019 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1019_next-greater-node-in-linked-list` |
| 1020 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1020_number-of-enclaves` |
| 1021 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1021_remove-outermost-parentheses` |
| 1022 | unverified | source_fidelity.json is missing | no | 3 | 2 | 0 | 0 | 0 | `dsa/leetcode/1022_sum-of-root-to-leaf-binary-numbers` |
| 1023 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1023_camelcase-matching` |
| 1024 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1024_video-stitching` |
| 1025 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/1025_divisor-game` |
| 1026 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/1026_maximum-difference-between-node-and-ancestor` |
| 1027 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1027_longest-arithmetic-subsequence` |
| 1028 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1028_recover-a-tree-from-preorder-traversal` |
| 1029 | unverified | source_fidelity.json is missing | no | 3 | 1 | 0 | 0 | 0 | `dsa/leetcode/1029_two-city-scheduling` |
| 1030 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1030_matrix-cells-in-distance-order` |
| 1031 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1031_maximum-sum-of-two-non-overlapping-subarrays` |
| 1032 | unverified | source_fidelity.json is missing | no | 1 | 1 | 0 | 0 | 0 | `dsa/leetcode/1032_stream-of-characters` |
| 1033 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1033_moving-stones-until-consecutive` |
| 1034 | unverified | source_fidelity.json is missing | no | 3 | 1 | 0 | 0 | 0 | `dsa/leetcode/1034_coloring-a-border` |
| 1035 | unverified | source_fidelity.json is missing | no | 3 | 1 | 0 | 0 | 0 | `dsa/leetcode/1035_uncrossed-lines` |
| 1036 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/1036_escape-a-large-maze` |
| 1037 | unverified | source_fidelity.json is missing | no | 2 | 1 | 0 | 0 | 0 | `dsa/leetcode/1037_valid-boomerang` |
| 1038 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/1038_binary-search-tree-to-greater-sum-tree` |
| 1039 | unverified | source_fidelity.json is missing | no | 3 | 2 | 0 | 0 | 0 | `dsa/leetcode/1039_minimum-score-triangulation-of-polygon` |
| 1040 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/1040_moving-stones-until-consecutive-ii` |
| 1041 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1041_robot-bounded-in-circle` |
| 1042 | unverified | source_fidelity.json is missing | no | 3 | 1 | 0 | 0 | 0 | `dsa/leetcode/1042_flower-planting-with-no-adjacent` |
| 1043 | unverified | source_fidelity.json is missing | no | 3 | 1 | 0 | 0 | 0 | `dsa/leetcode/1043_partition-array-for-maximum-sum` |
| 1044 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/1044_longest-duplicate-substring` |
| 1045 | unverified | source_fidelity.json is missing | no | 1 | 0 | 0 | 3 | 0 | `dsa/leetcode/1045_customers-who-bought-all-products` |
| 1046 | unverified | source_fidelity.json is missing | no | 2 | 1 | 0 | 0 | 0 | `dsa/leetcode/1046_last-stone-weight` |
| 1047 | unverified | source_fidelity.json is missing | no | 2 | 1 | 0 | 0 | 0 | `dsa/leetcode/1047_remove-all-adjacent-duplicates-in-string` |
| 1048 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1048_longest-string-chain` |
| 1049 | unverified | source_fidelity.json is missing | no | 2 | 1 | 0 | 0 | 0 | `dsa/leetcode/1049_last-stone-weight-ii` |
| 1050 | unverified | source_fidelity.json is missing | no | 1 | 0 | 0 | 2 | 0 | `dsa/leetcode/1050_actors-and-directors-who-cooperated-at-least-three-times` |
| 1051 | unverified | source_fidelity.json is missing | no | 3 | 2 | 0 | 0 | 0 | `dsa/leetcode/1051_height-checker` |
| 1052 | unverified | source_fidelity.json is missing | no | 2 | 1 | 0 | 0 | 0 | `dsa/leetcode/1052_grumpy-bookstore-owner` |
| 1053 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1053_previous-permutation-with-one-swap` |
| 1054 | unverified | source_fidelity.json is missing | no | 2 | 1 | 0 | 0 | 0 | `dsa/leetcode/1054_distant-barcodes` |
| 1055 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1055_shortest-way-to-form-string` |
| 1056 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1056_confusing-number` |
| 1057 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/1057_campus-bikes` |
| 1058 | unverified | source_fidelity.json is missing | no | 3 | 2 | 0 | 0 | 0 | `dsa/leetcode/1058_minimize-rounding-error-to-meet-target` |
| 1059 | unverified | source_fidelity.json is missing | no | 3 | 2 | 0 | 0 | 0 | `dsa/leetcode/1059_all-paths-from-source-lead-to-destination` |
| 1060 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1060_missing-element-in-sorted-array` |
| 1061 | unverified | source_fidelity.json is missing | no | 3 | 1 | 0 | 0 | 0 | `dsa/leetcode/1061_lexicographically-smallest-equivalent-string` |
| 1062 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1062_longest-repeating-substring` |
| 1063 | unverified | source_fidelity.json is missing | no | 3 | 2 | 0 | 0 | 0 | `dsa/leetcode/1063_number-of-valid-subarrays` |
| 1064 | unverified | source_fidelity.json is missing | no | 3 | 1 | 0 | 0 | 0 | `dsa/leetcode/1064_fixed-point` |
| 1065 | unverified | source_fidelity.json is missing | no | 3 | 1 | 0 | 0 | 0 | `dsa/leetcode/1065_index-pairs-of-a-string` |
| 1066 | unverified | source_fidelity.json is missing | no | 3 | 1 | 0 | 0 | 0 | `dsa/leetcode/1066_campus-bikes-ii` |
| 1067 | unverified | source_fidelity.json is missing | no | 3 | 2 | 0 | 0 | 0 | `dsa/leetcode/1067_digit-count-in-range` |
| 1068 | unverified | source_fidelity.json is missing | no | 1 | 0 | 0 | 3 | 0 | `dsa/leetcode/1068_product-sales-analysis-i` |
| 1069 | unverified | source_fidelity.json is missing | no | 1 | 0 | 0 | 2 | 0 | `dsa/leetcode/1069_product-sales-analysis-ii` |
| 1070 | unverified | source_fidelity.json is missing | no | 1 | 0 | 0 | 2 | 0 | `dsa/leetcode/1070_product-sales-analysis-iii` |
| 1071 | unverified | source_fidelity.json is missing | no | 4 | 0 | 0 | 0 | 0 | `dsa/leetcode/1071_greatest-common-divisor-of-strings` |
| 1072 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1072_flip-columns-for-maximum-number-of-equal-rows` |
| 1073 | unverified | source_fidelity.json is missing | no | 3 | 1 | 0 | 0 | 0 | `dsa/leetcode/1073_adding-two-negabinary-numbers` |
| 1074 | unverified | source_fidelity.json is missing | no | 3 | 2 | 0 | 0 | 0 | `dsa/leetcode/1074_number-of-submatrices-that-sum-to-target` |
| 1075 | unverified | source_fidelity.json is missing | no | 1 | 0 | 0 | 3 | 0 | `dsa/leetcode/1075_project-employees-i` |
| 1076 | unverified | source_fidelity.json is missing | no | 1 | 0 | 0 | 2 | 0 | `dsa/leetcode/1076_project-employees-ii` |
| 1077 | unverified | source_fidelity.json is missing | no | 1 | 0 | 0 | 3 | 0 | `dsa/leetcode/1077_project-employees-iii` |
| 1078 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/1078_occurrences-after-bigram` |
| 1079 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1079_letter-tile-possibilities` |
| 1080 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1080_insufficient-nodes-in-root-to-leaf-paths` |
| 1081 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/1081_smallest-subsequence-of-distinct-characters` |
| 1082 | unverified | source_fidelity.json is missing | no | 1 | 0 | 0 | 2 | 0 | `dsa/leetcode/1082_sales-analysis-i` |
| 1083 | unverified | source_fidelity.json is missing | no | 1 | 0 | 0 | 3 | 0 | `dsa/leetcode/1083_sales-analysis-ii` |
| 1084 | unverified | source_fidelity.json is missing | no | 1 | 0 | 0 | 3 | 0 | `dsa/leetcode/1084_sales-analysis-iii` |
| 1085 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/1085_sum-of-digits-in-the-minimum-number` |
| 1086 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/1086_high-five` |
| 1087 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/1087_brace-expansion` |
| 1088 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/1088_confusing-number-ii` |
| 1089 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/1089_duplicate-zeros` |
| 1090 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1090_largest-values-from-labels` |
| 1091 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1091_shortest-path-in-binary-matrix` |
| 1092 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/1092_shortest-common-supersequence` |
| 1093 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/1093_statistics-from-a-large-sample` |
| 1094 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/1094_car-pooling` |
| 1095 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/1095_find-in-mountain-array` |
| 1096 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/1096_brace-expansion-ii` |
| 1097 | unverified | source_fidelity.json is missing | no | 1 | 0 | 0 | 2 | 0 | `dsa/leetcode/1097_game-play-analysis-v` |
| 1098 | unverified | source_fidelity.json is missing | no | 1 | 0 | 0 | 3 | 0 | `dsa/leetcode/1098_unpopular-books` |
| 1099 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/1099_two-sum-less-than-k` |
| 1100 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/1100_find-k-length-substrings-with-no-repeated-characters` |
| 1101 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/1101_the-earliest-moment-when-everyone-become-friends` |
| 1102 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1102_path-with-maximum-minimum-value` |
| 1103 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/1103_distribute-candies-to-people` |
| 1104 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/1104_path-in-zigzag-labelled-binary-tree` |
| 1105 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/1105_filling-bookcase-shelves` |
| 1106 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1106_parsing-a-boolean-expression` |
| 1107 | unverified | source_fidelity.json is missing | no | 1 | 0 | 0 | 2 | 0 | `dsa/leetcode/1107_new-users-daily-count` |
| 1108 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/1108_defanging-an-ip-address` |
| 1109 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/1109_corporate-flight-bookings` |
| 1110 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/1110_delete-nodes-and-return-forest` |
| 1111 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/1111_maximum-nesting-depth-of-two-valid-parentheses-strings` |
| 1112 | unverified | source_fidelity.json is missing | no | 1 | 0 | 0 | 2 | 0 | `dsa/leetcode/1112_highest-grade-for-each-student` |
| 1113 | unverified | source_fidelity.json is missing | no | 1 | 0 | 0 | 2 | 0 | `dsa/leetcode/1113_reported-posts` |
| 1114 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/1114_print-in-order` |
| 1115 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/1115_print-foobar-alternately` |
| 1116 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/1116_print-zero-even-odd` |
| 1117 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/1117_building-h2o` |
| 1118 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1118_number-of-days-in-a-month` |
| 1119 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1119_remove-vowels-from-a-string` |
| 1120 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/1120_maximum-average-subtree` |
| 1121 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/1121_divide-array-into-increasing-sequences` |
| 1122 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/1122_relative-sort-array` |
| 1123 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1123_lowest-common-ancestor-of-deepest-leaves` |
| 1124 | unverified | source_fidelity.json is missing | no | 2 | 1 | 0 | 0 | 0 | `dsa/leetcode/1124_longest-well-performing-interval` |
| 1125 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/1125_smallest-sufficient-team` |
| 1126 | unverified | source_fidelity.json is missing | no | 1 | 0 | 0 | 2 | 0 | `dsa/leetcode/1126_active-businesses` |
| 1127 | unverified | source_fidelity.json is missing | no | 1 | 0 | 0 | 2 | 0 | `dsa/leetcode/1127_user-purchase-platform` |
| 1128 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/1128_number-of-equivalent-domino-pairs` |
| 1129 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/1129_shortest-path-with-alternating-colors` |
| 1130 | unverified | source_fidelity.json is missing | no | 2 | 1 | 0 | 0 | 0 | `dsa/leetcode/1130_minimum-cost-tree-from-leaf-values` |
| 1131 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/1131_maximum-of-absolute-value-expression` |
| 1132 | unverified | source_fidelity.json is missing | no | 1 | 0 | 0 | 1 | 0 | `dsa/leetcode/1132_reported-posts-ii` |
| 1133 | unverified | source_fidelity.json is missing | no | 2 | 1 | 0 | 0 | 0 | `dsa/leetcode/1133_largest-unique-number` |
| 1134 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/1134_armstrong-number` |
| 1135 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/1135_connecting-cities-with-minimum-cost` |
| 1136 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/1136_parallel-courses` |
| 1137 | unverified | source_fidelity.json is missing | no | 2 | 1 | 0 | 0 | 0 | `dsa/leetcode/1137_n-th-tribonacci-number` |
| 1138 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/1138_alphabet-board-path` |
| 1139 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/1139_largest-1-bordered-square` |
| 1140 | unverified | source_fidelity.json is missing | no | 2 | 1 | 0 | 0 | 0 | `dsa/leetcode/1140_stone-game-ii` |
| 1141 | unverified | source_fidelity.json is missing | no | 1 | 0 | 0 | 1 | 0 | `dsa/leetcode/1141_user-activity-for-the-past-30-days-i` |
| 1142 | unverified | source_fidelity.json is missing | no | 1 | 0 | 0 | 1 | 0 | `dsa/leetcode/1142_user-activity-for-the-past-30-days-ii` |
| 1143 | unverified | source_fidelity.json is missing | no | 3 | 1 | 0 | 0 | 0 | `dsa/leetcode/1143_longest-common-subsequence` |
| 1144 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/1144_decrease-elements-to-make-array-zigzag` |
| 1145 | unverified | source_fidelity.json is missing | no | 2 | 1 | 0 | 0 | 0 | `dsa/leetcode/1145_binary-tree-coloring-game` |
| 1146 | unverified | source_fidelity.json is missing | no | 1 | 1 | 0 | 0 | 0 | `dsa/leetcode/1146_snapshot-array` |
| 1147 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1147_longest-chunked-palindrome-decomposition` |
| 1148 | unverified | source_fidelity.json is missing | no | 1 | 0 | 0 | 2 | 0 | `dsa/leetcode/1148_article-views-i` |
| 1149 | unverified | source_fidelity.json is missing | no | 1 | 0 | 0 | 2 | 0 | `dsa/leetcode/1149_article-views-ii` |
| 1150 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/1150_check-if-a-number-is-majority-element-in-a-sorted-array` |
| 1151 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1151_minimum-swaps-to-group-all-1s-together` |
| 1152 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1152_analyze-user-website-visit-pattern` |
| 1153 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1153_string-transforms-into-another-string` |
| 1154 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1154_day-of-the-year` |
| 1155 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1155_number-of-dice-rolls-with-target-sum` |
| 1156 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1156_swap-for-longest-repeated-character-substring` |
| 1157 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1157_online-majority-element-in-subarray` |
| 1158 | unverified | source_fidelity.json is missing | no | 1 | 0 | 0 | 3 | 0 | `dsa/leetcode/1158_market-analysis-i` |
| 1159 | unverified | source_fidelity.json is missing | no | 1 | 0 | 0 | 4 | 0 | `dsa/leetcode/1159_market-analysis-ii` |
| 1160 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1160_find-words-that-can-be-formed-by-characters` |
| 1161 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1161_maximum-level-sum-of-a-binary-tree` |
| 1162 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1162_as-far-from-land-as-possible` |
| 1163 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1163_last-substring-in-lexicographical-order` |
| 1164 | unverified | source_fidelity.json is missing | no | 1 | 0 | 0 | 2 | 0 | `dsa/leetcode/1164_product-price-at-a-given-date` |
| 1165 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/1165_single-row-keyboard` |
| 1166 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/1166_design-file-system` |
| 1167 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1167_minimum-cost-to-connect-sticks` |
| 1168 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/1168_optimize-water-distribution-in-a-village` |
| 1169 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1169_invalid-transactions` |
| 1170 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1170_compare-strings-by-frequency-of-the-smallest-character` |
| 1171 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1171_remove-zero-sum-consecutive-nodes-from-linked-list` |
| 1172 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1172_dinner-plate-stacks` |
| 1173 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 2 | 0 | `dsa/leetcode/1173_immediate-food-delivery-i` |
| 1174 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 2 | 0 | `dsa/leetcode/1174_immediate-food-delivery-ii` |
| 1175 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1175_prime-arrangements` |
| 1176 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1176_diet-plan-performance` |
| 1177 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1177_can-make-palindrome-from-substring` |
| 1178 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1178_number-of-valid-words-for-each-puzzle` |
| 1179 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 2 | 0 | `dsa/leetcode/1179_reformat-department-table` |
| 1180 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1180_count-substrings-with-only-one-distinct-letter` |
| 1181 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1181_before-and-after-puzzle` |
| 1182 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/1182_shortest-distance-to-target-color` |
| 1183 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/1183_maximum-number-of-ones` |
| 1184 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1184_distance-between-bus-stops` |
| 1185 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1185_day-of-the-week` |
| 1186 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1186_maximum-subarray-sum-with-one-deletion` |
| 1187 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1187_make-array-strictly-increasing` |
| 1188 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/1188_design-bounded-blocking-queue` |
| 1189 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1189_maximum-number-of-balloons` |
| 1190 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1190_reverse-substrings-between-each-pair-of-parentheses` |
| 1191 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1191_k-concatenation-maximum-sum` |
| 1192 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/1192_critical-connections-in-a-network` |
| 1193 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 2 | 0 | `dsa/leetcode/1193_monthly-transactions-i` |
| 1194 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 3 | 0 | `dsa/leetcode/1194_tournament-winners` |
| 1195 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1195_fizz-buzz-multithreaded` |
| 1196 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1196_how-many-apples-can-you-put-into-the-basket` |
| 1197 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1197_minimum-knight-moves` |
| 1198 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1198_find-smallest-common-element-in-all-rows` |
| 1199 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1199_minimum-time-to-build-blocks` |
| 1200 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1200_minimum-absolute-difference` |
| 1201 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1201_ugly-number-iii` |
| 1202 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1202_smallest-string-with-swaps` |
| 1203 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/1203_sort-items-by-groups-respecting-dependencies` |
| 1204 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 2 | 0 | `dsa/leetcode/1204_last-person-to-fit-in-the-bus` |
| 1205 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 3 | 0 | `dsa/leetcode/1205_monthly-transactions-ii` |
| 1206 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1206_design-skiplist` |
| 1207 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1207_unique-number-of-occurrences` |
| 1208 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1208_get-equal-substrings-within-budget` |
| 1209 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1209_remove-all-adjacent-duplicates-in-string-ii` |
| 1210 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1210_minimum-moves-to-reach-target-with-rotations` |
| 1211 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 2 | 0 | `dsa/leetcode/1211_queries-quality-and-percentage` |
| 1212 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 3 | 0 | `dsa/leetcode/1212_team-scores-in-football-tournament` |
| 1213 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1213_intersection-of-three-sorted-arrays` |
| 1214 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1214_two-sum-bsts` |
| 1215 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/1215_stepping-numbers` |
| 1216 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1216_valid-palindrome-iii` |
| 1217 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1217_minimum-cost-to-move-chips-to-the-same-position` |
| 1218 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1218_longest-arithmetic-subsequence-of-given-difference` |
| 1219 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1219_path-with-maximum-gold` |
| 1220 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1220_count-vowels-permutation` |
| 1221 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1221_split-a-string-in-balanced-strings` |
| 1222 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1222_queens-that-can-attack-the-king` |
| 1223 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1223_dice-roll-simulation` |
| 1224 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1224_maximum-equal-frequency` |
| 1225 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 3 | 0 | `dsa/leetcode/1225_report-contiguous-dates` |
| 1226 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1226_the-dining-philosophers` |
| 1227 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1227_airplane-seat-assignment-probability` |
| 1228 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1228_missing-number-in-arithmetic-progression` |
| 1229 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1229_meeting-scheduler` |
| 1230 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1230_toss-strange-coins` |
| 1231 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1231_divide-chocolate` |
| 1232 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1232_check-if-it-is-a-straight-line` |
| 1233 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1233_remove-sub-folders-from-the-filesystem` |
| 1234 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1234_replace-the-substring-for-balanced-string` |
| 1235 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1235_maximum-profit-in-job-scheduling` |
| 1236 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1236_web-crawler` |
| 1237 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1237_find-positive-integer-solution-for-a-given-equation` |
| 1238 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1238_circular-permutation-in-binary-representation` |
| 1239 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1239_maximum-length-of-a-concatenated-string-with-unique-characters` |
| 1240 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1240_tiling-a-rectangle-with-the-fewest-squares` |
| 1241 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 2 | 0 | `dsa/leetcode/1241_number-of-comments-per-post` |
| 1242 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1242_web-crawler-multithreaded` |
| 1243 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1243_array-transformation` |
| 1244 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1244_design-a-leaderboard` |
| 1245 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1245_tree-diameter` |
| 1246 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1246_palindrome-removal` |
| 1247 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1247_minimum-swaps-to-make-strings-equal` |
| 1248 | unverified | source_fidelity.json is missing | no | 3 | 2 | 0 | 0 | 0 | `dsa/leetcode/1248_count-number-of-nice-subarrays` |
| 1249 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1249_minimum-remove-to-make-valid-parentheses` |
| 1250 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1250_check-if-it-is-a-good-array` |
| 1251 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 3 | 0 | `dsa/leetcode/1251_average-selling-price` |
| 1252 | unverified | source_fidelity.json is missing | no | 3 | 1 | 0 | 0 | 0 | `dsa/leetcode/1252_cells-with-odd-values-in-a-matrix` |
| 1253 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1253_reconstruct-a-2-row-binary-matrix` |
| 1254 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1254_number-of-closed-islands` |
| 1255 | unverified | source_fidelity.json is missing | no | 3 | 1 | 0 | 0 | 0 | `dsa/leetcode/1255_maximum-score-words-formed-by-letters` |
| 1256 | unverified | source_fidelity.json is missing | no | 3 | 1 | 0 | 0 | 0 | `dsa/leetcode/1256_encode-number` |
| 1257 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1257_smallest-common-region` |
| 1258 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1258_synonymous-sentences` |
| 1259 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1259_handshakes-that-dont-cross` |
| 1260 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1260_shift-2d-grid` |
| 1261 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1261_find-elements-in-a-contaminated-binary-tree` |
| 1262 | unverified | source_fidelity.json is missing | no | 3 | 1 | 0 | 0 | 0 | `dsa/leetcode/1262_greatest-sum-divisible-by-three` |
| 1263 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1263_minimum-moves-to-move-a-box-to-their-target-location` |
| 1264 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1264_page-recommendations` |
| 1265 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1265_print-immutable-linked-list-in-reverse` |
| 1266 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1266_minimum-time-visiting-all-points` |
| 1267 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1267_count-servers-that-communicate` |
| 1268 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1268_search-suggestions-system` |
| 1269 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1269_number-of-ways-to-stay-in-the-same-place-after-some-steps` |
| 1270 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1270_all-people-report-to-the-given-manager` |
| 1271 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1271_hexspeak` |
| 1272 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1272_remove-interval` |
| 1273 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1273_delete-tree-nodes` |
| 1274 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1274_number-of-ships-in-a-rectangle` |
| 1275 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1275_find-winner-on-a-tic-tac-toe-game` |
| 1276 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1276_number-of-burgers-with-no-waste-of-ingredients` |
| 1277 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1277_count-square-submatrices-with-all-ones` |
| 1278 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1278_palindrome-partitioning-iii` |
| 1279 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1279_traffic-light-controlled-intersection` |
| 1280 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1280_students-and-examinations` |
| 1281 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1281_subtract-the-product-and-sum-of-digits-of-an-integer` |
| 1282 | unverified | source_fidelity.json is missing | no | 3 | 2 | 0 | 0 | 0 | `dsa/leetcode/1282_group-the-people-given-the-group-size-they-belong-to` |
| 1283 | unverified | source_fidelity.json is missing | no | 3 | 2 | 0 | 0 | 0 | `dsa/leetcode/1283_find-the-smallest-divisor-given-a-threshold` |
| 1284 | unverified | source_fidelity.json is missing | no | 3 | 2 | 0 | 0 | 0 | `dsa/leetcode/1284_minimum-number-of-flips-to-convert-binary-matrix-to-zero-matrix` |
| 1285 | unverified | source_fidelity.json is missing | no | 3 | 1 | 0 | 0 | 0 | `dsa/leetcode/1285_find-the-start-and-end-number-of-continuous-ranges` |
| 1286 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1286_iterator-for-combination` |
| 1287 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1287_element-appearing-more-than-25-in-sorted-array` |
| 1288 | unverified | source_fidelity.json is missing | no | 3 | 2 | 0 | 0 | 0 | `dsa/leetcode/1288_remove-covered-intervals` |
| 1289 | unverified | source_fidelity.json is missing | no | 3 | 2 | 0 | 0 | 0 | `dsa/leetcode/1289_minimum-falling-path-sum-ii` |
| 1290 | unverified | source_fidelity.json is missing | no | 3 | 1 | 0 | 0 | 0 | `dsa/leetcode/1290_convert-binary-number-in-a-linked-list-to-integer` |
| 1291 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1291_sequential-digits` |
| 1292 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1292_maximum-side-length-of-a-square-with-sum-less-than-or-equal-to-threshold` |
| 1293 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1293_shortest-path-in-a-grid-with-obstacles-elimination` |
| 1294 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1294_weather-type-in-each-country` |
| 1295 | unverified | source_fidelity.json is missing | no | 3 | 1 | 0 | 0 | 0 | `dsa/leetcode/1295_find-numbers-with-even-number-of-digits` |
| 1296 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1296_divide-array-in-sets-of-k-consecutive-numbers` |
| 1297 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1297_maximum-number-of-occurrences-of-a-substring` |
| 1298 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1298_maximum-candies-you-can-get-from-boxes` |
| 1299 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1299_replace-elements-with-greatest-element-on-right-side` |
| 1300 | unverified | source_fidelity.json is missing | no | 3 | 2 | 0 | 0 | 0 | `dsa/leetcode/1300_sum-of-mutated-array-closest-to-target` |
| 1301 | unverified | source_fidelity.json is missing | no | 3 | 1 | 0 | 0 | 0 | `dsa/leetcode/1301_number-of-paths-with-max-score` |
| 1302 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1302_deepest-leaves-sum` |
| 1303 | unverified | source_fidelity.json is missing | no | 3 | 1 | 0 | 1 | 0 | `dsa/leetcode/1303_find-the-team-size` |
| 1304 | unverified | source_fidelity.json is missing | no | 3 | 1 | 0 | 0 | 0 | `dsa/leetcode/1304_find-n-unique-integers-sum-up-to-zero` |
| 1305 | unverified | source_fidelity.json is missing | no | 3 | 1 | 0 | 0 | 0 | `dsa/leetcode/1305_all-elements-in-two-binary-search-trees` |
| 1306 | unverified | source_fidelity.json is missing | no | 3 | 2 | 0 | 0 | 0 | `dsa/leetcode/1306_jump-game-iii` |
| 1307 | unverified | source_fidelity.json is missing | no | 3 | 1 | 0 | 0 | 0 | `dsa/leetcode/1307_verbal-arithmetic-puzzle` |
| 1308 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1308_running-total-for-different-genders` |
| 1309 | unverified | source_fidelity.json is missing | no | 3 | 1 | 0 | 0 | 0 | `dsa/leetcode/1309_decrypt-string-from-alphabet-to-integer-mapping` |
| 1310 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1310_xor-queries-of-a-subarray` |
| 1311 | unverified | source_fidelity.json is missing | no | 3 | 2 | 0 | 0 | 0 | `dsa/leetcode/1311_get-watched-videos-by-your-friends` |
| 1312 | unverified | source_fidelity.json is missing | no | 3 | 2 | 0 | 0 | 0 | `dsa/leetcode/1312_minimum-insertion-steps-to-make-a-string-palindrome` |
| 1313 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1313_decompress-run-length-encoded-list` |
| 1314 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1314_matrix-block-sum` |
| 1315 | unverified | source_fidelity.json is missing | no | 3 | 1 | 0 | 0 | 0 | `dsa/leetcode/1315_sum-of-nodes-with-even-valued-grandparent` |
| 1316 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1316_distinct-echo-substrings` |
| 1317 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1317_convert-integer-to-the-sum-of-two-no-zero-integers` |
| 1318 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1318_minimum-flips-to-make-a-or-b-equal-to-c` |
| 1319 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1319_number-of-operations-to-make-network-connected` |
| 1320 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1320_minimum-distance-to-type-a-word-using-two-fingers` |
| 1321 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1321_restaurant-growth` |
| 1322 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1322_ads-performance` |
| 1323 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1323_maximum-69-number` |
| 1324 | unverified | source_fidelity.json is missing | no | 3 | 1 | 0 | 0 | 0 | `dsa/leetcode/1324_print-words-vertically` |
| 1325 | unverified | source_fidelity.json is missing | no | 3 | 2 | 0 | 0 | 0 | `dsa/leetcode/1325_delete-leaves-with-a-given-value` |
| 1326 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1326_minimum-number-of-taps-to-open-to-water-a-garden` |
| 1327 | unverified | source_fidelity.json is missing | no | 3 | 2 | 0 | 0 | 0 | `dsa/leetcode/1327_list-the-products-ordered-in-a-period` |
| 1328 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1328_break-a-palindrome` |
| 1329 | unverified | source_fidelity.json is missing | no | 3 | 1 | 0 | 0 | 0 | `dsa/leetcode/1329_sort-the-matrix-diagonally` |
| 1330 | unverified | source_fidelity.json is missing | no | 3 | 2 | 0 | 0 | 0 | `dsa/leetcode/1330_reverse-subarray-to-maximize-array-value` |
| 1331 | unverified | source_fidelity.json is missing | no | 3 | 1 | 0 | 0 | 0 | `dsa/leetcode/1331_rank-transform-of-an-array` |
| 1332 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1332_remove-palindromic-subsequences` |
| 1333 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1333_filter-restaurants-by-vegan-friendly-price-and-distance` |
| 1334 | unverified | source_fidelity.json is missing | no | 3 | 1 | 0 | 0 | 0 | `dsa/leetcode/1334_find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance` |
| 1335 | unverified | source_fidelity.json is missing | no | 3 | 2 | 0 | 0 | 0 | `dsa/leetcode/1335_minimum-difficulty-of-a-job-schedule` |
| 1336 | unverified | source_fidelity.json is missing | no | 3 | 1 | 0 | 0 | 0 | `dsa/leetcode/1336_number-of-transactions-per-visit` |
| 1337 | unverified | source_fidelity.json is missing | no | 3 | 1 | 0 | 0 | 0 | `dsa/leetcode/1337_the-k-weakest-rows-in-a-matrix` |
| 1338 | unverified | source_fidelity.json is missing | no | 3 | 2 | 0 | 0 | 0 | `dsa/leetcode/1338_reduce-array-size-to-the-half` |
| 1339 | unverified | source_fidelity.json is missing | no | 3 | 2 | 0 | 0 | 0 | `dsa/leetcode/1339_maximum-product-of-splitted-binary-tree` |
| 1340 | unverified | source_fidelity.json is missing | no | 3 | 1 | 0 | 0 | 0 | `dsa/leetcode/1340_jump-game-v` |
| 1341 | unverified | source_fidelity.json is missing | no | 3 | 1 | 0 | 0 | 0 | `dsa/leetcode/1341_movie-rating` |
| 1342 | unverified | source_fidelity.json is missing | no | 3 | 1 | 0 | 0 | 0 | `dsa/leetcode/1342_number-of-steps-to-reduce-a-number-to-zero` |
| 1343 | unverified | source_fidelity.json is missing | no | 3 | 1 | 0 | 0 | 0 | `dsa/leetcode/1343_number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold` |
| 1344 | unverified | source_fidelity.json is missing | no | 3 | 1 | 0 | 0 | 0 | `dsa/leetcode/1344_angle-between-hands-of-a-clock` |
| 1345 | unverified | source_fidelity.json is missing | no | 3 | 1 | 0 | 0 | 0 | `dsa/leetcode/1345_jump-game-iv` |
| 1346 | unverified | source_fidelity.json is missing | no | 3 | 1 | 0 | 0 | 0 | `dsa/leetcode/1346_check-if-n-and-its-double-exist` |
| 1347 | unverified | source_fidelity.json is missing | no | 3 | 1 | 0 | 0 | 0 | `dsa/leetcode/1347_minimum-number-of-steps-to-make-two-strings-anagram` |
| 1348 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1348_tweet-counts-per-frequency` |
| 1349 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1349_maximum-students-taking-exam` |
| 1350 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1350_students-with-invalid-departments` |
| 1351 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1351_count-negative-numbers-in-a-sorted-matrix` |
| 1352 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1352_product-of-the-last-k-numbers` |
| 1353 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1353_maximum-number-of-events-that-can-be-attended` |
| 1354 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1354_construct-target-array-with-multiple-sums` |
| 1355 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1355_activity-participants` |
| 1356 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1356_sort-integers-by-the-number-of-1-bits` |
| 1357 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1357_apply-discount-every-n-orders` |
| 1358 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1358_number-of-substrings-containing-all-three-characters` |
| 1359 | unverified | source_fidelity.json is missing | no | 3 | 2 | 0 | 0 | 0 | `dsa/leetcode/1359_count-all-valid-pickup-and-delivery-options` |
| 1360 | unverified | source_fidelity.json is missing | no | 3 | 1 | 0 | 0 | 0 | `dsa/leetcode/1360_number-of-days-between-two-dates` |
| 1361 | unverified | source_fidelity.json is missing | no | 3 | 2 | 0 | 0 | 0 | `dsa/leetcode/1361_validate-binary-tree-nodes` |
| 1362 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1362_closest-divisors` |
| 1363 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1363_largest-multiple-of-three` |
| 1364 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1364_number-of-trusted-contacts-of-a-customer` |
| 1365 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1365_how-many-numbers-are-smaller-than-the-current-number` |
| 1366 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1366_rank-teams-by-votes` |
| 1367 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1367_linked-list-in-binary-tree` |
| 1368 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1368_minimum-cost-to-make-at-least-one-valid-path-in-a-grid` |
| 1369 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1369_get-the-second-most-recent-activity` |
| 1370 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1370_increasing-decreasing-string` |
| 1371 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1371_find-the-longest-substring-containing-vowels-in-even-counts` |
| 1372 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1372_longest-zigzag-path-in-a-binary-tree` |
| 1373 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1373_maximum-sum-bst-in-binary-tree` |
| 1374 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1374_generate-a-string-with-characters-that-have-odd-counts` |
| 1375 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1375_number-of-times-binary-string-is-prefix-aligned` |
| 1376 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1376_time-needed-to-inform-all-employees` |
| 1377 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1377_frog-position-after-t-seconds` |
| 1378 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1378_replace-employee-id-with-the-unique-identifier` |
| 1379 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1379_find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree` |
| 1380 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1380_lucky-numbers-in-a-matrix` |
| 1381 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1381_design-a-stack-with-increment-operation` |
| 1382 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1382_balance-a-binary-search-tree` |
| 1383 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1383_maximum-performance-of-a-team` |
| 1384 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1384_total-sales-amount-by-year` |
| 1385 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1385_find-the-distance-value-between-two-arrays` |
| 1386 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1386_cinema-seat-allocation` |
| 1387 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1387_sort-integers-by-the-power-value` |
| 1388 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1388_pizza-with-3n-slices` |
| 1389 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1389_create-target-array-in-the-given-order` |
| 1390 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1390_four-divisors` |
| 1391 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1391_check-if-there-is-a-valid-path-in-a-grid` |
| 1392 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1392_longest-happy-prefix` |
| 1393 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1393_capital-gainloss` |
| 1394 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1394_find-lucky-integer-in-an-array` |
| 1395 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1395_count-number-of-teams` |
| 1396 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1396_design-underground-system` |
| 1397 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1397_find-all-good-strings` |
| 1398 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1398_customers-who-bought-products-a-and-b-but-not-c` |
| 1399 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1399_count-largest-group` |
| 1400 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1400_construct-k-palindrome-strings` |
| 1401 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1401_circle-and-rectangle-overlapping` |
| 1402 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1402_reducing-dishes` |
| 1403 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1403_minimum-subsequence-in-non-increasing-order` |
| 1404 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1404_number-of-steps-to-reduce-a-number-in-binary-representation-to-one` |
| 1405 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1405_longest-happy-string` |
| 1406 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1406_stone-game-iii` |
| 1407 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1407_top-travellers` |
| 1408 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1408_string-matching-in-an-array` |
| 1409 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1409_queries-on-a-permutation-with-key` |
| 1410 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1410_html-entity-parser` |
| 1411 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1411_number-of-ways-to-paint-n-3-grid` |
| 1412 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1412_find-the-quiet-students-in-all-exams` |
| 1413 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1413_minimum-value-to-get-positive-step-by-step-sum` |
| 1414 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1414_find-the-minimum-number-of-fibonacci-numbers-whose-sum-is-k` |
| 1415 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1415_the-k-th-lexicographical-string-of-all-happy-strings-of-length-n` |
| 1416 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1416_restore-the-array` |
| 1417 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1417_reformat-the-string` |
| 1418 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1418_display-table-of-food-orders-in-a-restaurant` |
| 1419 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1419_minimum-number-of-frogs-croaking` |
| 1420 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1420_build-array-where-you-can-find-the-maximum-exactly-k-comparisons` |
| 1421 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1421_npv-queries` |
| 1422 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1422_maximum-score-after-splitting-a-string` |
| 1423 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1423_maximum-points-you-can-obtain-from-cards` |
| 1424 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1424_diagonal-traverse-ii` |
| 1425 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1425_constrained-subsequence-sum` |
| 1426 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1426_counting-elements` |
| 1427 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1427_perform-string-shifts` |
| 1428 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1428_leftmost-column-with-at-least-a-one` |
| 1429 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1429_first-unique-number` |
| 1430 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1430_check-if-a-string-is-a-valid-sequence-from-root-to-leaves-path-in-a-binary-tree` |
| 1431 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1431_kids-with-the-greatest-number-of-candies` |
| 1432 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1432_max-difference-you-can-get-from-changing-an-integer` |
| 1433 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1433_check-if-a-string-can-break-another-string` |
| 1434 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1434_number-of-ways-to-wear-different-hats-to-each-other` |
| 1435 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1435_create-a-session-bar-chart` |
| 1436 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1436_destination-city` |
| 1437 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1437_check-if-all-1s-are-at-least-length-k-places-away` |
| 1438 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1438_longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit` |
| 1439 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1439_find-the-kth-smallest-sum-of-a-matrix-with-sorted-rows` |
| 1440 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1440_evaluate-boolean-expression` |
| 1441 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1441_build-an-array-with-stack-operations` |
| 1442 | unverified | source_fidelity.json is missing | no | 3 | 1 | 0 | 0 | 0 | `dsa/leetcode/1442_count-triplets-that-can-form-two-arrays-of-equal-xor` |
| 1443 | unverified | source_fidelity.json is missing | no | 3 | 1 | 0 | 0 | 0 | `dsa/leetcode/1443_minimum-time-to-collect-all-apples-in-a-tree` |
| 1444 | unverified | source_fidelity.json is missing | no | 3 | 1 | 0 | 0 | 0 | `dsa/leetcode/1444_number-of-ways-of-cutting-a-pizza` |
| 1445 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1445_apples-oranges` |
| 1446 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1446_consecutive-characters` |
| 1447 | unverified | source_fidelity.json is missing | no | 4 | 2 | 0 | 0 | 0 | `dsa/leetcode/1447_simplified-fractions` |
| 1448 | unverified | source_fidelity.json is missing | no | 3 | 2 | 0 | 0 | 0 | `dsa/leetcode/1448_count-good-nodes-in-binary-tree` |
| 1449 | unverified | source_fidelity.json is missing | no | 4 | 3 | 0 | 0 | 0 | `dsa/leetcode/1449_form-largest-integer-with-digits-that-add-up-to-target` |
| 1450 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1450_number-of-students-doing-homework-at-a-given-time` |
| 1451 | unverified | source_fidelity.json is missing | no | 3 | 1 | 0 | 0 | 0 | `dsa/leetcode/1451_rearrange-words-in-a-sentence` |
| 1452 | unverified | source_fidelity.json is missing | no | 3 | 2 | 0 | 0 | 0 | `dsa/leetcode/1452_people-whose-list-of-favorite-companies-is-not-a-subset-of-another-list` |
| 1453 | unverified | source_fidelity.json is missing | no | 3 | 2 | 0 | 0 | 0 | `dsa/leetcode/1453_maximum-number-of-darts-inside-of-a-circular-dartboard` |
| 1454 | unverified | source_fidelity.json is missing | no | 3 | 2 | 0 | 0 | 0 | `dsa/leetcode/1454_active-users` |
| 1455 | unverified | source_fidelity.json is missing | no | 3 | 1 | 0 | 0 | 0 | `dsa/leetcode/1455_check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence` |
| 1456 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1456_maximum-number-of-vowels-in-a-substring-of-given-length` |
| 1457 | unverified | source_fidelity.json is missing | no | 3 | 2 | 0 | 0 | 0 | `dsa/leetcode/1457_pseudo-palindromic-paths-in-a-binary-tree` |
| 1458 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1458_max-dot-product-of-two-subsequences` |
| 1459 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1459_rectangles-area` |
| 1460 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1460_make-two-arrays-equal-by-reversing-subarrays` |
| 1461 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1461_check-if-a-string-contains-all-binary-codes-of-size-k` |
| 1462 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1462_course-schedule-iv` |
| 1463 | unverified | source_fidelity.json is missing | no | 3 | 2 | 0 | 0 | 0 | `dsa/leetcode/1463_cherry-pickup-ii` |
| 1464 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1464_maximum-product-of-two-elements-in-an-array` |
| 1465 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1465_maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts` |
| 1466 | unverified | source_fidelity.json is missing | no | 3 | 2 | 0 | 0 | 0 | `dsa/leetcode/1466_reorder-routes-to-make-all-paths-lead-to-the-city-zero` |
| 1467 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1467_probability-of-a-two-boxes-having-the-same-number-of-distinct-balls` |
| 1468 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1468_calculate-salaries` |
| 1469 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1469_find-all-the-lonely-nodes` |
| 1470 | unverified | source_fidelity.json is missing | no | 3 | 2 | 0 | 0 | 0 | `dsa/leetcode/1470_shuffle-the-array` |
| 1471 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1471_the-k-strongest-values-in-an-array` |
| 1472 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1472_design-browser-history` |
| 1473 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1473_paint-house-iii` |
| 1474 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1474_delete-n-nodes-after-m-nodes-of-a-linked-list` |
| 1475 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1475_final-prices-with-a-special-discount-in-a-shop` |
| 1476 | unverified | source_fidelity.json is missing | no | 3 | 2 | 0 | 0 | 0 | `dsa/leetcode/1476_subrectangle-queries` |
| 1477 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1477_find-two-non-overlapping-sub-arrays-each-with-target-sum` |
| 1478 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1478_allocate-mailboxes` |
| 1479 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1479_sales-by-day-of-the-week` |
| 1480 | unverified | source_fidelity.json is missing | no | 3 | 1 | 0 | 0 | 0 | `dsa/leetcode/1480_running-sum-of-1d-array` |
| 1481 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/1481_least-number-of-unique-integers-after-k-removals` |
| 1482 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1482_minimum-number-of-days-to-make-m-bouquets` |
| 1483 | unverified | source_fidelity.json is missing | no | 1 | 1 | 0 | 0 | 0 | `dsa/leetcode/1483_kth-ancestor-of-a-tree-node` |
| 1484 | unverified | source_fidelity.json is missing | no | 1 | 0 | 0 | 3 | 0 | `dsa/leetcode/1484_group-sold-products-by-the-date` |
| 1485 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1485_clone-binary-tree-with-random-pointer` |
| 1486 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/1486_xor-operation-in-an-array` |
| 1487 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1487_making-file-names-unique` |
| 1488 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1488_avoid-flood-in-the-city` |
| 1489 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/1489_find-critical-and-pseudo-critical-edges-in-minimum-spanning-tree` |
| 1490 | unverified | source_fidelity.json is missing | no | 3 | 2 | 0 | 0 | 0 | `dsa/leetcode/1490_clone-n-ary-tree` |
| 1491 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1491_average-salary-excluding-the-minimum-and-maximum-salary` |
| 1492 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1492_the-kth-factor-of-n` |
| 1493 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1493_longest-subarray-of-1s-after-deleting-one-element` |
| 1494 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1494_parallel-courses-ii` |
| 1495 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 5 | 0 | `dsa/leetcode/1495_friendly-movies-streamed-last-month` |
| 1496 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1496_path-crossing` |
| 1497 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1497_check-if-array-pairs-are-divisible-by-k` |
| 1498 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1498_number-of-subsequences-that-satisfy-the-given-sum-condition` |
| 1499 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1499_max-value-of-equation` |
| 1500 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1500_design-a-file-sharing-system` |
| 1501 | unverified | source_fidelity.json is missing | no | 3 | 2 | 0 | 3 | 0 | `dsa/leetcode/1501_countries-you-can-safely-invest-in` |
| 1502 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1502_can-make-arithmetic-progression-from-sequence` |
| 1503 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1503_last-moment-before-all-ants-fall-out-of-a-plank` |
| 1504 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1504_count-submatrices-with-all-ones` |
| 1505 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1505_minimum-possible-integer-after-at-most-k-adjacent-swaps-on-digits` |
| 1506 | unverified | source_fidelity.json is missing | no | 3 | 1 | 0 | 0 | 0 | `dsa/leetcode/1506_find-root-of-n-ary-tree` |
| 1507 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1507_reformat-date` |
| 1508 | unverified | source_fidelity.json is missing | no | 3 | 1 | 0 | 0 | 0 | `dsa/leetcode/1508_range-sum-of-sorted-subarray-sums` |
| 1509 | unverified | source_fidelity.json is missing | no | 3 | 2 | 0 | 0 | 0 | `dsa/leetcode/1509_minimum-difference-between-largest-and-smallest-value-in-three-moves` |
| 1510 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1510_stone-game-iv` |
| 1511 | unverified | source_fidelity.json is missing | no | 3 | 1 | 0 | 0 | 0 | `dsa/leetcode/1511_customer-order-frequency` |
| 1512 | unverified | source_fidelity.json is missing | no | 3 | 2 | 0 | 0 | 0 | `dsa/leetcode/1512_number-of-good-pairs` |
| 1513 | unverified | source_fidelity.json is missing | no | 3 | 2 | 0 | 0 | 0 | `dsa/leetcode/1513_number-of-substrings-with-only-1s` |
| 1514 | unverified | source_fidelity.json is missing | no | 3 | 1 | 0 | 0 | 0 | `dsa/leetcode/1514_path-with-maximum-probability` |
| 1515 | unverified | source_fidelity.json is missing | no | 3 | 2 | 0 | 0 | 0 | `dsa/leetcode/1515_best-position-for-a-service-centre` |
| 1516 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1516_move-sub-tree-of-n-ary-tree` |
| 1517 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1517_find-users-with-valid-e-mails` |
| 1518 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1518_water-bottles` |
| 1519 | unverified | source_fidelity.json is missing | no | 3 | 2 | 0 | 0 | 0 | `dsa/leetcode/1519_number-of-nodes-in-the-sub-tree-with-the-same-label` |
| 1520 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1520_maximum-number-of-non-overlapping-substrings` |
| 1521 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1521_find-a-value-of-a-mysterious-function-closest-to-target` |
| 1522 | unverified | source_fidelity.json is missing | no | 3 | 2 | 0 | 0 | 0 | `dsa/leetcode/1522_diameter-of-n-ary-tree` |
| 1523 | unverified | source_fidelity.json is missing | no | 3 | 2 | 0 | 0 | 0 | `dsa/leetcode/1523_count-odd-numbers-in-an-interval-range` |
| 1524 | unverified | source_fidelity.json is missing | no | 3 | 2 | 0 | 0 | 0 | `dsa/leetcode/1524_number-of-sub-arrays-with-odd-sum` |
| 1525 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1525_number-of-good-ways-to-split-a-string` |
| 1526 | unverified | source_fidelity.json is missing | no | 3 | 2 | 0 | 0 | 0 | `dsa/leetcode/1526_minimum-number-of-increments-on-subarrays-to-form-a-target-array` |
| 1527 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1527_patients-with-a-condition` |
| 1528 | unverified | source_fidelity.json is missing | no | 3 | 2 | 0 | 0 | 0 | `dsa/leetcode/1528_shuffle-string` |
| 1529 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1529_minimum-suffix-flips` |
| 1530 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1530_number-of-good-leaf-nodes-pairs` |
| 1531 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1531_string-compression-ii` |
| 1532 | unverified | source_fidelity.json is missing | no | 3 | 2 | 0 | 0 | 0 | `dsa/leetcode/1532_the-most-recent-three-orders` |
| 1533 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1533_find-the-index-of-the-large-integer` |
| 1534 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1534_count-good-triplets` |
| 1535 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1535_find-the-winner-of-an-array-game` |
| 1536 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1536_minimum-swaps-to-arrange-a-binary-grid` |
| 1537 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1537_get-the-maximum-score` |
| 1538 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1538_guess-the-majority-in-a-hidden-array` |
| 1539 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/1539_kth-missing-positive-number` |
| 1540 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1540_can-convert-string-in-k-moves` |
| 1541 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1541_minimum-insertions-to-balance-a-parentheses-string` |
| 1542 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1542_find-longest-awesome-substring` |
| 1543 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1543_fix-product-name-format` |
| 1544 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1544_make-the-string-great` |
| 1545 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1545_find-kth-bit-in-nth-binary-string` |
| 1546 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1546_maximum-number-of-non-overlapping-subarrays-with-sum-equals-target` |
| 1547 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1547_minimum-cost-to-cut-a-stick` |
| 1548 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1548_the-most-similar-path-in-a-graph` |
| 1549 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1549_the-most-recent-orders-for-each-product` |
| 1550 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1550_three-consecutive-odds` |
| 1551 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1551_minimum-operations-to-make-array-equal` |
| 1552 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1552_magnetic-force-between-two-balls` |
| 1553 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1553_minimum-number-of-days-to-eat-n-oranges` |
| 1554 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1554_strings-differ-by-one-character` |
| 1555 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1555_bank-account-summary` |
| 1556 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1556_thousand-separator` |
| 1557 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1557_minimum-number-of-vertices-to-reach-all-nodes` |
| 1558 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1558_minimum-numbers-of-function-calls-to-make-target-array` |
| 1559 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1559_detect-cycles-in-2d-grid` |
| 1560 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1560_most-visited-sector-in-a-circular-track` |
| 1561 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1561_maximum-number-of-coins-you-can-get` |
| 1562 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1562_find-latest-group-of-size-m` |
| 1563 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1563_stone-game-v` |
| 1564 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1564_put-boxes-into-the-warehouse-i` |
| 1565 | unverified | source_fidelity.json is missing | no | 3 | 1 | 0 | 0 | 0 | `dsa/leetcode/1565_unique-orders-and-customers-per-month` |
| 1566 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1566_detect-pattern-of-length-m-repeated-k-or-more-times` |
| 1567 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1567_maximum-length-of-subarray-with-positive-product` |
| 1568 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1568_minimum-number-of-days-to-disconnect-island` |
| 1569 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1569_number-of-ways-to-reorder-array-to-get-same-bst` |
| 1570 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1570_dot-product-of-two-sparse-vectors` |
| 1571 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1571_warehouse-manager` |
| 1572 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1572_matrix-diagonal-sum` |
| 1573 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1573_number-of-ways-to-split-a-string` |
| 1574 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1574_shortest-subarray-to-be-removed-to-make-array-sorted` |
| 1575 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1575_count-all-possible-routes` |
| 1576 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1576_replace-all-s-to-avoid-consecutive-repeating-characters` |
| 1577 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1577_number-of-ways-where-square-of-number-is-equal-to-product-of-two-numbers` |
| 1578 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1578_minimum-time-to-make-rope-colorful` |
| 1579 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1579_remove-max-number-of-edges-to-keep-graph-fully-traversable` |
| 1580 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1580_put-boxes-into-the-warehouse-ii` |
| 1581 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1581_customer-who-visited-but-did-not-make-any-transactions` |
| 1582 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1582_special-positions-in-a-binary-matrix` |
| 1583 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1583_count-unhappy-friends` |
| 1584 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1584_min-cost-to-connect-all-points` |
| 1585 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1585_check-if-string-is-transformable-with-substring-sort-operations` |
| 1586 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1586_binary-search-tree-iterator-ii` |
| 1587 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1587_bank-account-summary-ii` |
| 1588 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1588_sum-of-all-odd-length-subarrays` |
| 1589 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1589_maximum-sum-obtained-of-any-permutation` |
| 1590 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1590_make-sum-divisible-by-p` |
| 1591 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1591_strange-printer-ii` |
| 1592 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1592_rearrange-spaces-between-words` |
| 1593 | unverified | source_fidelity.json is missing | no | 3 | 2 | 0 | 0 | 0 | `dsa/leetcode/1593_split-a-string-into-the-max-number-of-unique-substrings` |
| 1594 | unverified | source_fidelity.json is missing | no | 3 | 1 | 0 | 0 | 0 | `dsa/leetcode/1594_maximum-non-negative-product-in-a-matrix` |
| 1595 | unverified | source_fidelity.json is missing | no | 3 | 1 | 0 | 0 | 0 | `dsa/leetcode/1595_minimum-cost-to-connect-two-groups-of-points` |
| 1596 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1596_the-most-frequently-ordered-products-for-each-customer` |
| 1597 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1597_build-binary-expression-tree-from-infix-expression` |
| 1598 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1598_crawler-log-folder` |
| 1599 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1599_maximum-profit-of-operating-a-centennial-wheel` |
| 1600 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1600_throne-inheritance` |
| 1601 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1601_maximum-number-of-achievable-transfer-requests` |
| 1602 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1602_find-nearest-right-node-in-binary-tree` |
| 1603 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1603_design-parking-system` |
| 1604 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/1604_alert-using-same-key-card-three-or-more-times-in-a-one-hour-period` |
| 1605 | unverified | source_fidelity.json is missing | no | 2 | 1 | 0 | 0 | 0 | `dsa/leetcode/1605_find-valid-matrix-given-row-and-column-sums` |
| 1606 | unverified | source_fidelity.json is missing | no | 3 | 1 | 0 | 0 | 0 | `dsa/leetcode/1606_find-servers-that-handled-most-number-of-requests` |
| 1607 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1607_sellers-with-no-sales` |
| 1608 | unverified | source_fidelity.json is missing | no | 3 | 2 | 0 | 0 | 0 | `dsa/leetcode/1608_special-array-with-x-elements-greater-than-or-equal-x` |
| 1609 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1609_even-odd-tree` |
| 1610 | unverified | source_fidelity.json is missing | no | 3 | 2 | 0 | 0 | 0 | `dsa/leetcode/1610_maximum-number-of-visible-points` |
| 1611 | unverified | source_fidelity.json is missing | no | 3 | 2 | 0 | 0 | 0 | `dsa/leetcode/1611_minimum-one-bit-operations-to-make-integers-zero` |
| 1612 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1612_check-if-two-expression-trees-are-equivalent` |
| 1613 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1613_find-the-missing-ids` |
| 1614 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1614_maximum-nesting-depth-of-the-parentheses` |
| 1615 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1615_maximal-network-rank` |
| 1616 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1616_split-two-strings-to-make-palindrome` |
| 1617 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1617_count-subtrees-with-max-distance-between-cities` |
| 1618 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1618_maximum-font-to-fit-a-sentence-in-a-screen` |
| 1619 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1619_mean-of-array-after-removing-some-elements` |
| 1620 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1620_coordinate-with-maximum-network-quality` |
| 1621 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1621_number-of-sets-of-k-non-overlapping-line-segments` |
| 1622 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1622_fancy-sequence` |
| 1623 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1623_all-valid-triplets-that-can-represent-a-country` |
| 1624 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1624_largest-substring-between-two-equal-characters` |
| 1625 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1625_lexicographically-smallest-string-after-applying-operations` |
| 1626 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1626_best-team-with-no-conflicts` |
| 1627 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1627_graph-connectivity-with-threshold` |
| 1628 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1628_design-an-expression-tree-with-evaluate-function` |
| 1629 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1629_slowest-key` |
| 1630 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1630_arithmetic-subarrays` |
| 1631 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1631_path-with-minimum-effort` |
| 1632 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1632_rank-transform-of-a-matrix` |
| 1633 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1633_percentage-of-users-attended-a-contest` |
| 1634 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1634_add-two-polynomials-represented-as-linked-lists` |
| 1635 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1635_hopper-company-queries-i` |
| 1636 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1636_sort-array-by-increasing-frequency` |
| 1637 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1637_widest-vertical-area-between-two-points-containing-no-points` |
| 1638 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1638_count-substrings-that-differ-by-one-character` |
| 1639 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1639_number-of-ways-to-form-a-target-string-given-a-dictionary` |
| 1640 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1640_check-array-formation-through-concatenation` |
| 1641 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1641_count-sorted-vowel-strings` |
| 1642 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1642_furthest-building-you-can-reach` |
| 1643 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1643_kth-smallest-instructions` |
| 1644 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1644_lowest-common-ancestor-of-a-binary-tree-ii` |
| 1645 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1645_hopper-company-queries-ii` |
| 1646 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1646_get-maximum-in-generated-array` |
| 1647 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1647_minimum-deletions-to-make-character-frequencies-unique` |
| 1648 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1648_sell-diminishing-valued-colored-balls` |
| 1649 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1649_create-sorted-array-through-instructions` |
| 1650 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1650_lowest-common-ancestor-of-a-binary-tree-iii` |
| 1651 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1651_hopper-company-queries-iii` |
| 1652 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1652_defuse-the-bomb` |
| 1653 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1653_minimum-deletions-to-make-string-balanced` |
| 1654 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1654_minimum-jumps-to-reach-home` |
| 1655 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1655_distribute-repeating-integers` |
| 1656 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1656_design-an-ordered-stream` |
| 1657 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1657_determine-if-two-strings-are-close` |
| 1658 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1658_minimum-operations-to-reduce-x-to-zero` |
| 1659 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1659_maximize-grid-happiness` |
| 1660 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/1660_correct-a-binary-tree` |
| 1661 | unverified | source_fidelity.json is missing | no | 1 | 0 | 0 | 1 | 0 | `dsa/leetcode/1661_average-time-of-process-per-machine` |
| 1662 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1662_check-if-two-string-arrays-are-equivalent` |
| 1663 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/1663_smallest-string-with-a-given-numeric-value` |
| 1664 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1664_ways-to-make-a-fair-array` |
| 1665 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1665_minimum-initial-energy-to-finish-tasks` |
| 1666 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/1666_change-the-root-of-a-binary-tree` |
| 1667 | unverified | source_fidelity.json is missing | no | 1 | 0 | 0 | 1 | 0 | `dsa/leetcode/1667_fix-names-in-a-table` |
| 1668 | unverified | source_fidelity.json is missing | no | 3 | 2 | 0 | 0 | 0 | `dsa/leetcode/1668_maximum-repeating-substring` |
| 1669 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/1669_merge-in-between-linked-lists` |
| 1670 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/1670_design-front-middle-back-queue` |
| 1671 | unverified | source_fidelity.json is missing | no | 2 | 1 | 0 | 0 | 0 | `dsa/leetcode/1671_minimum-number-of-removals-to-make-mountain-array` |
| 1672 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1672_richest-customer-wealth` |
| 1673 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/1673_find-the-most-competitive-subsequence` |
| 1674 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1674_minimum-moves-to-make-array-complementary` |
| 1675 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1675_minimize-deviation-in-array` |
| 1676 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1676_lowest-common-ancestor-of-a-binary-tree-iv` |
| 1677 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1677_products-worth-over-invoices` |
| 1678 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1678_goal-parser-interpretation` |
| 1679 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1679_max-number-of-k-sum-pairs` |
| 1680 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1680_concatenation-of-consecutive-binary-numbers` |
| 1681 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1681_minimum-incompatibility` |
| 1682 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1682_longest-palindromic-subsequence-ii` |
| 1683 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 4 | 0 | `dsa/leetcode/1683_invalid-tweets` |
| 1684 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1684_count-the-number-of-consistent-strings` |
| 1685 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1685_sum-of-absolute-differences-in-a-sorted-array` |
| 1686 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1686_stone-game-vi` |
| 1687 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1687_delivering-boxes-from-storage-to-ports` |
| 1688 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1688_count-of-matches-in-tournament` |
| 1689 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1689_partitioning-into-minimum-number-of-deci-binary-numbers` |
| 1690 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1690_stone-game-vii` |
| 1691 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1691_maximum-height-by-stacking-cuboids` |
| 1692 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1692_count-ways-to-distribute-candies` |
| 1693 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1693_daily-leads-and-partners` |
| 1694 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1694_reformat-phone-number` |
| 1695 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1695_maximum-erasure-value` |
| 1696 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1696_jump-game-vi` |
| 1697 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1697_checking-existence-of-edge-length-limited-paths` |
| 1698 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1698_number-of-distinct-substrings-in-a-string` |
| 1699 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1699_number-of-calls-between-two-persons` |
| 1700 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1700_number-of-students-unable-to-eat-lunch` |
| 1701 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1701_average-waiting-time` |
| 1702 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1702_maximum-binary-string-after-change` |
| 1703 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1703_minimum-adjacent-swaps-for-k-consecutive-ones` |
| 1704 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1704_determine-if-string-halves-are-alike` |
| 1705 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1705_maximum-number-of-eaten-apples` |
| 1706 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1706_where-will-the-ball-fall` |
| 1707 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1707_maximum-xor-with-an-element-from-array` |
| 1708 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1708_largest-subarray-length-k` |
| 1709 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1709_biggest-window-between-visits` |
| 1710 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1710_maximum-units-on-a-truck` |
| 1711 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1711_count-good-meals` |
| 1712 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1712_ways-to-split-array-into-three-subarrays` |
| 1713 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1713_minimum-operations-to-make-a-subsequence` |
| 1714 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1714_sum-of-special-evenly-spaced-elements-in-array` |
| 1715 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1715_count-apples-and-oranges` |
| 1716 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1716_calculate-money-in-leetcode-bank` |
| 1717 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1717_maximum-score-from-removing-substrings` |
| 1718 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1718_construct-the-lexicographically-largest-valid-sequence` |
| 1719 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1719_number-of-ways-to-reconstruct-a-tree` |
| 1720 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1720_decode-xored-array` |
| 1721 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1721_swapping-nodes-in-a-linked-list` |
| 1722 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1722_minimize-hamming-distance-after-swap-operations` |
| 1723 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1723_find-minimum-time-to-finish-all-jobs` |
| 1724 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1724_checking-existence-of-edge-length-limited-paths-ii` |
| 1725 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1725_number-of-rectangles-that-can-form-the-largest-square` |
| 1726 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1726_tuple-with-same-product` |
| 1727 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1727_largest-submatrix-with-rearrangements` |
| 1728 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1728_cat-and-mouse-ii` |
| 1729 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1729_find-followers-count` |
| 1730 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1730_shortest-path-to-get-food` |
| 1731 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1731_the-number-of-employees-which-report-to-each-employee` |
| 1732 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1732_find-the-highest-altitude` |
| 1733 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1733_minimum-number-of-people-to-teach` |
| 1734 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1734_decode-xored-permutation` |
| 1735 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1735_count-ways-to-make-array-with-product` |
| 1736 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1736_latest-time-by-replacing-hidden-digits` |
| 1737 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1737_change-minimum-characters-to-satisfy-one-of-three-conditions` |
| 1738 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1738_find-kth-largest-xor-coordinate-value` |
| 1739 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1739_building-boxes` |
| 1740 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1740_find-distance-in-a-binary-tree` |
| 1741 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1741_find-total-time-spent-by-each-employee` |
| 1742 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1742_maximum-number-of-balls-in-a-box` |
| 1743 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1743_restore-the-array-from-adjacent-pairs` |
| 1744 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1744_can-you-eat-your-favorite-candy-on-your-favorite-day` |
| 1745 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1745_palindrome-partitioning-iv` |
| 1746 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1746_maximum-subarray-sum-after-one-operation` |
| 1747 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1747_leetflex-banned-accounts` |
| 1748 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1748_sum-of-unique-elements` |
| 1749 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1749_maximum-absolute-sum-of-any-subarray` |
| 1750 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1750_minimum-length-of-string-after-deleting-similar-ends` |
| 1751 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1751_maximum-number-of-events-that-can-be-attended-ii` |
| 1752 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1752_check-if-array-is-sorted-and-rotated` |
| 1753 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1753_maximum-score-from-removing-stones` |
| 1754 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1754_largest-merge-of-two-strings` |
| 1755 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1755_closest-subsequence-sum` |
| 1756 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1756_design-most-recently-used-queue` |
| 1757 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1757_recyclable-and-low-fat-products` |
| 1758 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1758_minimum-changes-to-make-alternating-binary-string` |
| 1759 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1759_count-number-of-homogenous-substrings` |
| 1760 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1760_minimum-limit-of-balls-in-a-bag` |
| 1761 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1761_minimum-degree-of-a-connected-trio-in-a-graph` |
| 1762 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1762_buildings-with-an-ocean-view` |
| 1763 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1763_longest-nice-substring` |
| 1764 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1764_form-array-by-concatenating-subarrays-of-another-array` |
| 1765 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1765_map-of-highest-peak` |
| 1766 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1766_tree-of-coprimes` |
| 1767 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1767_find-the-subtasks-that-did-not-execute` |
| 1768 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1768_merge-strings-alternately` |
| 1769 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1769_minimum-number-of-operations-to-move-all-balls-to-each-box` |
| 1770 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1770_maximum-score-from-performing-multiplication-operations` |
| 1771 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1771_maximize-palindrome-length-from-subsequences` |
| 1772 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1772_sort-features-by-popularity` |
| 1773 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1773_count-items-matching-a-rule` |
| 1774 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1774_closest-dessert-cost` |
| 1775 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1775_equal-sum-arrays-with-minimum-number-of-operations` |
| 1776 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1776_car-fleet-ii` |
| 1777 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 2 | 0 | `dsa/leetcode/1777_products-price-for-each-store` |
| 1778 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1778_shortest-path-in-a-hidden-grid` |
| 1779 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1779_find-nearest-point-that-has-the-same-x-or-y-coordinate` |
| 1780 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1780_check-if-number-is-a-sum-of-powers-of-three` |
| 1781 | unverified | source_fidelity.json is missing | no | 3 | 2 | 0 | 0 | 0 | `dsa/leetcode/1781_sum-of-beauty-of-all-substrings` |
| 1782 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1782_count-pairs-of-nodes` |
| 1783 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1783_grand-slam-titles` |
| 1784 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1784_check-if-binary-string-has-at-most-one-segment-of-ones` |
| 1785 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1785_minimum-elements-to-add-to-form-a-given-sum` |
| 1786 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1786_number-of-restricted-paths-from-first-to-last-node` |
| 1787 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1787_make-the-xor-of-all-segments-equal-to-zero` |
| 1788 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1788_maximize-the-beauty-of-the-garden` |
| 1789 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1789_primary-department-for-each-employee` |
| 1790 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1790_check-if-one-string-swap-can-make-strings-equal` |
| 1791 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1791_find-center-of-star-graph` |
| 1792 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1792_maximum-average-pass-ratio` |
| 1793 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1793_maximum-score-of-a-good-subarray` |
| 1794 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1794_count-pairs-of-equal-substrings-with-minimum-difference` |
| 1795 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1795_rearrange-products-table` |
| 1796 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1796_second-largest-digit-in-a-string` |
| 1797 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1797_design-authentication-manager` |
| 1798 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1798_maximum-number-of-consecutive-values-you-can-make` |
| 1799 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1799_maximize-score-after-n-operations` |
| 1800 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1800_maximum-ascending-subarray-sum` |
| 1801 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1801_number-of-orders-in-the-backlog` |
| 1802 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1802_maximum-value-at-a-given-index-in-a-bounded-array` |
| 1803 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1803_count-pairs-with-xor-in-a-range` |
| 1804 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1804_implement-trie-ii-prefix-tree` |
| 1805 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1805_number-of-different-integers-in-a-string` |
| 1806 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1806_minimum-number-of-operations-to-reinitialize-a-permutation` |
| 1807 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1807_evaluate-the-bracket-pairs-of-a-string` |
| 1808 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1808_maximize-number-of-nice-divisors` |
| 1809 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1809_ad-free-sessions` |
| 1810 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1810_minimum-path-cost-in-a-hidden-grid` |
| 1811 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1811_find-interview-candidates` |
| 1812 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1812_determine-color-of-a-chessboard-square` |
| 1813 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1813_sentence-similarity-iii` |
| 1814 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1814_count-nice-pairs-in-an-array` |
| 1815 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1815_maximum-number-of-groups-getting-fresh-donuts` |
| 1816 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1816_truncate-sentence` |
| 1817 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/1817_finding-the-users-active-minutes` |
| 1818 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1818_minimum-absolute-sum-difference` |
| 1819 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/1819_number-of-different-subsequences-gcds` |
| 1820 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/1820_maximum-number-of-accepted-invitations` |
| 1821 | unverified | source_fidelity.json is missing | no | 1 | 0 | 0 | 2 | 0 | `dsa/leetcode/1821_find-customers-with-positive-revenue-this-year` |
| 1822 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1822_sign-of-the-product-of-an-array` |
| 1823 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/1823_find-the-winner-of-the-circular-game` |
| 1824 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1824_minimum-sideway-jumps` |
| 1825 | unverified | source_fidelity.json is missing | no | 1 | 0 | 0 | 0 | 0 | `dsa/leetcode/1825_finding-mk-average` |
| 1826 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1826_faulty-sensor` |
| 1827 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1827_minimum-operations-to-make-the-array-increasing` |
| 1828 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1828_queries-on-number-of-points-inside-a-circle` |
| 1829 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1829_maximum-xor-for-each-query` |
| 1830 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1830_minimum-number-of-operations-to-make-string-sorted` |
| 1831 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 2 | 0 | `dsa/leetcode/1831_maximum-transaction-each-day` |
| 1832 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1832_check-if-the-sentence-is-pangram` |
| 1833 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1833_maximum-ice-cream-bars` |
| 1834 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1834_single-threaded-cpu` |
| 1835 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1835_find-xor-sum-of-all-pairs-bitwise-and` |
| 1836 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1836_remove-duplicates-from-an-unsorted-linked-list` |
| 1837 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1837_sum-of-digits-in-base-k` |
| 1838 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1838_frequency-of-the-most-frequent-element` |
| 1839 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1839_longest-substring-of-all-vowels-in-order` |
| 1840 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1840_maximum-building-height` |
| 1841 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 3 | 0 | `dsa/leetcode/1841_league-statistics` |
| 1842 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1842_next-palindrome-using-same-digits` |
| 1843 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 1 | 0 | `dsa/leetcode/1843_suspicious-bank-accounts` |
| 1844 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1844_replace-all-digits-with-characters` |
| 1845 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1845_seat-reservation-manager` |
| 1846 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1846_maximum-element-after-decreasing-and-rearranging` |
| 1847 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1847_closest-room` |
| 1848 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1848_minimum-distance-to-the-target-element` |
| 1849 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1849_splitting-a-string-into-descending-consecutive-values` |
| 1850 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1850_minimum-adjacent-swaps-to-reach-the-kth-smallest-number` |
| 1851 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1851_minimum-interval-to-include-each-query` |
| 1852 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1852_distinct-numbers-in-each-subarray` |
| 1853 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1853_convert-date-format` |
| 1854 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1854_maximum-population-year` |
| 1855 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1855_maximum-distance-between-a-pair-of-values` |
| 1856 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1856_maximum-subarray-min-product` |
| 1857 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1857_largest-color-value-in-a-directed-graph` |
| 1858 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1858_longest-word-with-all-prefixes` |
| 1859 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1859_sorting-the-sentence` |
| 1860 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1860_incremental-memory-leak` |
| 1861 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1861_rotating-the-box` |
| 1862 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1862_sum-of-floored-pairs` |
| 1863 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1863_sum-of-all-subset-xor-totals` |
| 1864 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1864_minimum-number-of-swaps-to-make-the-binary-string-alternating` |
| 1865 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1865_finding-pairs-with-a-certain-sum` |
| 1866 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1866_number-of-ways-to-rearrange-sticks-with-k-sticks-visible` |
| 1867 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1867_orders-with-maximum-quantity-above-average` |
| 1868 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1868_product-of-two-run-length-encoded-arrays` |
| 1869 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1869_longer-contiguous-segments-of-ones-than-zeros` |
| 1870 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1870_minimum-speed-to-arrive-on-time` |
| 1871 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1871_jump-game-vii` |
| 1872 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1872_stone-game-viii` |
| 1873 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1873_calculate-special-bonus` |
| 1874 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1874_minimize-product-sum-of-two-arrays` |
| 1875 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1875_group-employees-of-the-same-salary` |
| 1876 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1876_substrings-of-size-three-with-distinct-characters` |
| 1877 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1877_minimize-maximum-pair-sum-in-array` |
| 1878 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1878_get-biggest-three-rhombus-sums-in-a-grid` |
| 1879 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1879_minimum-xor-sum-of-two-arrays` |
| 1880 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1880_check-if-word-equals-summation-of-two-words` |
| 1881 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1881_maximum-value-after-insertion` |
| 1882 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1882_process-tasks-using-servers` |
| 1883 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1883_minimum-skips-to-arrive-at-meeting-on-time` |
| 1884 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1884_egg-drop-with-2-eggs-and-n-floors` |
| 1885 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1885_count-pairs-in-two-arrays` |
| 1886 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1886_determine-whether-matrix-can-be-obtained-by-rotation` |
| 1887 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1887_reduction-operations-to-make-the-array-elements-equal` |
| 1888 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1888_minimum-number-of-flips-to-make-the-binary-string-alternating` |
| 1889 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1889_minimum-space-wasted-from-packaging` |
| 1890 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1890_the-latest-login-in-2020` |
| 1891 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1891_cutting-ribbons` |
| 1892 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1892_page-recommendations-ii` |
| 1893 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1893_check-if-all-the-integers-in-a-range-are-covered` |
| 1894 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1894_find-the-student-that-will-replace-the-chalk` |
| 1895 | unverified | source_fidelity.json is missing | no | 3 | 2 | 0 | 0 | 0 | `dsa/leetcode/1895_largest-magic-square` |
| 1896 | unverified | source_fidelity.json is missing | no | 3 | 2 | 0 | 0 | 0 | `dsa/leetcode/1896_minimum-cost-to-change-the-final-value-of-expression` |
| 1897 | unverified | source_fidelity.json is missing | no | 3 | 2 | 0 | 0 | 0 | `dsa/leetcode/1897_redistribute-characters-to-make-all-strings-equal` |
| 1898 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1898_maximum-number-of-removable-characters` |
| 1899 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1899_merge-triplets-to-form-target-triplet` |
| 1900 | unverified | source_fidelity.json is missing | no | 3 | 2 | 0 | 0 | 0 | `dsa/leetcode/1900_the-earliest-and-latest-rounds-where-players-compete` |
| 1901 | unverified | source_fidelity.json is missing | no | 3 | 2 | 0 | 0 | 0 | `dsa/leetcode/1901_find-a-peak-element-ii` |
| 1902 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1902_depth-of-bst-given-insertion-order` |
| 1903 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1903_largest-odd-number-in-string` |
| 1904 | unverified | source_fidelity.json is missing | no | 3 | 2 | 0 | 0 | 0 | `dsa/leetcode/1904_the-number-of-full-rounds-you-have-played` |
| 1905 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1905_count-sub-islands` |
| 1906 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1906_minimum-absolute-difference-queries` |
| 1907 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1907_count-salary-categories` |
| 1908 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1908_game-of-nim` |
| 1909 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1909_remove-one-element-to-make-the-array-strictly-increasing` |
| 1910 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1910_remove-all-occurrences-of-a-substring` |
| 1911 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1911_maximum-alternating-subsequence-sum` |
| 1912 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1912_design-movie-rental-system` |
| 1913 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1913_maximum-product-difference-between-two-pairs` |
| 1914 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1914_cyclically-rotating-a-grid` |
| 1915 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1915_number-of-wonderful-substrings` |
| 1916 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1916_count-ways-to-build-rooms-in-an-ant-colony` |
| 1917 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1917_leetcodify-friends-recommendations` |
| 1918 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/1918_kth-smallest-subarray-sum` |
| 1919 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1919_leetcodify-similar-friends` |
| 1920 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1920_build-array-from-permutation` |
| 1921 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1921_eliminate-maximum-number-of-monsters` |
| 1922 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1922_count-good-numbers` |
| 1923 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1923_longest-common-subpath` |
| 1924 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/1924_erect-the-fence-ii` |
| 1925 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/1925_count-square-sum-triples` |
| 1926 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1926_nearest-exit-from-entrance-in-maze` |
| 1927 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1927_sum-game` |
| 1928 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1928_minimum-cost-to-reach-destination-in-time` |
| 1929 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1929_concatenation-of-array` |
| 1930 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1930_unique-length-3-palindromic-subsequences` |
| 1931 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1931_painting-a-grid-with-three-different-colors` |
| 1932 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1932_merge-bsts-to-create-single-bst` |
| 1933 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1933_check-if-string-is-decomposable-into-value-equal-substrings` |
| 1934 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 1 | 0 | `dsa/leetcode/1934_confirmation-rate` |
| 1935 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1935_maximum-number-of-words-you-can-type` |
| 1936 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1936_add-minimum-number-of-rungs` |
| 1937 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1937_maximum-number-of-points-with-cost` |
| 1938 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1938_maximum-genetic-difference-query` |
| 1939 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1939_users-that-actively-request-confirmation-messages` |
| 1940 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1940_longest-common-subsequence-between-sorted-arrays` |
| 1941 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1941_check-if-all-characters-have-equal-number-of-occurrences` |
| 1942 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1942_the-number-of-the-smallest-unoccupied-chair` |
| 1943 | unverified | source_fidelity.json is missing | no | 3 | 1 | 0 | 0 | 0 | `dsa/leetcode/1943_describe-the-painting` |
| 1944 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1944_number-of-visible-people-in-a-queue` |
| 1945 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1945_sum-of-digits-of-string-after-convert` |
| 1946 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1946_largest-number-after-mutating-substring` |
| 1947 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1947_maximum-compatibility-score-sum` |
| 1948 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1948_delete-duplicate-folders-in-system` |
| 1949 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1949_strong-friendship` |
| 1950 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1950_maximum-of-minimum-values-in-all-subarrays` |
| 1951 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1951_all-the-pairs-with-the-maximum-number-of-common-followers` |
| 1952 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1952_three-divisors` |
| 1953 | unverified | source_fidelity.json is missing | no | 3 | 2 | 0 | 0 | 0 | `dsa/leetcode/1953_maximum-number-of-weeks-for-which-you-can-work` |
| 1954 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1954_minimum-garden-perimeter-to-collect-enough-apples` |
| 1955 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1955_count-number-of-special-subsequences` |
| 1956 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1956_minimum-time-for-k-virus-variants-to-spread` |
| 1957 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1957_delete-characters-to-make-fancy-string` |
| 1958 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1958_check-if-move-is-legal` |
| 1959 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1959_minimum-total-space-wasted-with-k-resizing-operations` |
| 1960 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1960_maximum-product-of-the-length-of-two-palindromic-substrings` |
| 1961 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1961_check-if-string-is-a-prefix-of-array` |
| 1962 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1962_remove-stones-to-minimize-the-total` |
| 1963 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1963_minimum-number-of-swaps-to-make-the-string-balanced` |
| 1964 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1964_find-the-longest-valid-obstacle-course-at-each-position` |
| 1965 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1965_employees-with-missing-information` |
| 1966 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1966_binary-searchable-numbers-in-an-unsorted-array` |
| 1967 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1967_number-of-strings-that-appear-as-substrings-in-word` |
| 1968 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1968_array-with-elements-not-equal-to-average-of-neighbors` |
| 1969 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1969_minimum-non-zero-product-of-the-array-elements` |
| 1970 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1970_last-day-where-you-can-still-cross` |
| 1971 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1971_find-if-path-exists-in-graph` |
| 1972 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1972_first-and-last-call-on-the-same-day` |
| 1973 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1973_count-nodes-equal-to-sum-of-descendants` |
| 1974 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1974_minimum-time-to-type-word-using-special-typewriter` |
| 1975 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1975_maximum-matrix-sum` |
| 1976 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1976_number-of-ways-to-arrive-at-destination` |
| 1977 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1977_number-of-ways-to-separate-numbers` |
| 1978 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1978_employees-whose-manager-left-the-company` |
| 1979 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1979_find-greatest-common-divisor-of-array` |
| 1980 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1980_find-unique-binary-string` |
| 1981 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1981_minimize-the-difference-between-target-and-chosen-elements` |
| 1982 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1982_find-array-given-subset-sums` |
| 1983 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1983_widest-pair-of-indices-with-equal-range-sum` |
| 1984 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1984_minimum-difference-between-highest-and-lowest-of-k-scores` |
| 1985 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1985_find-the-kth-largest-integer-in-the-array` |
| 1986 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1986_minimum-number-of-work-sessions-to-finish-the-tasks` |
| 1987 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1987_number-of-unique-good-subsequences` |
| 1988 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 3 | 0 | `dsa/leetcode/1988_find-cutoff-score-for-each-school` |
| 1989 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1989_maximum-number-of-people-that-can-be-caught-in-tag` |
| 1990 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 1 | 0 | `dsa/leetcode/1990_count-the-number-of-experiments` |
| 1991 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1991_find-the-middle-index-in-array` |
| 1992 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/1992_find-all-groups-of-farmland` |
| 1993 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/1993_operations-on-tree` |
| 1994 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1994_the-number-of-good-subsets` |
| 1995 | unverified | source_fidelity.json is missing | no | 3 | 2 | 0 | 0 | 0 | `dsa/leetcode/1995_count-special-quadruplets` |
| 1996 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1996_the-number-of-weak-characters-in-the-game` |
| 1997 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1997_first-day-where-you-have-been-in-all-the-rooms` |
| 1998 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1998_gcd-sort-of-an-array` |
| 1999 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/1999_smallest-greater-multiple-made-of-two-digits` |
| 2000 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2000_reverse-prefix-of-word` |
| 2001 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2001_number-of-pairs-of-interchangeable-rectangles` |
| 2002 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2002_maximum-product-of-the-length-of-two-palindromic-subsequences` |
| 2003 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2003_smallest-missing-genetic-value-in-each-subtree` |
| 2004 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2004_the-number-of-seniors-and-juniors-to-join-the-company` |
| 2005 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2005_subtree-removal-game-with-fibonacci-tree` |
| 2006 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2006_count-number-of-pairs-with-absolute-difference-k` |
| 2007 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2007_find-original-array-from-doubled-array` |
| 2008 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2008_maximum-earnings-from-taxi` |
| 2009 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2009_minimum-number-of-operations-to-make-array-continuous` |
| 2010 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2010_the-number-of-seniors-and-juniors-to-join-the-company-ii` |
| 2011 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2011_final-value-of-variable-after-performing-operations` |
| 2012 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2012_sum-of-beauty-in-the-array` |
| 2013 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2013_detect-squares` |
| 2014 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2014_longest-subsequence-repeated-k-times` |
| 2015 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2015_average-height-of-buildings-in-each-segment` |
| 2016 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2016_maximum-difference-between-increasing-elements` |
| 2017 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2017_grid-game` |
| 2018 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2018_check-if-word-can-be-placed-in-crossword` |
| 2019 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2019_the-score-of-students-solving-math-expression` |
| 2020 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2020_number-of-accounts-that-did-not-stream` |
| 2021 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2021_brightest-position-on-street` |
| 2022 | unverified | source_fidelity.json is missing | no | 3 | 1 | 0 | 0 | 0 | `dsa/leetcode/2022_convert-1d-array-into-2d-array` |
| 2023 | unverified | source_fidelity.json is missing | no | 3 | 2 | 0 | 0 | 0 | `dsa/leetcode/2023_number-of-pairs-of-strings-with-concatenation-equal-to-target` |
| 2024 | unverified | source_fidelity.json is missing | no | 3 | 1 | 0 | 0 | 0 | `dsa/leetcode/2024_maximize-the-confusion-of-an-exam` |
| 2025 | unverified | source_fidelity.json is missing | no | 3 | 2 | 0 | 0 | 0 | `dsa/leetcode/2025_maximum-number-of-ways-to-partition-an-array` |
| 2026 | unverified | source_fidelity.json is missing | no | 3 | 2 | 0 | 0 | 0 | `dsa/leetcode/2026_low-quality-problems` |
| 2027 | unverified | source_fidelity.json is missing | no | 3 | 1 | 0 | 0 | 0 | `dsa/leetcode/2027_minimum-moves-to-convert-string` |
| 2028 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2028_find-missing-observations` |
| 2029 | unverified | source_fidelity.json is missing | no | 3 | 2 | 0 | 0 | 0 | `dsa/leetcode/2029_stone-game-ix` |
| 2030 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2030_smallest-k-length-subsequence-with-occurrences-of-a-letter` |
| 2031 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2031_count-subarrays-with-more-ones-than-zeros` |
| 2032 | unverified | source_fidelity.json is missing | no | 3 | 1 | 0 | 0 | 0 | `dsa/leetcode/2032_two-out-of-three` |
| 2033 | unverified | source_fidelity.json is missing | no | 3 | 1 | 0 | 0 | 0 | `dsa/leetcode/2033_minimum-operations-to-make-a-uni-value-grid` |
| 2034 | unverified | source_fidelity.json is missing | no | 3 | 2 | 0 | 0 | 0 | `dsa/leetcode/2034_stock-price-fluctuation` |
| 2035 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2035_partition-array-into-two-arrays-to-minimize-sum-difference` |
| 2036 | unverified | source_fidelity.json is missing | no | 3 | 2 | 0 | 0 | 0 | `dsa/leetcode/2036_maximum-alternating-subarray-sum` |
| 2037 | unverified | source_fidelity.json is missing | no | 3 | 2 | 0 | 0 | 0 | `dsa/leetcode/2037_minimum-number-of-moves-to-seat-everyone` |
| 2038 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2038_remove-colored-pieces-if-both-neighbors-are-the-same-color` |
| 2039 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2039_the-time-when-the-network-becomes-idle` |
| 2040 | unverified | source_fidelity.json is missing | no | 3 | 2 | 0 | 0 | 0 | `dsa/leetcode/2040_kth-smallest-product-of-two-sorted-arrays` |
| 2041 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2041_accepted-candidates-from-the-interviews` |
| 2042 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2042_check-if-numbers-are-ascending-in-a-sentence` |
| 2043 | unverified | source_fidelity.json is missing | no | 3 | 1 | 0 | 0 | 0 | `dsa/leetcode/2043_simple-bank-system` |
| 2044 | unverified | source_fidelity.json is missing | no | 3 | 2 | 0 | 0 | 0 | `dsa/leetcode/2044_count-number-of-maximum-bitwise-or-subsets` |
| 2045 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2045_second-minimum-time-to-reach-destination` |
| 2046 | unverified | source_fidelity.json is missing | no | 3 | 1 | 0 | 0 | 0 | `dsa/leetcode/2046_sort-linked-list-already-sorted-using-absolute-values` |
| 2047 | unverified | source_fidelity.json is missing | no | 3 | 2 | 0 | 0 | 0 | `dsa/leetcode/2047_number-of-valid-words-in-a-sentence` |
| 2048 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2048_next-greater-numerically-balanced-number` |
| 2049 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2049_count-nodes-with-the-highest-score` |
| 2050 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2050_parallel-courses-iii` |
| 2051 | unverified | source_fidelity.json is missing | no | 1 | 0 | 0 | 0 | 0 | `dsa/leetcode/2051_the-category-of-each-member-in-the-store` |
| 2052 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2052_minimum-cost-to-separate-sentence-into-rows` |
| 2053 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2053_kth-distinct-string-in-an-array` |
| 2054 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2054_two-best-non-overlapping-events` |
| 2055 | unverified | source_fidelity.json is missing | no | 2 | 1 | 0 | 0 | 0 | `dsa/leetcode/2055_plates-between-candles` |
| 2056 | unverified | source_fidelity.json is missing | no | 3 | 1 | 0 | 0 | 0 | `dsa/leetcode/2056_number-of-valid-move-combinations-on-chessboard` |
| 2057 | unverified | source_fidelity.json is missing | no | 3 | 1 | 0 | 0 | 0 | `dsa/leetcode/2057_smallest-index-with-equal-value` |
| 2058 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2058_find-the-minimum-and-maximum-number-of-nodes-between-critical-points` |
| 2059 | unverified | source_fidelity.json is missing | no | 3 | 2 | 0 | 0 | 0 | `dsa/leetcode/2059_minimum-operations-to-convert-number` |
| 2060 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2060_check-if-an-original-string-exists-given-two-encoded-strings` |
| 2061 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2061_number-of-spaces-cleaning-robot-cleaned` |
| 2062 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2062_count-vowel-substrings-of-a-string` |
| 2063 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2063_vowels-of-all-substrings` |
| 2064 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2064_minimized-maximum-of-products-distributed-to-any-store` |
| 2065 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2065_maximum-path-quality-of-a-graph` |
| 2066 | unverified | source_fidelity.json is missing | no | 1 | 1 | 0 | 0 | 0 | `dsa/leetcode/2066_account-balance` |
| 2067 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2067_number-of-equal-count-substrings` |
| 2068 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2068_check-whether-two-strings-are-almost-equivalent` |
| 2069 | unverified | source_fidelity.json is missing | no | 1 | 1 | 0 | 0 | 0 | `dsa/leetcode/2069_walking-robot-simulation-ii` |
| 2070 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2070_most-beautiful-item-for-each-query` |
| 2071 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2071_maximum-number-of-tasks-you-can-assign` |
| 2072 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2072_the-winner-university` |
| 2073 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2073_time-needed-to-buy-tickets` |
| 2074 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2074_reverse-nodes-in-even-length-groups` |
| 2075 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2075_decode-the-slanted-ciphertext` |
| 2076 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2076_process-restricted-friend-requests` |
| 2077 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2077_paths-in-maze-that-lead-to-same-room` |
| 2078 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2078_two-furthest-houses-with-different-colors` |
| 2079 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2079_watering-plants` |
| 2080 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2080_range-frequency-queries` |
| 2081 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2081_sum-of-k-mirror-numbers` |
| 2082 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2082_the-number-of-rich-customers` |
| 2083 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2083_substrings-that-begin-and-end-with-the-same-letter` |
| 2084 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2084_drop-type-1-orders-for-customers-with-type-0-orders` |
| 2085 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2085_count-common-words-with-one-occurrence` |
| 2086 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2086_minimum-number-of-food-buckets-to-feed-the-hamsters` |
| 2087 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2087_minimum-cost-homecoming-of-a-robot-in-a-grid` |
| 2088 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2088_count-fertile-pyramids-in-a-land` |
| 2089 | unverified | source_fidelity.json is missing | no | 3 | 1 | 0 | 0 | 0 | `dsa/leetcode/2089_find-target-indices-after-sorting-array` |
| 2090 | unverified | source_fidelity.json is missing | no | 3 | 1 | 0 | 0 | 0 | `dsa/leetcode/2090_k-radius-subarray-averages` |
| 2091 | unverified | source_fidelity.json is missing | no | 3 | 2 | 0 | 0 | 0 | `dsa/leetcode/2091_removing-minimum-and-maximum-from-array` |
| 2092 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2092_find-all-people-with-secret` |
| 2093 | unverified | source_fidelity.json is missing | no | 3 | 2 | 0 | 0 | 0 | `dsa/leetcode/2093_minimum-cost-to-reach-city-with-discounts` |
| 2094 | unverified | source_fidelity.json is missing | no | 3 | 1 | 0 | 0 | 0 | `dsa/leetcode/2094_finding-3-digit-even-numbers` |
| 2095 | unverified | source_fidelity.json is missing | no | 3 | 2 | 0 | 0 | 0 | `dsa/leetcode/2095_delete-the-middle-node-of-a-linked-list` |
| 2096 | unverified | source_fidelity.json is missing | no | 2 | 1 | 0 | 0 | 0 | `dsa/leetcode/2096_step-by-step-directions-from-a-binary-tree-node-to-another` |
| 2097 | unverified | source_fidelity.json is missing | no | 3 | 1 | 0 | 0 | 0 | `dsa/leetcode/2097_valid-arrangement-of-pairs` |
| 2098 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2098_subsequence-of-size-k-with-the-largest-even-sum` |
| 2099 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2099_find-subsequence-of-length-k-with-the-largest-sum` |
| 2100 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2100_find-good-days-to-rob-the-bank` |
| 2101 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2101_detonate-the-maximum-bombs` |
| 2102 | unverified | source_fidelity.json is missing | no | 2 | 1 | 0 | 0 | 0 | `dsa/leetcode/2102_sequentially-ordinal-rank-tracker` |
| 2103 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2103_rings-and-rods` |
| 2104 | unverified | source_fidelity.json is missing | no | 3 | 2 | 0 | 0 | 0 | `dsa/leetcode/2104_sum-of-subarray-ranges` |
| 2105 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2105_watering-plants-ii` |
| 2106 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2106_maximum-fruits-harvested-after-at-most-k-steps` |
| 2107 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2107_number-of-unique-flavors-after-sharing-k-candies` |
| 2108 | unverified | source_fidelity.json is missing | no | 3 | 2 | 0 | 0 | 0 | `dsa/leetcode/2108_find-first-palindromic-string-in-the-array` |
| 2109 | unverified | source_fidelity.json is missing | no | 3 | 1 | 0 | 0 | 0 | `dsa/leetcode/2109_adding-spaces-to-a-string` |
| 2110 | unverified | source_fidelity.json is missing | no | 3 | 2 | 0 | 0 | 0 | `dsa/leetcode/2110_number-of-smooth-descent-periods-of-a-stock` |
| 2111 | unverified | source_fidelity.json is missing | no | 3 | 2 | 0 | 0 | 0 | `dsa/leetcode/2111_minimum-operations-to-make-the-array-k-increasing` |
| 2112 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2112_the-airport-with-the-most-traffic` |
| 2113 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2113_elements-in-array-after-removing-and-replacing-elements` |
| 2114 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2114_maximum-number-of-words-found-in-sentences` |
| 2115 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2115_find-all-possible-recipes-from-given-supplies` |
| 2116 | unverified | source_fidelity.json is missing | no | 4 | 0 | 0 | 0 | 0 | `dsa/leetcode/2116_check-if-a-parentheses-string-can-be-valid` |
| 2117 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2117_abbreviating-the-product-of-a-range` |
| 2118 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/2118_build-the-equation` |
| 2119 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2119_a-number-after-a-double-reversal` |
| 2120 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2120_execution-of-all-suffix-instructions-staying-in-a-grid` |
| 2121 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/2121_intervals-between-identical-elements` |
| 2122 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2122_recover-the-original-array` |
| 2123 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2123_minimum-operations-to-remove-adjacent-ones-in-matrix` |
| 2124 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2124_check-if-all-as-appears-before-all-bs` |
| 2125 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/2125_number-of-laser-beams-in-a-bank` |
| 2126 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/2126_destroying-asteroids` |
| 2127 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2127_maximum-employees-to-be-invited-to-a-meeting` |
| 2128 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2128_remove-all-ones-with-row-and-column-flips` |
| 2129 | unverified | source_fidelity.json is missing | no | 3 | 2 | 0 | 0 | 0 | `dsa/leetcode/2129_capitalize-the-title` |
| 2130 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2130_maximum-twin-sum-of-a-linked-list` |
| 2131 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2131_longest-palindrome-by-concatenating-two-letter-words` |
| 2132 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2132_stamping-the-grid` |
| 2133 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2133_check-if-every-row-and-column-contains-all-numbers` |
| 2134 | unverified | source_fidelity.json is missing | no | 3 | 1 | 0 | 0 | 0 | `dsa/leetcode/2134_minimum-swaps-to-group-all-1s-together-ii` |
| 2135 | unverified | source_fidelity.json is missing | no | 2 | 1 | 0 | 0 | 0 | `dsa/leetcode/2135_count-words-obtained-after-adding-a-letter` |
| 2136 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2136_earliest-possible-day-of-full-bloom` |
| 2137 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2137_pour-water-between-buckets-to-make-water-levels-equal` |
| 2138 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/2138_divide-a-string-into-groups-of-size-k` |
| 2139 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2139_minimum-moves-to-reach-target-score` |
| 2140 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2140_solving-questions-with-brainpower` |
| 2141 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2141_maximum-running-time-of-n-computers` |
| 2142 | unverified | source_fidelity.json is missing | no | 1 | 1 | 0 | 0 | 0 | `dsa/leetcode/2142_the-number-of-passengers-in-each-bus-i` |
| 2143 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2143_choose-numbers-from-two-arrays-in-range` |
| 2144 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2144_minimum-cost-of-buying-candies-with-discount` |
| 2145 | unverified | source_fidelity.json is missing | no | 3 | 1 | 0 | 0 | 0 | `dsa/leetcode/2145_count-the-hidden-sequences` |
| 2146 | unverified | source_fidelity.json is missing | no | 3 | 2 | 0 | 0 | 0 | `dsa/leetcode/2146_k-highest-ranked-items-within-a-price-range` |
| 2147 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2147_number-of-ways-to-divide-a-long-corridor` |
| 2148 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2148_count-elements-with-strictly-smaller-and-greater-elements` |
| 2149 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2149_rearrange-array-elements-by-sign` |
| 2150 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2150_find-all-lonely-numbers-in-the-array` |
| 2151 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2151_maximum-good-people-based-on-statements` |
| 2152 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2152_minimum-number-of-lines-to-cover-points` |
| 2153 | unverified | source_fidelity.json is missing | no | 1 | 1 | 0 | 0 | 0 | `dsa/leetcode/2153_the-number-of-passengers-in-each-bus-ii` |
| 2154 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2154_keep-multiplying-found-values-by-two` |
| 2155 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2155_all-divisions-with-the-highest-score-of-a-binary-array` |
| 2156 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2156_find-substring-with-given-hash-value` |
| 2157 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2157_groups-of-strings` |
| 2158 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2158_amount-of-new-area-painted-each-day` |
| 2159 | unverified | source_fidelity.json is missing | no | 1 | 0 | 0 | 2 | 0 | `dsa/leetcode/2159_order-two-columns-independently` |
| 2160 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2160_minimum-sum-of-four-digit-number-after-splitting-digits` |
| 2161 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2161_partition-array-according-to-given-pivot` |
| 2162 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2162_minimum-cost-to-set-cooking-time` |
| 2163 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2163_minimum-difference-in-sums-after-removal-of-elements` |
| 2164 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2164_sort-even-and-odd-indices-independently` |
| 2165 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2165_smallest-value-of-the-rearranged-number` |
| 2166 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2166_design-bitset` |
| 2167 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2167_minimum-time-to-remove-all-cars-containing-illegal-goods` |
| 2168 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2168_unique-substrings-with-equal-digit-frequency` |
| 2169 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2169_count-operations-to-obtain-zero` |
| 2170 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2170_minimum-operations-to-make-the-array-alternating` |
| 2171 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2171_removing-minimum-number-of-magic-beans` |
| 2172 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2172_maximum-and-sum-of-array` |
| 2173 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2173_longest-winning-streak` |
| 2174 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2174_remove-all-ones-with-row-and-column-flips-ii` |
| 2175 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2175_the-change-in-global-rankings` |
| 2176 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2176_count-equal-and-divisible-pairs-in-an-array` |
| 2177 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2177_find-three-consecutive-integers-that-sum-to-a-given-number` |
| 2178 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2178_maximum-split-of-positive-even-integers` |
| 2179 | unverified | source_fidelity.json is missing | no | 3 | 1 | 0 | 0 | 0 | `dsa/leetcode/2179_count-good-triplets-in-an-array` |
| 2180 | unverified | source_fidelity.json is missing | no | 3 | 1 | 0 | 0 | 0 | `dsa/leetcode/2180_count-integers-with-even-digit-sum` |
| 2181 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2181_merge-nodes-in-between-zeros` |
| 2182 | unverified | source_fidelity.json is missing | no | 3 | 1 | 0 | 0 | 0 | `dsa/leetcode/2182_construct-string-with-repeat-limit` |
| 2183 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2183_count-array-pairs-divisible-by-k` |
| 2184 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2184_number-of-ways-to-build-sturdy-brick-wall` |
| 2185 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2185_counting-words-with-a-given-prefix` |
| 2186 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2186_minimum-number-of-steps-to-make-two-strings-anagram-ii` |
| 2187 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2187_minimum-time-to-complete-trips` |
| 2188 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2188_minimum-time-to-finish-the-race` |
| 2189 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2189_number-of-ways-to-build-house-of-cards` |
| 2190 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2190_most-frequent-number-following-key-in-an-array` |
| 2191 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2191_sort-the-jumbled-numbers` |
| 2192 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2192_all-ancestors-of-a-node-in-a-directed-acyclic-graph` |
| 2193 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2193_minimum-number-of-moves-to-make-palindrome` |
| 2194 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2194_cells-in-a-range-on-an-excel-sheet` |
| 2195 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2195_append-k-integers-with-minimal-sum` |
| 2196 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2196_create-binary-tree-from-descriptions` |
| 2197 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/2197_replace-non-coprime-numbers-in-array` |
| 2198 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2198_number-of-single-divisor-triplets` |
| 2199 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2199_finding-the-topic-of-each-post` |
| 2200 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/2200_find-all-k-distant-indices-in-an-array` |
| 2201 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/2201_count-artifacts-that-can-be-extracted` |
| 2202 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/2202_maximize-the-topmost-element-after-k-moves` |
| 2203 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/2203_minimum-weighted-subgraph-with-the-required-paths` |
| 2204 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/2204_distance-to-a-cycle-in-undirected-graph` |
| 2205 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2205_the-number-of-users-that-are-eligible-for-discount` |
| 2206 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2206_divide-array-into-equal-pairs` |
| 2207 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2207_maximize-number-of-subsequences-in-a-string` |
| 2208 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2208_minimum-operations-to-halve-array-sum` |
| 2209 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2209_minimum-white-tiles-after-covering-with-carpets` |
| 2210 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2210_count-hills-and-valleys-in-an-array` |
| 2211 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2211_count-collisions-on-a-road` |
| 2212 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2212_maximum-points-in-an-archery-competition` |
| 2213 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2213_longest-substring-of-one-repeating-character` |
| 2214 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2214_minimum-health-to-beat-game` |
| 2215 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2215_find-the-difference-of-two-arrays` |
| 2216 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2216_minimum-deletions-to-make-array-beautiful` |
| 2217 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2217_find-palindrome-with-fixed-length` |
| 2218 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2218_maximum-value-of-k-coins-from-piles` |
| 2219 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2219_maximum-sum-score-of-array` |
| 2220 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2220_minimum-bit-flips-to-convert-number` |
| 2221 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2221_find-triangular-sum-of-an-array` |
| 2222 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2222_number-of-ways-to-select-buildings` |
| 2223 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2223_sum-of-scores-of-built-strings` |
| 2224 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2224_minimum-number-of-operations-to-convert-time` |
| 2225 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2225_find-players-with-zero-or-one-losses` |
| 2226 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2226_maximum-candies-allocated-to-k-children` |
| 2227 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2227_encrypt-and-decrypt-strings` |
| 2228 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2228_users-with-two-purchases-within-seven-days` |
| 2229 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2229_check-if-an-array-is-consecutive` |
| 2230 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2230_the-users-that-are-eligible-for-discount` |
| 2231 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2231_largest-number-after-digit-swaps-by-parity` |
| 2232 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2232_minimize-result-by-adding-parentheses-to-expression` |
| 2233 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2233_maximum-product-after-k-increments` |
| 2234 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2234_maximum-total-beauty-of-the-gardens` |
| 2235 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2235_add-two-integers` |
| 2236 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2236_root-equals-sum-of-children` |
| 2237 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2237_count-positions-on-street-with-required-brightness` |
| 2238 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2238_number-of-times-a-driver-was-a-passenger` |
| 2239 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2239_find-closest-number-to-zero` |
| 2240 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2240_number-of-ways-to-buy-pens-and-pencils` |
| 2241 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2241_design-an-atm-machine` |
| 2242 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2242_maximum-score-of-a-node-sequence` |
| 2243 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2243_calculate-digit-sum-of-a-string` |
| 2244 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2244_minimum-rounds-to-complete-all-tasks` |
| 2245 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2245_maximum-trailing-zeros-in-a-cornered-path` |
| 2246 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2246_longest-path-with-different-adjacent-characters` |
| 2247 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2247_maximum-cost-of-trip-with-k-highways` |
| 2248 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2248_intersection-of-multiple-arrays` |
| 2249 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2249_count-lattice-points-inside-a-circle` |
| 2250 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2250_count-number-of-rectangles-containing-each-point` |
| 2251 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2251_number-of-flowers-in-full-bloom` |
| 2252 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2252_dynamic-pivoting-of-a-table` |
| 2253 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2253_dynamic-unpivoting-of-a-table` |
| 2254 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2254_design-video-sharing-platform` |
| 2255 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2255_count-prefixes-of-a-given-string` |
| 2256 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2256_minimum-average-difference` |
| 2257 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2257_count-unguarded-cells-in-the-grid` |
| 2258 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2258_escape-the-spreading-fire` |
| 2259 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2259_remove-digit-from-number-to-maximize-result` |
| 2260 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2260_minimum-consecutive-cards-to-pick-up` |
| 2261 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2261_k-divisible-elements-subarrays` |
| 2262 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2262_total-appeal-of-a-string` |
| 2263 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2263_make-array-non-decreasing-or-non-increasing` |
| 2264 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2264_largest-3-same-digit-number-in-string` |
| 2265 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/2265_count-nodes-equal-to-average-of-subtree` |
| 2266 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/2266_count-number-of-texts` |
| 2267 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/2267_check-if-there-is-a-valid-parentheses-string-path` |
| 2268 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/2268_minimum-number-of-keypresses` |
| 2269 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/2269_find-the-k-beauty-of-a-number` |
| 2270 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/2270_number-of-ways-to-split-array` |
| 2271 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/2271_maximum-white-tiles-covered-by-a-carpet` |
| 2272 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/2272_substring-with-largest-variance` |
| 2273 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2273_find-resultant-array-after-removing-anagrams` |
| 2274 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2274_maximum-consecutive-floors-without-special-floors` |
| 2275 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2275_largest-combination-with-bitwise-and-greater-than-zero` |
| 2276 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2276_count-integers-in-intervals` |
| 2277 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2277_closest-node-to-path-in-tree` |
| 2278 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2278_percentage-of-letter-in-string` |
| 2279 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2279_maximum-bags-with-full-capacity-of-rocks` |
| 2280 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2280_minimum-lines-to-represent-a-line-chart` |
| 2281 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2281_sum-of-total-strength-of-wizards` |
| 2282 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2282_number-of-people-that-can-be-seen-in-a-grid` |
| 2283 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2283_check-if-number-has-equal-digit-count-and-digit-value` |
| 2284 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2284_sender-with-largest-word-count` |
| 2285 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2285_maximum-total-importance-of-roads` |
| 2286 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2286_booking-concert-tickets-in-groups` |
| 2287 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2287_rearrange-characters-to-make-target-string` |
| 2288 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/2288_apply-discount-to-prices` |
| 2289 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/2289_steps-to-make-array-non-decreasing` |
| 2290 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/2290_minimum-obstacle-removal-to-reach-corner` |
| 2291 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2291_maximum-profit-from-trading-stocks` |
| 2292 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2292_products-with-three-or-more-orders-in-two-consecutive-years` |
| 2293 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/2293_min-max-game` |
| 2294 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2294_partition-array-such-that-maximum-difference-is-k` |
| 2295 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/2295_replace-elements-in-an-array` |
| 2296 | unverified | source_fidelity.json is missing | no | 1 | 0 | 0 | 0 | 0 | `dsa/leetcode/2296_design-a-text-editor` |
| 2297 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2297_jump-game-viii` |
| 2298 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2298_tasks-count-in-the-weekend` |
| 2299 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2299_strong-password-checker-ii` |
| 2300 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/2300_successful-pairs-of-spells-and-potions` |
| 2301 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2301_match-substring-after-replacement` |
| 2302 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2302_count-subarrays-with-score-less-than-k` |
| 2303 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2303_calculate-amount-paid-in-taxes` |
| 2304 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2304_minimum-path-cost-in-a-grid` |
| 2305 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2305_fair-distribution-of-cookies` |
| 2306 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2306_naming-a-company` |
| 2307 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/2307_check-for-contradictions-in-equations` |
| 2308 | unverified | source_fidelity.json is missing | no | 1 | 0 | 0 | 0 | 0 | `dsa/leetcode/2308_arrange-table-by-gender` |
| 2309 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2309_greatest-english-letter-in-upper-and-lower-case` |
| 2310 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2310_sum-of-numbers-with-units-digit-k` |
| 2311 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2311_longest-binary-subsequence-less-than-or-equal-to-k` |
| 2312 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2312_selling-pieces-of-wood` |
| 2313 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/2313_minimum-flips-in-binary-tree-to-get-result` |
| 2314 | unverified | source_fidelity.json is missing | no | 1 | 0 | 0 | 0 | 0 | `dsa/leetcode/2314_the-first-day-of-the-maximum-recorded-degree-in-each-city` |
| 2315 | unverified | source_fidelity.json is missing | no | 3 | 1 | 0 | 0 | 0 | `dsa/leetcode/2315_count-asterisks` |
| 2316 | unverified | source_fidelity.json is missing | no | 2 | 1 | 0 | 0 | 0 | `dsa/leetcode/2316_count-unreachable-pairs-of-nodes-in-an-undirected-graph` |
| 2317 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2317_maximum-xor-after-operations` |
| 2318 | unverified | source_fidelity.json is missing | no | 2 | 1 | 0 | 0 | 0 | `dsa/leetcode/2318_number-of-distinct-roll-sequences` |
| 2319 | unverified | source_fidelity.json is missing | no | 2 | 1 | 0 | 0 | 0 | `dsa/leetcode/2319_check-if-matrix-is-x-matrix` |
| 2320 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2320_count-number-of-ways-to-place-houses` |
| 2321 | unverified | source_fidelity.json is missing | no | 3 | 1 | 0 | 0 | 0 | `dsa/leetcode/2321_maximum-score-of-spliced-array` |
| 2322 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2322_minimum-score-after-removals-on-a-tree` |
| 2323 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/2323_find-minimum-time-to-finish-all-jobs-ii` |
| 2324 | unverified | source_fidelity.json is missing | no | 1 | 0 | 0 | 0 | 0 | `dsa/leetcode/2324_product-sales-analysis-iv` |
| 2325 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2325_decode-the-message` |
| 2326 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2326_spiral-matrix-iv` |
| 2327 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2327_number-of-people-aware-of-a-secret` |
| 2328 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2328_number-of-increasing-paths-in-a-grid` |
| 2329 | unverified | source_fidelity.json is missing | no | 1 | 0 | 0 | 0 | 0 | `dsa/leetcode/2329_product-sales-analysis-v` |
| 2330 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2330_valid-palindrome-iv` |
| 2331 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2331_evaluate-boolean-binary-tree` |
| 2332 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2332_the-latest-time-to-catch-a-bus` |
| 2333 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2333_minimum-sum-of-squared-difference` |
| 2334 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2334_subarray-with-elements-greater-than-varying-threshold` |
| 2335 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2335_minimum-amount-of-time-to-fill-cups` |
| 2336 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2336_smallest-number-in-infinite-set` |
| 2337 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2337_move-pieces-to-obtain-a-string` |
| 2338 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2338_count-the-number-of-ideal-arrays` |
| 2339 | unverified | source_fidelity.json is missing | no | 1 | 0 | 0 | 0 | 0 | `dsa/leetcode/2339_all-the-matches-of-the-league` |
| 2340 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/2340_minimum-adjacent-swaps-to-make-a-valid-array` |
| 2341 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2341_maximum-number-of-pairs-in-array` |
| 2342 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2342_max-sum-of-a-pair-with-equal-sum-of-digits` |
| 2343 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2343_query-kth-smallest-trimmed-number` |
| 2344 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2344_minimum-deletions-to-make-array-divisible` |
| 2345 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/2345_finding-the-number-of-visible-mountains` |
| 2346 | unverified | source_fidelity.json is missing | no | 1 | 0 | 0 | 0 | 0 | `dsa/leetcode/2346_compute-the-rank-as-a-percentage` |
| 2347 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2347_best-poker-hand` |
| 2348 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2348_number-of-zero-filled-subarrays` |
| 2349 | unverified | source_fidelity.json is missing | no | 1 | 1 | 0 | 0 | 0 | `dsa/leetcode/2349_design-a-number-container-system` |
| 2350 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2350_shortest-impossible-sequence-of-rolls` |
| 2351 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2351_first-letter-to-appear-twice` |
| 2352 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2352_equal-row-and-column-pairs` |
| 2353 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2353_design-a-food-rating-system` |
| 2354 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2354_number-of-excellent-pairs` |
| 2355 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2355_maximum-number-of-books-you-can-take` |
| 2356 | unverified | source_fidelity.json is missing | no | 1 | 0 | 0 | 1 | 0 | `dsa/leetcode/2356_number-of-unique-subjects-taught-by-each-teacher` |
| 2357 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/2357_make-array-zero-by-subtracting-equal-amounts` |
| 2358 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/2358_maximum-number-of-groups-entering-a-competition` |
| 2359 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/2359_find-closest-node-to-given-two-nodes` |
| 2360 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/2360_longest-cycle-in-a-graph` |
| 2361 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/2361_minimum-costs-using-the-train-line` |
| 2362 | unverified | source_fidelity.json is missing | no | 1 | 0 | 0 | 0 | 0 | `dsa/leetcode/2362_generate-the-invoice` |
| 2363 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2363_merge-similar-items` |
| 2364 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/2364_count-number-of-bad-pairs` |
| 2365 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/2365_task-scheduler-ii` |
| 2366 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/2366_minimum-replacements-to-sort-the-array` |
| 2367 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/2367_number-of-arithmetic-triplets` |
| 2368 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/2368_reachable-nodes-with-restrictions` |
| 2369 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2369_check-if-there-is-a-valid-partition-for-the-array` |
| 2370 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2370_longest-ideal-subsequence` |
| 2371 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2371_minimize-maximum-value-in-a-grid` |
| 2372 | unverified | source_fidelity.json is missing | no | 1 | 1 | 0 | 0 | 0 | `dsa/leetcode/2372_calculate-the-influence-of-each-salesperson` |
| 2373 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2373_largest-local-values-in-a-matrix` |
| 2374 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2374_node-with-highest-edge-score` |
| 2375 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2375_construct-smallest-number-from-di-string` |
| 2376 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2376_count-special-integers` |
| 2377 | unverified | source_fidelity.json is missing | no | 1 | 1 | 0 | 0 | 0 | `dsa/leetcode/2377_sort-the-olympic-table` |
| 2378 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2378_choose-edges-to-maximize-score-in-a-tree` |
| 2379 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2379_minimum-recolors-to-get-k-consecutive-black-blocks` |
| 2380 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2380_time-needed-to-rearrange-a-binary-string` |
| 2381 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2381_shifting-letters-ii` |
| 2382 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2382_maximum-segment-sum-after-removals` |
| 2383 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2383_minimum-hours-of-training-to-win-a-competition` |
| 2384 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2384_largest-palindromic-number` |
| 2385 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2385_amount-of-time-for-binary-tree-to-be-infected` |
| 2386 | unverified | source_fidelity.json is missing | no | 2 | 1 | 0 | 0 | 0 | `dsa/leetcode/2386_find-the-k-sum-of-an-array` |
| 2387 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/2387_median-of-a-row-wise-sorted-matrix` |
| 2388 | unverified | source_fidelity.json is missing | no | 1 | 0 | 0 | 0 | 0 | `dsa/leetcode/2388_change-null-values-in-a-table-to-the-previous-value` |
| 2389 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/2389_longest-subsequence-with-limited-sum` |
| 2390 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/2390_removing-stars-from-a-string` |
| 2391 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/2391_minimum-amount-of-time-to-collect-garbage` |
| 2392 | unverified | source_fidelity.json is missing | no | 2 | 1 | 0 | 0 | 0 | `dsa/leetcode/2392_build-a-matrix-with-conditions` |
| 2393 | unverified | source_fidelity.json is missing | no | 2 | 1 | 0 | 0 | 0 | `dsa/leetcode/2393_count-strictly-increasing-subarrays` |
| 2394 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 1 | 0 | `dsa/leetcode/2394_employees-with-deductions` |
| 2395 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2395_find-subarrays-with-equal-sum` |
| 2396 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2396_strictly-palindromic-number` |
| 2397 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2397_maximum-rows-covered-by-columns` |
| 2398 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2398_maximum-number-of-robots-within-budget` |
| 2399 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2399_check-distances-between-same-letters` |
| 2400 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2400_number-of-ways-to-reach-a-position-after-exactly-k-steps` |
| 2401 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2401_longest-nice-subarray` |
| 2402 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2402_meeting-rooms-iii` |
| 2403 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2403_minimum-time-to-kill-all-monsters` |
| 2404 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2404_most-frequent-even-element` |
| 2405 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2405_optimal-partition-of-string` |
| 2406 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2406_divide-intervals-into-minimum-number-of-groups` |
| 2407 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2407_longest-increasing-subsequence-ii` |
| 2408 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2408_design-sql` |
| 2409 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2409_count-days-spent-together` |
| 2410 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2410_maximum-matching-of-players-with-trainers` |
| 2411 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2411_smallest-subarrays-with-maximum-bitwise-or` |
| 2412 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2412_minimum-money-required-before-transactions` |
| 2413 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2413_smallest-even-multiple` |
| 2414 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2414_length-of-the-longest-alphabetical-continuous-substring` |
| 2415 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2415_reverse-odd-levels-of-binary-tree` |
| 2416 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2416_sum-of-prefix-scores-of-strings` |
| 2417 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2417_closest-fair-integer` |
| 2418 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2418_sort-the-people` |
| 2419 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2419_longest-subarray-with-maximum-bitwise-and` |
| 2420 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2420_find-all-good-indices` |
| 2421 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2421_number-of-good-paths` |
| 2422 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2422_merge-operations-to-turn-array-into-a-palindrome` |
| 2423 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2423_remove-letter-to-equalize-frequency` |
| 2424 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2424_longest-uploaded-prefix` |
| 2425 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2425_bitwise-xor-of-all-pairings` |
| 2426 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2426_number-of-pairs-satisfying-inequality` |
| 2427 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2427_number-of-common-factors` |
| 2428 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2428_maximum-sum-of-an-hourglass` |
| 2429 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2429_minimize-xor` |
| 2430 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2430_maximum-deletions-on-a-string` |
| 2431 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2431_maximize-total-tastiness-of-purchased-fruits` |
| 2432 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2432_the-employee-that-worked-on-the-longest-task` |
| 2433 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2433_find-the-original-array-of-prefix-xor` |
| 2434 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2434_using-a-robot-to-print-the-lexicographically-smallest-string` |
| 2435 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2435_paths-in-matrix-whose-sum-is-divisible-by-k` |
| 2436 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2436_minimum-split-into-subarrays-with-gcd-greater-than-one` |
| 2437 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2437_number-of-valid-clock-times` |
| 2438 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2438_range-product-queries-of-powers` |
| 2439 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2439_minimize-maximum-of-array` |
| 2440 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2440_create-components-with-same-value` |
| 2441 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2441_largest-positive-integer-that-exists-with-its-negative` |
| 2442 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2442_count-number-of-distinct-integers-after-reverse-operations` |
| 2443 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2443_sum-of-number-and-its-reverse` |
| 2444 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2444_count-subarrays-with-fixed-bounds` |
| 2445 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2445_number-of-nodes-with-value-one` |
| 2446 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2446_determine-if-two-events-have-conflict` |
| 2447 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2447_number-of-subarrays-with-gcd-equal-to-k` |
| 2448 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2448_minimum-cost-to-make-array-equal` |
| 2449 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2449_minimum-number-of-operations-to-make-arrays-similar` |
| 2450 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2450_number-of-distinct-binary-strings-after-applying-operations` |
| 2451 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2451_odd-string-difference` |
| 2452 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2452_words-within-two-edits-of-dictionary` |
| 2453 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2453_destroy-sequential-targets` |
| 2454 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2454_next-greater-element-iv` |
| 2455 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2455_average-value-of-even-numbers-that-are-divisible-by-three` |
| 2456 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2456_most-popular-video-creator` |
| 2457 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2457_minimum-addition-to-make-integer-beautiful` |
| 2458 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2458_height-of-binary-tree-after-subtree-removal-queries` |
| 2459 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2459_sort-array-by-moving-items-to-empty-space` |
| 2460 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2460_apply-operations-to-an-array` |
| 2461 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2461_maximum-sum-of-distinct-subarrays-with-length-k` |
| 2462 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2462_total-cost-to-hire-k-workers` |
| 2463 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2463_minimum-total-distance-traveled` |
| 2464 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2464_minimum-subarrays-in-a-valid-split` |
| 2465 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2465_number-of-distinct-averages` |
| 2466 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2466_count-ways-to-build-good-strings` |
| 2467 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2467_most-profitable-path-in-a-tree` |
| 2468 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2468_split-message-based-on-limit` |
| 2469 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2469_convert-the-temperature` |
| 2470 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2470_number-of-subarrays-with-lcm-equal-to-k` |
| 2471 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2471_minimum-number-of-operations-to-sort-a-binary-tree-by-level` |
| 2472 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2472_maximum-number-of-non-overlapping-palindrome-substrings` |
| 2473 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2473_minimum-cost-to-buy-apples` |
| 2474 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2474_customers-with-strictly-increasing-purchases` |
| 2475 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2475_number-of-unequal-triplets-in-array` |
| 2476 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2476_closest-nodes-queries-in-a-binary-search-tree` |
| 2477 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2477_minimum-fuel-cost-to-report-to-the-capital` |
| 2478 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2478_number-of-beautiful-partitions` |
| 2479 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2479_maximum-xor-of-two-non-overlapping-subtrees` |
| 2480 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2480_form-a-chemical-bond` |
| 2481 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2481_minimum-cuts-to-divide-a-circle` |
| 2482 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2482_difference-between-ones-and-zeros-in-row-and-column` |
| 2483 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2483_minimum-penalty-for-a-shop` |
| 2484 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2484_count-palindromic-subsequences` |
| 2485 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2485_find-the-pivot-integer` |
| 2486 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2486_append-characters-to-string-to-make-subsequence` |
| 2487 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2487_remove-nodes-from-linked-list` |
| 2488 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2488_count-subarrays-with-median-k` |
| 2489 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2489_number-of-substrings-with-fixed-ratio` |
| 2490 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2490_circular-sentence` |
| 2491 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2491_divide-players-into-teams-of-equal-skill` |
| 2492 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2492_minimum-score-of-a-path-between-two-cities` |
| 2493 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2493_divide-nodes-into-the-maximum-number-of-groups` |
| 2494 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2494_merge-overlapping-events-in-the-same-hall` |
| 2495 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2495_number-of-subarrays-having-even-product` |
| 2496 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2496_maximum-value-of-a-string-in-an-array` |
| 2497 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2497_maximum-star-sum-of-a-graph` |
| 2498 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2498_frog-jump-ii` |
| 2499 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2499_minimum-total-cost-to-make-arrays-unequal` |
| 2500 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2500_delete-greatest-value-in-each-row` |
| 2501 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2501_longest-square-streak-in-an-array` |
| 2502 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2502_design-memory-allocator` |
| 2503 | unverified | source_fidelity.json is missing | no | 3 | 2 | 0 | 0 | 0 | `dsa/leetcode/2503_maximum-number-of-points-from-grid-queries` |
| 2504 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2504_concatenate-the-name-and-the-profession` |
| 2505 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2505_bitwise-or-of-all-subsequence-sums` |
| 2506 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2506_count-pairs-of-similar-strings` |
| 2507 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2507_smallest-value-after-replacing-with-sum-of-prime-factors` |
| 2508 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2508_add-edges-to-make-degrees-of-all-nodes-even` |
| 2509 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2509_cycle-length-queries-in-a-tree` |
| 2510 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2510_check-if-there-is-a-path-with-equal-number-of-0s-and-1s` |
| 2511 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2511_maximum-enemy-forts-that-can-be-captured` |
| 2512 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2512_reward-top-k-students` |
| 2513 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2513_minimize-the-maximum-of-two-arrays` |
| 2514 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2514_count-anagrams` |
| 2515 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2515_shortest-distance-to-target-string-in-a-circular-array` |
| 2516 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2516_take-k-of-each-character-from-left-and-right` |
| 2517 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2517_maximum-tastiness-of-candy-basket` |
| 2518 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2518_number-of-great-partitions` |
| 2519 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2519_count-the-number-of-k-big-indices` |
| 2520 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2520_count-the-digits-that-divide-a-number` |
| 2521 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2521_distinct-prime-factors-of-product-of-array` |
| 2522 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2522_partition-string-into-substrings-with-values-at-most-k` |
| 2523 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2523_closest-prime-numbers-in-range` |
| 2524 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2524_maximum-frequency-score-of-a-subarray` |
| 2525 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2525_categorize-box-according-to-criteria` |
| 2526 | unverified | source_fidelity.json is missing | no | 1 | 1 | 0 | 0 | 0 | `dsa/leetcode/2526_find-consecutive-integers-from-a-data-stream` |
| 2527 | unverified | source_fidelity.json is missing | no | 2 | 1 | 0 | 0 | 0 | `dsa/leetcode/2527_find-xor-beauty-of-array` |
| 2528 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2528_maximize-the-minimum-powered-city` |
| 2529 | unverified | source_fidelity.json is missing | no | 3 | 2 | 0 | 0 | 0 | `dsa/leetcode/2529_maximum-count-of-positive-integer-and-negative-integer` |
| 2530 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2530_maximal-score-after-applying-k-operations` |
| 2531 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2531_make-number-of-distinct-characters-equal` |
| 2532 | unverified | source_fidelity.json is missing | no | 2 | 1 | 0 | 0 | 0 | `dsa/leetcode/2532_time-to-cross-a-bridge` |
| 2533 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2533_number-of-good-binary-strings` |
| 2534 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2534_time-taken-to-cross-the-door` |
| 2535 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2535_difference-between-element-sum-and-digit-sum-of-an-array` |
| 2536 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/2536_increment-submatrices-by-one` |
| 2537 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2537_count-the-number-of-good-subarrays` |
| 2538 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2538_difference-between-maximum-and-minimum-price-sum` |
| 2539 | unverified | source_fidelity.json is missing | no | 3 | 2 | 0 | 0 | 0 | `dsa/leetcode/2539_count-the-number-of-good-subsequences` |
| 2540 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2540_minimum-common-value` |
| 2541 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2541_minimum-operations-to-make-array-equal-ii` |
| 2542 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2542_maximum-subsequence-score` |
| 2543 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2543_check-if-point-is-reachable` |
| 2544 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2544_alternating-digit-sum` |
| 2545 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2545_sort-the-students-by-their-kth-score` |
| 2546 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2546_apply-bitwise-operations-to-make-strings-equal` |
| 2547 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2547_minimum-cost-to-split-an-array` |
| 2548 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2548_maximum-price-to-fill-a-bag` |
| 2549 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2549_count-distinct-numbers-on-board` |
| 2550 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2550_count-collisions-of-monkeys-on-a-polygon` |
| 2551 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2551_put-marbles-in-bags` |
| 2552 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2552_count-increasing-quadruplets` |
| 2553 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2553_separate-the-digits-in-an-array` |
| 2554 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2554_maximum-number-of-integers-to-choose-from-a-range-i` |
| 2555 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2555_maximize-win-from-two-segments` |
| 2556 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2556_disconnect-path-in-a-binary-matrix-by-at-most-one-flip` |
| 2557 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2557_maximum-number-of-integers-to-choose-from-a-range-ii` |
| 2558 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2558_take-gifts-from-the-richest-pile` |
| 2559 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2559_count-vowel-strings-in-ranges` |
| 2560 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2560_house-robber-iv` |
| 2561 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2561_rearranging-fruits` |
| 2562 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2562_find-the-array-concatenation-value` |
| 2563 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2563_count-the-number-of-fair-pairs` |
| 2564 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2564_substring-xor-queries` |
| 2565 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2565_subsequence-with-the-minimum-score` |
| 2566 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2566_maximum-difference-by-remapping-a-digit` |
| 2567 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2567_minimum-score-by-changing-two-elements` |
| 2568 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2568_minimum-impossible-or` |
| 2569 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2569_handling-sum-queries-after-update` |
| 2570 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2570_merge-two-2d-arrays-by-summing-values` |
| 2571 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2571_minimum-operations-to-reduce-an-integer-to-0` |
| 2572 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2572_count-the-number-of-square-free-subsets` |
| 2573 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2573_find-the-string-with-lcp` |
| 2574 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2574_left-and-right-sum-differences` |
| 2575 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2575_find-the-divisibility-array-of-a-string` |
| 2576 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2576_find-the-maximum-number-of-marked-indices` |
| 2577 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2577_minimum-time-to-visit-a-cell-in-a-grid` |
| 2578 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2578_split-with-minimum-sum` |
| 2579 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2579_count-total-number-of-colored-cells` |
| 2580 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2580_count-ways-to-group-overlapping-ranges` |
| 2581 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2581_count-number-of-possible-root-nodes` |
| 2582 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2582_pass-the-pillow` |
| 2583 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2583_kth-largest-sum-in-a-binary-tree` |
| 2584 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2584_split-the-array-to-make-coprime-products` |
| 2585 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2585_number-of-ways-to-earn-points` |
| 2586 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/2586_count-the-number-of-vowel-strings-in-range` |
| 2587 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/2587_rearrange-array-to-maximize-prefix-score` |
| 2588 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/2588_count-the-number-of-beautiful-subarrays` |
| 2589 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/2589_minimum-time-to-complete-all-tasks` |
| 2590 | unverified | source_fidelity.json is missing | no | 1 | 0 | 0 | 0 | 0 | `dsa/leetcode/2590_design-a-todo-list` |
| 2591 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/2591_distribute-money-to-maximum-children` |
| 2592 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/2592_maximize-greatness-of-an-array` |
| 2593 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/2593_find-score-of-an-array-after-marking-all-elements` |
| 2594 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/2594_minimum-time-to-repair-cars` |
| 2595 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/2595_number-of-even-and-odd-bits` |
| 2596 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/2596_check-knight-tour-configuration` |
| 2597 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/2597_the-number-of-beautiful-subsets` |
| 2598 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/2598_smallest-missing-non-negative-integer-after-operations` |
| 2599 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/2599_make-the-prefix-sum-non-negative` |
| 2600 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/2600_k-items-with-the-maximum-sum` |
| 2601 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2601_prime-subtraction-operation` |
| 2602 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/2602_minimum-operations-to-make-all-array-elements-equal` |
| 2603 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/2603_collect-coins-in-a-tree` |
| 2604 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/2604_minimum-time-to-eat-all-grains` |
| 2605 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/2605_form-smallest-number-from-two-digit-arrays` |
| 2606 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/2606_find-the-substring-with-maximum-cost` |
| 2607 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/2607_make-k-subarray-sums-equal` |
| 2608 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/2608_shortest-cycle-in-a-graph` |
| 2609 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2609_find-the-longest-balanced-substring-of-a-binary-string` |
| 2610 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2610_convert-an-array-into-a-2d-array-with-conditions` |
| 2611 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2611_mice-and-cheese` |
| 2612 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2612_minimum-reverse-operations` |
| 2613 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2613_beautiful-pairs` |
| 2614 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2614_prime-in-diagonal` |
| 2615 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2615_sum-of-distances` |
| 2616 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2616_minimize-the-maximum-difference-of-pairs` |
| 2617 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2617_minimum-number-of-visited-cells-in-a-grid` |
| 2618 | unverified | source_fidelity.json is missing | no | 4 | 4 | 0 | 0 | 0 | `dsa/leetcode/2618_check-if-object-instance-of-class` |
| 2619 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2619_array-prototype-last` |
| 2620 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2620_counter` |
| 2621 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2621_sleep` |
| 2622 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2622_cache-with-time-limit` |
| 2623 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2623_memoize` |
| 2624 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2624_snail-traversal` |
| 2625 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2625_flatten-deeply-nested-array` |
| 2626 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2626_array-reduce-transformation` |
| 2627 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2627_debounce` |
| 2628 | unverified | source_fidelity.json is missing | no | 4 | 4 | 0 | 0 | 0 | `dsa/leetcode/2628_json-deep-equal` |
| 2629 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2629_function-composition` |
| 2630 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2630_memoize-ii` |
| 2631 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2631_group-by` |
| 2632 | unverified | source_fidelity.json is missing | no | 4 | 4 | 0 | 0 | 0 | `dsa/leetcode/2632_curry` |
| 2633 | unverified | source_fidelity.json is missing | no | 4 | 4 | 0 | 0 | 0 | `dsa/leetcode/2633_convert-object-to-json-string` |
| 2634 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2634_filter-elements-from-array` |
| 2635 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2635_apply-transform-over-each-element-in-array` |
| 2636 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2636_promise-pool` |
| 2637 | unverified | source_fidelity.json is missing | no | 4 | 4 | 0 | 0 | 0 | `dsa/leetcode/2637_promise-time-limit` |
| 2638 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2638_count-the-number-of-k-free-subsets` |
| 2639 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2639_find-the-width-of-columns-of-a-grid` |
| 2640 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2640_find-the-score-of-all-prefixes-of-an-array` |
| 2641 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2641_cousins-in-binary-tree-ii` |
| 2642 | unverified | source_fidelity.json is missing | no | 1 | 1 | 0 | 0 | 0 | `dsa/leetcode/2642_design-graph-with-shortest-path-calculator` |
| 2643 | unverified | source_fidelity.json is missing | no | 3 | 1 | 0 | 0 | 0 | `dsa/leetcode/2643_row-with-maximum-ones` |
| 2644 | unverified | source_fidelity.json is missing | no | 3 | 1 | 0 | 0 | 0 | `dsa/leetcode/2644_find-the-maximum-divisibility-score` |
| 2645 | unverified | source_fidelity.json is missing | no | 3 | 2 | 0 | 0 | 0 | `dsa/leetcode/2645_minimum-additions-to-make-valid-string` |
| 2646 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/2646_minimize-the-total-price-of-the-trips` |
| 2647 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2647_color-the-triangle-red` |
| 2648 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2648_generate-fibonacci-sequence` |
| 2649 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2649_nested-array-generator` |
| 2650 | unverified | source_fidelity.json is missing | no | 4 | 3 | 0 | 0 | 0 | `dsa/leetcode/2650_design-cancellable-function` |
| 2651 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2651_calculate-delayed-arrival-time` |
| 2652 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2652_sum-multiples` |
| 2653 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2653_sliding-subarray-beauty` |
| 2654 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2654_minimum-number-of-operations-to-make-all-array-elements-equal-to-1` |
| 2655 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2655_find-maximal-uncovered-ranges` |
| 2656 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2656_maximum-sum-with-exactly-k-elements` |
| 2657 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2657_find-the-prefix-common-array-of-two-arrays` |
| 2658 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2658_maximum-number-of-fish-in-a-grid` |
| 2659 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2659_make-array-empty` |
| 2660 | unverified | source_fidelity.json is missing | no | 4 | 4 | 0 | 0 | 0 | `dsa/leetcode/2660_determine-the-winner-of-a-bowling-game` |
| 2661 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2661_first-completely-painted-row-or-column` |
| 2662 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2662_minimum-cost-of-a-path-with-special-roads` |
| 2663 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2663_lexicographically-smallest-beautiful-string` |
| 2664 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2664_the-knights-tour` |
| 2665 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2665_counter-ii` |
| 2666 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2666_allow-one-function-call` |
| 2667 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2667_create-hello-world-function` |
| 2668 | unverified | source_fidelity.json is missing | no | 1 | 1 | 0 | 0 | 0 | `dsa/leetcode/2668_find-latest-salaries` |
| 2669 | unverified | source_fidelity.json is missing | no | 1 | 1 | 0 | 0 | 0 | `dsa/leetcode/2669_count-artist-occurrences-on-spotify-ranking-list` |
| 2670 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2670_find-the-distinct-difference-array` |
| 2671 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2671_frequency-tracker` |
| 2672 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2672_number-of-adjacent-elements-with-the-same-color` |
| 2673 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2673_make-costs-of-paths-equal-in-a-binary-tree` |
| 2674 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2674_split-a-circular-linked-list` |
| 2675 | unverified | source_fidelity.json is missing | no | 5 | 0 | 0 | 0 | 0 | `dsa/leetcode/2675_array-of-objects-to-matrix` |
| 2676 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2676_throttle` |
| 2677 | unverified | source_fidelity.json is missing | no | 4 | 0 | 0 | 0 | 0 | `dsa/leetcode/2677_chunk-array` |
| 2678 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2678_number-of-senior-citizens` |
| 2679 | unverified | source_fidelity.json is missing | no | 2 | 1 | 0 | 0 | 0 | `dsa/leetcode/2679_sum-in-a-matrix` |
| 2680 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2680_maximum-or` |
| 2681 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2681_power-of-heroes` |
| 2682 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2682_find-the-losers-of-the-circular-game` |
| 2683 | unverified | source_fidelity.json is missing | no | 3 | 2 | 0 | 0 | 0 | `dsa/leetcode/2683_neighboring-bitwise-xor` |
| 2684 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/2684_maximum-number-of-moves-in-a-grid` |
| 2685 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2685_count-the-number-of-complete-components` |
| 2686 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2686_immediate-food-delivery-iii` |
| 2687 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2687_bikes-last-time-used` |
| 2688 | unverified | source_fidelity.json is missing | no | 3 | 1 | 0 | 0 | 0 | `dsa/leetcode/2688_find-active-users` |
| 2689 | unverified | source_fidelity.json is missing | no | 3 | 1 | 0 | 0 | 0 | `dsa/leetcode/2689_extract-kth-character-from-the-rope-tree` |
| 2690 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2690_infinite-method-object` |
| 2691 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2691_immutability-helper` |
| 2692 | unverified | source_fidelity.json is missing | no | 4 | 0 | 0 | 0 | 0 | `dsa/leetcode/2692_make-object-immutable` |
| 2693 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/2693_call-function-with-custom-context` |
| 2694 | unverified | source_fidelity.json is missing | no | 4 | 0 | 0 | 0 | 0 | `dsa/leetcode/2694_event-emitter` |
| 2695 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2695_array-wrapper` |
| 2696 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2696_minimum-string-length-after-removing-substrings` |
| 2697 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2697_lexicographically-smallest-palindrome` |
| 2698 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2698_find-the-punishment-number-of-an-integer` |
| 2699 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2699_modify-graph-edge-weights` |
| 2700 | unverified | source_fidelity.json is missing | no | 5 | 4 | 0 | 0 | 0 | `dsa/leetcode/2700_differences-between-two-objects` |
| 2701 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2701_consecutive-transactions-with-increasing-amounts` |
| 2702 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2702_minimum-operations-to-make-numbers-non-positive` |
| 2703 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2703_return-length-of-arguments-passed` |
| 2704 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2704_to-be-or-not-to-be` |
| 2705 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2705_compact-object` |
| 2706 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2706_buy-two-chocolates` |
| 2707 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2707_extra-characters-in-a-string` |
| 2708 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2708_maximum-strength-of-a-group` |
| 2709 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2709_greatest-common-divisor-traversal` |
| 2710 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2710_remove-trailing-zeros-from-a-string` |
| 2711 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2711_difference-of-number-of-distinct-values-on-diagonals` |
| 2712 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2712_minimum-cost-to-make-all-characters-equal` |
| 2713 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2713_maximum-strictly-increasing-cells-in-a-matrix` |
| 2714 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2714_find-shortest-path-with-k-hops` |
| 2715 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2715_timeout-cancellation` |
| 2716 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2716_minimize-string-length` |
| 2717 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2717_semi-ordered-permutation` |
| 2718 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2718_sum-of-matrix-after-queries` |
| 2719 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2719_count-of-integers` |
| 2720 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2720_popularity-percentage` |
| 2721 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2721_execute-asynchronous-functions-in-parallel` |
| 2722 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2722_join-two-arrays-by-id` |
| 2723 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2723_add-two-promises` |
| 2724 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2724_sort-by` |
| 2725 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2725_interval-cancellation` |
| 2726 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2726_calculator-with-method-chaining` |
| 2727 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2727_is-object-empty` |
| 2728 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2728_count-houses-in-a-circular-street` |
| 2729 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2729_check-if-the-number-is-fascinating` |
| 2730 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2730_find-the-longest-semi-repetitive-substring` |
| 2731 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2731_movement-of-robots` |
| 2732 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2732_find-a-good-subset-of-the-matrix` |
| 2733 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2733_neither-minimum-nor-maximum` |
| 2734 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2734_lexicographically-smallest-string-after-substring-operation` |
| 2735 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2735_collecting-chocolates` |
| 2736 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2736_maximum-sum-queries` |
| 2737 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2737_find-the-closest-marked-node` |
| 2738 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2738_count-occurrences-in-text` |
| 2739 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2739_total-distance-traveled` |
| 2740 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2740_find-the-value-of-the-partition` |
| 2741 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2741_special-permutations` |
| 2742 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2742_painting-the-walls` |
| 2743 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2743_count-substrings-without-repeating-character` |
| 2744 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2744_find-maximum-number-of-string-pairs` |
| 2745 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2745_construct-the-longest-new-string` |
| 2746 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2746_decremental-string-concatenation` |
| 2747 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2747_count-zero-request-servers` |
| 2748 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2748_number-of-beautiful-pairs` |
| 2749 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2749_minimum-operations-to-make-the-integer-zero` |
| 2750 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2750_ways-to-split-array-into-good-subarrays` |
| 2751 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2751_robot-collisions` |
| 2752 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2752_customers-with-maximum-number-of-transactions-on-consecutive-days` |
| 2753 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2753_count-houses-in-a-circular-street-ii` |
| 2754 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2754_bind-function-to-context` |
| 2755 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2755_deep-merge-of-two-objects` |
| 2756 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2756_query-batching` |
| 2757 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2757_generate-circular-array-values` |
| 2758 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2758_next-day` |
| 2759 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2759_convert-json-string-to-object` |
| 2760 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2760_longest-even-odd-subarray-with-threshold` |
| 2761 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2761_prime-pairs-with-target-sum` |
| 2762 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2762_continuous-subarrays` |
| 2763 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2763_sum-of-imbalance-numbers-of-all-subarrays` |
| 2764 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2764_is-array-a-preorder-of-some-binary-tree` |
| 2765 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2765_longest-alternating-subarray` |
| 2766 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2766_relocate-marbles` |
| 2767 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2767_partition-string-into-minimum-beautiful-substrings` |
| 2768 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2768_number-of-black-blocks` |
| 2769 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2769_find-the-maximum-achievable-number` |
| 2770 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2770_maximum-number-of-jumps-to-reach-the-last-index` |
| 2771 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2771_longest-non-decreasing-subarray-from-two-arrays` |
| 2772 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2772_apply-operations-to-make-all-array-elements-equal-to-zero` |
| 2773 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2773_height-of-special-binary-tree` |
| 2774 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2774_array-upper-bound` |
| 2775 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2775_undefined-to-null` |
| 2776 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2776_convert-callback-based-function-to-promise-based-function` |
| 2777 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2777_date-range-generator` |
| 2778 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2778_sum-of-squares-of-special-elements` |
| 2779 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2779_maximum-beauty-of-an-array-after-applying-operation` |
| 2780 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2780_minimum-index-of-a-valid-split` |
| 2781 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2781_length-of-the-longest-valid-substring` |
| 2782 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2782_number-of-unique-categories` |
| 2783 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2783_flight-occupancy-and-waitlist-analysis` |
| 2784 | unverified | source_fidelity.json is missing | no | 4 | 4 | 0 | 0 | 0 | `dsa/leetcode/2784_check-if-array-is-good` |
| 2785 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2785_sort-vowels-in-a-string` |
| 2786 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2786_visit-array-positions-to-maximize-score` |
| 2787 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2787_ways-to-express-an-integer-as-sum-of-powers` |
| 2788 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2788_split-strings-by-separator` |
| 2789 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2789_largest-element-in-an-array-after-merge-operations` |
| 2790 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2790_maximum-number-of-groups-with-increasing-length` |
| 2791 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2791_count-paths-that-can-form-a-palindrome-in-a-tree` |
| 2792 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2792_count-nodes-that-are-great-enough` |
| 2793 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 1 | 0 | `dsa/leetcode/2793_status-of-flight-tickets` |
| 2794 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2794_create-object-from-two-arrays` |
| 2795 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2795_parallel-execution-of-promises-for-individual-results-retrieval` |
| 2796 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2796_repeat-string` |
| 2797 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2797_partial-function-with-placeholders` |
| 2798 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2798_number-of-employees-who-met-the-target` |
| 2799 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2799_count-complete-subarrays-in-an-array` |
| 2800 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2800_shortest-string-that-contains-three-strings` |
| 2801 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2801_count-stepping-numbers-in-range` |
| 2802 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2802_find-the-k-th-lucky-number` |
| 2803 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2803_factorial-generator` |
| 2804 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2804_array-prototype-foreach` |
| 2805 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2805_custom-interval` |
| 2806 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2806_account-balance-after-rounded-purchase` |
| 2807 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2807_insert-greatest-common-divisors-in-linked-list` |
| 2808 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2808_minimum-seconds-to-equalize-a-circular-array` |
| 2809 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2809_minimum-time-to-make-array-sum-at-most-x` |
| 2810 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2810_faulty-keyboard` |
| 2811 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2811_check-if-it-is-possible-to-split-array` |
| 2812 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2812_find-the-safest-path-in-a-grid` |
| 2813 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2813_maximum-elegance-of-a-k-length-subsequence` |
| 2814 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2814_minimum-time-takes-to-reach-destination-without-drowning` |
| 2815 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2815_max-pair-sum-in-an-array` |
| 2816 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2816_double-a-number-represented-as-a-linked-list` |
| 2817 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2817_minimum-absolute-difference-between-elements-with-constraint` |
| 2818 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2818_apply-operations-to-maximize-score` |
| 2819 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2819_minimum-relative-loss-after-buying-chocolates` |
| 2820 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 1 | 0 | `dsa/leetcode/2820_election-results` |
| 2821 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2821_delay-the-resolution-of-each-promise` |
| 2822 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2822_inversion-of-object` |
| 2823 | unverified | source_fidelity.json is missing | no | 4 | 0 | 0 | 0 | 0 | `dsa/leetcode/2823_deep-object-filter` |
| 2824 | unverified | source_fidelity.json is missing | no | 3 | 2 | 0 | 0 | 0 | `dsa/leetcode/2824_count-pairs-whose-sum-is-less-than-target` |
| 2825 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2825_make-string-a-subsequence-using-cyclic-increments` |
| 2826 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2826_sorting-three-groups` |
| 2827 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2827_number-of-beautiful-integers-in-the-range` |
| 2828 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2828_check-if-a-string-is-an-acronym-of-words` |
| 2829 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2829_determine-the-minimum-sum-of-a-k-avoiding-array` |
| 2830 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2830_maximize-the-profit-as-the-salesman` |
| 2831 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2831_find-the-longest-equal-subarray` |
| 2832 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2832_maximal-range-that-each-element-is-maximum-in-it` |
| 2833 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2833_furthest-point-from-origin` |
| 2834 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2834_find-the-minimum-possible-sum-of-a-beautiful-array` |
| 2835 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2835_minimum-operations-to-form-subsequence-with-target-sum` |
| 2836 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2836_maximize-value-of-function-in-a-ball-passing-game` |
| 2837 | unverified | source_fidelity.json is missing | no | 1 | 1 | 0 | 0 | 0 | `dsa/leetcode/2837_total-traveled-distance` |
| 2838 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2838_maximum-coins-heroes-can-collect` |
| 2839 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2839_check-if-strings-can-be-made-equal-with-operations-i` |
| 2840 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2840_check-if-strings-can-be-made-equal-with-operations-ii` |
| 2841 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2841_maximum-sum-of-almost-unique-subarray` |
| 2842 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2842_count-k-subsequences-of-a-string-with-maximum-beauty` |
| 2843 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2843_count-symmetric-integers` |
| 2844 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2844_minimum-operations-to-make-a-special-number` |
| 2845 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2845_count-of-interesting-subarrays` |
| 2846 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2846_minimum-edge-weight-equilibrium-queries-in-a-tree` |
| 2847 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2847_smallest-number-with-given-digit-product` |
| 2848 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2848_points-that-intersect-with-cars` |
| 2849 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2849_determine-if-a-cell-is-reachable-at-a-given-time` |
| 2850 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2850_minimum-moves-to-spread-stones-over-grid` |
| 2851 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2851_string-transformation` |
| 2852 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2852_sum-of-remoteness-of-all-cells` |
| 2853 | unverified | source_fidelity.json is missing | no | 1 | 1 | 0 | 0 | 0 | `dsa/leetcode/2853_highest-salaries-difference` |
| 2854 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2854_rolling-average-steps` |
| 2855 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2855_minimum-right-shifts-to-sort-the-array` |
| 2856 | unverified | source_fidelity.json is missing | no | 4 | 0 | 0 | 0 | 0 | `dsa/leetcode/2856_minimum-array-length-after-pair-removals` |
| 2857 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2857_count-pairs-of-points-with-distance-k` |
| 2858 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2858_minimum-edge-reversals-so-every-node-is-reachable` |
| 2859 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2859_sum-of-values-at-indices-with-k-set-bits` |
| 2860 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2860_happy-students` |
| 2861 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2861_maximum-number-of-alloys` |
| 2862 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2862_maximum-element-sum-of-a-complete-subset-of-indices` |
| 2863 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2863_maximum-length-of-semi-decreasing-subarrays` |
| 2864 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2864_maximum-odd-binary-number` |
| 2865 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2865_beautiful-towers-i` |
| 2866 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2866_beautiful-towers-ii` |
| 2867 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2867_count-valid-paths-in-a-tree` |
| 2868 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2868_the-wording-game` |
| 2869 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2869_minimum-operations-to-collect-elements` |
| 2870 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2870_minimum-number-of-operations-to-make-array-empty` |
| 2871 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2871_split-array-into-maximum-number-of-subarrays` |
| 2872 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2872_maximum-number-of-k-divisible-components` |
| 2873 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2873_maximum-value-of-an-ordered-triplet-i` |
| 2874 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2874_maximum-value-of-an-ordered-triplet-ii` |
| 2875 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2875_minimum-size-subarray-in-infinite-array` |
| 2876 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2876_count-visited-nodes-in-a-directed-graph` |
| 2877 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2877_create-a-dataframe-from-list` |
| 2878 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2878_get-the-size-of-a-dataframe` |
| 2879 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2879_display-the-first-three-rows` |
| 2880 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2880_select-data` |
| 2881 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2881_create-a-new-column` |
| 2882 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2882_drop-duplicate-rows` |
| 2883 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2883_drop-missing-data` |
| 2884 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2884_modify-columns` |
| 2885 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2885_rename-columns` |
| 2886 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2886_change-data-type` |
| 2887 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2887_fill-missing-data` |
| 2888 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2888_reshape-data-concatenate` |
| 2889 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2889_reshape-data-pivot` |
| 2890 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2890_reshape-data-melt` |
| 2891 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2891_method-chaining` |
| 2892 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2892_minimizing-array-after-replacing-pairs-with-their-product` |
| 2893 | unverified | source_fidelity.json is missing | no | 3 | 1 | 0 | 0 | 0 | `dsa/leetcode/2893_calculate-orders-within-each-interval` |
| 2894 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2894_divisible-and-non-divisible-sums-difference` |
| 2895 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2895_minimum-processing-time` |
| 2896 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2896_apply-operations-to-make-two-strings-equal` |
| 2897 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2897_apply-operations-on-array-to-maximize-sum-of-squares` |
| 2898 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2898_maximum-linear-stock-score` |
| 2899 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2899_last-visited-integers` |
| 2900 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2900_longest-unequal-adjacent-groups-subsequence-i` |
| 2901 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2901_longest-unequal-adjacent-groups-subsequence-ii` |
| 2902 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2902_count-of-sub-multisets-with-bounded-sum` |
| 2903 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2903_find-indices-with-index-and-value-difference-i` |
| 2904 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2904_shortest-and-lexicographically-smallest-beautiful-string` |
| 2905 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2905_find-indices-with-index-and-value-difference-ii` |
| 2906 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2906_construct-product-matrix` |
| 2907 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2907_maximum-profitable-triplets-with-increasing-prices-i` |
| 2908 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2908_minimum-sum-of-mountain-triplets-i` |
| 2909 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2909_minimum-sum-of-mountain-triplets-ii` |
| 2910 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2910_minimum-number-of-groups-to-create-a-valid-assignment` |
| 2911 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2911_minimum-changes-to-make-k-semi-palindromes` |
| 2912 | unverified | source_fidelity.json is missing | no | 3 | 2 | 0 | 0 | 0 | `dsa/leetcode/2912_number-of-ways-to-reach-destination-in-the-grid` |
| 2913 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2913_subarrays-distinct-element-sum-of-squares-i` |
| 2914 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2914_minimum-number-of-changes-to-make-binary-string-beautiful` |
| 2915 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2915_length-of-the-longest-subsequence-that-sums-to-target` |
| 2916 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2916_subarrays-distinct-element-sum-of-squares-ii` |
| 2917 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2917_find-the-k-or-of-an-array` |
| 2918 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2918_minimum-equal-sum-of-two-arrays-after-replacing-zeros` |
| 2919 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2919_minimum-increment-operations-to-make-array-beautiful` |
| 2920 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2920_maximum-points-after-collecting-coins-from-all-nodes` |
| 2921 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2921_maximum-profitable-triplets-with-increasing-prices-ii` |
| 2922 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 1 | 0 | `dsa/leetcode/2922_market-analysis-iii` |
| 2923 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2923_find-champion-i` |
| 2924 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2924_find-champion-ii` |
| 2925 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2925_maximum-score-after-applying-operations-on-a-tree` |
| 2926 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2926_maximum-balanced-subsequence-sum` |
| 2927 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2927_distribute-candies-among-children-iii` |
| 2928 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2928_distribute-candies-among-children-i` |
| 2929 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2929_distribute-candies-among-children-ii` |
| 2930 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2930_number-of-strings-which-can-be-rearranged-to-contain-substring` |
| 2931 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2931_maximum-spending-after-buying-items` |
| 2932 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2932_maximum-strong-pair-xor-i` |
| 2933 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2933_high-access-employees` |
| 2934 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2934_minimum-operations-to-maximize-last-elements-in-arrays` |
| 2935 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2935_maximum-strong-pair-xor-ii` |
| 2936 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2936_number-of-equal-numbers-blocks` |
| 2937 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2937_make-three-strings-equal` |
| 2938 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2938_separate-black-and-white-balls` |
| 2939 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2939_maximum-xor-product` |
| 2940 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2940_find-building-where-alice-and-bob-can-meet` |
| 2941 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2941_maximum-gcd-sum-of-a-subarray` |
| 2942 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2942_find-words-containing-character` |
| 2943 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2943_maximize-area-of-square-hole-in-grid` |
| 2944 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2944_minimum-number-of-coins-for-fruits` |
| 2945 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2945_find-maximum-non-decreasing-array-length` |
| 2946 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2946_matrix-similarity-after-cyclic-shifts` |
| 2947 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2947_count-beautiful-substrings-i` |
| 2948 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2948_make-lexicographically-smallest-array-by-swapping-elements` |
| 2949 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2949_count-beautiful-substrings-ii` |
| 2950 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 1 | 0 | `dsa/leetcode/2950_number-of-divisible-substrings` |
| 2951 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2951_find-the-peaks` |
| 2952 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2952_minimum-number-of-coins-to-be-added` |
| 2953 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2953_count-complete-substrings` |
| 2954 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2954_count-the-number-of-infection-sequences` |
| 2955 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2955_number-of-same-end-substrings` |
| 2956 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2956_find-common-elements-between-two-arrays` |
| 2957 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2957_remove-adjacent-almost-equal-characters` |
| 2958 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2958_length-of-longest-subarray-with-at-most-k-frequency` |
| 2959 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2959_number-of-possible-sets-of-closing-branches` |
| 2960 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2960_count-tested-devices-after-test-operations` |
| 2961 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2961_double-modular-exponentiation` |
| 2962 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2962_count-subarrays-where-max-element-appears-at-least-k-times` |
| 2963 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2963_count-the-number-of-good-partitions` |
| 2964 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2964_number-of-divisible-triplet-sums` |
| 2965 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2965_find-missing-and-repeated-values` |
| 2966 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2966_divide-array-into-arrays-with-max-difference` |
| 2967 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2967_minimum-cost-to-make-array-equalindromic` |
| 2968 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2968_apply-operations-to-maximize-frequency-score` |
| 2969 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2969_minimum-number-of-coins-for-fruits-ii` |
| 2970 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2970_count-the-number-of-incremovable-subarrays-i` |
| 2971 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2971_find-polygon-with-the-largest-perimeter` |
| 2972 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2972_count-the-number-of-incremovable-subarrays-ii` |
| 2973 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2973_find-number-of-coins-to-place-in-tree-nodes` |
| 2974 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2974_minimum-number-game` |
| 2975 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2975_maximum-square-area-by-removing-fences-from-a-field` |
| 2976 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2976_minimum-cost-to-convert-string-i` |
| 2977 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2977_minimum-cost-to-convert-string-ii` |
| 2978 | unverified | source_fidelity.json is missing | no | 1 | 0 | 0 | 1 | 0 | `dsa/leetcode/2978_symmetric-coordinates` |
| 2979 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/2979_most-expensive-item-that-can-not-be-bought` |
| 2980 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/2980_check-if-bitwise-or-has-trailing-zeros` |
| 2981 | unverified | source_fidelity.json is missing | no | 3 | 2 | 0 | 0 | 0 | `dsa/leetcode/2981_find-longest-special-substring-that-occurs-thrice-i` |
| 2982 | unverified | source_fidelity.json is missing | no | 3 | 2 | 0 | 0 | 0 | `dsa/leetcode/2982_find-longest-special-substring-that-occurs-thrice-ii` |
| 2983 | unverified | source_fidelity.json is missing | no | 3 | 1 | 0 | 0 | 0 | `dsa/leetcode/2983_palindrome-rearrangement-queries` |
| 2984 | unverified | source_fidelity.json is missing | no | 3 | 2 | 0 | 0 | 0 | `dsa/leetcode/2984_find-peak-calling-hours-for-each-city` |
| 2985 | unverified | source_fidelity.json is missing | no | 3 | 1 | 0 | 0 | 0 | `dsa/leetcode/2985_calculate-compressed-mean` |
| 2986 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2986_find-third-transaction` |
| 2987 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2987_find-expensive-cities` |
| 2988 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2988_manager-of-the-largest-department` |
| 2989 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2989_class-performance` |
| 2990 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2990_loan-types` |
| 2991 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2991_top-three-wineries` |
| 2992 | unverified | source_fidelity.json is missing | no | 3 | 1 | 0 | 0 | 0 | `dsa/leetcode/2992_number-of-self-divisible-permutations` |
| 2993 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2993_friday-purchases-i` |
| 2994 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2994_friday-purchases-ii` |
| 2995 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2995_viewers-turned-streamers` |
| 2996 | unverified | source_fidelity.json is missing | no | 3 | 1 | 0 | 0 | 0 | `dsa/leetcode/2996_smallest-missing-integer-greater-than-sequential-prefix-sum` |
| 2997 | unverified | source_fidelity.json is missing | no | 3 | 1 | 0 | 0 | 0 | `dsa/leetcode/2997_minimum-number-of-operations-to-make-array-xor-equal-to-k` |
| 2998 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2998_minimum-number-of-operations-to-make-x-and-y-equal` |
| 2999 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/2999_count-the-number-of-powerful-integers` |
| 3000 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/3000_maximum-area-of-longest-diagonal-rectangle` |
| 3001 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/3001_minimum-moves-to-capture-the-queen` |
| 3002 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3002_maximum-size-of-a-set-after-removals` |
| 3003 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3003_maximize-the-number-of-partitions-after-operations` |
| 3004 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3004_maximum-subtree-of-the-same-color` |
| 3005 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/3005_count-elements-with-maximum-frequency` |
| 3006 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/3006_find-beautiful-indices-in-the-given-array-i` |
| 3007 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/3007_maximum-number-that-sum-of-the-prices-is-less-than-or-equal-to-k` |
| 3008 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/3008_find-beautiful-indices-in-the-given-array-ii` |
| 3009 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/3009_maximum-number-of-intersections-on-the-chart` |
| 3010 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3010_divide-an-array-into-subarrays-with-minimum-cost-i` |
| 3011 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3011_find-if-array-can-be-sorted` |
| 3012 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3012_minimize-length-of-array-using-operations` |
| 3013 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3013_divide-an-array-into-subarrays-with-minimum-cost-ii` |
| 3014 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3014_minimum-number-of-pushes-to-type-word-i` |
| 3015 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3015_count-the-number-of-houses-at-a-certain-distance-i` |
| 3016 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3016_minimum-number-of-pushes-to-type-word-ii` |
| 3017 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3017_count-the-number-of-houses-at-a-certain-distance-ii` |
| 3018 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3018_maximum-number-of-removal-queries-that-can-be-processed-i` |
| 3019 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3019_number-of-changing-keys` |
| 3020 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3020_find-the-maximum-number-of-elements-in-subset` |
| 3021 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3021_alice-and-bob-playing-flower-game` |
| 3022 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3022_minimize-or-of-remaining-elements-using-operations` |
| 3023 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3023_find-pattern-in-infinite-stream-i` |
| 3024 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/3024_type-of-triangle` |
| 3025 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3025_find-the-number-of-ways-to-place-people-i` |
| 3026 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3026_maximum-good-subarray-sum` |
| 3027 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3027_find-the-number-of-ways-to-place-people-ii` |
| 3028 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/3028_ant-on-the-boundary` |
| 3029 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3029_minimum-time-to-revert-word-to-initial-state-i` |
| 3030 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3030_find-the-grid-of-region-average` |
| 3031 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3031_minimum-time-to-revert-word-to-initial-state-ii` |
| 3032 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3032_count-numbers-with-unique-digits-ii` |
| 3033 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/3033_modify-the-matrix` |
| 3034 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/3034_number-of-subarrays-that-match-a-pattern-i` |
| 3035 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3035_maximum-palindromes-after-operations` |
| 3036 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/3036_number-of-subarrays-that-match-a-pattern-ii` |
| 3037 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3037_find-pattern-in-infinite-stream-ii` |
| 3038 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3038_maximum-number-of-operations-with-the-same-score-i` |
| 3039 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/3039_apply-operations-to-make-string-empty` |
| 3040 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/3040_maximum-number-of-operations-with-the-same-score-ii` |
| 3041 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/3041_maximize-consecutive-elements-in-an-array-after-modification` |
| 3042 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3042_count-prefix-and-suffix-pairs-i` |
| 3043 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/3043_find-the-length-of-the-longest-common-prefix` |
| 3044 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3044_most-frequent-prime` |
| 3045 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3045_count-prefix-and-suffix-pairs-ii` |
| 3046 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/3046_split-the-array` |
| 3047 | unverified | source_fidelity.json is missing | no | 4 | 4 | 0 | 0 | 0 | `dsa/leetcode/3047_find-the-largest-area-of-square-inside-two-rectangles` |
| 3048 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3048_earliest-second-to-mark-indices-i` |
| 3049 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3049_earliest-second-to-mark-indices-ii` |
| 3050 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 1 | 0 | `dsa/leetcode/3050_pizza-toppings-cost-analysis` |
| 3051 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 1 | 0 | `dsa/leetcode/3051_find-candidates-for-data-scientist-position` |
| 3052 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 1 | 0 | `dsa/leetcode/3052_maximize-items` |
| 3053 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3053_classifying-triangles-by-lengths` |
| 3054 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3054_binary-tree-nodes` |
| 3055 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3055_top-percentile-fraud` |
| 3056 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3056_snaps-analysis` |
| 3057 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3057_employees-project-allocation` |
| 3058 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3058_friends-with-no-mutual-friends` |
| 3059 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3059_find-all-unique-email-domains` |
| 3060 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3060_user-activities-within-time-bounds` |
| 3061 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3061_calculate-trapping-rain-water` |
| 3062 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3062_winner-of-the-linked-list-game` |
| 3063 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3063_linked-list-frequency` |
| 3064 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/3064_guess-the-number-using-bitwise-questions-i` |
| 3065 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3065_minimum-operations-to-exceed-threshold-value-i` |
| 3066 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/3066_minimum-operations-to-exceed-threshold-value-ii` |
| 3067 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/3067_count-pairs-of-connectable-servers-in-a-weighted-tree-network` |
| 3068 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3068_find-the-maximum-sum-of-node-values` |
| 3069 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/3069_distribute-elements-into-two-arrays-i` |
| 3070 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/3070_count-submatrices-with-top-left-element-and-sum-less-than-k` |
| 3071 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/3071_minimum-operations-to-write-the-letter-y-on-a-grid` |
| 3072 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3072_distribute-elements-into-two-arrays-ii` |
| 3073 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/3073_maximum-increasing-triplet-value` |
| 3074 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/3074_apple-redistribution-into-boxes` |
| 3075 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3075_maximize-happiness-of-selected-children` |
| 3076 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/3076_shortest-uncommon-substring-in-an-array` |
| 3077 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3077_maximum-strength-of-k-disjoint-subarrays` |
| 3078 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3078_match-alphanumerical-pattern-in-matrix-i` |
| 3079 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/3079_find-the-sum-of-encrypted-integers` |
| 3080 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/3080_mark-elements-on-array-by-performing-queries` |
| 3081 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/3081_replace-question-marks-in-string-to-minimize-its-value` |
| 3082 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3082_find-the-sum-of-the-power-of-all-subsequences` |
| 3083 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3083_existence-of-a-substring-in-a-string-and-its-reverse` |
| 3084 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/3084_count-substrings-starting-and-ending-with-given-character` |
| 3085 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3085_minimum-deletions-to-make-string-k-special` |
| 3086 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/3086_minimum-moves-to-pick-k-ones` |
| 3087 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3087_find-trending-hashtags` |
| 3088 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3088_make-string-anti-palindrome` |
| 3089 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3089_find-bursty-behavior` |
| 3090 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3090_maximum-length-substring-with-two-occurrences` |
| 3091 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3091_apply-operations-to-make-sum-of-array-greater-than-or-equal-to-k` |
| 3092 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3092_most-frequent-ids` |
| 3093 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3093_longest-common-suffix-queries` |
| 3094 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/3094_guess-the-number-using-bitwise-questions-ii` |
| 3095 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3095_shortest-subarray-with-or-at-least-k-i` |
| 3096 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3096_minimum-levels-to-gain-more-points` |
| 3097 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3097_shortest-subarray-with-or-at-least-k-ii` |
| 3098 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3098_find-the-sum-of-subsequence-powers` |
| 3099 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/3099_harshad-number` |
| 3100 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/3100_water-bottles-ii` |
| 3101 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/3101_count-alternating-subarrays` |
| 3102 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/3102_minimize-manhattan-distances` |
| 3103 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3103_find-trending-hashtags-ii` |
| 3104 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3104_find-longest-self-contained-substring` |
| 3105 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3105_longest-strictly-increasing-or-strictly-decreasing-subarray` |
| 3106 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3106_lexicographically-smallest-string-after-operations-with-constraint` |
| 3107 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3107_minimum-operations-to-make-median-of-array-equal-to-k` |
| 3108 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/3108_minimum-cost-walk-in-weighted-graph` |
| 3109 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/3109_find-the-index-of-permutation` |
| 3110 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/3110_score-of-a-string` |
| 3111 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3111_minimum-rectangles-to-cover-points` |
| 3112 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3112_minimum-time-to-visit-disappearing-nodes` |
| 3113 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3113_find-the-number-of-subarrays-where-boundary-elements-are-maximum` |
| 3114 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/3114_latest-time-you-can-obtain-after-replacing-characters` |
| 3115 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/3115_maximum-prime-difference` |
| 3116 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/3116_kth-smallest-amount-with-single-denomination-combination` |
| 3117 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3117_minimum-sum-of-values-by-dividing-array` |
| 3118 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3118_friday-purchase-iii` |
| 3119 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3119_maximum-number-of-potholes-that-can-be-fixed` |
| 3120 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3120_count-the-number-of-special-characters-i` |
| 3121 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3121_count-the-number-of-special-characters-ii` |
| 3122 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3122_minimum-number-of-operations-to-satisfy-conditions` |
| 3123 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/3123_find-edges-in-shortest-paths` |
| 3124 | unverified | source_fidelity.json is missing | no | 1 | 1 | 0 | 0 | 0 | `dsa/leetcode/3124_find-longest-calls` |
| 3125 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3125_maximum-number-that-makes-result-of-bitwise-and-zero` |
| 3126 | unverified | source_fidelity.json is missing | no | 1 | 1 | 0 | 0 | 0 | `dsa/leetcode/3126_server-utilization-time` |
| 3127 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3127_make-a-square-with-the-same-color` |
| 3128 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3128_right-triangles` |
| 3129 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3129_find-all-possible-stable-binary-arrays-i` |
| 3130 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3130_find-all-possible-stable-binary-arrays-ii` |
| 3131 | unverified | source_fidelity.json is missing | no | 3 | 1 | 0 | 0 | 0 | `dsa/leetcode/3131_find-the-integer-added-to-array-i` |
| 3132 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/3132_find-the-integer-added-to-array-ii` |
| 3133 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/3133_minimum-array-end` |
| 3134 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3134_find-the-median-of-the-uniqueness-array` |
| 3135 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3135_equalize-strings-by-adding-or-removing-characters-at-ends` |
| 3136 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3136_valid-word` |
| 3137 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/3137_minimum-number-of-operations-to-make-word-k-periodic` |
| 3138 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3138_minimum-length-of-anagram-concatenation` |
| 3139 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3139_minimum-cost-to-equalize-array` |
| 3140 | unverified | source_fidelity.json is missing | no | 1 | 0 | 0 | 2 | 0 | `dsa/leetcode/3140_consecutive-available-seats-ii` |
| 3141 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/3141_maximum-hamming-distances` |
| 3142 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3142_check-if-grid-satisfies-conditions` |
| 3143 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3143_maximum-points-inside-the-square` |
| 3144 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/3144_minimum-substring-partition-of-equal-character-frequency` |
| 3145 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/3145_find-products-of-elements-of-big-array` |
| 3146 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/3146_permutation-difference-between-two-strings` |
| 3147 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3147_taking-maximum-energy-from-the-mystic-dungeon` |
| 3148 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3148_maximum-difference-score-in-a-grid` |
| 3149 | unverified | source_fidelity.json is missing | no | 3 | 2 | 0 | 0 | 0 | `dsa/leetcode/3149_find-the-minimum-cost-array-permutation` |
| 3150 | unverified | source_fidelity.json is missing | no | 3 | 1 | 0 | 0 | 0 | `dsa/leetcode/3150_invalid-tweets-ii` |
| 3151 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3151_special-array-i` |
| 3152 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3152_special-array-ii` |
| 3153 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3153_sum-of-digit-differences-of-all-pairs` |
| 3154 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3154_find-number-of-ways-to-reach-the-k-th-stair` |
| 3155 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3155_maximum-number-of-upgradable-servers` |
| 3156 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 1 | 0 | `dsa/leetcode/3156_employee-task-duration-and-concurrent-tasks` |
| 3157 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3157_find-the-level-of-tree-with-minimum-sum` |
| 3158 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3158_find-the-xor-of-numbers-which-appear-twice` |
| 3159 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/3159_find-occurrences-of-an-element-in-an-array` |
| 3160 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/3160_find-the-number-of-distinct-colors-among-the-balls` |
| 3161 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/3161_block-placement-queries` |
| 3162 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/3162_find-the-number-of-good-pairs-i` |
| 3163 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/3163_string-compression-iii` |
| 3164 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/3164_find-the-number-of-good-pairs-ii` |
| 3165 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/3165_maximum-sum-of-subsequence-with-non-adjacent-elements` |
| 3166 | unverified | source_fidelity.json is missing | no | 1 | 0 | 0 | 2 | 0 | `dsa/leetcode/3166_calculate-parking-fees-and-duration` |
| 3167 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3167_better-compression-of-string` |
| 3168 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3168_minimum-number-of-chairs-in-a-waiting-room` |
| 3169 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3169_count-days-without-meetings` |
| 3170 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/3170_lexicographically-minimum-string-after-removing-stars` |
| 3171 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3171_find-subarray-with-bitwise-or-closest-to-k` |
| 3172 | unverified | source_fidelity.json is missing | no | 1 | 0 | 0 | 3 | 0 | `dsa/leetcode/3172_second-day-verification` |
| 3173 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3173_bitwise-or-of-adjacent-elements` |
| 3174 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/3174_clear-digits` |
| 3175 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/3175_find-the-first-player-to-win-k-games-in-a-row` |
| 3176 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/3176_find-the-maximum-length-of-a-good-subsequence-i` |
| 3177 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/3177_find-the-maximum-length-of-a-good-subsequence-ii` |
| 3178 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3178_find-the-child-who-has-the-ball-after-k-seconds` |
| 3179 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/3179_find-the-n-th-value-after-k-seconds` |
| 3180 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/3180_maximum-total-reward-using-operations-i` |
| 3181 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/3181_maximum-total-reward-using-operations-ii` |
| 3182 | unverified | source_fidelity.json is missing | no | 1 | 0 | 0 | 4 | 0 | `dsa/leetcode/3182_find-top-scoring-students` |
| 3183 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3183_the-number-of-ways-to-make-the-sum` |
| 3184 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/3184_count-pairs-that-form-a-complete-day-i` |
| 3185 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/3185_count-pairs-that-form-a-complete-day-ii` |
| 3186 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/3186_maximum-total-damage-with-spell-casting` |
| 3187 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/3187_peaks-in-array` |
| 3188 | unverified | source_fidelity.json is missing | no | 1 | 0 | 0 | 1 | 0 | `dsa/leetcode/3188_find-top-scoring-students-ii` |
| 3189 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/3189_minimum-moves-to-get-a-peaceful-board` |
| 3190 | unverified | source_fidelity.json is missing | no | 2 | 1 | 0 | 0 | 0 | `dsa/leetcode/3190_find-minimum-operations-to-make-all-elements-divisible-by-three` |
| 3191 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/3191_minimum-operations-to-make-binary-array-elements-equal-to-one-i` |
| 3192 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/3192_minimum-operations-to-make-binary-array-elements-equal-to-one-ii` |
| 3193 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3193_count-the-number-of-inversions` |
| 3194 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3194_minimum-average-of-smallest-and-largest-elements` |
| 3195 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/3195_find-the-minimum-area-to-cover-all-ones-i` |
| 3196 | unverified | source_fidelity.json is missing | no | 4 | 0 | 0 | 0 | 0 | `dsa/leetcode/3196_maximize-total-cost-of-alternating-subarrays` |
| 3197 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/3197_find-the-minimum-area-to-cover-all-ones-ii` |
| 3198 | unverified | source_fidelity.json is missing | no | 1 | 0 | 0 | 2 | 0 | `dsa/leetcode/3198_find-cities-in-each-state` |
| 3199 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/3199_count-triplets-with-even-xor-set-bits-i` |
| 3200 | unverified | source_fidelity.json is missing | no | 4 | 4 | 0 | 0 | 0 | `dsa/leetcode/3200_maximum-height-of-a-triangle` |
| 3201 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3201_find-the-maximum-length-of-valid-subsequence-i` |
| 3202 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/3202_find-the-maximum-length-of-valid-subsequence-ii` |
| 3203 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/3203_find-minimum-diameter-after-merging-two-trees` |
| 3204 | unverified | source_fidelity.json is missing | no | 1 | 0 | 0 | 2 | 0 | `dsa/leetcode/3204_bitwise-user-permissions-analysis` |
| 3205 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/3205_maximum-array-hopping-score-i` |
| 3206 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/3206_alternating-groups-i` |
| 3207 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/3207_maximum-points-after-enemy-battles` |
| 3208 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3208_alternating-groups-ii` |
| 3209 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3209_number-of-subarrays-with-and-value-of-k` |
| 3210 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/3210_find-the-encrypted-string` |
| 3211 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/3211_generate-binary-strings-without-adjacent-zeros` |
| 3212 | unverified | source_fidelity.json is missing | no | 3 | 2 | 0 | 0 | 0 | `dsa/leetcode/3212_count-submatrices-with-equal-frequency-of-x-and-y` |
| 3213 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/3213_construct-string-with-minimum-cost` |
| 3214 | unverified | source_fidelity.json is missing | no | 1 | 0 | 0 | 1 | 0 | `dsa/leetcode/3214_year-on-year-growth-rate` |
| 3215 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/3215_count-triplets-with-even-xor-set-bits-ii` |
| 3216 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3216_lexicographically-smallest-string-after-a-swap` |
| 3217 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3217_delete-nodes-from-linked-list-present-in-array` |
| 3218 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3218_minimum-cost-for-cutting-cake-i` |
| 3219 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3219_minimum-cost-for-cutting-cake-ii` |
| 3220 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3220_odd-and-even-transactions` |
| 3221 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3221_maximum-array-hopping-score-ii` |
| 3222 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3222_find-the-winning-player-in-coin-game` |
| 3223 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3223_minimum-length-of-string-after-operations` |
| 3224 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3224_minimum-array-changes-to-make-differences-equal` |
| 3225 | unverified | source_fidelity.json is missing | no | 3 | 2 | 0 | 0 | 0 | `dsa/leetcode/3225_maximum-score-from-grid-operations` |
| 3226 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3226_number-of-bit-changes-to-make-two-integers-equal` |
| 3227 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3227_vowels-game-in-a-string` |
| 3228 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3228_maximum-number-of-operations-to-move-ones-to-the-end` |
| 3229 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3229_minimum-operations-to-make-array-equal-to-target` |
| 3230 | unverified | source_fidelity.json is missing | no | 1 | 0 | 0 | 1 | 0 | `dsa/leetcode/3230_customer-purchasing-behavior-analysis` |
| 3231 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3231_minimum-number-of-increasing-subsequence-to-be-removed` |
| 3232 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3232_find-if-digit-game-can-be-won` |
| 3233 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3233_find-the-count-of-numbers-which-are-not-special` |
| 3234 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3234_count-the-number-of-substrings-with-dominant-ones` |
| 3235 | unverified | source_fidelity.json is missing | no | 4 | 4 | 0 | 0 | 0 | `dsa/leetcode/3235_check-if-the-rectangle-corner-is-reachable` |
| 3236 | unverified | source_fidelity.json is missing | no | 1 | 0 | 0 | 0 | 0 | `dsa/leetcode/3236_ceo-subordinate-hierarchy` |
| 3237 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/3237_alt-and-tab-simulation` |
| 3238 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3238_find-the-number-of-winning-players` |
| 3239 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3239_minimum-number-of-flips-to-make-binary-grid-palindromic-i` |
| 3240 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3240_minimum-number-of-flips-to-make-binary-grid-palindromic-ii` |
| 3241 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3241_time-taken-to-mark-all-nodes` |
| 3242 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3242_design-neighbor-sum-service` |
| 3243 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3243_shortest-distance-after-road-addition-queries-i` |
| 3244 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3244_shortest-distance-after-road-addition-queries-ii` |
| 3245 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3245_alternating-groups-iii` |
| 3246 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3246_premier-league-table-ranking` |
| 3247 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3247_number-of-subsequences-with-odd-sum` |
| 3248 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3248_snake-in-matrix` |
| 3249 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3249_count-the-number-of-good-nodes` |
| 3250 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3250_find-the-count-of-monotonic-pairs-i` |
| 3251 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3251_find-the-count-of-monotonic-pairs-ii` |
| 3252 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3252_premier-league-table-ranking-ii` |
| 3253 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3253_construct-string-with-minimum-cost-easy` |
| 3254 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3254_find-the-power-of-k-size-subarrays-i` |
| 3255 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3255_find-the-power-of-k-size-subarrays-ii` |
| 3256 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3256_maximum-value-sum-by-placing-three-rooks-i` |
| 3257 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3257_maximum-value-sum-by-placing-three-rooks-ii` |
| 3258 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3258_count-substrings-that-satisfy-k-constraint-i` |
| 3259 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3259_maximum-energy-boost-from-two-drinks` |
| 3260 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3260_find-the-largest-palindrome-divisible-by-k` |
| 3261 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3261_count-substrings-that-satisfy-k-constraint-ii` |
| 3262 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3262_find-overlapping-shifts` |
| 3263 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3263_convert-doubly-linked-list-to-array-i` |
| 3264 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3264_final-array-state-after-k-multiplication-operations-i` |
| 3265 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3265_count-almost-equal-pairs-i` |
| 3266 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3266_final-array-state-after-k-multiplication-operations-ii` |
| 3267 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3267_count-almost-equal-pairs-ii` |
| 3268 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3268_find-overlapping-shifts-ii` |
| 3269 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3269_constructing-two-increasing-arrays` |
| 3270 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3270_find-the-key-of-the-numbers` |
| 3271 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3271_hash-divided-string` |
| 3272 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3272_find-the-count-of-good-integers` |
| 3273 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3273_minimum-amount-of-damage-dealt-to-bob` |
| 3274 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3274_check-if-two-chessboard-squares-have-the-same-color` |
| 3275 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3275_k-th-nearest-obstacle-queries` |
| 3276 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3276_select-cells-in-grid-with-maximum-score` |
| 3277 | unverified | source_fidelity.json is missing | no | 3 | 2 | 0 | 0 | 0 | `dsa/leetcode/3277_maximum-xor-score-subarray-queries` |
| 3278 | unverified | source_fidelity.json is missing | no | 3 | 1 | 0 | 0 | 0 | `dsa/leetcode/3278_find-candidates-for-data-scientist-position-ii` |
| 3279 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3279_maximum-total-area-occupied-by-pistons` |
| 3280 | unverified | source_fidelity.json is missing | no | 3 | 2 | 0 | 0 | 0 | `dsa/leetcode/3280_convert-date-to-binary` |
| 3281 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3281_maximize-score-of-numbers-in-ranges` |
| 3282 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3282_reach-end-of-array-with-max-score` |
| 3283 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3283_maximum-number-of-moves-to-kill-all-pawns` |
| 3284 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3284_sum-of-consecutive-subarrays` |
| 3285 | unverified | source_fidelity.json is missing | no | 3 | 2 | 0 | 0 | 0 | `dsa/leetcode/3285_find-indices-of-stable-mountains` |
| 3286 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3286_find-a-safe-walk-through-a-grid` |
| 3287 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/3287_find-the-maximum-sequence-value-of-array` |
| 3288 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/3288_length-of-the-longest-increasing-path` |
| 3289 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3289_the-two-sneaky-numbers-of-digitville` |
| 3290 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/3290_maximum-multiplication-score` |
| 3291 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3291_minimum-number-of-valid-strings-to-form-target-i` |
| 3292 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3292_minimum-number-of-valid-strings-to-form-target-ii` |
| 3293 | unverified | source_fidelity.json is missing | no | 1 | 0 | 0 | 3 | 0 | `dsa/leetcode/3293_calculate-product-final-price` |
| 3294 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/3294_convert-doubly-linked-list-to-array-ii` |
| 3295 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/3295_report-spam-message` |
| 3296 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3296_minimum-number-of-seconds-to-make-mountain-height-zero` |
| 3297 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3297_count-substrings-that-can-be-rearranged-to-contain-a-string-i` |
| 3298 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3298_count-substrings-that-can-be-rearranged-to-contain-a-string-ii` |
| 3299 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3299_sum-of-consecutive-subsequences` |
| 3300 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3300_minimum-element-after-replacement-with-digit-sum` |
| 3301 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3301_maximize-the-total-height-of-unique-towers` |
| 3302 | unverified | source_fidelity.json is missing | no | 4 | 4 | 0 | 0 | 0 | `dsa/leetcode/3302_find-the-lexicographically-smallest-valid-sequence` |
| 3303 | unverified | source_fidelity.json is missing | no | 4 | 4 | 0 | 0 | 0 | `dsa/leetcode/3303_find-the-occurrence-of-first-almost-equal-substring` |
| 3304 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/3304_find-the-k-th-character-in-string-game-i` |
| 3305 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3305_count-of-substrings-containing-every-vowel-and-k-consonants-i` |
| 3306 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3306_count-of-substrings-containing-every-vowel-and-k-consonants-ii` |
| 3307 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/3307_find-the-k-th-character-in-string-game-ii` |
| 3308 | unverified | source_fidelity.json is missing | no | 1 | 0 | 0 | 0 | 0 | `dsa/leetcode/3308_find-top-performing-driver` |
| 3309 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/3309_maximum-possible-number-by-binary-concatenation` |
| 3310 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3310_remove-methods-from-project` |
| 3311 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3311_construct-2d-grid-matching-graph-layout` |
| 3312 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3312_sorted-gcd-pair-queries` |
| 3313 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3313_find-the-last-marked-nodes-in-tree` |
| 3314 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3314_construct-the-minimum-bitwise-array-i` |
| 3315 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3315_construct-the-minimum-bitwise-array-ii` |
| 3316 | unverified | source_fidelity.json is missing | no | 4 | 0 | 0 | 0 | 0 | `dsa/leetcode/3316_find-maximum-removals-from-source-string` |
| 3317 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3317_find-the-number-of-possible-ways-for-an-event` |
| 3318 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3318_find-x-sum-of-all-k-long-subarrays-i` |
| 3319 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3319_k-th-largest-perfect-subtree-size-in-binary-tree` |
| 3320 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3320_count-the-number-of-winning-sequences` |
| 3321 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/3321_find-x-sum-of-all-k-long-subarrays-ii` |
| 3322 | unverified | source_fidelity.json is missing | no | 1 | 0 | 0 | 0 | 0 | `dsa/leetcode/3322_premier-league-table-ranking-iii` |
| 3323 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/3323_minimize-connected-groups-by-inserting-interval` |
| 3324 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/3324_find-the-sequence-of-strings-appeared-on-the-screen` |
| 3325 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/3325_count-substrings-with-k-frequency-characters-i` |
| 3326 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3326_minimum-division-operations-to-make-array-non-decreasing` |
| 3327 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/3327_check-if-dfs-strings-are-palindromes` |
| 3328 | unverified | source_fidelity.json is missing | no | 1 | 0 | 0 | 2 | 0 | `dsa/leetcode/3328_find-cities-in-each-state-ii` |
| 3329 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/3329_count-substrings-with-k-frequency-characters-ii` |
| 3330 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3330_find-the-original-typed-string-i` |
| 3331 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/3331_find-subtree-sizes-after-changes` |
| 3332 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/3332_maximum-points-tourist-can-earn` |
| 3333 | unverified | source_fidelity.json is missing | no | 3 | 2 | 0 | 0 | 0 | `dsa/leetcode/3333_find-the-original-typed-string-ii` |
| 3334 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3334_find-the-maximum-factor-score-of-array` |
| 3335 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/3335_total-characters-in-string-after-transformations-i` |
| 3336 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3336_find-the-number-of-subsequences-with-equal-gcd` |
| 3337 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3337_total-characters-in-string-after-transformations-ii` |
| 3338 | unverified | source_fidelity.json is missing | no | 1 | 0 | 0 | 2 | 0 | `dsa/leetcode/3338_second-highest-salary-ii` |
| 3339 | unverified | source_fidelity.json is missing | no | 3 | 2 | 0 | 0 | 0 | `dsa/leetcode/3339_find-the-number-of-k-even-arrays` |
| 3340 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/3340_check-balanced-string` |
| 3341 | unverified | source_fidelity.json is missing | no | 3 | 2 | 0 | 0 | 0 | `dsa/leetcode/3341_find-minimum-time-to-reach-last-room-i` |
| 3342 | unverified | source_fidelity.json is missing | no | 3 | 2 | 0 | 0 | 0 | `dsa/leetcode/3342_find-minimum-time-to-reach-last-room-ii` |
| 3343 | unverified | source_fidelity.json is missing | no | 3 | 2 | 0 | 0 | 0 | `dsa/leetcode/3343_count-number-of-balanced-permutations` |
| 3344 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/3344_maximum-sized-array` |
| 3345 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3345_smallest-divisible-digit-product-i` |
| 3346 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3346_maximum-frequency-of-an-element-after-performing-operations-i` |
| 3347 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3347_maximum-frequency-of-an-element-after-performing-operations-ii` |
| 3348 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3348_smallest-divisible-digit-product-ii` |
| 3349 | unverified | source_fidelity.json is missing | no | 2 | 3 | 0 | 0 | 0 | `dsa/leetcode/3349_adjacent-increasing-subarrays-detection-i` |
| 3350 | unverified | source_fidelity.json is missing | no | 2 | 3 | 0 | 0 | 0 | `dsa/leetcode/3350_adjacent-increasing-subarrays-detection-ii` |
| 3351 | unverified | source_fidelity.json is missing | no | 2 | 3 | 0 | 0 | 0 | `dsa/leetcode/3351_sum-of-good-subsequences` |
| 3352 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3352_count-k-reducible-numbers-less-than-n` |
| 3353 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/3353_minimum-total-operations` |
| 3354 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/3354_make-array-elements-equal-to-zero` |
| 3355 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/3355_zero-array-transformation-i` |
| 3356 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/3356_zero-array-transformation-ii` |
| 3357 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3357_minimize-the-maximum-adjacent-element-difference` |
| 3358 | unverified | source_fidelity.json is missing | no | 1 | 0 | 0 | 2 | 0 | `dsa/leetcode/3358_books-with-null-ratings` |
| 3359 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3359_find-sorted-submatrices-with-maximum-element-at-most-k` |
| 3360 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/3360_stone-removal-game` |
| 3361 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/3361_shift-distance-between-two-strings` |
| 3362 | unverified | source_fidelity.json is missing | no | 3 | 2 | 0 | 0 | 0 | `dsa/leetcode/3362_zero-array-transformation-iii` |
| 3363 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/3363_find-the-maximum-number-of-fruits-collected` |
| 3364 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3364_minimum-positive-sum-subarray` |
| 3365 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3365_rearrange-k-substrings-to-form-target-string` |
| 3366 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/3366_minimum-array-sum` |
| 3367 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/3367_maximize-sum-of-weights-after-edge-removals` |
| 3368 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3368_first-letter-capitalization` |
| 3369 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3369_design-an-array-statistics-tracker` |
| 3370 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3370_smallest-number-with-all-set-bits` |
| 3371 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3371_identify-the-largest-outlier-in-an-array` |
| 3372 | unverified | source_fidelity.json is missing | no | 3 | 1 | 0 | 0 | 0 | `dsa/leetcode/3372_maximize-the-number-of-target-nodes-after-connecting-trees-i` |
| 3373 | unverified | source_fidelity.json is missing | no | 3 | 1 | 0 | 0 | 0 | `dsa/leetcode/3373_maximize-the-number-of-target-nodes-after-connecting-trees-ii` |
| 3374 | unverified | source_fidelity.json is missing | no | 3 | 1 | 0 | 0 | 0 | `dsa/leetcode/3374_first-letter-capitalization-ii` |
| 3375 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3375_minimum-operations-to-make-array-values-equal-to-k` |
| 3376 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3376_minimum-time-to-break-locks-i` |
| 3377 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3377_digit-operations-to-make-two-integers-equal` |
| 3378 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3378_count-connected-components-in-lcm-graph` |
| 3379 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3379_transformed-array` |
| 3380 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3380_maximum-area-rectangle-with-point-constraints-i` |
| 3381 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3381_maximum-subarray-sum-with-length-divisible-by-k` |
| 3382 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3382_maximum-area-rectangle-with-point-constraints-ii` |
| 3383 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/3383_minimum-runes-to-add-to-cast-spell` |
| 3384 | unverified | source_fidelity.json is missing | no | 1 | 0 | 0 | 3 | 0 | `dsa/leetcode/3384_team-dominance-by-pass-success` |
| 3385 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/3385_minimum-time-to-break-locks-ii` |
| 3386 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/3386_button-with-longest-push-time` |
| 3387 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3387_maximize-amount-after-two-days-of-conversions` |
| 3388 | unverified | source_fidelity.json is missing | no | 2 | 1 | 0 | 0 | 0 | `dsa/leetcode/3388_count-beautiful-splits-in-an-array` |
| 3389 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3389_minimum-operations-to-make-character-frequencies-equal` |
| 3390 | unverified | source_fidelity.json is missing | no | 1 | 0 | 0 | 3 | 0 | `dsa/leetcode/3390_longest-team-pass-streak` |
| 3391 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/3391_design-a-3d-binary-matrix-with-efficient-layer-tracking` |
| 3392 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/3392_count-subarrays-of-length-three-with-a-condition` |
| 3393 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3393_count-paths-with-the-given-xor-value` |
| 3394 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3394_check-if-grid-can-be-cut-into-sections` |
| 3395 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3395_subsequences-with-a-unique-middle-mode-i` |
| 3396 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3396_minimum-number-of-operations-to-make-elements-in-array-distinct` |
| 3397 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/3397_maximum-number-of-distinct-elements-after-operations` |
| 3398 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3398_smallest-substring-with-identical-characters-i` |
| 3399 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3399_smallest-substring-with-identical-characters-ii` |
| 3400 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/3400_maximum-number-of-matching-indices-after-right-shifts` |
| 3401 | unverified | source_fidelity.json is missing | no | 1 | 0 | 0 | 2 | 0 | `dsa/leetcode/3401_find-circular-gift-exchange-chains` |
| 3402 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/3402_minimum-operations-to-make-columns-strictly-increasing` |
| 3403 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/3403_find-the-lexicographically-largest-string-from-the-box-i` |
| 3404 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/3404_count-special-subsequences` |
| 3405 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3405_count-the-number-of-arrays-with-k-matching-adjacent-elements` |
| 3406 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/3406_find-the-lexicographically-largest-string-from-the-box-ii` |
| 3407 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3407_substring-matching-pattern` |
| 3408 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3408_design-task-manager` |
| 3409 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3409_longest-subsequence-with-decreasing-adjacent-difference` |
| 3410 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/3410_maximize-subarray-sum-after-removing-all-occurrences-of-one-element` |
| 3411 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3411_maximum-subarray-with-equal-products` |
| 3412 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/3412_find-mirror-score-of-a-string` |
| 3413 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/3413_maximum-coins-from-k-consecutive-bags` |
| 3414 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3414_maximum-score-of-non-overlapping-intervals` |
| 3415 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/3415_find-products-with-three-consecutive-digits` |
| 3416 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3416_subsequences-with-a-unique-middle-mode-ii` |
| 3417 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3417_zigzag-grid-traversal-with-skip` |
| 3418 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3418_maximum-amount-of-money-robot-can-earn` |
| 3419 | unverified | source_fidelity.json is missing | no | 4 | 4 | 0 | 0 | 0 | `dsa/leetcode/3419_minimize-the-maximum-edge-weight-of-graph` |
| 3420 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/3420_count-non-decreasing-subarrays-after-k-operations` |
| 3421 | unverified | source_fidelity.json is missing | no | 1 | 1 | 0 | 0 | 0 | `dsa/leetcode/3421_find-students-who-improved` |
| 3422 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/3422_minimum-operations-to-make-subarray-elements-equal` |
| 3423 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/3423_maximum-difference-between-adjacent-elements-in-a-circular-array` |
| 3424 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/3424_minimum-cost-to-make-arrays-identical` |
| 3425 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/3425_longest-special-path` |
| 3426 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/3426_manhattan-distances-of-all-arrangements-of-pieces` |
| 3427 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/3427_sum-of-variable-length-subarrays` |
| 3428 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3428_maximum-and-minimum-sums-of-at-most-size-k-subsequences` |
| 3429 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/3429_paint-house-iv` |
| 3430 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/3430_maximum-and-minimum-sums-of-at-most-size-k-subarrays` |
| 3431 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3431_minimum-unlocked-indices-to-sort-nums` |
| 3432 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3432_count-partitions-with-even-sum-difference` |
| 3433 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3433_count-mentions-per-user` |
| 3434 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/3434_maximum-frequency-after-subarray-operation` |
| 3435 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3435_frequencies-of-shortest-supersequences` |
| 3436 | unverified | source_fidelity.json is missing | no | 1 | 0 | 0 | 3 | 0 | `dsa/leetcode/3436_find-valid-emails` |
| 3437 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3437_permutations-iii` |
| 3438 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3438_find-valid-pair-of-adjacent-digits-in-string` |
| 3439 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3439_reschedule-meetings-for-maximum-free-time-i` |
| 3440 | unverified | source_fidelity.json is missing | no | 4 | 0 | 0 | 0 | 0 | `dsa/leetcode/3440_reschedule-meetings-for-maximum-free-time-ii` |
| 3441 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3441_minimum-cost-good-caption` |
| 3442 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/3442_maximum-difference-between-even-and-odd-frequency-i` |
| 3443 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/3443_maximum-manhattan-distance-after-k-changes` |
| 3444 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3444_minimum-increments-for-target-multiples-in-an-array` |
| 3445 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3445_maximum-difference-between-even-and-odd-frequency-ii` |
| 3446 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3446_sort-matrix-by-diagonals` |
| 3447 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3447_assign-elements-to-groups-with-constraints` |
| 3448 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3448_count-substrings-divisible-by-last-digit` |
| 3449 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3449_maximize-the-minimum-game-score` |
| 3450 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3450_maximum-students-on-a-single-bench` |
| 3451 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3451_find-invalid-ip-addresses` |
| 3452 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3452_sum-of-good-numbers` |
| 3453 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/3453_separate-squares-i` |
| 3454 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/3454_separate-squares-ii` |
| 3455 | unverified | source_fidelity.json is missing | no | 4 | 0 | 0 | 0 | 0 | `dsa/leetcode/3455_shortest-matching-substring` |
| 3456 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3456_find-special-substring-of-length-k` |
| 3457 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3457_eat-pizzas` |
| 3458 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3458_select-k-disjoint-special-substrings` |
| 3459 | unverified | source_fidelity.json is missing | no | 4 | 0 | 0 | 0 | 0 | `dsa/leetcode/3459_length-of-longest-v-shaped-diagonal-segment` |
| 3460 | unverified | source_fidelity.json is missing | no | 4 | 0 | 0 | 0 | 0 | `dsa/leetcode/3460_longest-common-prefix-after-at-most-one-removal` |
| 3461 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3461_check-if-digits-are-equal-in-string-after-operations-i` |
| 3462 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3462_maximum-sum-with-at-most-k-elements` |
| 3463 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3463_check-if-digits-are-equal-in-string-after-operations-ii` |
| 3464 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3464_maximize-the-distance-between-points-on-a-square` |
| 3465 | unverified | source_fidelity.json is missing | no | 1 | 0 | 0 | 3 | 0 | `dsa/leetcode/3465_find-products-with-valid-serial-numbers` |
| 3466 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3466_maximum-coin-collection` |
| 3467 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/3467_transform-array-by-parity` |
| 3468 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3468_find-the-number-of-copy-arrays` |
| 3469 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3469_find-minimum-cost-to-remove-array-elements` |
| 3470 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3470_permutations-iv` |
| 3471 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3471_find-the-largest-almost-missing-integer` |
| 3472 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3472_longest-palindromic-subsequence-after-at-most-k-operations` |
| 3473 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3473_sum-of-k-subarrays-with-length-at-least-m` |
| 3474 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3474_lexicographically-smallest-generated-string` |
| 3475 | unverified | source_fidelity.json is missing | no | 1 | 0 | 0 | 3 | 0 | `dsa/leetcode/3475_dna-pattern-recognition` |
| 3476 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3476_maximize-profit-from-task-assignment` |
| 3477 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/3477_fruits-into-baskets-ii` |
| 3478 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/3478_choose-k-elements-with-maximum-sum` |
| 3479 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/3479_fruits-into-baskets-iii` |
| 3480 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/3480_maximize-subarrays-after-removing-one-conflicting-pair` |
| 3481 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/3481_apply-substitutions` |
| 3482 | unverified | source_fidelity.json is missing | no | 0 | 0 | 0 | 0 | 0 | `dsa/leetcode/3482_analyze-organization-hierarchy` |
| 3483 | unverified | source_fidelity.json is missing | no | 4 | 0 | 0 | 0 | 0 | `dsa/leetcode/3483_unique-3-digit-even-numbers` |
| 3484 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/3484_design-spreadsheet` |
| 3485 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3485_longest-common-prefix-of-k-strings-after-removal` |
| 3486 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3486_longest-special-path-ii` |
| 3487 | unverified | source_fidelity.json is missing | no | 4 | 0 | 0 | 0 | 0 | `dsa/leetcode/3487_maximum-unique-subarray-sum-after-deletion` |
| 3488 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3488_closest-equal-element-queries` |
| 3489 | unverified | source_fidelity.json is missing | no | 4 | 0 | 0 | 0 | 0 | `dsa/leetcode/3489_zero-array-transformation-iv` |
| 3490 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/3490_count-beautiful-numbers` |
| 3491 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/3491_phone-number-prefix` |
| 3492 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/3492_maximum-containers-on-a-ship` |
| 3493 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3493_properties-graph` |
| 3494 | unverified | source_fidelity.json is missing | no | 3 | 2 | 0 | 0 | 0 | `dsa/leetcode/3494_find-the-minimum-amount-of-time-to-brew-potions` |
| 3495 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/3495_minimum-operations-to-make-array-elements-zero` |
| 3496 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/3496_maximize-score-after-pair-deletions` |
| 3497 | unverified | source_fidelity.json is missing | no | 2 | 0 | 0 | 0 | 0 | `dsa/leetcode/3497_analyze-subscription-conversion` |
| 3498 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/3498_reverse-degree-of-a-string` |
| 3499 | unverified | source_fidelity.json is missing | no | 4 | 4 | 0 | 0 | 0 | `dsa/leetcode/3499_maximize-active-section-with-trade-i` |
| 3500 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3500_minimum-cost-to-divide-array-into-subarrays` |
| 3501 | unverified | source_fidelity.json is missing | no | 4 | 4 | 0 | 0 | 0 | `dsa/leetcode/3501_maximize-active-section-with-trade-ii` |
| 3502 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/3502_minimum-cost-to-reach-every-position` |
| 3503 | unverified | source_fidelity.json is missing | no | 4 | 4 | 0 | 0 | 0 | `dsa/leetcode/3503_longest-palindrome-after-substring-concatenation-i` |
| 3504 | unverified | source_fidelity.json is missing | no | 4 | 4 | 0 | 0 | 0 | `dsa/leetcode/3504_longest-palindrome-after-substring-concatenation-ii` |
| 3505 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/3505_minimum-operations-to-make-elements-within-k-subarrays-equal` |
| 3506 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/3506_find-time-required-to-eliminate-bacterial-strains` |
| 3507 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/3507_minimum-pair-removal-to-sort-array-i` |
| 3508 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/3508_implement-router` |
| 3509 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3509_maximum-product-of-subsequences-with-an-alternating-sum-equal-to-k` |
| 3510 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/3510_minimum-pair-removal-to-sort-array-ii` |
| 3511 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3511_make-a-positive-array` |
| 3512 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3512_minimum-operations-to-make-array-sum-divisible-by-k` |
| 3513 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/3513_number-of-unique-xor-triplets-i` |
| 3514 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/3514_number-of-unique-xor-triplets-ii` |
| 3515 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3515_shortest-path-in-a-weighted-tree` |
| 3516 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3516_find-closest-person` |
| 3517 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3517_smallest-palindromic-rearrangement-i` |
| 3518 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3518_smallest-palindromic-rearrangement-ii` |
| 3519 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3519_count-numbers-with-non-decreasing-digits` |
| 3520 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3520_minimum-threshold-for-inversion-pairs-count` |
| 3521 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3521_find-product-recommendation-pairs` |
| 3522 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3522_calculate-score-after-performing-instructions` |
| 3523 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/3523_make-array-non-decreasing` |
| 3524 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3524_find-x-value-of-array-i` |
| 3525 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3525_find-x-value-of-array-ii` |
| 3526 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/3526_range-xor-queries-with-subarray-reversals` |
| 3527 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/3527_find-the-most-common-response` |
| 3528 | unverified | source_fidelity.json is missing | no | 2 | 1 | 0 | 0 | 0 | `dsa/leetcode/3528_unit-conversion-i` |
| 3529 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3529_count-cells-in-overlapping-horizontal-and-vertical-substrings` |
| 3530 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/3530_maximum-profit-from-valid-topological-order-in-dag` |
| 3531 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3531_count-covered-buildings` |
| 3532 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/3532_path-existence-queries-in-a-graph-i` |
| 3533 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3533_concatenated-divisibility` |
| 3534 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3534_path-existence-queries-in-a-graph-ii` |
| 3535 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/3535_unit-conversion-ii` |
| 3536 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3536_maximum-product-of-two-digits` |
| 3537 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3537_fill-a-special-grid` |
| 3538 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/3538_merge-operations-for-minimum-travel-time` |
| 3539 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3539_find-sum-of-array-product-of-magical-sequences` |
| 3540 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/3540_minimum-time-to-visit-all-houses` |
| 3541 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/3541_find-most-frequent-vowel-and-consonant` |
| 3542 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3542_minimum-operations-to-convert-all-elements-to-zero` |
| 3543 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3543_maximum-weighted-k-edge-path` |
| 3544 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3544_subtree-inversion-sum` |
| 3545 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3545_minimum-deletions-for-at-most-k-distinct-characters` |
| 3546 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/3546_equal-sum-grid-partition-i` |
| 3547 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/3547_maximum-sum-of-edge-values-in-a-graph` |
| 3548 | unverified | source_fidelity.json is missing | no | 4 | 4 | 0 | 0 | 0 | `dsa/leetcode/3548_equal-sum-grid-partition-ii` |
| 3549 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3549_multiply-two-polynomials` |
| 3550 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3550_smallest-index-with-digit-sum-equal-to-index` |
| 3551 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3551_minimum-swaps-to-sort-by-digit-sum` |
| 3552 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/3552_grid-teleportation-traversal` |
| 3553 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/3553_minimum-weighted-subgraph-with-the-required-paths-ii` |
| 3554 | unverified | source_fidelity.json is missing | no | 1 | 1 | 0 | 0 | 0 | `dsa/leetcode/3554_find-category-recommendation-pairs` |
| 3555 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/3555_smallest-subarray-to-sort-in-every-sliding-window` |
| 3556 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/3556_sum-of-largest-prime-substrings` |
| 3557 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/3557_find-maximum-number-of-non-intersecting-substrings` |
| 3558 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/3558_number-of-ways-to-assign-edge-weights-i` |
| 3559 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/3559_number-of-ways-to-assign-edge-weights-ii` |
| 3560 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/3560_find-minimum-log-transportation-cost` |
| 3561 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3561_resulting-string-after-adjacent-removals` |
| 3562 | unverified | source_fidelity.json is missing | no | 4 | 4 | 0 | 0 | 0 | `dsa/leetcode/3562_maximum-profit-from-trading-stocks-with-discounts` |
| 3563 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3563_lexicographically-smallest-string-after-adjacent-removals` |
| 3564 | unverified | source_fidelity.json is missing | no | 1 | 1 | 0 | 0 | 0 | `dsa/leetcode/3564_seasonal-sales-analysis` |
| 3565 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/3565_sequential-grid-path-cover` |
| 3566 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/3566_partition-array-into-two-equal-product-subsets` |
| 3567 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3567_minimum-absolute-difference-in-sliding-submatrix` |
| 3568 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3568_minimum-moves-to-clean-the-classroom` |
| 3569 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/3569_maximize-count-of-distinct-primes-after-split` |
| 3570 | unverified | source_fidelity.json is missing | no | 1 | 1 | 0 | 0 | 0 | `dsa/leetcode/3570_find-books-with-no-available-copies` |
| 3571 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/3571_find-the-shortest-superstring-ii` |
| 3572 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/3572_maximize-ysum-by-picking-a-triplet-of-distinct-xvalues` |
| 3573 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/3573_best-time-to-buy-and-sell-stock-v` |
| 3574 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3574_maximize-subarray-gcd-score` |
| 3575 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3575_maximum-good-subtree-score` |
| 3576 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/3576_transform-array-to-all-equal-elements` |
| 3577 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/3577_count-the-number-of-computer-unlocking-permutations` |
| 3578 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/3578_count-partitions-with-max-min-difference-at-most-k` |
| 3579 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3579_minimum-steps-to-convert-string-with-operations` |
| 3580 | unverified | source_fidelity.json is missing | no | 1 | 1 | 0 | 0 | 0 | `dsa/leetcode/3580_find-consistently-improving-employees` |
| 3581 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/3581_count-odd-letters-from-number` |
| 3582 | unverified | source_fidelity.json is missing | no | 3 | 1 | 0 | 0 | 0 | `dsa/leetcode/3582_generate-tag-for-video-caption` |
| 3583 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3583_count-special-triplets` |
| 3584 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3584_maximum-product-of-first-and-last-elements-of-a-subsequence` |
| 3585 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3585_find-weighted-median-node-in-tree` |
| 3586 | unverified | source_fidelity.json is missing | no | 1 | 1 | 0 | 0 | 0 | `dsa/leetcode/3586_find-covid-recovery-patients` |
| 3587 | unverified | source_fidelity.json is missing | no | 4 | 4 | 0 | 0 | 0 | `dsa/leetcode/3587_minimum-adjacent-swaps-to-alternate-parity` |
| 3588 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3588_find-maximum-area-of-a-triangle` |
| 3589 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3589_count-prime-gap-balanced-subarrays` |
| 3590 | unverified | source_fidelity.json is missing | no | 3 | 2 | 0 | 0 | 0 | `dsa/leetcode/3590_kth-smallest-path-xor-sum` |
| 3591 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3591_check-if-any-element-has-prime-frequency` |
| 3592 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3592_inverse-coin-change` |
| 3593 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3593_minimum-increments-to-equalize-leaf-paths` |
| 3594 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3594_minimum-time-to-transport-all-individuals` |
| 3595 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/3595_once-twice` |
| 3596 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3596_minimum-cost-path-with-alternating-directions-i` |
| 3597 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3597_partition-string` |
| 3598 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3598_longest-common-prefix-between-adjacent-strings-after-removals` |
| 3599 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3599_partition-array-to-minimize-xor` |
| 3600 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3600_maximize-spanning-tree-stability-with-upgrades` |
| 3601 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3601_find-drivers-with-improved-fuel-efficiency` |
| 3602 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3602_hexadecimal-and-hexatrigesimal-conversion` |
| 3603 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3603_minimum-cost-path-with-alternating-directions-ii` |
| 3604 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3604_minimum-time-to-reach-destination-in-directed-graph` |
| 3605 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3605_minimum-stability-factor-of-array` |
| 3606 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/3606_coupon-code-validator` |
| 3607 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/3607_power-grid-maintenance` |
| 3608 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3608_minimum-time-for-k-connected-components` |
| 3609 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3609_minimum-moves-to-reach-target-in-grid` |
| 3610 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3610_minimum-number-of-primes-to-sum-to-target` |
| 3611 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3611_find-overbooked-employees` |
| 3612 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3612_process-string-with-special-operations-i` |
| 3613 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3613_minimize-maximum-component-cost` |
| 3614 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3614_process-string-with-special-operations-ii` |
| 3615 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3615_longest-palindromic-path-in-graph` |
| 3616 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3616_number-of-student-replacements` |
| 3617 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3617_find-students-with-study-spiral-pattern` |
| 3618 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3618_split-array-by-prime-indices` |
| 3619 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3619_count-islands-with-total-value-divisible-by-k` |
| 3620 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3620_network-recovery-pathways` |
| 3621 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3621_number-of-integers-with-popcount-depth-equal-to-k-i` |
| 3622 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3622_check-divisibility-by-digit-sum-and-product` |
| 3623 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3623_count-number-of-trapezoids-i` |
| 3624 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3624_number-of-integers-with-popcount-depth-equal-to-k-ii` |
| 3625 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/3625_count-number-of-trapezoids-ii` |
| 3626 | unverified | source_fidelity.json is missing | no | 1 | 1 | 0 | 0 | 0 | `dsa/leetcode/3626_find-stores-with-inventory-imbalance` |
| 3627 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/3627_maximum-median-sum-of-subsequences-of-size-3` |
| 3628 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3628_maximum-number-of-subsequences-after-one-inserting` |
| 3629 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3629_minimum-jumps-to-reach-end-via-prime-teleportation` |
| 3630 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3630_partition-array-for-maximum-xor-and-and` |
| 3631 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/3631_sort-threats-by-severity-and-exploitability` |
| 3632 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/3632_subarrays-with-xor-at-least-k` |
| 3633 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/3633_earliest-finish-time-for-land-and-water-rides-i` |
| 3634 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3634_minimum-removals-to-balance-array` |
| 3635 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/3635_earliest-finish-time-for-land-and-water-rides-ii` |
| 3636 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/3636_threshold-majority-queries` |
| 3637 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/3637_trionic-array-i` |
| 3638 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/3638_maximum-balanced-shipments` |
| 3639 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3639_minimum-time-to-activate-string` |
| 3640 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/3640_trionic-array-ii` |
| 3641 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3641_longest-semi-repeating-subarray` |
| 3642 | unverified | source_fidelity.json is missing | no | 1 | 1 | 0 | 0 | 0 | `dsa/leetcode/3642_find-books-with-polarized-opinions` |
| 3643 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/3643_flip-square-submatrix-vertically` |
| 3644 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3644_maximum-k-to-sort-a-permutation` |
| 3645 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3645_maximum-total-from-optimal-activation-order` |
| 3646 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/3646_next-special-palindrome-number` |
| 3647 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3647_maximum-weight-in-two-bags` |
| 3648 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/3648_minimum-sensors-to-cover-grid` |
| 3649 | unverified | source_fidelity.json is missing | no | 3 | 3 | 0 | 0 | 0 | `dsa/leetcode/3649_number-of-perfect-pairs` |
| 3650 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/3650_minimum-cost-path-with-edge-reversals` |
| 3651 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/3651_minimum-cost-path-with-teleportations` |
| 3652 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/3652_best-time-to-buy-and-sell-stock-using-strategy` |
| 3653 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/3653_xor-after-range-multiplication-queries-i` |
| 3654 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/3654_minimum-sum-after-divisible-sum-deletions` |
| 3655 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/3655_xor-after-range-multiplication-queries-ii` |
| 3656 | unverified | source_fidelity.json is missing | no | 2 | 2 | 0 | 0 | 0 | `dsa/leetcode/3656_determine-if-a-simple-graph-exists` |
| 3657 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3657_find-loyal-customers` |
| 3658 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3658_gcd-of-odd-and-even-sums` |
| 3659 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3659_partition-array-into-k-distinct-groups` |
| 3660 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3660_jump-game-ix` |
| 3661 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3661_maximum-walls-destroyed-by-robots` |
| 3662 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3662_filter-characters-by-frequency` |
| 3663 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3663_find-the-least-frequent-digit` |
| 3664 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3664_two-letter-card-game` |
| 3665 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3665_twisted-mirror-path-count` |
| 3666 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3666_minimum-operations-to-equalize-binary-string` |
| 3667 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3667_sort-array-by-absolute-value` |
| 3668 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3668_restore-finishing-order` |
| 3669 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3669_balanced-k-factor-decomposition` |
| 3670 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3670_maximum-product-of-two-integers-with-no-common-bits` |
| 3671 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3671_sum-of-beautiful-subsequences` |
| 3672 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3672_sum-of-weighted-modes-in-subarrays` |
| 3673 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3673_find-zombie-sessions` |
| 3674 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3674_minimum-operations-to-equalize-array` |
| 3675 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3675_minimum-operations-to-transform-string` |
| 3676 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3676_count-bowl-subarrays` |
| 3677 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3677_count-binary-palindromic-numbers` |
| 3678 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3678_smallest-absent-positive-greater-than-average` |
| 3679 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3679_minimum-discards-to-balance-inventory` |
| 3680 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3680_generate-schedule` |
| 3681 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3681_maximum-xor-of-subsequences` |
| 3682 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3682_minimum-index-sum-of-common-elements` |
| 3683 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3683_earliest-time-to-finish-one-task` |
| 3684 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3684_maximize-sum-of-at-most-k-distinct-elements` |
| 3685 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3685_subsequence-sum-after-capping-elements` |
| 3686 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3686_number-of-stable-subsequences` |
| 3687 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3687_library-late-fee-calculator` |
| 3688 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3688_bitwise-or-of-even-numbers-in-an-array` |
| 3689 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3689_maximum-total-subarray-value-i` |
| 3690 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3690_split-and-merge-array-transformation` |
| 3691 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3691_maximum-total-subarray-value-ii` |
| 3692 | unverified | source_fidelity.json is missing | no | 3 | 0 | 0 | 0 | 0 | `dsa/leetcode/3692_majority-frequency-characters` |

## Known repository-wide regression debt

These failures are separate from the active submission queue. Their last-observed dates are retained so the final cleanup pass knows when fresh full-suite evidence is required.

| Category | Last observed | ID | Title | Reference | Complexity | Detail | Package |
|---|---|---:|---|---|---|---|---|
| generic_certificate_route_has_no_python_or_sql_reference | 2026-07-29 | 2648 | Generate Fibonacci Sequence | javascript | asymptotic_optimality | The repository-wide certificate real-test sweep selects only a Python or SQL app-local reference. These packages currently expose another runtime shape or lack that selectable reference, so their subtests fail before certificate behavior can be proven. | `dsa/leetcode/2648_generate-fibonacci-sequence` |
| generic_certificate_route_has_no_python_or_sql_reference | 2026-07-29 | 2649 | Nested Array Generator | javascript | asymptotic_optimality | The repository-wide certificate real-test sweep selects only a Python or SQL app-local reference. These packages currently expose another runtime shape or lack that selectable reference, so their subtests fail before certificate behavior can be proven. | `dsa/leetcode/2649_nested-array-generator` |
| generic_certificate_route_has_no_python_or_sql_reference | 2026-07-29 | 2650 | Design Cancellable Function | javascript | asymptotic_optimality | The repository-wide certificate real-test sweep selects only a Python or SQL app-local reference. These packages currently expose another runtime shape or lack that selectable reference, so their subtests fail before certificate behavior can be proven. | `dsa/leetcode/2650_design-cancellable-function` |
| generic_certificate_route_has_no_python_or_sql_reference | 2026-07-29 | 2665 | Counter II | javascript | asymptotic_optimality | The repository-wide certificate real-test sweep selects only a Python or SQL app-local reference. These packages currently expose another runtime shape or lack that selectable reference, so their subtests fail before certificate behavior can be proven. | `dsa/leetcode/2665_counter-ii` |
| generic_certificate_route_has_no_python_or_sql_reference | 2026-07-29 | 2666 | Allow One Function Call | javascript | asymptotic_optimality | The repository-wide certificate real-test sweep selects only a Python or SQL app-local reference. These packages currently expose another runtime shape or lack that selectable reference, so their subtests fail before certificate behavior can be proven. | `dsa/leetcode/2666_allow-one-function-call` |
| generic_certificate_route_has_no_python_or_sql_reference | 2026-07-29 | 2667 | Create Hello World Function | javascript | asymptotic_optimality | The repository-wide certificate real-test sweep selects only a Python or SQL app-local reference. These packages currently expose another runtime shape or lack that selectable reference, so their subtests fail before certificate behavior can be proven. | `dsa/leetcode/2667_create-hello-world-function` |
| generic_certificate_route_has_no_python_or_sql_reference | 2026-07-29 | 2676 | Throttle | javascript | bounded_domain | The repository-wide certificate real-test sweep selects only a Python or SQL app-local reference. These packages currently expose another runtime shape or lack that selectable reference, so their subtests fail before certificate behavior can be proven. | `dsa/leetcode/2676_throttle` |
| generic_certificate_route_has_no_python_or_sql_reference | 2026-07-29 | 2690 | Infinite Method Object | javascript | asymptotic_optimality | The repository-wide certificate real-test sweep selects only a Python or SQL app-local reference. These packages currently expose another runtime shape or lack that selectable reference, so their subtests fail before certificate behavior can be proven. | `dsa/leetcode/2690_infinite-method-object` |
| generic_certificate_route_has_no_python_or_sql_reference | 2026-07-29 | 2803 | Factorial Generator | javascript | asymptotic_optimality | The repository-wide certificate real-test sweep selects only a Python or SQL app-local reference. These packages currently expose another runtime shape or lack that selectable reference, so their subtests fail before certificate behavior can be proven. | `dsa/leetcode/2803_factorial-generator` |
| generic_certificate_route_has_no_python_or_sql_reference | 2026-07-29 | 2804 | Array Prototype ForEach | javascript | asymptotic_optimality | The repository-wide certificate real-test sweep selects only a Python or SQL app-local reference. These packages currently expose another runtime shape or lack that selectable reference, so their subtests fail before certificate behavior can be proven. | `dsa/leetcode/2804_array-prototype-foreach` |
| generic_certificate_route_has_no_python_or_sql_reference | 2026-07-29 | 2805 | Custom Interval | javascript | bounded_concurrency | The repository-wide certificate real-test sweep selects only a Python or SQL app-local reference. These packages currently expose another runtime shape or lack that selectable reference, so their subtests fail before certificate behavior can be proven. | `dsa/leetcode/2805_custom-interval` |
| generic_certificate_route_has_no_python_or_sql_reference | 2026-07-29 | 2821 | Delay the Resolution of Each Promise | javascript | bounded_concurrency | The repository-wide certificate real-test sweep selects only a Python or SQL app-local reference. These packages currently expose another runtime shape or lack that selectable reference, so their subtests fail before certificate behavior can be proven. | `dsa/leetcode/2821_delay-the-resolution-of-each-promise` |
| certificate_route_not_selected | 2026-07-29 | 2670 | Find the Distinct Difference Array | python | bounded_domain | The real-test request reaches runtime scaling instead of the package's verified non-scaling certificate path. | `dsa/leetcode/2670_find-the-distinct-difference-array` |
| certificate_route_not_selected | 2026-07-29 | 3285 | Find Indices of Stable Mountains | python | asymptotic_optimality | The real-test request reaches runtime scaling instead of the package's verified non-scaling certificate path. | `dsa/leetcode/3285_find-indices-of-stable-mountains` |
| reference_hits_python_step_cap | 2026-07-29 | 3690 | Split and Merge Array Transformation | python | bounded_domain | The stored reference reaches the Python execution step cap in the repository-wide certificate real-test sweep. | `dsa/leetcode/3690_split-and-merge-array-transformation` |

## Regeneration

```powershell
.\.venv\Scripts\python.exe tools\audit_leetcode_migration.py
.\.venv\Scripts\python.exe tools\audit_leetcode_source_fidelity.py --max-frontend-id 4005
.\.venv\Scripts\python.exe tools\audit_end_of_corpus_rework_gaps.py
```
