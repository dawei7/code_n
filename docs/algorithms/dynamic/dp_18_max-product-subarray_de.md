# Max Product Subarray

| | |
|---|---|
| **ID** | `dp_18` |
| **Kategorie** | dynamic |
| **Komplexität (erforderlich)** | $O(n)$ |
| **Schwierigkeit** | 5/10 |
| **Relevanz für Vorstellungsgespräche** | 9/10 |
| **Wikipedia** | [Maximum subarray problem](https://en.wikipedia.org/wiki/Maximum_subarray_problem) (verwandt) |

## Problemstellung

Gegeben ist ein Array von Ganzzahlen `nums` (welches **negative Zahlen und Nullen** enthalten kann). Finde das **zusammenhängende Subarray** mit dem größten Produkt.

**Eingabe:** ein Array `nums`.
**Ausgabe:** das maximale Produkt eines beliebigen zusammenhängenden Subarrays.

**Beispiel:**

| nums | Antwort | Subarray |
|---|---:|---|
| `[2, 3, -2, 4]` | 6 | `[2, 3]` |
| `[-2, 0, -1]` | 0 | `[]` oder `[0]` (jedes Produkt ≤ 0 ist zulässig) |
| `[-2, 3, -4]` | 24 | `[-2, 3, -4]` |
| `[0, 2]` | 2 | `[2]` |
| `[-1, -2, -3, -4]` | 24 | `[-1, -2, -3, -4]` |

## Anwendung

- Das klassische Problem "**Subarray mit maximaler Summe**", jedoch mit Produkt statt Summe. Die interessante Wendung: Wenn zwei negative Zahlen multipliziert werden, kehrt sich das Vorzeichen um, daher müssen wir sowohl das Minimum als auch das Maximum verfolgen.
- Häufig bei Google, Meta und Amazon — eine großartige Interviewfrage, um zu prüfen, ob man an den "Negative-Edge-Case" denkt.

## Ansatz

Für die maximale Summe verfolgt der Kadane-Algorithmus nur das Maximum, das an jeder Position endet. Für das **maximale Produkt** kehrt die Multiplikation mit einer negativen Zahl das Vorzeichen um. Daher könnte das größte Produkt, das an Position `i` endet, vom *kleinsten* (negativsten) Produkt an Position `i-1` stammen.

Definiere zwei Arrays:
- `max_ending[i]` = maximales Produkt eines Subarrays, das bei `i` endet.
- `min_ending[i]` = minimales Produkt eines Subarrays, das bei `i` endet.

**Rekurrenz:** an Position `i`:
```
candidate_a = nums[i]
candidate_b = max_ending[i-1] * nums[i]
candidate_c = min_ending[i-1] * nums[i]
max_ending[i] = max(candidate_a, candidate_b, candidate_c)
min_ending[i] = min(candidate_a, candidate_b, candidate_c)
```

(Der `candidate_a` deckt den Fall ab, in dem ein Neustart bei `i` besser ist als eine Erweiterung.)

**Nullen:** Wenn `nums[i] == 0`, sind sowohl das Maximum als auch das Minimum 0 (ein leeres Subarray würde ausreichen, aber wir verwenden 0 für die Semantik des "Null-Resets").

**Platzoptimierung:** Identisch zu Kadane — behalte nur das letzte `max_ending` und `min_ending` sowie ein laufendes Ergebnis bei.

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for dp_18: Max Product Subarray.

Track both cur_max and cur_min (negatives flip sign).
"""


def solve(arr):
    if not arr:
        return 0
    best = arr[0]
    cur_max = arr[0]
    cur_min = arr[0]
    for v in arr[1:]:
        if v < 0:
            cur_max, cur_min = cur_min, cur_max
        cur_max = max(v, cur_max * v)
        cur_min = min(v, cur_min * v)
        if cur_max > best:
            best = cur_max
    return best
```

</details>

## Durchlauf

`nums = [2, 3, -2, 4]`. Erwartet: 6.

| i | x | x<0? | max_ending (vorher) | min_ending (vorher) | neues max | neues min | best |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 2 | nein | 2 (init) | 2 (init) | 2 | 2 | 2 |
| 1 | 3 | nein | 2 | 2 | max(3, 2·3=6) = 6 | min(3, 2·3=6) = 3 | 6 |
| 2 | -2 | ja | 6 | 3 | swap→ max=3, min=6, dann max(-2, 3·-2=-6)=-2, min(-2, 6·-2=-12)=-12 | -2 | -12 | 6 |
| 3 | 4 | nein | -2 | -12 | max(4, -2·4=-8) = 4 | min(4, -12·4=-48) = -48 | **6** |

Antwort: 6. ✓ (Subarray [2, 3] → Produkt 6.)

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(n)$ | $O(1)$ |
| **Durchschnittlicher Fall** | $O(n)$ | $O(1)$ |
| **Schlechtester Fall** | $O(n)$ | $O(1)$ |

Ein Durchlauf, zwei Variablen, $O(1)$ zusätzlicher Platz.

## Varianten & Optimierungen

- **Divide and Conquer** — für sehr große Arrays, bei denen Parallelisierung wichtig ist, liefert D&C $O(n log n)$ Arbeit mit $O(log n)$ Tiefe.
- **Modulares Produkt** — wenn `nums` sehr große Werte enthalten kann und das Produkt modulo M benötigt wird, verwende modulare Arithmetik in der Rekurrenz.
- **Zählen von Subarrays mit Produkt < K** — Sliding Window. Anderes Problem, ähnliche Struktur.
- **Rekonstruktion des Subarrays** — speichere den Startindex des besten Subarrays; setze ihn auf `i` zurück, wenn ein Neustart erfolgt.

## Anwendungen in der Praxis

- **Maximaler Gewinn aus einer Sequenz von Preisänderungen** — wenn man Long- und Short-Positionen einnehmen kann, erfasst das maximale Produkt beide Richtungen.
- **Signalverarbeitung** — Finden der Sequenz mit dem größten "Gewinn" (Gain) in einem verrauschten Signal.
- **Genetische Algorithmen** — Fitness kann als Produkt von Multiplikatoren modelliert werden; das Finden des optimalen Sub-Fensters entspricht diesem DP.
- **Portfolio-Analytik** — das geometrische Mittel über ein Fenster ist der Logarithmus des maximalen Produkts.
- **Bildverarbeitung** — Faltungskerne (Convolution Kernels) haben oft negative Werte; das maximale Produkt findet die Region mit der stärksten "Verstärkung".

## Verwandte Algorithmen in cOde(n)

- **[dp_11 — House Robber](dp_11_house-robber.md)** — gleiche rollierende Struktur, aber eine Max-von-zwei-Entscheidung, kein Min-und-Max. (d=5/10, r=9/10)
- **[dp_12 — Min Cost Path](dp_12_min-cost-path.md)** — eine weitere Variante des maximalen Pfadprodukts auf einem Gitter. (d=4/10, r=9/10)
- **[dp_09 — Rod Cutting](dp_09_rod-cutting.md)** — gleiches 1D DP, anderes Ziel. (d=5/10, r=9/10)

---

*Diese Dokumentation ist ein Originalinhalt für cOde(n), modelliert nach der kanonischen Struktur, die von Referenzseiten für kompetitives Programmieren verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folge dem Wikipedia-Link am Seitenanfang. Quell-Repository: <https://github.com/dawei7/code_n>.*