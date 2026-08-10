## General

**Reduce one innermost union at a time**

The expression combines two operations. Commas form a union of alternatives, while neighboring expressions concatenate through a Cartesian product. Nested braces make a direct left-to-right split difficult because a comma belongs only to its current brace depth.

This solution avoids building a formal parser. It repeatedly finds an innermost brace pair, substitutes each alternative into the surrounding expression, and recursively expands the resulting expressions. Once no braces remain, the expression is one complete word.

**Why the first closing brace identifies an innermost group**

`j = exp.find('}')` chooses the first closing brace. No brace can close inside the group ending at `j`, because such an inner closing brace would have appeared earlier. The matching opening brace is therefore the last opening brace before it, found with `rfind`.

The code separates the current expression into prefix `a = exp[:i]`, group content `exp[i + 1:j]`, and suffix `c = exp[j + 1:]`. Because this group is innermost, its content contains no braces. Splitting it on commas yields its complete alternatives, which may be multi-letter strings such as `"ab"`.

For every alternative `b`, the recursive call receives `a + b + c`. This performs the group’s union by creating one branch per member. It also performs concatenation automatically: the chosen text remains adjacent to the unchanged prefix and suffix.

For example, in `"{a,b}{c,{d,e}}"`, the first closing brace reduces `"{a,b}"`, producing branches beginning with `a` and `b`. Later recursion reduces the innermost `"{d,e}"`, then its containing group. All combinations arise because every earlier branch is recursively paired with every later choice.

**Terminate at complete words**

Each recursive substitution removes one matched brace pair. The number of braces strictly decreases, so recursion must eventually reach an expression with no `'}'`. At that point, no union syntax remains and `exp` is one concrete lowercase word.

The word is inserted into set `s` rather than appended to a list. Set semantics are required because different grammar branches can represent the same word. For example, a union might contain `a` directly and also another expression that expands to `a`. Both recursive paths reach the same string, but the result must contain it once.

**Why all and only represented words appear**

At one innermost group, the represented language is the union over replacing that group by each of its alternatives. The recursive loop explores exactly those replacements. Prefix and suffix text remain fixed around the replacement, which preserves every concatenation required by the surrounding expression.

Assume recursion correctly expands expressions with fewer brace pairs. Applying that fact to every replacement branch yields exactly the words represented by the current expression. The base expression without braces represents its one literal word, which the set records. By induction on the number of brace pairs, the final set is exactly $R(expression)$.

Finally, `sorted(s)` converts the set to the required lexicographically ordered list. Sorting after deduplication ensures duplicate derivations do not create repeated output entries or unnecessary comparisons among identical final words.

## Complexity detail

Let $E$ be the encoded expression length, $R$ the number of distinct returned words, $L$ a maximum returned word length, and $P$ the number of recursive leaf derivations before deduplication. $P$ can exceed $R$ because separate branches can produce the same word.

The package records $O(E + S + RL\log R)$ time and $O(E + S)$ space, where $S$ summarizes expansion work and stored expanded string content. The final comparison sort performs $O(R\log R)$ comparisons, each costing up to $O(L)$ for long common prefixes, which explains $RL\log R$.

For the exact Python code, every recursive node scans its current string with `find` and `rfind` and creates new strings by concatenation. A conservative explicit bound is proportional to the total length of all intermediate expressions, which can be described as $O(PE)$ in a broad worst case. Inserting leaf words into the set costs expected $O(L)$ hashing per derivation.

The set stores $O(RL)$ characters. The recursion depth is at most the number of brace pairs, bounded by $O(E)$, and active intermediate strings can add further expression-sized storage. The output list also contains the $R$ distinct word references and strings.

## Alternatives and edge cases

- **Recursive-descent parser:** Parse union and concatenation as separate grammar levels and return a set from each subexpression. This mirrors the formal grammar directly and can avoid repeatedly rescanning entire intermediate strings.
- **Stack-based set evaluation:** Maintain sets for the current concatenation and accumulated union at each brace depth. It avoids recursive string substitution but requires careful precedence handling.
- **Generate then deduplicate:** Using a list at leaves and converting to a set later is correct but can store many duplicate derivations unnecessarily.
- **No braces:** The first `find` returns `-1`, so the complete literal word is inserted immediately and returned as a one-element list.
- **Nested braces:** Selecting the first closing brace and last preceding opening brace guarantees the reduced group is innermost.
- **Multi-letter alternatives:** `split(',')` returns whole alternative strings, and substitution preserves them without treating each letter as a separate union choice.
- **Duplicate derivations:** The set collapses them, satisfying the rule that every word appears at most once.
- **Concatenated groups:** Recursive branching of one group remains in the prefix when later groups branch, producing the full Cartesian product.
- **Lexicographic order:** Sets are unordered, so the final `sorted` call is essential.
- **Valid grammar guarantee:** The algorithm assumes every closing brace has a matching opening brace and that innermost commas separate alternatives. Malformed syntax would require validation not present here.
- **Expression growth and shrinkage:** Replacing a group can change string length, but the next recursive call searches its newly formed expression from scratch, so stored indices never become stale.
