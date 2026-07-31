# First Letter Capitalization II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3374 |
| Difficulty | Hard |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/first-letter-capitalization-ii/) |

## Problem Description

### Goal

The `user_content` table stores a unique integer identifier and a text value. Normalize every space-delimited word so its first character is uppercase and its remaining letters are lowercase. When a word consists of exactly two nonempty alphabetic parts joined by one hyphen, capitalize the first character of both parts instead.

Every other character is formatting and must stay in its original position. This includes leading, trailing, and repeated spaces as well as backslashes, `@`, `/`, `^`, commas, and malformed hyphen patterns. A leading, trailing, repeated, or symbol-adjacent hyphen does not create a valid two-part hyphenated word. Return each identifier, the untouched source text as `original_text`, and the normalized text as `converted_text`.

### Function Contract

**Inputs**

Table `user_content`:

- `content_id`: An integer that uniquely identifies the row.
- `content_text`: A text value containing English letters and the permitted formatting characters `\`, space, `@`, `-`, `/`, `^`, and `,`.

Let $n$ be the number of rows, let $S$ be the total number of characters across all `content_text` values, and let $L$ be the maximum length of one whitespace-delimited word.

**Return value**

- A table with columns `content_id`, `original_text`, and `converted_text`, ordered by `content_id` ascending.

### Examples

**Example 1**

- Input row: `(1, "hello world of SQL")`
- Output row: `(1, "hello world of SQL", "Hello World Of Sql")`

**Example 2**

- Input row: `(2, "the QUICK-brown fox")`
- Output row: `(2, "the QUICK-brown fox", "The Quick-Brown Fox")`

**Example 3**

- Input row: `(4, "foo--bar -baz lOO-daR-@Daz-")`
- Output row: `(4, "foo--bar -baz lOO-daR-@Daz-", "Foo--bar -baz Loo-dar-@daz-")`
- Explanation: None of the malformed multi-hyphen tokens is a two-part alphabetic hyphenated word.
