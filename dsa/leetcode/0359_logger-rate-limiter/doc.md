# Logger Rate Limiter

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 359 |
| Difficulty | Easy |
| Topics | Hash Table, Design, Data Stream |
| Official Link | [LeetCode](https://leetcode.com/problems/logger-rate-limiter/) |

## Problem Description
### Goal
Design a logger that receives chronological calls `shouldPrintMessage(timestamp, message)`. A message may be printed when it has never been printed before or when at least ten seconds have elapsed since its most recent permitted print.

Return `True` for a permitted occurrence and record that timestamp. Return `False` for an occurrence arriving sooner, and do not let a rejected call restart or extend the waiting interval. Rate limits are tracked independently by exact message text, so different messages do not block one another. Process every call against persistent state and return one boolean per operation.

### Function Contract
**Inputs**

- `operations`: for the app adapter, a chronological list of `["shouldPrintMessage", timestamp, message]` operations

**Return value**

- A Boolean result for every operation, where `True` means the message should be printed. Native LeetCode calls `Logger.shouldPrintMessage(timestamp, message)` directly.

### Examples
**Example 1**

- Input: `operations = [["shouldPrintMessage",1,"foo"],["shouldPrintMessage",2,"bar"],["shouldPrintMessage",3,"foo"],["shouldPrintMessage",8,"bar"],["shouldPrintMessage",10,"foo"],["shouldPrintMessage",11,"foo"]]`
- Output: `[True,True,False,False,False,True]`

**Example 2**

- Input: `operations = [["shouldPrintMessage",1,"notice"],["shouldPrintMessage",11,"notice"]]`
- Output: `[True,True]`

**Example 3**

- Input: `operations = [["shouldPrintMessage",5,"a"],["shouldPrintMessage",5,"b"],["shouldPrintMessage",5,"a"]]`
- Output: `[True,True,False]`
