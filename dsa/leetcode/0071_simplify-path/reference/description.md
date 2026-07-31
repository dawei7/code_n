## Description

You receive an absolute path for a Unix-style file system. It always begins with `/`. Return its simplified canonical form.

Interpret path components according to these rules:

- A component equal to `.` denotes the current directory.
- A component equal to `..` denotes the parent directory.
- Two or more consecutive `/` characters act like one separator.
- Any other sequence of periods is an ordinary directory or file name; for example, `...` and `....` are valid names.

The canonical result must satisfy all of the following:

- It starts with exactly one `/`.
- Adjacent directory names are separated by exactly one `/`.
- It has no trailing `/` unless the result is the root path itself.
- It contains no `.` or `..` components used as current- or parent-directory navigation.
