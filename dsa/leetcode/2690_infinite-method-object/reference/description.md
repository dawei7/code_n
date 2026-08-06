## Description

Create an object that behaves as though it has a method for every possible string property name. Accessing any property must yield a callable function, and invoking that function must return the exact property name that was accessed.

The property does not need to have been declared in advance. Names may be empty, ordinary identifiers, or strings containing punctuation and other characters that require bracket notation. For example, calling `obj.abc123()` returns `"abc123"`, while `obj[".-qw73n|^2It"]()` returns that exact punctuation-heavy name.
