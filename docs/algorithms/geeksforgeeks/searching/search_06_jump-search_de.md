# Jump Search (Block Search)

| | |
|---|---|
| **ID** | `search_06` |
| **Kategorie** | searching |
| **Komplexität (erforderlich)** | $O(\sqrt{N})$ Zeit, $O(1)$ Platz |
| **Schwierigkeit** | 2/10 |
| **Relevanz für Vorstellungsgespräche** | 2/10 |
| **Wikipedia** | [Jump search](https://en.wikipedia.org/wiki/Jump_search) |

## Problemstellung

Gegeben ist ein sortiertes Array `arr` und ein `target`-Wert.
Finden Sie den Index des `target` im Array. Wenn das `target` nicht vorhanden ist, geben Sie `-1` zurück.
Sie müssen dies lösen, indem Sie in festen Schritten vorwärts springen, um den korrekten Block zu finden, und anschließend eine lineare Suche innerhalb dieses Blocks durchführen.

**Eingabe:** Ein sortiertes Array `arr` und ein `target`-Wert.
**Ausgabe:** Eine Ganzzahl, die den Index repräsentiert.

## Wann man es verwendet

- Wenn Sie ein sortiertes Array haben, aber Binary Search rechnerisch ineffizient ist, weil "Rückwärtssprünge" deutlich teurer sind als Vorwärtssprünge (z. B. bei der Suche nach Daten auf einem physischen Magnetbandlaufwerk oder beim Iterieren durch eine Singly Linked List mit "Skip"-Pointern).

## Ansatz

**1. Die Block-Sprung-Strategie:**
Anstatt jedes einzelne Element zu prüfen (Lineare Suche $O(N)$), können wir Datenblöcke überspringen!
Wenn wir in Schritten der Größe `m` springen:
Index 0, Index m, Index 2m, Index 3m...
Bei jedem Sprung prüfen wir, ob `arr[km] >= target`.
Da das Array sortiert ist, wissen wir in dem Moment, in dem `arr[km]` größer als unser `target` wird, dass wir darüber hinausgesprungen sind!
Das `target` muss mathematisch im vorherigen Block zwischen Index (k-1)m und Index km eingeschlossen sein.

**2. Die lokalisierte lineare Suche:**
Sobald wir den korrekten Block der Größe `m` identifiziert haben, springen wir genau einmal zum Anfang des Blocks zurück und führen eine standardmäßige $O(m)$ Lineare Suche durch, bis wir das `target` finden.

**3. Wahl der optimalen Blockgröße:**
Was ist die mathematisch perfekte Sprunggröße `m`?
Im Schlechtesten Fall müssen wir \frac{N}{m} Mal springen, um den letzten Block zu erreichen.
Anschließend müssen wir m-1 Elemente in diesem Block linear durchsuchen.
Gesamtoperationen = \frac{N}{m} + m - 1.
Mittels Analysis bilden wir die Ableitung nach m und setzen diese auf 0, um das Minimum zu finden:
-\frac{N}{m^2} + 1 = 0 -> m^2 = N -> m = \sqrt{N}.
Daher ist die optimale Sprunggröße exakt die Quadratwurzel der Array-Länge!

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for search_06: Jump Search.

Auto-generated from challenges/algorithms/searching.py:SPECS.
O(log n) time.
"""


def solve(data, target, n):
    import math
    step = max(1, int(math.sqrt(n)))
    prev = 0
    # Find the block where the target could be.
    while prev < n and data[min(step, n) - 1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1
    # Linear scan inside the block.
    for index in range(prev, min(step, n)):
        if data[index] == target:
            return index
    return -1
```

</details>

## Durchlauf

`arr = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]`, `target = 55`.
`N = 11`. `step = sqrt(11) = 3`. `prev = 0`.

1. **Sprung 1:** Prüfe Index `3-1 = 2`. `arr[2] = 1`.
   - `1 < 55`. Springe! `prev = 3`, `step = 6`.
2. **Sprung 2:** Prüfe Index `6-1 = 5`. `arr[5] = 5`.
   - `5 < 55`. Springe! `prev = 6`, `step = 9`.
3. **Sprung 3:** Prüfe Index `9-1 = 8`. `arr[8] = 21`.
   - `21 < 55`. Springe! `prev = 9`, `step = 12`.
4. **Sprung 4:** `min(step, n) - 1 = min(12, 11) - 1 = 10`. `arr[10] = 55`.
   - `55 < 55` ist FALSCH! Schleife terminiert.

Block identifiziert! `prev = 9`, Endgrenze = `min(12, 11) = 11`.
1. **Lineare Suche:** `i = 9`. `arr[9] = 34 == 55`? Falsch.
2. `i = 10`. `arr[10] = 55 == 55`? WAHR!
Gib `10` zurück. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(1)$ | $O(1)$ |
| **Durchschnittlicher Fall** | $O(\sqrt{N})$ | $O(1)$ |
| **Schlechtester Fall** | $O(\sqrt{N})$ | $O(1)$ |

Die Anzahl der Sprünge ist durch \frac{N}{\sqrt{N}} = \sqrt{N} begrenzt. Die Anzahl der Schritte der linearen Suche ist durch die Blockgröße \sqrt{N} begrenzt.
Daher ist die gesamte Zeitkomplexität $O(\sqrt{N} + \sqrt{N})$ = $O(\sqrt{N})$.
Dies ist der Linearen Suche $O(N)$ weit überlegen, aber der Binary Search $O(\log N)$ weit unterlegen.
Die Platzkomplexität beträgt $O(1)$.

## Varianten & Optimierungen

- **Multi-Level Jump Search:** Warum nur eine lineare Suche im letzten Block durchführen? Wenn die Blockgröße \sqrt{N} immer noch sehr groß ist, kann man eine Jump Search INNERHALB des Blocks durchführen! (Unter Verwendung einer neuen Blockgröße von N^{1/4}). Die rekursive Wiederholung dieses Vorgangs erzeugt ein System, das sich einer Zeitkomplexität von $O(\log N)$ annähert, konzeptionell identisch mit einer B-Baum-Struktur oder einer Skip List!

## Anwendungen in der Praxis

- **Skip Lists:** Die grundlegende Logik, "Express-Spuren" über einer Linked List zu erstellen, um $O(\log N)$ Suchzeiten zu erreichen, ohne auf zusammenhängende Speicher-Arrays angewiesen zu sein.
- **Magnetbandlaufwerke / Sequentielle Speicherung:** Das Rückwärtsspulen auf physischen Kassetten dauert deutlich länger als das Vorspulen. Binary Search springt in 50 % der Fälle rückwärts! Jump Search springt nur EINMAL exakt rückwärts (wenn der Block gefunden wurde), was es für physische sequentielle Medien weit überlegen macht.

## Verwandte Algorithmen in cOde(n)

- **[search_01 - Linear Search](search_01_linear-search.md)** — Der grundlegende $O(N)$-Algorithmus, der innerhalb des letzten Blocks verwendet wird.
- **[search_02 - Binary Search](search_02_binary-search.md)** — Der mathematisch optimale Suchalgorithmus für speicherbasierte Arrays.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) verfasst wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitive Programmierung verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Seitenanfang. Quell-Repository: <https://github.com/dawei7/code_n>.*