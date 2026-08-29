# Roman Numerals - Optimal Approach

## 1. Problem Essence & Formal Mathematical Formulation

For a number written in Roman numerals to be considered valid there are basic rules which must be followed. Even though the rules allow some numbers to be expressed in more than one way there is always a "best" (minimal-length) way of writing a particular number.

For example, $16$ can be written as `XVI` (3 chars), `XIIIIII` (7 chars), or `VVVI` (4 chars), but `XVI` is the minimal form.

Let $\{s_1, s_2, \dots, s_{1000}\}$ be the 1000 valid Roman numeral strings given in `roman.txt`.

The objective is to find the **number of characters saved** by writing each of the 1000 Roman numerals in its minimal canonical form:

$$
\Delta_{\text{chars}} = \sum_{i=1}^{1000} \left( |s_i| - |s_i^*| \right)
$$

where $s_i^*$ is the minimal canonical form of $s_i$.

---

## 2. The Naive Approach & Fundamental Bottlenecks

### Two-Way Conversion (Parse to Int then Format to Roman)
A naive approach parses every Roman numeral string into an integer, formats the integer back into a canonical minimal Roman string, and computes length differences:
```python
def naive_roman_numerals():
    # parses Roman to integer then integer back to Roman for each line
    # ...
```

### Direct Regex Sub-String Replacement
1. Any non-minimal valid Roman numeral string can only contain inefficiencies matching one of six specific patterns:
   - `VIIII` ($9$, 5 chars) $\to$ `IX` (2 chars): saves $3$ characters.
   - `IIII` ($4$, 4 chars) $\to$ `IV` (2 chars): saves $2$ characters.
   - `LXXXX` ($90$, 5 chars) $\to$ `XC` (2 chars): saves $3$ characters.
   - `XXXX` ($40$, 4 chars) $\to$ `XL` (2 chars): saves $2$ characters.
   - `DCCCC` ($900$, 5 chars) $\to$ `CM` (2 chars): saves $3$ characters.
   - `CCCC` ($400$, 4 chars) $\to$ `CD` (2 chars): saves $2$ characters.
2. Replacing these patterns with any arbitrary 2-character placeholder (such as `"XX"`) produces the exact same length as the minimal Roman numeral, computing the total savings in $\approx 0.001$ seconds.

---

## 3. Core Intuition & Mathematical Structure

### Subtractive Transformation Patterns

| Inefficient Pattern | Value | Minimal Subtractive Form | Original Length | Minimal Length | Characters Saved |
| :---: | :---: | :---: | :---: | :---: | :---: |
| `VIIII` | $9$ | `IX` | $5$ | $2$ | **$3$** |
| `IIII` | $4$ | `IV` | $4$ | $2$ | **$2$** |
| `LXXXX` | $90$ | `XC` | $5$ | $2$ | **$3$** |
| `XXXX` | $40$ | `XL` | $4$ | $2$ | **$2$** |
| `DCCCC` | $900$ | `CM` | $5$ | $2$ | **$3$** |
| `CCCC` | $400$ | `CD` | $4$ | $2$ | **$2$** |

---

## 4. Rigorous Mathematical Breakthrough & Derivations

### Regex Length Difference Pipeline
1. Compile the regular expression:

$$
\mathcal{P} = \text{r"VIIII|IIII|LXXXX|XXXX|DCCCC|CCCC"}
$$

2. Compute total original characters:

$$
L_{\text{orig}} = \sum_{i=1}^{1000} \operatorname{len}(s_i)
$$

3. Compute total simplified characters:

$$
L_{\text{min}} = \sum_{i=1}^{1000} \operatorname{len}(\mathcal{P}.\operatorname{sub}(\text{"XX"}, s_i))
$$

4. Return $L_{\text{orig}} - L_{\text{min}}$.

---

## 5. Concrete Step-by-Step Example Walkthrough

### Example 1: Sample String Transformations
- `MMMMDCCCCXXXXVIII` ($18$ chars)
  - `DCCCC` $\to$ `CM` (saves 3)
  - `XXXX` $\to$ `XL` (saves 2)
  - Result: `MMMMCMXLVIII` ($13$ chars, saves $18 - 13 = \mathbf{5}$ chars).
- `VIIII` ($5$ chars) $\to$ `IX` ($2$ chars, saves $\mathbf{3}$ chars).

### Example 2: Target Evaluation across 1000 Numerals
- Processing all lines in `roman.txt`:

$$
\Delta_{\text{chars}} = \mathbf{743}
$$

---

## 6. Implementation Architecture & Algorithmic Blueprint

### Algorithmic Execution Pipeline

| Stage | Operation | Code / Formula Action | Complexity |
| :---: | :--- | :--- | :---: |
| **Stage 1** | **File Loading** | Read lines from `roman.txt` | $\mathcal{O}(N \cdot L)$ |
| **Stage 2** | **Regex Compile** | `re.compile(r"VIIII|IIII|LXXXX|XXXX|DCCCC|CCCC")` | $\mathcal{O}(1)$ |
| **Stage 3** | **Original Length** | `sum(len(line) for line in lines)` | $1000$ lines |
| **Stage 4** | **Substituted Length**| `sum(len(pattern.sub("XX", line)) for line in lines)` | $1000$ lines |
| **Stage 5** | **Return Value** | Return `original_len - minimal_len = 743` | $\mathcal{O}(1)$ |

---

## 7. Mathematical Complexity & Edge Case Invariants

| Dimension | Complexity | Performance / Resource Bounds |
| :--- | :--- | :--- |
| **Time Complexity** | $\mathcal{O}(N \cdot L)$ where $N = 1000, L \le 20$ | $\approx 0.001$ seconds |
| **Space Complexity** | $\mathcal{O}(N \cdot L)$ | Text buffer $\approx 10$ KB |
| **Dynamic Execution** | $100\%$ Inline | Regex subtractive length substitution |

### Critical Invariants & Edge Cases Handled:
1. **Dynamic Path Resolution**: Resolves `roman.txt` relative to package location without relying on external working directories.
2. **Order of Patterns**: Matching `VIIII` before `IIII` (and `LXXXX` before `XXXX`, `DCCCC` before `CCCC`) ensures greedy matching of 5-character sequences over 4-character subsets.