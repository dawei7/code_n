## Function Contract

**Inputs**

- `input`: A valid newline-separated hierarchy in which leading tabs encode depth.

**Return value**

Return the greatest character length of an absolute path to a file, counting `/` separators but not serialization tabs or newlines; return `0` if there is no file.
