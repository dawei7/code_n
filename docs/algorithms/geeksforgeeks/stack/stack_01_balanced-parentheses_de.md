# Balanced Parentheses

| | |
|---|---|
| **ID** | `stack_01` |
| **Kategorie** | stack |
| **Komplexität (erforderlich)** | $O(N)$ |
| **Schwierigkeit** | 2/10 |
| **Relevanz für Vorstellungsgespräche** | 9/10 |
| **LeetCode-Äquivalent** | [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) |

## Problemstellung

Gegeben ist ein String `s`, der nur die Zeichen `'('`, `')'`, `'{'`, `'}'`, `'['` und `']'` enthält. Bestimme, ob der Eingabestring gültig ist.
Ein Eingabestring ist gültig, wenn:
1. Öffnende Klammern durch den gleichen Typ von Klammern geschlossen werden.
2. Öffnende Klammern in der korrekten Reihenfolge geschlossen werden.
3. Jede schließende Klammer eine entsprechende öffnende Klammer desselben Typs hat.

**Eingabe:** Ein String `s`.
**Ausgabe:** Ein boolescher Wert, der angibt, ob der String perfekt balanciert ist.

**Beispiel 1:**
`s = "()[]{}"`
Ausgabe: `True`.

**Beispiel 2:**
`s = "([)]"`
Ausgabe: `False`. (Die `]` versucht die `[` zu schließen, während die `(` noch aktiv offen ist).

## Anwendung

- Dies ist die klassische Einführung in die **Stack**-Datenstruktur.
- Wird universell in Compilern und Syntax-Lintern verwendet, um die Codestruktur zu verifizieren.

## Ansatz

Ein Stack folgt dem **LIFO**-Prinzip (Last-In, First-Out). Dies bildet verschachtelte Strukturen perfekt ab, da die *zuletzt geöffnete* Klammer diejenige ist, die *zuerst* geschlossen werden muss.

1. Initialisiere einen leeren Stack.
2. Iteriere durch jedes Zeichen im String:
   - Wenn das Zeichen eine **öffnende Klammer** (`(`, `{`, `[`) ist, führe ein `push` auf den Stack aus.
   - Wenn das Zeichen eine **schließende Klammer** (`)`, `}`, `]`) ist:
     - Wenn der Stack leer ist, bedeutet dies, dass wir versuchen, eine Klammer zu schließen, die nie geöffnet wurde. Gib `False` zurück.
     - Führe ein `pop` des obersten Elements vom Stack aus.
     - Überprüfe, ob die gepoppte öffnende Klammer zum Typ der aktuellen schließenden Klammer passt. Wenn sie nicht übereinstimmen, gib `False` zurück.
3. Überprüfe nach Abschluss der Schleife den Stack. Wenn er leer ist, wurden alle geöffneten Klammern erfolgreich geschlossen (gib `True` zurück). Wenn er noch Elemente enthält, wurden einige Klammern geöffnet, aber nie geschlossen (gib `False` zurück).

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for stack_01: Balanced Parentheses.

Walk the string; push each opening bracket, and on a closing
bracket pop the top and check that it pairs correctly. Return
True iff the stack is empty at the end. O(n).
"""


def solve(s, n):
    pairs = {")": "(", "]": "[", "}": "{"}
    stack = []
    for ch in s:
        if ch in "([{":
            stack.append(ch)
        elif ch in ")]}":
            if not stack or stack[-1] != pairs[ch]:
                return False
            stack.pop()
    return not stack
```

</details>

## Durchlauf

`s = "{[()]}"`

1. `char = '{'`. Öffnend. `push`. Stack: `['{']`.
2. `char = '['`. Öffnend. `push`. Stack: `['{', '[']`.
3. `char = '('`. Öffnend. `push`. Stack: `['{', '[', '(']`.
4. `char = ')'`. Schließend. 
   - `pop` oberstes Element: `'('`. 
   - Passt `'('` zu `matching_bracket[')']`? Ja.
   - Stack: `['{', '[']`.
5. `char = ']'`. Schließend.
   - `pop` oberstes Element: `'['`.
   - Passt `'['` zu `matching_bracket[']']`? Ja.
   - Stack: `['{']`.
6. `char = '}'`. Schließend.
   - `pop` oberstes Element: `'{'`.
   - Passt `'{'` zu `matching_bracket['}']`? Ja.
   - Stack: `[]`.

Schleife endet. Stack ist leer. Gib `True` zurück. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(N)$ | $O(1)$ |
| **Durchschnittlicher Fall** | $O(N)$ | $O(N)$ |
| **Schlechtester Fall** | $O(N)$ | $O(N)$ |

Wir verarbeiten jedes Zeichen im String genau einmal. Dictionary-Lookups und Stack-`push`/`pop`-Operationen benötigen $O(1)$ Zeit. Die Zeitkomplexität beträgt $O(N)$.
Im schlechtesten Fall (z. B. `s = "(((((((((("`) pushen wir alle $N$ Zeichen auf den Stack. Die Platzkomplexität beträgt $O(N)$.

## Varianten & Optimierungen

- **Einzelner Klammertyp $O(1)$ Platz:** Wenn der String NUR `(` und `)` enthält, benötigt man keinen Stack! Man kann einfach einen Integer `count` führen. Inkrementiere bei `(`, dekrementiere bei `)`. Wenn `count` jemals unter 0 fällt, gib `False` zurück. Am Ende gib `count == 0` zurück.
- **Longest Valid Parentheses (DP):** Ein deutlich schwierigeres Problem, das nach der Länge des längsten gültigen zusammenhängenden Teilstrings fragt.

## Anwendungen in der Praxis

- **HTML/XML-Parsing:** Browser verwenden genau diese Stack-Logik, um sicherzustellen, dass ein `<h1>`-Tag durch ein `</h1>`-Tag geschlossen wird, bevor das übergeordnete `<div>` geschlossen wird.

## Verwandte Algorithmen in cOde(n)

- **[stack_08 - Evaluate Reverse Polish Notation](stack_08_evaluate-reverse-polish-notation.md)** — Eine weitere grundlegende Anwendung von Stacks bei der sequenziellen Verarbeitung linearer Strings.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) geschrieben wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitive Programmierung verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folge dem Wikipedia-Link am Seitenanfang. Quell-Repository: <https://github.com/dawei7/code_n>.*