# Permutationen

| | |
|---|---|
| **ID** | `backtrack_02` |
| **Kategorie** | Backtracking |
| **Komplexität (erforderlich)** | $O(N * N!)$ Zeit, $O(N)$ Speicherplatz |
| **Schwierigkeitsgrad** | 4/10 |
| **Relevanz für Vorstellungsgespräche** | 9/10 |
| **LeetCode-Äquivalent** | [Permutationen](https://leetcode.com/problems/permutations/) |

## Aufgabenstellung

Gegeben sei ein Array `nums` mit unterschiedlichen ganzen Zahlen. Gib alle möglichen Permutationen zurück. Die Antwort kann in beliebiger Reihenfolge zurückgegeben werden.
Eine Permutation ist eine Neuanordnung aller Elemente in eine bestimmte Reihenfolge.

**Eingabe:** Ein Array `nums` mit ganzen Zahlen, die alle unterschiedlich sind.
**Ausgabe:** Eine Liste von Listen, wobei jede innere Liste eine gültige Permutation darstellt.

## Anwendungsfälle

- Um jede mögliche Reihenfolge der Elemente zu generieren.
- Im Gegensatz zu Teilmengen ist bei Permutationen die Reihenfolge von Bedeutung (`[1, 2]` unterscheidet sich von `[2, 1]`) und Permutationen müssen immer JEDES Element des ursprünglichen Arrays enthalten.

## Vorgehensweise

**1. Der Entscheidungsbaum:**
An der allerersten Position unserer Permutation können wir BELIEBIGE der N Zahlen auswählen.
Für die zweite Position können wir BELIEBIGE der verbleibenden N-1 Zahlen auswählen.
Dadurch entsteht ein Baum mit genau N! (N-Fakultät) Blättern!

**2. Der Backtracking-Zustand:**
Wir definieren eine rekursive Funktion `backtrack(current_perm)`:
- `current_perm`: Eine Liste, in der die von uns ausgewählten Zahlen in der richtigen Reihenfolge gesammelt werden.
Da die Reihenfolge eine Rolle spielt, verwenden wir KEINEN `index`-Parameter, um uns zu zwingen, nur vorwärts zu schauen (wie wir es bei Teilmengen getan haben). Bei Permutationen durchlaufen wir immer das GESAMTE Array `nums`, um nach verfügbaren Zahlen zu suchen!

**3. Basisfall:**
Wenn `len(current_perm) == len(nums)`, ist unsere Permutation vollständig!
Wir fügen eine Kopie an das globale Ergebnis an und kehren zurück.

**4. Der rekursive Schritt (Backtracking):**
Wir durchlaufen jede Zahl in `nums`.
Wenn die Zahl BEREITS in `current_perm` enthalten ist, überspringen wir sie (da wir dasselbe Element nicht zweimal verwenden können).
Wenn sie verfügbar ist:
- Fügen wir sie an `current_perm` an.
- Gehen wir rekursiv tiefer.
- Backtracking: Entfernen wir sie aus `current_perm`, damit die nächste Iteration der Schleife versuchen kann, eine andere Zahl für diese Position auszuwählen.

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for backtrack_02: Permutations.

Return every ordering of ``arr`` as a list of lists. Standard
backtracking: pick each unused element in turn, recurse, then
unpick. The output list of permutations is sorted so the
verify can do a plain equality check.
"""


def solve(arr, n):
    if n == 0:
        return [[]]
    result = []
    used = [False] * n

    def helper(path):
        if len(path) == n:
            result.append(list(path))
            return
        for i in range(n):
            if not used[i]:
                used[i] = True
                path.append(arr[i])
                helper(path)
                path.pop()
                used[i] = False

    helper([])
    result.sort()
    return result
```

</details>

## Schritt-für-Schritt-Anleitung

`nums = [1, 2]`. N=2.

1. `backtrack([])`:
   - Schleife `num = 1`: nicht in `[]`. Anhängen. `perm = [1]`.
 - `backtrack([1])`:
 - Schleife `num = 1`: in `[1]`. Überspringen.
       - Schleife `num = 2`: nicht in `[1]`. Anfügen. `perm = [1, 2]`.
 - `backtrack([1, 2])`: Basisfall! `[1, 2]` an das Ergebnis anhängen.
 - Rückverfolgung: `2` entfernen. `perm = [1]`.
   - Rückverfolgung: `1` entfernen. `perm = []`.
   - Schleife `num = 2`: nicht in `[]`. Anfügen. `perm = [2]`.
 - `backtrack([2])`:
       - Schleife `num = 1`: nicht in `[2]`. Anfügen. `perm = [2, 1]`.
 - `backtrack([2, 1])`: Basisfall! `[2, 1]` an das Ergebnis anhängen.
       - Rückverfolgung: `1` entfernen. `perm = [2]`.
 - Schleife `num = 2`: in `[2]`. Überspringen.
   - Rückverfolgung: `2` entfernen. `perm = []`.

Ergebnis: `[[1, 2], [2, 1]]`. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(N * N!)$ | $O(N)$ |
| **Durchschnittlicher Fall** | $O(N * N!)$ | $O(N)$ |
| **Schlechteste** | $O(N * N!)$ | $O(N)$ |

Es gibt genau N! Blätter. An jedem Blatt dauert das Kopieren des Arrays $O(N)$ Zeit. Die Gesamtzeit beträgt streng $O(N x N!)$.
*(Anmerkung: Das Ermitteln von `num in current_perm` dauert $O(N)$ Zeit, wodurch die theoretische Zeit $O(N^2 x N!)$ beträgt. Wir können dies jedoch mithilfe eines Hash-Sets oder eines booleschen Arrays auf $O(1)$ Suchvorgänge optimieren).*
Die Platzkomplexität beträgt $O(N)$ für den Rekursionsstapel und die Zustandsliste.

## Varianten & Optimierungen

- **Permutationen II (mit Duplikaten):** Was ist, wenn `nums = [1, 1, 2]`? Der grundlegende Algorithmus liefert doppelte Permutationen.
  1. Verwende ein boolesches `used[]`-Array anstelle von `num in current_perm` (da die beiden `1`s unterschiedliche Objekte an verschiedenen Indizes sind).
  2. Sortiere das Array zunächst.
  3. Überspringe innerhalb der Schleife identische Nachbarn, WENN deren identischer Zwilling in der aktuellen Rekursionstiefe noch NICHT verwendet wurde: `if i > 0 and nums[i] == nums[i-1] and not used[i-1]: continue`.
- **Optimierung durch Vertauschen an Ort und Stelle:** Anstatt eine separate `current_perm`-Liste zu verwalten, kannst du das `nums`-Array direkt bearbeiten! Übergebe ein `index`, das die Grenze der festen Elemente darstellt. Für das aktuelle `index` durchlaufe `j` von `index` bis `N`, tausche `nums[index]` und `nums[j]` aus, rufe `index+1` rekursiv auf und tausche sie wieder aus, um zurückzuspringen!

## Anwendungen in der Praxis

- **Handelsreisenden-Problem (Brute-Force):** Berechnung der Gesamtstrecke für jede einzelne mögliche Permutation der zu besuchenden Städte, um den absolut kürzesten Weg zu finden.
- **Kryptografie:** Brute-Force-Analyse aller möglichen Transpositionschiffren oder Schlüsselumstellungen.

## Verwandte Algorithmen in cOde(n)

- **[backtrack_01 – Teilmengen](backtrack_01_subset-sum-decision.md)** — Das $O(2^N)$-Grundprinzip, bei dem die Reihenfolge keine Rolle spielt.
- **[backtrack_03 – Kombinationssumme](backtrack_03_combination-sum.md)** – Ein Hybrid, bei dem die Reihenfolge keine Rolle spielt, die Elemente jedoch unbegrenzt wiederverwendet werden können!

---

*Diese Dokumentation ist ein Originalbeitrag, der für cOde(n) verfasst wurde
und sich an der kanonischen Struktur orientiert, die von Referenzseiten zum Thema
Wettbewerbsprogrammierung verwendet wird. Den kanonischen Enzyklopädieeintrag finden Sie unter dem
Wikipedia-Link oben auf der Seite. Quell-Repository:
<https://github.com/dawei7/code_n>.*
