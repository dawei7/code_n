# Jump Game (I und II)

| | |
|---|---|
| **ID** | `greedy_07` |
| **Kategorie** | greedy |
| **Komplexität (erforderlich)** | $O(N)$ Zeit, $O(1)$ Platz |
| **Schwierigkeit** | 6/10 |
| **Relevanz für Vorstellungsgespräche** | 9/10 |
| **LeetCode-Äquivalent** | [Jump Game](https://leetcode.com/problems/jump-game/), [Jump Game II](https://leetcode.com/problems/jump-game-ii/) |

## Problemstellung

**Jump Game I (Entscheidungsproblem):** Gegeben ist ein Array `nums` von Ganzzahlen. Sie starten am ersten Index des Arrays, wobei jedes Element die *maximale* Sprungweite an dieser Position angibt. Geben Sie `true` zurück, wenn Sie den letzten Index erreichen können, andernfalls `false`.

**Jump Game II (Optimierungsproblem):** Gleiche Ausgangslage, jedoch ist *garantiert*, dass der letzte Index erreicht werden kann. Finden Sie die **minimale Anzahl an Sprüngen**, die erforderlich ist, um diesen zu erreichen.

**Eingabe:** Ein Array `nums` von Ganzzahlen.
**Ausgabe:** Ein Boolean (Jump Game I) oder eine Ganzzahl (Jump Game II).

## Wann ist dieser Ansatz zu verwenden?

- Um $O(N^2)$ Dynamic Programming Array-Traversierungsprobleme effizient in $O(N)$ Greedy-Probleme zu überführen.
- Extrem verbreitet in FAANG-Interviews, um zu prüfen, ob Kandidaten überlappende Reichweiten erkennen können.

## Ansatz: Jump Game I

**1. Der "Max Reach" Tracker:**
Während wir das Array durchlaufen, möchten wir den absolut weitesten Index kennen, den wir aktuell erreichen können. Nennen wir diesen `max_reach`.
An Index `i` können wir bis zu `nums[i]` Schritte springen. Daher ist der am weitesten entfernte Index, den wir *von* `i` aus erreichen können, `i + nums[i]`.
Wir aktualisieren `max_reach = max(max_reach, i + nums[i])`.

**2. Die Abbruchbedingung:**
Was passiert, wenn `max_reach` bei Index 3 steht, wir aber gerade in unserer Schleife bei `i = 4` sind?
Das bedeutet, es war mathematisch unmöglich, überhaupt Index 4 zu erreichen! Wir stecken fest!
Wenn zu irgendeinem Zeitpunkt `i > max_reach` gilt, geben wir `False` zurück.

**3. Die Erfolgsbedingung:**
Wenn zu irgendeinem Zeitpunkt `max_reach >= len(nums) - 1` gilt, können wir das Ende erreichen! Geben Sie `True` zurück.

## Ansatz: Jump Game II

**1. Das "Window of Reach" (BFS-Logik als Greedy getarnt):**
Um die Anzahl der Sprünge zu minimieren, sollten wir nicht jedes Mal blind so weit wie möglich springen. Was, wenn ein kürzerer Sprung uns auf ein massives Sprungbrett (z. B. `nums[i] = 100`) befördert?
Anstatt eines einzelnen `max_reach` verfolgen wir ein "Fenster" von Indizes, die wir mit unserer aktuellen Anzahl an Sprüngen erreichen können.
- `current_end`: Das Ende unseres aktuellen Sprungfensters.
- `farthest`: Der absolut weiteste Index, den wir bisher während der Iteration *innerhalb* des aktuellen Fensters entdeckt haben.

**2. Der Greedy-Auslöser:**
Wir iterieren durch das Array. Bei jedem Schritt aktualisieren wir `farthest = max(farthest, i + nums[i])`.
Wenn unser Schleifeniterator `i` das `current_end` unseres Fensters erreicht, bedeutet dies, dass wir zwingend einen Sprung machen MÜSSEN, um fortzufahren!
Also erhöhen wir unseren `jump_count` und setzen unser neues `current_end` auf den `farthest` Index, den wir entdeckt haben.

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for greedy_07: Jump Game.

Auto-generated from challenges/algorithms/greedy.py:SPECS.
O(n) time.
"""


def solve(arr, n):
    if n <= 1:
        return 0
    jumps = 0
    current_end = 0
    farthest = 0
    for i in range(n - 1):
        farthest = max(farthest, i + arr[i])
        if i == current_end:
            jumps += 1
            current_end = farthest
    return jumps
```

</details>

## Durchlauf (Jump Game II)

`nums = [2, 3, 1, 1, 4]`. Länge 5.
`jumps = 0`, `current_end = 0`, `farthest = 0`.

1. `i = 0` (Wert 2):
   - `farthest = max(0, 0 + 2) = 2`.
   - `i == current_end` (0 == 0).
   - `jumps = 1`. `current_end = 2`.
2. `i = 1` (Wert 3):
   - `farthest = max(2, 1 + 3) = 4`.
   - `i == current_end` (1 == 2) -> False.
3. `i = 2` (Wert 1):
   - `farthest = max(4, 2 + 1) = 4`.
   - `i == current_end` (2 == 2) -> True.
   - `jumps = 2`. `current_end = 4`.
   - `current_end >= 4`. Abbruch!

Ergebnis `jumps = 2`. ✓ (Sprung von 0 nach 1, dann von 1 nach 4).

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(N)$ | $O(1)$ |
| **Durchschnittlicher Fall** | $O(N)$ | $O(1)$ |
| **Schlechtester Fall** | $O(N)$ | $O(1)$ |

Beide Algorithmen verwenden einen einzigen linearen Durchlauf durch das Array und führen an jedem Index $O(1)$ arithmetische Operationen aus. Die Zeitkomplexität ist strikt $O(N)$.
Es werden nur primitive Ganzzahlvariablen verwendet (`max_reach`, `farthest`, `current_end`, `jumps`), wodurch die Platzkomplexität perfekt $O(1)$ ist.
*(Hinweis: Die Lösung von Jump Game II mit Top-Down DP benötigt $O(N^2)$ Zeit und $O(N)$ Platz. Der Greedy-Ansatz ist hier dem DP-Ansatz weit überlegen).*

## Varianten & Optimierungen

- **Jump Game III (BFS):** Wenn `nums[i]` es erlaubt, VORWÄRTS oder RÜCKWÄRTS zu genau `i + nums[i]` oder `i - nums[i]` zu springen, bricht die Greedy-Logik zusammen! Sie müssen eine standardmäßige Breadth-First Search (`graph_02`) verwenden, um den kürzesten Pfad zu finden.
- **Jump Game VII (Sliding Window):** Wenn Sie nur zwischen `[i + minJump, i + maxJump]` springen können, erfordern die überlappenden Intervalle eine Kombination aus Greedy und einem Sliding Window oder einem Präfixsummen-Array.

## Praxisanwendungen

- **Netzwerk-Routing:** Optimierung der Hop-Anzahl in paketvermittelten Netzwerken, bei denen verschiedene Knoten unterschiedliche Übertragungsradien haben (analog zu `nums[i]`).

## Verwandte Algorithmen in cOde(n)

- **[greedy_06 - Gas Station](greedy_06_gas-station.md)** — Eine weitere $O(N)$ Array-Traversierung, bei der ein Akkumulator dynamisch über Erfolg oder Misserfolg entscheidet.
- **[dp_12 - Minimum Jumps to Reach End](../dynamic/dp_12_minimum-jumps-to-reach-end.md)** — Der deutlich langsamere $O(N^2)$ Dynamic Programming Ansatz für genau dieses Problem (wird oft gelehrt, bevor die Greedy-Lösung präsentiert wird!).

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) verfasst wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitive Programmierung verwendet wird. Für den enzyklopädischen Eintrag folgen Sie dem Wikipedia-Link am Seitenanfang. Quell-Repository: <https://github.com/dawei7/code_n>.*