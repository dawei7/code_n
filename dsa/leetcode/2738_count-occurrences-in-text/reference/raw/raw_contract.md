## Function Contract

**Inputs**

- `Files`: A table with columns `file_name` (varchar) and `content` (text).

**Return value**

Return a table with columns `word` (varchar) and `count` (int) containing two rows for `'bull'` and `'bear'` indicating the number of files containing at least one space-enclosed occurrence. Row order is unrestricted.
