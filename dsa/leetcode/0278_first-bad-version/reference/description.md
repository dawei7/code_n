## Description

You manage a product whose newest release fails its quality check. Each version is built from the preceding one, so every release after a bad version is bad as well.

The versions are numbered `[1, 2, ..., n]`. Find the earliest bad version—the point that causes all subsequent versions to be bad.

The API `bool isBadVersion(version)` reports whether a particular version is bad. Implement the search while minimizing the number of calls to this API.
