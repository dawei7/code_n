### 1. Description

Given a text file `file.txt`, transpose its content.

You may assume that each row has the same number of columns, and each field is separated by the `' '` character.

**Example:**

If `file.txt` has the following content:

```
name age
alice 21
ryan 30
```

Output the following:

```
name alice ryan
age 21 30
```

### 2. Function Contract

**Inputs**

The script reads `file.txt` from its working directory; it does not receive function arguments or standard input.

**Return value**

Write the transposed fields to standard output, using one space between adjacent output fields.