## Description

The `user_permissions` table stores one integer permission mask for each user. Every bit position represents a distinct access level or feature: a set bit means that the user possesses the corresponding permission.

Produce one result row with two combined masks. `common_perms` must contain exactly the bits set for every user, so it is the bitwise AND of all values in `permissions`. `any_perms` must contain every bit set for at least one user, so it is the bitwise OR of those values.

The result may be returned in any order.
