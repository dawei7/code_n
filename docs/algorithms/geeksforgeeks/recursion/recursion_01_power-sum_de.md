# The Power Sum

| | |
|---|---|
| **ID** | `recursion_01` |
| **Kategorie** | Rekursion |
| **Komplexität (erforderlich)** | $O(2^{N^{1/N}})$ Zeit, $O(N^{1/N})$ Platz |
| **Schwierigkeit** | 5/10 |
| **Relevanz für Vorstellungsgespräche** | 4/10 |
| **HackerRank-Äquivalent** | [The Power Sum](https://www.hackerrank.com/challenges/the-power-sum/problem) |

## Problemstellung

Ermitteln Sie die Anzahl der Möglichkeiten, wie eine gegebene Ganzzahl X als Summe der N-ten Potenzen von **eindeutigen** natürlichen Zahlen ausgedrückt werden kann.

Zum Beispiel, wenn X=13 und N=2.
Wir müssen die Anzahl der Möglichkeiten finden, 13 als Summe eindeutiger Quadratzahlen auszudrücken.
2^2 + 3^2 = 4 + 9 = 13.
Es gibt genau 1 Möglichkeit. Geben Sie 1 zurück.

Wenn X=100 und N=2:
10^2 = 100
6^2 + 8^2 = 36 + 64 = 100
1^2 + 3^2 + 4^2 + 5^2 + 7^2 = 1+9+16+25+49 = 100
Geben Sie 3 zurück.

**Eingabe:** Zwei Ganzzahlen X und N.
**Ausgabe:** Eine Ganzzahl, die die Anzahl der Kombinationen repräsentiert.

## Wann man es verwendet

- Um das grundlegendste Konzept der gesamten Rekursion zu erlernen: **"Take it or Leave it" (Auswählen / Nicht auswählen)**.
- Dies ist das rekursive Rückgrat, das das 0/1-Rucksackproblem (Knapsack Problem) und alle Algorithmen zur Teilmengen-Generierung antreibt.

## Ansatz

**1. Die rekursiven Entscheidungen:**
Wir haben eine Zielzahl X und eine Potenz N gegeben.
Wir beginnen mit dem Testen der Basis-Zahlen beginnend bei num = 1.
Für die aktuelle num haben wir genau zwei Möglichkeiten:
- **Möglichkeit 1 (Take it):** Wir schließen num^N in unsere Summe ein. Das bedeutet, unser neues verbleibendes Ziel ist X - num^N. Da wir eindeutige Zahlen verwenden müssen, gehen wir zur nächsten verfügbaren Zahl über: num + 1.
- **Möglichkeit 2 (Leave it):** Wir schließen num^N NICHT in unsere Summe ein. Unser Ziel bleibt exakt X, aber wir gehen zur nächsten verfügbaren Zahl über: num + 1.

Die Gesamtzahl der gültigen Wege ist einfach: `Take it + Leave it`.

**2. Die Basisfälle:**
Jede rekursive Funktion muss wissen, wann sie aufhören soll!
- **Erfolg:** Wenn unser Ziel X exakt `0` wird, bedeutet dies, dass unsere Entscheidungen perfekt zum ursprünglichen Ziel summiert wurden! Wir geben `1` zurück (was 1 gefundene gültige Kombination repräsentiert).
- **Fehler 1:** Wenn unser Ziel X `< 0` wird, bedeutet dies, dass wir das Ziel überschritten haben! Unsere Entscheidungen summierten sich zu einer zu großen Zahl. Geben Sie `0` zurück.
- **Fehler 2:** Wenn die Zahl, die wir gerade testen, num^N, strikt größer als das verbleibende Ziel X ist, dann ist es unmöglich, diese Zahl (oder irgendeine Zahl, die größer als sie ist) zu verwenden. Geben Sie `0` zurück.

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for recursion_01: Power Sum.

Recursive halving: x^n = (x^(n//2))^2, with an extra x when
n is odd. O(log n) time.
"""


def solve(x, n):
    if n == 0:
        return 1
    half = solve(x, n // 2)
    if n % 2 == 0:
        return half * half
    return x * half * half
```

</details>

## Durchlauf

X=13, N=2.
Start: `recurse(13, 1)`.

1. **`recurse(13, 1)`**: `val = 1^2 = 1`.
   - Take: `recurse(13 - 1, 2) => recurse(12, 2)`
   - Leave: `recurse(13, 2)`
2. **Untersuche `recurse(12, 2)`**: `val = 2^2 = 4`.
   - Take: `recurse(12 - 4, 3) => recurse(8, 3)`
   - Leave: `recurse(12, 3)`
3. **Untersuche `recurse(8, 3)`**: `val = 3^2 = 9`.
   - `val > target` (9 > 8).
   - Basisfall erreicht: Gib `0` zurück.
4. **Untersuche `recurse(12, 3)` (Der Leave-Zweig aus Schritt 2)**: `val = 3^2 = 9`.
   - Take: `recurse(12 - 9, 4) => recurse(3, 4)`
   - Leave: `recurse(12, 4)`
5. **Untersuche `recurse(3, 4)`**: `val = 4^2 = 16`.
   - `val > target` (16 > 3).
   - Basisfall erreicht: Gib `0` zurück.
6. **Springen wir zurück zum Leave-Zweig aus Schritt 1! `recurse(13, 2)`**:
   - `val = 2^2 = 4`.
   - Take: `recurse(13 - 4, 3) => recurse(9, 3)`
   - Leave: `recurse(13, 3)`
7. **Untersuche `recurse(9, 3)`**: `val = 3^2 = 9`.
   - Take: `recurse(9 - 9, 4) => recurse(0, 4)`
8. **Untersuche `recurse(0, 4)`**:
   - `target == 0`.
   - Basisfall erreicht: Gib `1` zurück! (Wir haben 2^2 + 3^2 gefunden).

Nachdem alle rekursiven Zweige zusammenlaufen und aufsummiert werden, ist der endgültige Rückgabewert für den Benutzer `1`. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(1)$ | $O(1)$ |
| **Durchschnittlicher Fall** | $O(2^{X^{1/N}})$ | $O(X^{1/N})$ |
| **Schlechtester Fall** | $O(2^{X^{1/N}})$ | $O(X^{1/N})$ |

Bei jedem Schritt spaltet sich die Rekursion in 2 Zweige auf (Take / Leave). Dies erzeugt eine Binärbaum-Struktur.
Die maximale Tiefe dieses Baums ist die größte Zahl, deren N-te Potenz \le X ist. Dies ist mathematisch durch \lfloor X^{1/N} \rfloor begrenzt.
Da ein Binärbaum der Tiefe D 2^D Knoten hat, beträgt die Zeitkomplexität $O(2^{X^{1/N}})$.
Die Platzkomplexität entspricht der maximalen Tiefe des Call Stacks während der Rekursion, was exakt der Tiefe des Baums entspricht: $O(X^{1/N})$.

*(Hinweis: Für X=100, N=2 beträgt die maximale Tiefe \sqrt{100} = 10. Der Baum hat 2^{10} = 1024 Knoten. Auf modernen Computern wird dies in Mikrosekunden sofort ausgeführt).*

## Varianten & Optimierungen

- **Coin Change II (`dp_04`):** Wenn das Problem die WIEDERVERWENDUNG derselben Zahlen erlauben würde (z. B. 2^2 + 2^2 + \dots), würde der "Take it"-Zweig `current_num` einfach NICHT inkrementieren. Er würde `recurse(target - val, current_num)` aufrufen.
- **Dynamische Programmierung / Memoization:** Die rekursiven Parameter sind `(target, current_num)`. Sie können die Ergebnisse dieser Tupel in einem 2D-Array oder einer Hash Map zwischenspeichern, um die Zeitkomplexität durch das Beschneiden überlappender Teilprobleme drastisch zu reduzieren!

## Anwendungen in der Praxis

- **Subset-Sum-Algorithmen:** Werden in der Finanzprüfung verwendet, um eine spezifische Kombination von Transaktionen (aus Tausenden) zu finden, die perfekt zu einem bestimmten fehlenden buchhalterischen Anomaliewert summieren.

## Verwandte Algorithmen in cOde(n)

- **[backtracking_01 - Subsets](../backtracking/backtracking_01_subsets.md)** — Die direkte Umsetzung des "Take it / Leave it"-Rekursionsbaums, der verwendet wird, um Kombinationen buchstäblich auszugeben.
- **[dp_06 - 0/1 Knapsack](../dynamic/dp_06_0-1-knapsack.md)** — Die stark optimierte Version der dynamischen Programmierung von "Take it / Leave it".

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) geschrieben wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für wettbewerbsorientiertes Programmieren verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Anfang der Seite. Quell-Repository: <https://github.com/dawei7/code_n>.*