# 0-1-Rucksackproblem (FPTAS-Approximation)

| | |
|---|---|
| **ID** | `approx_07` |
| **Kategorie** | Approximation |
| **Komplexität (erforderlich)** | $O(N^3 / ε)$ |
| **Schwierigkeitsgrad** | 9/10 |
| **Relevanz für Vorstellungsgespräche** | 2/10 |
| **Wikipedia** | [Polynomiales Approximationsschema](https://en.wikipedia.org/wiki/Polynomial-time_approximation_scheme) |

## Aufgabenstellung

Das 0-1-Rucksackproblem ist NP-schwer, was bedeutet, dass es keinen bekannten Algorithmus in polynomieller Zeit gibt, um es exakt zu lösen. Es ist jedoch **schwach NP-schwer**, was bedeutet, dass es eine Lösung mittels dynamischer Programmierung gibt ($O(N \cdot W)$). Wenn die Kapazität W eine Milliarde beträgt, scheitert die dynamische Programmierung (pseudopolynomiale Zeit).
Ihre Aufgabe ist es, ein **vollständig polynomiales Approximationsschema (FPTAS)** zu implementieren. Gegeben sei ein Fehlerparameter \epsilon (z. B. \epsilon = 0,1 für eine Fehlermarge von 10 %), gib eine gültige Rucksackpackung zurück, deren Gesamtwert mathematisch garantiert \ge (1 - \epsilon) x OPT liegt, und zwar in streng polynomieller Zeit relativ zu N und 1/\epsilon (völlig unabhängig vom riesigen W!).

**Eingabe:** N Gegenstände mit `values` und `weights`, einer Kapazität `W` und einem Float-Wert `epsilon`.
**Ausgabe:** Der approximierte Maximalwert.

## Wann man es verwenden sollte

- Wenn man eine riesige Rucksackkapazität und astronomisch hohe Gegenstandswerte hat, die beide Standard-DP-Arrays zum Explodieren bringen, aber dennoch eine unglaublich präzise mathematische Garantie benötigt (wie z. B. 99,9 % optimal).

## Ansatz

Das Standard-Rucksack-DP-Array lässt sich umkehren: Anstelle von DP[Gewicht] = max\_Wert können wir DP[Wert] = min\_Gewicht verwenden!
Dieser DP[Wert]-Ansatz läuft in $O(N \cdot V_{max})$, wobei V_{max} die Summe aller Werte ist.
Wenn die Werte der Gegenstände im Milliardenbereich liegen, ist V_{max} riesig, und $O(N \cdot V_{max})$ scheitert weiterhin.

**Die geniale FPTAS-Einsicht:**
Was wäre, wenn wir einfach alle Werte der Gegenstände durch eine riesige Zahl (einen Skalierungsfaktor K) dividieren und sie abrunden würden?
Anstatt dass ein Element \1.482.912 wert ist, skalieren wir es auf \14.
Jetzt ist V_{max} winzig! Der DP[value]-Algorithmus läuft sofort!
Da wir abgerundet haben, verlieren wir ein kleines bisschen an Genauigkeit. Die FPTAS-Mathematik berechnet den exakten Skalierungsfaktor K, der erforderlich ist, um sicherzustellen, dass unser Genauigkeitsverlust streng durch das \epsilon des Benutzers begrenzt ist.

1. Sei V_{highest} der Maximalwert eines beliebigen einzelnen Gegenstands.
2. Definiere den Skalierungsfaktor: K = \frac{\epsilon \cdot V_{highest}}{N}.
3. Erstelle ein neues Array mit skalierten Werten: `scaled_v[i] = floor(value[i] / K)`.
4. Führe die „Flipped Knapsack“-DP mit diesen winzigen `scaled_v`-Werten aus!
   – `dp[v]` speichert das **Mindestgewicht**, das erforderlich ist, um genau den skalierten Wert `v` zu erreichen.
5. Ermitteln Sie den maximalen skalierten Wert `v` in der DP-Tabelle, bei dem `dp[v] <= W`.
6. Um die tatsächliche Annäherung zu erhalten, betrachten Sie die Gegenstände, aus denen sich dieser skalierte Wert zusammensetzt, und addieren Sie deren **ursprüngliche, unskalierte** Werte!

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

## Schritt-für-Schritt-Anleitung

*(Konzeptionell)*
`values = [1000000, 2000000, 3000000]`, `W = 50`.
`epsilon = 0.3`, `N = 3`.

1. V_{highest} = 3000000.
2. K = (0,3 × 3000000) / 3 = 300000.
3. Skalierte Werte:
   - 1000000 / 300000 = 3,33 \rightarrow 3.
   - 2000000 / 300000 = 6,66 \rightarrow 6.
   - 3000000 / 300000 = 10,0 \rightarrow 10.
4. Unser DP-Array hat nun nur noch die Größe 3+6+10 = 19!
5. Wir führen die DP durch, um das minimale Gewicht für die Werte 0 bis 19 zu ermitteln. Dies erfordert genau 3 × 19 = 57 Operationen statt Millionen!
6. Wenn der beste gefundene skalierte Wert `16` ist, beträgt unser näherungsweiser tatsächlicher Wert 16 × 300000 = 4.800.000.
Der optimale Wert hätte zwar 5.000.000 betragen können, aber unser Ergebnis ist garantiert \ge (1 - 0,3) × 5.000.000 = 3.500.000. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(N^3 / ε)$ | $O(N^3 / ε)$ |
| **Durchschnittlicher Fall** | $O(N^3 / ε)$ | $O(N^3 / ε)$ |
| **Schlechtester Fall** | $O(N^3 / ε)$ | $O(N^3 / ε)$ |

Die Größe des DP-Arrays wird durch die maximal mögliche skalierte Summe begrenzt.
Max\_Scaled\_Sum \le N x (V_{highest} / K).
Setzen wir K = \frac{\epsilon \cdot V_{highest}}{N} ein:
Max\_Scaled\_Sum \le N \times \frac{V_{highest}}{\epsilon \cdot V_{highest} / N} = \frac{N^2}{\epsilon}.
Die DP durchläuft ein Array der Größe \frac{N^2}{\epsilon} N-mal.
Die Gesamtlaufzeit beträgt genau $O(N \cdot \frac{N^2}{\epsilon})$ = $O(\frac{N^3}{\epsilon})$.
Die Platzkomplexität beträgt $O(\frac{N^2}{\epsilon})$ für die Speicherung des 1D-DP-Arrays.

## Varianten & Optimierungen

- **Nachverfolgung der Elemente:** Um den genauen Wert der ausgewählten Elemente zu erhalten, anstatt am Ende einfach mit K zu multiplizieren, wird eine 2D-DP-Tabelle geführt, um die genau ausgewählten Elemente zurückzuverfolgen; anschließend wird die Summe von `original_value[i]` für die ausgewählten Elemente zurückgegeben.

## Anwendungen in der Praxis

- **Finanzmathematik:** Portfoliooptimierung, bei der die Geldbeträge unglaublich groß sind, was eine exakte DP unmöglich macht, eine Genauigkeit von 99 % jedoch völlig ausreichend ist.

## Verwandte Algorithmen in cOde(n)

- **[dp_03 – 0-1-Rucksackproblem](../dynamic/dp_03_knapsack.md)** — Die klassische $O(N \cdot W)$ exakte Lösung in pseudopolynomieller Zeit.
- **[bb_01 – 0-1-Rucksack-Problem: Branch-and-Bound](../branch_and_bound/bb_01_0-1-knapsack.md)** – Die exakte Lösung in exponentieller Zeit, die Suchräume beschneidet.

---

*Diese Dokumentation ist ein Originalbeitrag, der für cOde(n) verfasst wurde,
in Anlehnung an die kanonische Struktur, die von Referenzseiten zum Thema
Wettbewerbsprogrammierung verwendet wird. Den kanonischen Enzyklopädieeintrag finden Sie unter dem
Wikipedia-Link oben auf der Seite. Quell-Repository:
<https://github.com/dawei7/code_n>.*
