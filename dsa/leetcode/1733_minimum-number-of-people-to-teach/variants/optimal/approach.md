## General
**Discard friendships that already communicate**

Convert each user's languages to a set. For every friendship, test whether the two sets intersect. If they do, that pair needs no teaching regardless of which language is eventually selected. If they do not, add both endpoints to one set of affected users. Friendship is not transitive, so each listed pair is tested directly rather than through graph connectivity.

**Only affected users can require teaching**

Every broken friendship has both endpoints in the affected set. Teaching the chosen language to each affected user who does not already know it is sufficient: afterward every broken pair shares that language, while previously working pairs remain able to communicate. A user outside this set belongs to no broken friendship and never needs to be taught.

**Keep the most common existing language**

Suppose there are $P$ affected users. If the chosen language is already known by $q$ of them, exactly $P-q$ users need lessons. Count all language occurrences among affected users and retain the largest count. Choosing that most common language minimizes $P-q`; if the affected set is empty, the answer is zero.

## Complexity detail
Building all language sets costs $O(S)$ time and space. Testing a friendship can iterate through the smaller endpoint set, so all communication checks cost $O(C)$ time. Counting languages among affected users visits no more than the $S$ stored entries. The affected-user set needs $O(m)$ space, giving $O(S+C)$ time and $O(S+m)$ auxiliary space.

## Alternatives and edge cases
- **Try every language against every affected user:** This is correct but can take $O(nm)$ membership checks even when most available languages never occur among affected users.
- **Teach per broken friendship:** Choosing lessons independently can teach the same user repeatedly or choose incompatible languages; the contract requires one global language.
- **Graph connected components:** Friendship is explicitly non-transitive, so connectivity does not determine whether a listed pair shares a language.
- **No broken friendships:** Return zero without choosing or teaching a language.
- **User in several broken pairs:** Add that user once and count one possible lesson.
- **Unaffected language expert:** A language known only by users outside broken pairs cannot reduce the lesson count.
- **Tied frequencies:** Any tied most-common language gives the same minimum.
