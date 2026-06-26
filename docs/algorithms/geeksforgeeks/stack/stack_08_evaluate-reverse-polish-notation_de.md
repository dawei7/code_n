# Evaluate Reverse Polish Notation

| | |
|---|---|
| **ID** | `stack_08` |
| **Category** | stack |
| **Complexity (required)** | $O(N)$ Zeitkomplexität, $O(N)$ Platzkomplexität |
| **Difficulty** | 3/10 |
| **Interview relevance** | 7/10 |
| **LeetCode Equivalent** | [Evaluate Reverse Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation/) |

## Problem statement

Berechne den Wert eines arithmetischen Ausdrucks in **Reverse Polish Notation** (Postfix-Notation).
Gültige Operatoren sind `+`, `-`, `*` und `/`. Jeder Operand kann eine Ganzzahl oder ein weiterer Ausdruck sein.
Die Division zwischen zwei Ganzzahlen sollte in Richtung Null abgeschnitten werden.
Es wird garantiert, dass der gegebene RPN-Ausdruck immer gültig ist. Das bedeutet, dass der Ausdruck immer zu einem Ergebnis ausgewertet werden kann und keine Division durch Null auftritt.

**Input:** Ein Array von Strings `tokens`, das den RPN-Ausdruck repräsentiert.
**Output:** Eine Ganzzahl, die das endgültige berechnete Ergebnis darstellt.

## When to use it

- Um Code auszuführen! Genau so verarbeiten Computer tatsächlich mathematische Ausdrücke.

## Approach

**1. Die Eleganz von Postfix:**
Die menschliche Mathematik (Infix, wie `3 + 4 * 2`) ist für Computer unpraktisch, da man vorausschauen muss, um das `*` zu finden, es zu berechnen und dann zurückzugehen, um das `+` zu berechnen.
In Postfix (`3 4 2 * +`) ist die Mathematik völlig eindeutig und streng von links nach rechts strukturiert. Es gibt keine Klammern. Es gibt keine Vorrangregeln.

**2. Der Operand-Stack:**
Wir verarbeiten die Tokens streng von links nach rechts.
- Wenn wir eine Zahl sehen, pushen wir sie auf den Stack.
- Wenn wir einen Operator sehen, führen wir ein POP der obersten zwei Zahlen vom Stack durch!
  - Die erste gepoppte Zahl ist der `Right Operand`.
  - Die zweite gepoppte Zahl ist der `Left Operand`.
  - Wir wenden den Operator auf sie an: `Left [Operator] Right`.
  - Wir pushen das resultierende berechnete Integer-Ergebnis zurück auf den Stack!
Wenn der String vollständig verarbeitet ist, befindet sich genau EINE Zahl auf dem Stack. Das ist das Endergebnis!

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for stack_08: Evaluate Reverse Polish Notation.

Evaluate a postfix (Reverse Polish Notation) arithmetic
"""


def solve(tokens, n):
    """Evaluate a postfix expression and return the integer result."""
    if n == 0:
        return 0
    stack = []
    for tok in tokens:
        if tok in "+-*/":
            b = stack.pop()
            a = stack.pop()
            if tok == "+":
                stack.append(a + b)
            elif tok == "-":
                stack.append(a - b)
            elif tok == "*":
                stack.append(a * b)
            else:  # "/"
                # Truncate toward zero (Python's int() does this).
                stack.append(int(a / b))
        else:
            stack.append(int(tok))
    return stack[-1]
```

</details>

## Walk-through

`tokens = ["2", "1", "+", "3", "*"]`

1. `"2"`: Operand -> Stack = `[2]`.
2. `"1"`: Operand -> Stack = `[2, 1]`.
3. `"+"`: Operator -> Pop `1` (b), Pop `2` (a). Berechne `2 + 1 = 3`. Push `3`.
   - Stack = `[3]`.
4. `"3"`: Operand -> Stack = `[3, 3]`.
5. `"*"`: Operator -> Pop `3` (b), Pop `3` (a). Berechne `3 * 3 = 9`. Push `9`.
   - Stack = `[9]`.
6. Ende der Tokens. Gib `stack[0]` zurück.

Ergebnis: `9`. ✓
*(In menschlicher Infix-Notation war dies: `(2 + 1) * 3`)*

## Complexity

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(N)$ | $O(N)$ |
| **Durchschnittlicher Fall** | $O(N)$ | $O(N)$ |
| **Schlechtester Fall** | $O(N)$ | $O(N)$ |

Jedes Token wird in einem einzigen linearen Durchlauf genau einmal verarbeitet. Das Pushen und Poppen vom Stack sind $O(1)$-Operationen. Die Zeitkomplexität ist strikt $O(N)$.
Im schlimmsten Fall (ein Ausdruck, bei dem zuerst alle Zahlen und dann alle Operatoren stehen, z. B. `1 2 3 4 + + +`) hält der Stack vorübergehend $N/2$ Zahlen, bevor sie ausgewertet werden. Die Platzkomplexität ist $O(N)$.

## Variants & optimizations

- **Präfix-Notation (Polnische Notation):** Z. B. `+ * 2 3 4`. Der exakt gleiche Algorithmus findet Anwendung, jedoch iteriert man über das Tokens-Array vollständig in umgekehrter Reihenfolge (von rechts nach links)! Wenn man zwei Elemente für einen Operator poppt, ist das erste gepoppte Element `a` (links) und das zweite `b` (rechts).

## Real-world applications

- **JVM / Bytecode-Ausführung:** Die Java Virtual Machine (JVM) ist im Grunde eine Stack-Maschine. Sie verwendet keine CPU-Register, um Variablen während mathematischer Operationen zu halten; sie kompiliert Java-Code buchstäblich in Postfix-Bytecodes (`iload_1`, `iload_2`, `iadd`) und führt diesen exakten Algorithmus aus!
- **HP-Taschenrechner:** Hewlett-Packard machte RPN in den 1970er Jahren für ihre wissenschaftlichen Taschenrechner populär, da es Benutzern ermöglichte, komplexe Formeln auszuwerten, ohne die Klammertiefe im Kopf behalten zu müssen.

## Related algorithms in cOde(n)

- **[stack_07 - Infix to Postfix Conversion](stack_07_infix-to-postfix-conversion.md)** — Die Engine, die menschliche Mathematik in das Array konvertiert, das dieser Algorithmus verarbeitet.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) verfasst wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitive Programmierung verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Seitenanfang. Quell-Repository: <https://github.com/dawei7/code_n>.*