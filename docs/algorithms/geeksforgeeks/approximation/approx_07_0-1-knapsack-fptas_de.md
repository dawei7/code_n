# 0-1 Knapsack (FPTAS-Approximation)

| | |
|---|---|
| **ID** | `approx_07` |
| **Kategorie** | Approximation |
| **Komplexität (erforderlich)** | $O(N^3 / ε)$ |
| **Schwierigkeit** | 9/10 |
| **Relevanz für Vorstellungsgespräche** | 2/10 |
| **Wikipedia** | [Polynomial-time approximation scheme](https://en.wikipedia.org/wiki/Polynomial-time_approximation_scheme) |

## Problemstellung

Das 0-1 Knapsack-Problem ist NP-schwer, was bedeutet, dass kein Algorithmus in Polynomialzeit bekannt ist, um es exakt zu lösen. Es ist jedoch **schwach NP-schwer**, was bedeutet, dass es eine Lösung mittels Dynamischer Programmierung in $O(N \cdot W)$ gibt. Wenn die Kapazität W eine Milliarde beträgt, schlägt die DP fehl (pseudo-polynomiale Zeit).
Ihre Aufgabe ist es, ein **Fully Polynomial-Time Approximation Scheme (FPTAS)** zu implementieren. Gegeben einen Fehlerparameter \epsilon (z. B. \epsilon = 0.1 für eine Fehlertoleranz von 10 %), geben Sie eine gültige Packung für den Rucksack zurück, deren Gesamtwert mathematisch garantiert \ge (1 - \epsilon) x OPT ist, während die Laufzeit strikt polynomial in Bezug auf N und 1/\epsilon ist (völlig unabhängig vom massiven W!).

**Eingabe:** N Elemente mit `values` und `weights`, eine Kapazität `W` und ein Float `epsilon`.
**Ausgabe:** Der approximierte Maximalwert.

## Wann man es verwendet

- Wenn Sie eine massive Rucksackkapazität und astronomische Elementwerte haben, die sowohl Standard-DP-Arrays sprengen, Sie aber dennoch eine unglaublich präzise mathematische Garantie benötigen (z. B. 99,9 % optimal).

## Ansatz

Das Standard-Knapsack-DP-Array kann umgekehrt werden: Anstatt DP[weight] = max\_value können wir DP[value] = min\_weight verwenden!
Dieser DP[value]-Ansatz läuft in $O(N \cdot V_{max})$, wobei V_{max} die Summe aller Werte ist.
Wenn die Elementwerte in die Milliarden gehen, ist V_{max} massiv und $O(N \cdot V_{max})$ schlägt ebenfalls fehl.

**Die brillante FPTAS-Erkenntnis:**
Was wäre, wenn wir einfach alle Elementwerte durch eine massive Zahl (einen Skalierungsfaktor K) teilen und abrunden würden?
Anstatt dass ein Element einen Wert von 1.482.912 hat, skalieren wir es auf 14.
Jetzt ist V_{max} winzig! Der DP[value]-Algorithmus läuft sofort!
Da wir abgerundet haben, verlieren wir ein wenig Präzision. Die FPTAS-Mathematik berechnet den exakten Skalierungsfaktor K, der erforderlich ist, um sicherzustellen, dass unser Präzisionsverlust strikt durch das \epsilon des Benutzers begrenzt ist.

1. Sei V_{highest} der Maximalwert eines einzelnen Elements.
2. Definiere den Skalierungsfaktor: K = \frac{\epsilon \cdot V_{highest}}{N}.
3. Erstelle ein neues Array mit skalierten Werten: `scaled_v[i] = floor(value[i] / K)`.
4. Führe die umgekehrte Knapsack-DP mit diesen winzigen `scaled_v`-Werten aus!
   - `dp[v]` speichert das **minimale Gewicht**, das erforderlich ist, um exakt den skalierten Wert `v` zu erreichen.
5. Finde den maximalen skalierten Wert `v` in der DP-Tabelle, für den `dp[v] <= W` gilt.
6. Um die wahre Approximation zurückzugeben, betrachten Sie die Elemente, die diesen skalierten Wert gebildet haben, und summieren Sie deren **ursprüngliche, unskalierte** Werte!

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for approx_07: 0/1 Knapsack FPTAS.

Given n items with values and weights and capacity
"""


def solve(values, weights, n, capacity, eps):
    """0/1 Knapsack FPTAS: scale values, run DP, return result."""
    if capacity <= 0 or n == 0:
        return 0
    v_max = max(values) if values else 1
    if v_max == 0:
        return 0
    K = (eps * v_max) / n
    if K <= 0:
        K = 1
    scaled = [max(1, int(v / K)) for v in values]
    # DP: dp[w] = max scaled value for weight w.
    dp = [0] * (capacity + 1)
    for i in range(n):
        wi = min(weights[i], capacity)
        vi = scaled[i]
        for w in range(capacity, wi - 1, -1):
            cand = dp[w - wi] + vi
            if cand > dp[w]:
                dp[w] = cand
    return dp[capacity] * K
```

</details>

## Durchlauf

*(Konzeptionell)*
`values = [1000000, 2000000, 3000000]`, `W = 50`.
`epsilon = 0.3`, `N = 3`.

1. V_{highest} = 3000000.
2. K = (0.3 x 3000000) / 3 = 300000.
3. Skalierte Werte:
   - 1000000 / 300000 = 3.33 \rightarrow 3.
   - 2000000 / 300000 = 6.66 \rightarrow 6.
   - 3000000 / 300000 = 10.0 \rightarrow 10.
4. Unser DP-Array hat jetzt nur noch die Größe 3+6+10 = 19!
5. Wir führen die DP aus und finden das minimale Gewicht für die Werte 0 bis 19. Dies erfordert exakt 3 x 19 = 57 Operationen, anstatt Millionen!
6. Wenn der beste gefundene skalierte Wert `16` ist, beträgt unser approximierter realer Wert 16 x 300000 = 4.800.000.
Das Optimum hätte 5.000.000 sein können, aber unsere Antwort ist garantiert \ge (1 - 0.3) x 5.000.000 = 3.500.000. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(N^3 / ε)$ | $O(N^3 / ε)$ |
| **Durchschnittlicher Fall** | $O(N^3 / ε)$ | $O(N^3 / ε)$ |
| **Schlechtester Fall** | $O(N^3 / ε)$ | $O(N^3 / ε)$ |

Die Größe des DP-Arrays ist durch die maximal mögliche skalierte Summe begrenzt.
Max\_Scaled\_Sum \le N x (V_{highest} / K).
Setze K = \frac{\epsilon \cdot V_{highest}}{N} ein:
Max\_Scaled\_Sum \le N x \frac{V_{highest}}{\epsilon \cdot V_{highest} / N} = \frac{N^2}{\epsilon}.
Die DP iteriert N-mal über ein Array der Größe \frac{N^2}{\epsilon}.
Die Gesamtlaufzeit beträgt exakt $O(N \cdot \frac{N^2}{\epsilon})$ = $O(\frac{N^3}{\epsilon})$.
Die Platzkomplexität beträgt $O(\frac{N^2}{\epsilon})$, um das 1D-DP-Array zu speichern.

## Varianten & Optimierungen

- **Nachverfolgung der Elemente:** Um den exakten Wert der gewählten Elemente zu erhalten, anstatt am Ende nur mit K zu multiplizieren, führen Sie eine 2D-DP-Tabelle, um die exakt ausgewählten Elemente zurückzuverfolgen, und geben Sie dann die Summe der `original_value[i]` für die gewählten Elemente zurück.

## Anwendungen in der Praxis

- **Computational Finance:** Portfolio-Optimierung, bei der Geldwerte extrem groß sind, was eine exakte DP unmöglich macht, eine Genauigkeit von 99 % jedoch völlig ausreicht.

## Verwandte Algorithmen in cOde(n)

- **[dp_03 - 0-1 Knapsack](../dynamic/dp_03_knapsack.md)** — Die klassische $O(N \cdot W)$ pseudo-polynomiale exakte Lösung.
- **[bb_01 - 0-1 Knapsack Branch and Bound](../branch_and_bound/bb_01_0-1-knapsack.md)** — Die exakte exponentielle Lösung, die Suchräume beschneidet.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) geschrieben wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitive Programmierung verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Anfang der Seite. Quell-Repository: <https://github.com/dawei7/code_n>.*