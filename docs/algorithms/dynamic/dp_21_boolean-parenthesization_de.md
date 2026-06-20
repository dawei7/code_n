# Boolesche Klammerung

| | |
|---|---|
| **ID** | `dp_21` |
| **Kategorie** | dynamisch |
| **Komplexität (erforderlich)** | $O(N^3)$ Zeit, $O(N^2)$ Speicherplatz |
| **Schwierigkeitsgrad** | 8/10 |
| **Relevanz für Vorstellungsgespräche** | 5/10 |
| **GeeksForGeeks-Äquivalent** | [Problem zur booleschen Klammerung](https://www.geeksforgeeks.org/boolean-parenthesization-problem-dp-37/) |

## Problemstellung

Gegeben sei ein boolescher Ausdruck, bestehend aus den Symbolen `T` (Wahr) und `F` (Falsch), die durch boolesche Operatoren `&` (UND), `|` (ODER) und `^` (XOR) getrennt sind.
Zähle die Anzahl der Möglichkeiten, wie wir den Ausdruck so in Klammern setzen können, dass der gesamte Ausdruck den Wert `True` ergibt.

**Eingabe:** Eine Zeichenkette `s` der Länge N, die an geraden Indizes die Symbole `T, F` und an ungeraden Indizes die Operatoren `&, |, ^` enthält.
**Ausgabe:** Eine ganze Zahl, die die Anzahl der gültigen Klammerungsmöglichkeiten angibt. (Häufig modulo 10^9 + 7).

## Wann man es anwendet

- Der ultimative Test für **Intervall-DP** in Kombination mit kombinatorischer Logik.
- Wenn Sie diese Aufgabe lösen können, ist die Matrixkettenmultiplikation (`dp_13`) für Sie ein Kinderspiel.

## Vorgehensweise

**1. Definieren des Zustands:**
Anders als bei der Matrixkettenmultiplikation reicht ein einziges DP-Array nicht aus! Wir müssen nicht nur wissen, auf wie viele Arten ein Teilausdruck den Wert `True` ergibt. Aufgrund des `^` (XOR)-Operators kann ein `True` durch `True ^ False` UND `False ^ True` gebildet werden!
Daher müssen wir sowohl die `True` Möglichkeiten als auch die `False` Möglichkeiten verfolgen.
- `dpT[i][j]` = Anzahl der Möglichkeiten, auf die der Teilausdruck vom Index `i` bis `j` den Wert `True` ergibt.
- `dpF[i][j]` = Anzahl der Möglichkeiten, auf die der Teilausdruck vom Index `i` bis `j` den Wert `False` ergibt.

*(Hinweis: `i` und `j` verweisen nur auf die `T/F`-Symbole, die sich an den geraden Indizes 0, 2, 4 ... befinden)*

**2. Die Basisfälle ermitteln:**
Wenn `i == j`, ist der Teilausdruck ein einzelnes Symbol!
- Wenn `s[i] == 'T'`, dann `dpT[i][i] = 1` und `dpF[i][i] = 0`.
- Wenn `s[i] == 'F'`, dann `dpT[i][i] = 0` und `dpF[i][i] = 1`.

**3. Finde den Übergang (die Rekursionsbeziehung):**
Um einen Ausdruck von `i` bis `j` auszuwerten, teilen wir ihn an jedem möglichen Operator `k` auf.
Da sich die Symbole an geraden Indizes befinden, stehen die Operatoren an ungeraden Indizes k = i+1, i+3, \dots, j-1.
Der linke Teilausdruck ist `i` bis `k-1`. Der rechte Teilausdruck ist `k+1` bis `j`.
Für einen bestimmten Operator bei `s[k]` multiplizieren wir die Kombinationen kreuzweise:
- `leftT = dpT[i][k-1]`, `leftF = dpF[i][k-1]`
- `rightT = dpT[k+1][j]`, `rightF = dpF[k+1][j]`

Abhängig von `s[k]`:
- **Wenn `&` (UND):**
  - Um `True` zu erhalten, MÜSSEN beide Seiten wahr sein. `Ways = leftT * rightT`.
  - Um `False` zu erhalten, reicht jede andere Kombination aus. `Ways = (leftT * rightF) + (leftF * rightT) + (leftF * rightF)`.
- **Wenn `|` (ODER):**
  - Um `True` zu erhalten, muss mindestens eine Seite wahr sein. `Ways = (leftT * rightF) + (leftF * rightT) + (leftT * rightT)`.
  - Um `False` zu erhalten, MÜSSEN beide Seiten falsch sein. `Ways = leftF * rightF`.
- **Wenn `^` (XOR):**
  - Um `True` zu erhalten, müssen die Seiten UNTERSCHIEDLICH sein. `Ways = (leftT * rightF) + (leftF * rightT)`.
  - Um `False` zu erhalten, müssen die Seiten GLEICH sein. `Ways = (leftT * rightT) + (leftF * rightF)`.

Wir summieren diese `Ways` über ALLE möglichen Teilungspunkte `k` hinweg, um `dpT[i][j]` und `dpF[i][j]` zu bilden!

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

## Schritt-für-Schritt-Anleitung

`s = "T|F&T"`. N=5.
Basisfälle (Länge 1):
`dpT[0][0]=1` (T), `dpF[2][2]=1` (F), `dpT[4][4]=1` (T).

1. **Länge 3:**
   - **i=0, j=2 (`T|F`):** Aufteilung bei k=1 (`|`).
     - `dpT[0][2] = (1*0) + (1*1) + (0*0) = 1`.
 - `dpF[0][2] = (0*1) = 0`.
   - **i=2, j=4 (`F&T`):** Aufteilung bei k=3 (`&`).
     - `dpT[2][4] = (0*1) = 0`.
 - `dpF[2][4] = (0*0) + (1*1) + (1*0) = 1`.

2. **Länge 5:**
   - **i=0, j=4 (`T|F&T`):**
     - Aufteilung bei k=1 (`|`): Links `T` (0...0), Rechts `F&T` (2...4).
       - `leftT=1`, `rightT=0` (aus `dpT[2][4]`), `rightF=1`.
       - `Ways True` für `|`: `(1*0) + (1*1) + (0*0) = 1`.
     - Aufteilung bei k=3 (`&`): Links `T|F` (0...2), Rechts `T` (4...4).
       - `leftT=1`, `rightT=1`, `rightF=0`.
 - `Ways True` für `&`: `(1*1) = 1`.
     - Insgesamt `dpT[0][4]` = 1 + 1 = 2.

Das Ergebnis `dpT[0][4]` ist 2. ✓ (Möglichkeiten sind `(T|F)&T` -> `T&T` -> `T` sowie `T|(F&T)` -> `T|F` -> `T`).

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(N^3)$ | $O(N^2)$ |
| **Durchschnittlicher Fall** | $O(N^3)$ | $O(N^2)$ |
| **Schlechteste** | $O(N^3)$ | $O(N^2)$ |

Die Schleifen erzeugen $O(N^2)$ Intervalle. Für jedes Intervall testen wir $O(N)$ Teilungspunkte k. Die Gesamtzeit beträgt streng $O(N^3)$.
Die Platzkomplexität erfordert zwei N × N-Matrizen, die $O(N^2)$ Speicherplatz beanspruchen.

## Varianten & Optimierungen

- **Top-Down-Memoisation:** Intervall-DP ist bekanntermaßen schwierig korrekt zu schleifen (Bottom-Up nach Länge). Viele Entwickler ziehen es vor, dies als rekursive Funktion `solve(i, j, is_true)` mit einem N × N × 2-Memoization-Cache zu schreiben. Die Zeit- und Platzkomplexität ist mathematisch identisch, aber unter Zeitdruck in einem Vorstellungsgespräch ist dies wesentlich leichter zu lesen und zu implementieren!

## Praktische Anwendungen

- **Compiler-Design:** Parsen logischer Ausdrücke und Berechnen der Anzahl gültiger AST-Generationen (Abstract Syntax Tree) für mehrdeutige Grammatiken.

## Verwandte Algorithmen in cOde(n)

- **[dp_13 – Matrixkettenmultiplikation](dp_13_matrix-chain-multiplication.md)** — Das grundlegende Intervall-DP-Framework.

---

*Diese Dokumentation ist ein Originalbeitrag für cOde(n),
der sich an der kanonischen Struktur orientiert, die von Referenzseiten
zum Thema Wettbewerbsprogrammierung verwendet wird. Den kanonischen
Enzyklopädieeintrag finden Sie über den Wikipedia-Link oben auf der Seite.
Quell-Repository:
<https://github.com/dawei7/code_n>.*
