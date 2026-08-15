### 1. Description

**HTML entity parser** is the parser that takes HTML code as input and replace all the entities of the special characters by the characters itself.

The special characters and their entities for HTML are:

- **Quotation Mark:** the entity is `"` and symbol character is `"`.

- **Single Quote Mark:** the entity is `'` and symbol character is `'`.

- **Ampersand:** the entity is `&` and symbol character is `&`.

- **Greater Than Sign:** the entity is `>` and symbol character is `>`.

- **Less Than Sign:** the entity is `<` and symbol character is `<`.

- **Slash:** the entity is `⁄` and symbol character is `/`.

Given the input `text` string to the HTML parser, you have to implement the entity parser.

Return *the text after replacing the entities by the special characters*.

### 2. Function Contract

**Inputs**

- `text`: Input parameter (`str`).

**Return value**

- Returns `str`.

### 3. Examples

#### Example 1

- **Input:** $text = "\& is an HTML entity but \&ambassador; is not."$
- **Output:** `"& is an HTML entity but &ambassador; is not."`
- **Explanation:** The parser will replace the & entity by &

#### Example 2

- **Input:** $text = "and I quote: "...""$
- **Output:** `"and I quote: \"...\""`

### 4. Constraints

- $1 \le \text{text.length} \le 10^{5}$

- The string may contain any possible characters out of all the 256 ASCII characters.
