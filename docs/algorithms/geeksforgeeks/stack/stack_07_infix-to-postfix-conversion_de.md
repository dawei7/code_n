# Infix-zu-Postfix-Konvertierung

| | |
|---|---|
| **ID** | `stack_07` |
| **Kategorie** | stack |
| **Komplexität (erforderlich)** | $O(N)$ Zeit, $O(N)$ Platz |
| **Schwierigkeit** | 5/10 |
| **Relevanz für Vorstellungsgespräche** | 4/10 |
| **GeeksForGeeks-Äquivalent** | [Convert Infix expression to Postfix expression](https://www.geeksforgeeks.org/convert-infix-expression-to-postfix-expression/) |

## Problemstellung

Gegeben ist ein String, der einen arithmetischen Ausdruck in **Infix**-Notation darstellt (z. B. `A + B * C`). Konvertieren Sie diesen in die **Postfix**-Notation (z. B. `A B C * +`).
Die Konvertierung muss die standardmäßige mathematische Operatorrangfolge (z. B. haben `*` und `/` eine höhere Priorität als `+` und `-`) sowie Klammern `()` berücksichtigen.

**Eingabe:** Ein String `s`, der den Infix-Ausdruck darstellt.
**Ausgabe:** Ein String, der den Postfix-Ausdruck darstellt.

## Wann man es verwendet

- Beim Entwurf eines Compilers oder Interpreters. Moderne Computer können die standardmäßige „menschliche“ Infix-Notation aufgrund willkürlicher Rangfolgeregeln mathematisch nicht nativ auswerten. Sie MÜSSEN den Ausdruck zuerst in Postfix (umgekehrte polnische Notation) oder in abstrakte Syntaxbäume (Abstract Syntax Trees) konvertieren.

## Ansatz

**1. Die Shunting-Yard-Analogie:**
Dieser von Edsger Dijkstra erfundene Algorithmus ist analog zu einem Rangierbahnhof. Zahlen (Operanden) sind Eisenbahnwaggons, die direkt zum Ausgangsgleis durchfahren. Operatoren (`+`, `*`) werden in einen Rangierbahnhof (den Stack) umgeleitet, wo sie basierend auf ihrer Priorität warten, bis sie an der Reihe sind.

**2. Die Regeln für den Operator-Stack:**
Wir verarbeiten den String von links nach rechts.
- Wenn wir eine Zahl/einen Buchstaben sehen, hängen wir ihn sofort an den Ausgabe-String an. (Operanden kommen NIEMALS in den Stack).
- Wenn wir einen Operator sehen (z. B. `+`), betrachten wir den Stack.
  - Wenn das oberste Element des Stacks einen Operator mit **strikt geringerer** Priorität hat (z. B. Stack enthält `-` und wir haben `*`), pushen wir unseren Operator einfach auf den Stack.
  - Wenn das oberste Element des Stacks einen Operator mit **höherer oder gleicher** Priorität hat (z. B. Stack enthält `*` und wir haben `+`), hat der Stack-Operator Vorrang! Wir führen ein POP des `*` vom Stack aus und hängen es an die Ausgabe an. Wir führen so lange POP-Operationen durch, bis wir einen Operator mit geringerer Priorität finden, und DANN pushen wir unser `+` auf den Stack.

**3. Die Regeln für Klammern:**
Klammern setzen die standardmäßige Rangfolge physisch außer Kraft.
- Wenn wir `(` sehen, pushen wir es direkt auf den Stack. Es fungiert als absolute Barriere.
- Wenn wir `)` sehen, führen wir kontinuierlich POP-Operationen für Operatoren vom Stack aus und hängen sie an die Ausgabe an, bis wir auf das passende `(` stoßen. Dann verwerfen wir beide Klammern.

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for stack_07: Infix to Postfix Conversion.

Convert an infix arithmetic expression (operators
"""


def solve(expr, n):
    """Shunting-yard: infix -> postfix."""
    if n == 0:
        return ""
    prec = {"+": 1, "-": 1, "*": 2, "/": 2}
    stack = []
    out = []
    for ch in expr:
        if ch.isalnum():
            out.append(ch)
        elif ch == "(":
            stack.append(ch)
        elif ch == ")":
            while stack and stack[-1] != "(":
                out.append(stack.pop())
            if stack:
                stack.pop()  # pop the "("
        else:  # operator
            while stack and stack[-1] != "(" and prec.get(stack[-1], 0) >= prec[ch]:
                out.append(stack.pop())
            stack.append(ch)
    while stack:
        out.append(stack.pop())
    return "".join(out)
```

</details>

## Durchlauf

`expression = "A+B*C-D"`

1. `A`: Operand -> Ausgabe = `"A"`. Stack = `[]`.
2. `+`: Operator -> Stack ist leer. Push `+`. Stack = `[+]`.
3. `B`: Operand -> Ausgabe = `"A B"`.
4. `*`: Operator -> Oberstes Element ist `+`. `*` > `+`. Push `*`. Stack = `[+, *]`.
5. `C`: Operand -> Ausgabe = `"A B C"`.
6. `-`: Operator -> Oberstes Element ist `*`. `-` <= `*`. Pop `*` zur Ausgabe!
   - Ausgabe = `"A B C *"`. Stack = `[+]`.
   - Oberstes Element ist `+`. `-` <= `+`. Pop `+` zur Ausgabe!
   - Ausgabe = `"A B C * +"`. Stack = `[]`.
   - Stack ist leer. Push `-`. Stack = `[-]`.
7. `D`: Operand -> Ausgabe = `"A B C * + D"`.
8. Ende des Strings. Verbleibende Elemente vom Stack poppen: `-`.
   - Ausgabe = `"A B C * + D -"`.

Ergebnis: `ABC*+D-`. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(N)$ | $O(N)$ |
| **Durchschnittlicher Fall** | $O(N)$ | $O(N)$ |
| **Schlechtester Fall** | $O(N)$ | $O(N)$ |

Jedes einzelne Zeichen im String wird genau einmal verarbeitet.
Obwohl es eine `while`-Schleife innerhalb des Operator-Zweigs gibt, kann ein Operator nur EINMAL auf den Stack gepusht und daher nur EINMAL gepoppt werden.
Somit führt die `while`-Schleife über die gesamte Ausführung des Algorithmus hinweg global maximal N-mal aus.
Die Zeitkomplexität ist strikt $O(N)$.
Die Platzkomplexität beträgt $O(N)$ für den Stack und das Ausgabe-Array.

## Varianten & Optimierungen

- **Abstrakter Syntaxbaum (AST):** Anstatt einen String auszugeben, kann der Algorithmus trivial modifiziert werden, um einen Knoten eines Binärbaums auszugeben! Wenn ein Operator gepoppt wird, poppen Sie die letzten beiden Elemente aus der Ausgabe, fügen Sie sie als `left` und `right` Kinder des Operators hinzu und pushen Sie den Operator selbst zurück in die Ausgabe!

## Anwendungen in der Praxis

- **Taschenrechner / Mathematische Parser:** Der grundlegende Algorithmus innerhalb der `eval()`-Funktion von Python und Standard-GUI-Taschenrechnern, um Benutzereingaben zu parsen.

## Verwandte Algorithmen in cOde(n)

- **[stack_08 - Evaluate Reverse Polish Notation](stack_08_evaluate-reverse-polish-notation.md)** — Der Schwester-Algorithmus, der die hier generierte Ausgabe nimmt und die mathematischen Berechnungen tatsächlich ausführt.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) verfasst wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für Wettbewerbsprogrammierung verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Anfang der Seite. Quell-Repository: <https://github.com/dawei7/code_n>.*