# Strassen-Matrixmultiplikation

| | |
|---|---|
| **ID** | `dc_06` |
| **Kategorie** | divide_conquer |
| **Komplexität (erforderlich)** | $O(N^2.81)$ Zeit, $O(N^2)$ Platz |
| **Schwierigkeit** | 10/10 |
| **Relevanz für Vorstellungsgespräche** | 1/10 |
| **Wikipedia** | [Strassen-Algorithmus](https://en.wikipedia.org/wiki/Strassen_algorithm) |

## Problemstellung

Gegeben sind zwei quadratische Matrizen `A` und `B` der Größe N x N. Berechne deren Matrixprodukt C = A x B.
Wir nehmen der Einfachheit halber an, dass N eine Zweierpotenz ist.

**Eingabe:** Zwei 2D-Matrizen `A` und `B` der Dimensionen N x N.
**Ausgabe:** Eine 2D-Matrix, die das Produkt darstellt.

## Wann man ihn verwendet

- Ausschließlich ein akademischer Algorithmus, um fortgeschrittene theoretische obere Schranken der Informatik zu verstehen.
- Er ist das 2D-Matrix-Äquivalent zur Karatsuba-Multiplikation (`dc_04`) und beweist, dass $O(N^3)$ NICHT der schnellste Weg zur Multiplikation von Matrizen ist.

## Ansatz

**1. Der naive Ansatz ($O(N^3)$):**
Die Standard-Matrixmultiplikation berechnet jede Zelle C_{i,j} durch das Skalarprodukt der i-ten Zeile von A und der j-ten Spalte von B. Da es N^2 Zellen gibt und jedes Skalarprodukt N Multiplikationen erfordert, beträgt die Zeitkomplexität strikt $O(N^3)$.

**2. Naives Divide and Conquer ($O(N^3)$):**
Wir können die N x N Matrizen rekursiv in vier kleinere (N/2) x (N/2) Teilmatrizen (Quadranten) unterteilen.
$ A = \begin{bmatrix} A_{11} & A_{12} \\ A_{21} & A_{22} \end{bmatrix}, B = \begin{bmatrix} B_{11} & B_{12} \\ B_{21} & B_{22} \end{bmatrix} 
Die resultierende Matrix C wird wie folgt berechnet:
C_{11} = (A_{11} \times B_{11}) + (A_{12} \times B_{21})
C_{12} = (A_{11} \times B_{12}) + (A_{12} \times B_{22})
C_{21} = (A_{21} \times B_{11}) + (A_{22} \times B_{21})
C_{22} = (A_{21} \times B_{12}) + (A_{22} \times B_{22})

Beachte, dass wir zur Berechnung der 4 Quadranten von C **8 rekursive Multiplikationen** von Matrizen der Größe (N/2) durchführen müssen.
Nach dem Master-Theorem gilt T(N) = 8T(N/2) + $O(N^2)$ \implies $O(N^{\log_2(8)}$) = $O(N^3)$. Keine Verbesserung!

**3. Strassens "Zaubertrick" ($O(N^{2.81})$):**
Im Jahr 1969 entdeckte Volker Strassen eine unglaublich kontraintuitive algebraische Formel, die dieselben 4 Quadranten von C unter Verwendung von nur **7 rekursiven Multiplikationen** anstelle von 8 berechnet!
Er definierte 7 Zwischenmatrizen (M_1 bis M_7):
- M_1 = (A_{11} + A_{22}) \times (B_{11} + B_{22})
- M_2 = (A_{21} + A_{22}) \times B_{11}
- M_3 = A_{11} \times (B_{12} - B_{22})
- M_4 = A_{22} \times (B_{21} - B_{11})
- M_5 = (A_{11} + A_{12}) \times B_{22}
- M_6 = (A_{21} - A_{11}) \times (B_{11} + B_{12})
- M_7 = (A_{12} - A_{22}) \times (B_{21} + B_{22})

Unter Verwendung dieser 7 Matrizen werden die finalen 4 Quadranten von C rein durch Addition und Subtraktion (was $O(N^2)$ schnell ist!) wieder zusammengesetzt:
- C_{11} = M_1 + M_4 - M_5 + M_7
- C_{12} = M_3 + M_5
- C_{21} = M_2 + M_4
- C_{22} = M_1 - M_2 + M_3 + M_6

Die neue Rekursionsgleichung lautet T(N) = 7T(N/2) + $O(N^2)$.
Nach dem Master-Theorem beträgt die Zeitkomplexität $O(N^{\log_2(7)}$) \approx $O(N^{2.807})$.

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for dc_06: Strassen Matrix Multiplication.

Multiply two 2x2 matrices using Strassen's algorithm
"""


def solve(A, B, n):
    """Strassen 2x2 matrix multiplication.

    Seven products (p1..p7) replace the schoolbook eight,
    trading a few extra additions for one fewer multiply.
    """
    if n == 1:
        return [[A[0][0] * B[0][0]]]
    if n == 2:
        a, b, c, d = A[0][0], A[0][1], A[1][0], A[1][1]
        e, f, g, h = B[0][0], B[0][1], B[1][0], B[1][1]
        p1 = a * (f - h)
        p2 = (a + b) * h
        p3 = (c + d) * e
        p4 = d * (g - e)
        p5 = (a + d) * (e + h)
        p6 = (b - d) * (g + h)
        p7 = (a - c) * (e + f)
        c00 = p5 + p4 - p2 + p6
        c01 = p1 + p2
        c10 = p3 + p4
        c11 = p1 + p5 - p3 - p7
        return [[c00, c01], [c10, c11]]
    return _naive(A, B, n)

def _naive(A, B, n):
    C = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C
```

</details>

## Erläuterung

Aufgrund der hohen arithmetischen Komplexität wird auf eine manuelle Schritt-für-Schritt-Durchführung verzichtet. Die algebraische Expansion von C_{12} = M_3 + M_5 beweist die Logik perfekt:
M_3 + M_5 = [A_{11} \times (B_{12} - B_{22})] + [(A_{11} + A_{12}) \times B_{22}]
= A_{11}B_{12} - A_{11}B_{22} + A_{11}B_{22} + A_{12}B_{22}
= A_{11}B_{12} + A_{12}B_{22} (Die exakte Definition von C_{12}!)

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(N^2.81)$ | $O(N^2)$ |
| **Durchschnittlicher Fall** | $O(N^2.81)$ | $O(N^2)$ |
| **Schlechtester Fall** | $O(N^2.81)$ | $O(N^2)$ |

Der Algorithmus eliminiert einen rekursiven Multiplikationsaufruf und ändert T(N) = 8T(N/2) in T(N) = 7T(N/2). Die Zeitkomplexität sinkt strikt auf $O(N^{2.807})$.
Die Platzkomplexität beträgt $O(N^2)$ aufgrund der ständigen Allokation temporärer Teilmatrizen während der Additions- und Subtraktionsoperationen auf jeder Ebene des Rekursionsbaums.

## Varianten & Optimierungen

- **Coppersmith-Winograd-Algorithmus:** Strassen war erst der Anfang. Die theoretische Grenze wurde von Coppersmith und Winograd (und in jüngerer Zeit noch weiter) auf $O(N^{2.37})$ gesenkt. Diese Algorithmen werden jedoch als "Galaktische Algorithmen" bezeichnet – ihr konstanter Overhead ist so astronomisch groß, dass sie Strassen nur bei Matrizen übertreffen würden, die so massiv sind, dass sie nicht in das physische Universum passen würden.
- **Strassen-Schwellenwert:** Wie Karatsuba hat Strassen einen massiven Overhead durch Array-Allokationen und Additionen. Standardbibliotheken (wie BLAS oder NumPy) prüfen die Matrixgröße. Wenn N < \text{Schwellenwert} (z. B. 64 oder 128), wird auf eine hochoptimierte $O(N^3)$-Multiplikation auf Hardware-Ebene zurückgegriffen.

## Praxisanwendungen

- **Deep Learning / Neuronale Netze:** Während die Standard-$O(N^3)$-Multiplikation auf GPUs unter Verwendung von Tensor Cores stark optimiert ist, greifen einige hochspezialisierte mathematische Berechnungsbibliotheken bei massiven algebraischen Systemen auf strengen CPU-Architekturen auf Strassen zurück.

## Verwandte Algorithmen in cOde(n)

- **[dc_04 - Karatsuba-Multiplikation](dc_04_karatsuba-multiplication.md)** — Das 1D-Äquivalent für die Ganzzahlmultiplikation, das 1 von 4 rekursiven Aufrufen eliminiert ($O(N^{1.58})$).

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) verfasst wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitives Programmieren verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folge dem Wikipedia-Link am Seitenanfang. Quell-Repository: <https://github.com/dawei7/code_n>.*