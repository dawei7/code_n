## Function Contract

**Inputs**

`Person(personId, lastName, firstName)` contains one row per person. `Address(addressId, personId, city, state)` contains address data linked by `personId`.

**Return value**

Return a table with columns `firstName`, `lastName`, `city`, and `state`, preserving every person and using null location values when no address matches.
