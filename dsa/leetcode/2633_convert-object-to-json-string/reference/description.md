## Description

Given a valid JSON value, construct and return its JSON text representation without calling the built-in `JSON.stringify` method. The input may be a string, number, boolean, `null`, array, or object, and arrays and objects may contain any of those value types recursively.

The returned text must be valid compact JSON: do not insert spaces beyond characters that belong to string values. When serializing an object, emit its properties in the same order produced by `Object.keys(object)`. All input strings contain only alphanumeric characters, so no escape sequences are needed for their contents.
