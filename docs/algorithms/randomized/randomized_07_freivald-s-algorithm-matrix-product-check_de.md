# Freivalds-Algorithmus (Matrixprodukt-Prüfung)

| | |
|---|---|
| **ID** | `randomized_07` |
| **Kategorie** | randomized |
| **Komplexität (erforderlich)** | $O(k * N^2)$ |
| **Schwierigkeit** | 5/10 |
| **Relevanz für Vorstellungsgespräche** | 2/10 |
| **Wikipedia** | [Freivalds' algorithm](https://en.wikipedia.org/wiki/Freivalds%27_algorithm) |

## Problemstellung

Gegeben sind drei N x N Matrizen A, B und C. Überprüfen Sie, ob die Matrixmultiplikation von A und B gleich C ist (d. h. prüfen Sie, ob A x B = C gilt).
Eine naive Überprüfung würde einfach A x B berechnen und das Ergebnis mit C vergleichen, was bei Verwendung der Standardmultiplikation $O(N^3)$ Zeit in Anspruch nimmt.
Entwerfen Sie einen randomisierten Algorithmus, um die Gleichheit mit hoher Wahrscheinlichkeit in $O(N^2)$ Zeit zu verifizieren!

**Eingabe:** Drei 2D-Arrays A, B, C der Größe N x N.
**Ausgabe:** Boolean `True`, falls A x B = C, andernfalls `False`.

## Wann man ihn verwendet

- Wenn die Verifizierung eines rechenintensiven Ergebnisses wesentlich kostengünstiger ist als die eigene Berechnung des Ergebnisses.
- Ein klassisches Beispiel für einen Monte-Carlo-Algorithmus mit einseitigem Fehler (wenn er `False` ausgibt, ist es zu 100 % `False`. Wenn er `True` ausgibt, ist es *wahrscheinlich* `True`).

## Ansatz

Wenn wir versuchen, A x B zu berechnen, dauert dies $O(N^3)$.
Der elegante Trick von Freivalds besteht darin, einen zufälligen N x 1 Spaltenvektor r einzuführen, der nur `0`en und `1`en enthält.

Anstatt zu prüfen, ob A x B = C gilt, prüfen wir, ob A x (B x r) = C x r gilt.

**Warum ist das schneller?**
Weil die Matrixmultiplikation assoziativ ist!
1. Die Multiplikation von B (einer N x N Matrix) mit r (einem N x 1 Vektor) ergibt einen neuen N x 1 Vektor. Dies dauert exakt $O(N^2)$ Zeit!
2. Die Multiplikation von A (N x N) mit diesem neuen Vektor (N x 1) benötigt weitere $O(N^2)$ Zeit!
3. Die Multiplikation von C (N x N) mit r (N x 1) dauert $O(N^2)$ Zeit!
Durch die Multiplikation mit dem Zufallsvektor vermeiden wir die $O(N^3)$ Matrix-Matrix-Multiplikation vollständig und führen nur drei $O(N^2)$ Matrix-Vektor-Multiplikationen durch!

**Die Mathematik (Fehlerwahrscheinlichkeit):**
Wenn A x B = C gilt, dann wird A x (B x r) IMMER gleich C x r sein. (0 % Fehlerwahrscheinlichkeit).
Wenn A x B \neq C gilt, wie hoch ist die Wahrscheinlichkeit, dass sie nach der Multiplikation mit r auf wundersame Weise gleich sind?
Freivalds hat bewiesen, dass die Wahrscheinlichkeit eines falsch-positiven Ergebnisses für einen zufällig generierten 0/1-Vektor höchstens \frac{1}{2} beträgt!
Wenn wir diesen Test k-mal mit k verschiedenen Zufallsvektoren wiederholen, sinkt die Wahrscheinlichkeit eines falsch-positiven Ergebnisses exponentiell auf \frac{1}{2^k}.
Bereits bei k=10 Iterationen liegt die Fehlerrate bei < 0,1 %. Bei k=40 liegt die Fehlerrate bei weniger als eins zu einer Billion.

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for randomized_07: Freivald's Algorithm (Matrix Product Check).

Given three square n x n matrices A, B, C,
"""


def solve(mat_a, mat_b, mat_c, size, trials, seed_value):
    """Freivald's algorithm: k iterations of random
    vector r in {0, 1}^n; check if A*(B*r) == C*r.
    """
    import random
    rng = random.Random(seed_value)
    n = size
    A = mat_a
    B = mat_b
    C = mat_c
    for _ in range(max(1, trials)):
        r = [rng.randint(0, 1) for _ in range(n)]
        # Compute B * r.
        Br = [0] * n
        for i in range(n):
            s = 0
            for j in range(n):
                s += B[i][j] * r[j]
            Br[i] = s
        # Compute C * r.
        Cr = [0] * n
        for i in range(n):
            s = 0
            for j in range(n):
                s += C[i][j] * r[j]
            Cr[i] = s
        # Compute A * (B * r).
        ABr = [0] * n
        for i in range(n):
            s = 0
            for j in range(n):
                s += A[i][j] * Br[j]
            ABr[i] = s
        # Check A * (B * r) == C * r componentwise.
        if ABr != Cr:
            return False
    return True
```

</details>

## Durchlauf

Nehmen wir an, A x B \neq C und es gibt einen Fehler in der ersten Zeile.
`N = 2`.
`A * B = [[5, 5], [0, 0]]`
`C =     [[5, 6], [0, 0]]` *(Der Fehler ist 6 statt 5)*.

1. Zufallsvektor `r = [1, 1]`.
2. Berechne ABr = [[5, 5], [0, 0]] x [1, 1]^T = [10, 0]^T.
3. Berechne Cr = [[5, 6], [0, 0]] x [1, 1]^T = [11, 0]^T.
4. `[10, 0] != [11, 0]`. Der Algorithmus gibt sofort `False` zurück!

Was ist, wenn `r = [1, 0]`?
- ABr = [5, 0]^T.
- Cr = [5, 0]^T.
- `[5, 0] == [5, 0]`. FALSCH-POSITIV!
Deshalb müssen wir ihn k-mal ausführen. Der nächste Durchlauf wird wahrscheinlich `[1, 1]` oder `[0, 1]` wählen und den Fehler finden.

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(N^2)$ | $O(N)$ |
| **Durchschnittlicher Fall** | $O(k * N^2)$ | $O(N)$ |
| **Schlechtester Fall** | $O(k * N^2)$ | $O(N)$ |

Für jede der k Iterationen führen wir exakt drei Matrix-Vektor-Multiplikationen durch. Jede Multiplikation erfordert das Iterieren über N x N Elemente. Die Gesamtzeit beträgt $O(k \cdot N^2)$. Da k eine kleine Konstante ist, ist dies strikt $O(N^2)$, wodurch die Schranke des Strassen-Algorithmus für die Matrixmultiplikation ($O(N^{2.81})$) umgangen wird.
Die Platzkomplexität beträgt $O(N)$, um die 1D-Vektoren `r`, `Br`, `ABr` und `Cr` zu speichern.

## Varianten & Optimierungen

- **Fingerprinting:** Der Freivalds-Algorithmus ist eine spezifische Anwendung des "Polynomial Identity Testing" (Schwartz-Zippel-Lemma). Dieses übergeordnete Konzept – das Komprimieren massiver mathematischer Strukturen mittels Zufalls-Seeds zur Überprüfung auf Gleichheit – wird intensiv beim String-Fingerprinting (Rabin-Karp) und bei Merkle-Trees verwendet.

## Anwendungen in der Praxis

- **Hardware-Verifizierung:** Beim Entwurf spezialisierter ASICs oder GPUs für Tensor-Berechnungen kann man den Freivalds-Algorithmus in der Test-Suite verwenden, um schnell zu verifizieren, dass die Silizium-Logik Matrizen korrekt multipliziert, ohne auf die vollständige $O(N^3)$ CPU-Validierung warten zu müssen.

## Verwandte Algorithmen in cOde(n)

- **[randomized_06 - Estimating Pi](randomized_06_estimating-pi-via-monte-carlo.md)** — Ein weiterer grundlegender Monte-Carlo-Algorithmus.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) geschrieben wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für Wettbewerbsprogrammierung verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Seitenanfang. Quell-Repository: <https://github.com/dawei7/code_n>.*