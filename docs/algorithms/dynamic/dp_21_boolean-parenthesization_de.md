# Boolean Parenthesization

| | |
|---|---|
| **ID** | `dp_21` |
| **Kategorie** | dynamic |
| **Komplexität (erforderlich)** | $O(N^3)$ Zeit, $O(N^2)$ Platz |
| **Schwierigkeit** | 8/10 |
| **Relevanz für Vorstellungsgespräche** | 5/10 |
| **GeeksForGeeks Äquivalent** | [Boolean Parenthesization Problem](https://www.geeksforgeeks.org/boolean-parenthesization-problem-dp-37/) |

## Problemstellung

Gegeben ist ein boolescher Ausdruck, der aus den Symbolen `T` (True) und `F` (False) besteht, getrennt durch die booleschen Operatoren `&` (AND), `|` (OR) und `^` (XOR).
Zählen Sie die Anzahl der Möglichkeiten, den Ausdruck zu klammern, sodass der gesamte Ausdruck zu `True` evaluiert.

**Eingabe:** Ein String `s` der Länge N, der an geraden Indizes die Symbole `T, F` und an ungeraden Indizes die Operatoren `&, |, ^` enthält.
**Ausgabe:** Eine Ganzzahl, die die Anzahl der gültigen Klammerungen darstellt. (Oft modulo 10^9 + 7).

## Wann man es verwendet

- Der ultimative Test für **Interval DP** in Kombination mit kombinatorischer Logik.
- Wenn Sie dies lösen können, ist Matrix Chain Multiplication (`dp_13`) trivial für Sie.

## Ansatz

**1. Definition des Zustands:**
Im Gegensatz zur Matrix Chain Multiplication reicht ein einzelnes DP-Array nicht aus! Wir müssen nicht nur wissen, auf wie viele Arten ein Teilausdruck zu `True` evaluiert. Aufgrund des `^` (XOR)-Operators kann ein `True` durch `True ^ False` UND `False ^ True` gebildet werden!
Daher müssen wir SOWOHL die `True`-Wege als auch die `False`-Wege verfolgen.
- `dpT[i][j]` = Anzahl der Möglichkeiten, wie der Teilausdruck vom Index `i` bis `j` zu `True` evaluiert.
- `dpF[i][j]` = Anzahl der Möglichkeiten, wie der Teilausdruck vom Index `i` bis `j` zu `False` evaluiert.

*(Hinweis: `i` und `j` zeigen nur auf die `T/F`-Symbole, die sich an den geraden Indizes 0, 2, 4... befinden)*

**2. Bestimmung der Basisfälle:**
Wenn `i == j`, ist der Teilausdruck ein einzelnes Symbol!
- Wenn `s[i] == 'T'`, dann `dpT[i][i] = 1` und `dpF[i][i] = 0`.
- Wenn `s[i] == 'F'`, dann `dpT[i][i] = 0` und `dpF[i][i] = 1`.

**3. Bestimmung des Übergangs (Die Rekurrenz):**
Um einen Ausdruck von `i` bis `j` zu evaluieren, teilen wir ihn an jedem möglichen Operator `k`.
Da die Symbole an geraden Indizes stehen, befinden sich die Operatoren an den ungeraden Indizes k = i+1, i+3, \dots, j-1.
Der linke Teilausdruck ist `i` bis `k-1`. Der rechte Teilausdruck ist `k+1` bis `j`.
Für einen spezifischen Operator an `s[k]` multiplizieren wir die Kombinationen über Kreuz:
- `leftT = dpT[i][k-1]`, `leftF = dpF[i][k-1]`
- `rightT = dpT[k+1][j]`, `rightF = dpF[k+1][j]`

Abhängig von `s[k]`:
- **Wenn `&` (AND):**
  - Um `True` zu erhalten, MÜSSEN beide Seiten True sein. `Ways = leftT * rightT`.
  - Um `False` zu erhalten, funktioniert alles andere. `Ways = (leftT * rightF) + (leftF * rightT) + (leftF * rightF)`.
- **Wenn `|` (OR):**
  - Um `True` zu erhalten, muss mindestens eine Seite True sein. `Ways = (leftT * rightF) + (leftF * rightT) + (leftT * rightT)`.
  - Um `False` zu erhalten, MÜSSEN beide Seiten False sein. `Ways = leftF * rightF`.
- **Wenn `^` (XOR):**
  - Um `True` zu erhalten, müssen die Seiten UNTERSCHIEDLICH sein. `Ways = (leftT * rightF) + (leftF * rightT)`.
  - Um `False` zu erhalten, müssen die Seiten GLEICH sein. `Ways = (leftT * rightT) + (leftF * rightF)`.

Wir summieren diese `Ways` über ALLE möglichen Teilungspunkte `k`, um `dpT[i][j]` und `dpF[i][j]` aufzubauen!

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for dp_21: Boolean Parenthesization.

Count the number of ways to parenthesize a boolean
expression (operands T/F, operators &|^) so it evaluates
to True. Interval DP: T[i][j] / F[i][j] = count of ways
for s[i..j]. At each split, combine the four quadrants
based on the operator.
"""


def solve(s, n):
    if n == 0:
        return 0
    T = [[0] * n for _ in range(n)]
    F = [[0] * n for _ in range(n)]
    for i in range(0, n, 2):
        T[i][i] = 1 if s[i] == "T" else 0
        F[i][i] = 1 if s[i] == "F" else 0
    for gap in range(2, n, 2):
        for i in range(0, n - gap, 2):
            j = i + gap
            T[i][j] = F[i][j] = 0
            for k in range(i + 1, j, 2):
                op = s[k]
                lt, lf = T[i][k - 1], F[i][k - 1]
                rt, rf = T[k + 1][j], F[k + 1][j]
                if op == "&":
                    T[i][j] += lt * rt
                    F[i][j] += lt * rf + lf * rt + lf * rf
                elif op == "|":
                    T[i][j] += lt * rt + lt * rf + lf * rt
                    F[i][j] += lf * rf
                else:  # ^
                    T[i][j] += lt * rf + lf * rt
                    F[i][j] += lt * rt + lf * rf
    return T[0][n - 1]
```

</details>

## Durchlauf

`s = "T|F&T"`. N=5.
Basisfälle (Länge 1):
`dpT[0][0]=1` (T), `dpF[2][2]=1` (F), `dpT[4][4]=1` (T).

1. **Länge 3:**
   - **i=0, j=2 (`T|F`):** Teilung bei k=1 (`|`).
     - `dpT[0][2] = (1*0) + (1*1) + (0*0) = 1`.
     - `dpF[0][2] = (0*1) = 0`.
   - **i=2, j=4 (`F&T`):** Teilung bei k=3 (`&`).
     - `dpT[2][4] = (0*1) = 0`.
     - `dpF[2][4] = (0*0) + (1*1) + (1*0) = 1`.

2. **Länge 5:**
   - **i=0, j=4 (`T|F&T`):**
     - Teilung bei k=1 (`|`): Links `T` (0...0), Rechts `F&T` (2...4).
       - `leftT=1`, `rightT=0` (aus `dpT[2][4]`), `rightF=1`.
       - `Ways True` für `|`: `(1*0) + (1*1) + (0*0) = 1`.
     - Teilung bei k=3 (`&`): Links `T|F` (0...2), Rechts `T` (4...4).
       - `leftT=1`, `rightT=1`, `rightF=0`.
       - `Ways True` für `&`: `(1*1) = 1`.
     - Gesamt `dpT[0][4]` = 1 + 1 = 2.

Ergebnis `dpT[0][4]` ist 2. ✓ (Die Möglichkeiten sind `(T|F)&T` -> `T&T` -> `T`, und `T|(F&T)` -> `T|F` -> `T`).

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(N^3)$ | $O(N^2)$ |
| **Durchschnittlicher Fall** | $O(N^3)$ | $O(N^2)$ |
| **Schlechtester Fall** | $O(N^3)$ | $O(N^2)$ |

Die Schleifen erzeugen $O(N^2)$ Intervalle. Für jedes Intervall testen wir $O(N)$ Teilungspunkte k. Die Gesamtzeit beträgt strikt $O(N^3)$.
Die Platzkomplexität erfordert zwei N x N Matrizen, was $O(N^2)$ Platz beansprucht.

## Varianten & Optimierungen

- **Top-Down Memoization:** Interval DP ist bekanntermaßen schwierig korrekt in Schleifen zu implementieren (Bottom-Up nach Länge). Viele Entwickler bevorzugen es, dies als rekursive Funktion `solve(i, j, is_true)` mit einem N x N x 2 Memoization-Cache zu schreiben. Die Zeit-/Platzkomplexität ist mathematisch identisch, aber es ist wesentlich einfacher zu lesen und unter Zeitdruck in einem Vorstellungsgespräch zu implementieren!

## Anwendungen in der Praxis

- **Compiler-Design:** Parsen von logischen Ausdrücken und Berechnen der Anzahl gültiger AST (Abstract Syntax Tree)-Generierungen für mehrdeutige Grammatiken.

## Verwandte Algorithmen in cOde(n)

- **[dp_13 - Matrix Chain Multiplication](dp_13_matrix-chain-multiplication.md)** — Das grundlegende Interval DP-Framework.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) erstellt wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitives Programmieren verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Seitenanfang. Quell-Repository: <https://github.com/dawei7/code_n>.*