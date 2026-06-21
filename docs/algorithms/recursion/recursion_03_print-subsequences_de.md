# Alle Teilfolgen ausgeben

| | |
|---|---|
| **ID** | `recursion_03` |
| **Kategorie** | Rekursion |
| **Komplexität (erforderlich)** | $O(N \cdot 2^N)$ Zeit, $O(N)$ Platz |
| **Schwierigkeit** | 4/10 |
| **Relevanz für Vorstellungsgespräche** | 8/10 |
| **LeetCode-Äquivalent** | [Subsets](https://leetcode.com/problems/subsets/) |

## Problemstellung

Gegeben ist ein Array aus eindeutigen Ganzzahlen `nums`. Geben Sie alle möglichen Teilfolgen (Subsets) zurück.
Eine Teilfolge eines Arrays ist ein neues Array, das aus dem ursprünglichen Array durch das Löschen einiger (oder keiner) Elemente gebildet wird, ohne die relative Reihenfolge der verbleibenden Elemente zu verändern.
Die Lösungsmenge darf keine doppelten Teilmengen enthalten. Die Lösung kann in beliebiger Reihenfolge zurückgegeben werden.

**Eingabe:** Ein Ganzzahl-Array `nums`.
**Ausgabe:** Ein 2D-Array aus Ganzzahlen, das alle Teilfolgen repräsentiert.

## Wann man es verwendet

- Um jede einzelne mögliche Kombination von Elementen zu generieren.
- Der grundlegende "Pick / Not Pick"-Rekursionsbaum, angewendet auf die Akkumulation von Arrays anstelle von mathematischen Summen.

## Ansatz

**1. Der "Take it or Leave it"-Entscheidungsbaum:**
Wir verarbeiten die Elemente des Eingabe-Arrays nacheinander von links nach rechts.
Für jedes gegebene Element `nums[i]` haben wir zwei sich gegenseitig ausschließende Möglichkeiten:
- **Take it (Nehmen):** Wir fügen `nums[i]` zu unserer aktuell aufgebauten Teilfolge hinzu.
- **Leave it (Weglassen):** Wir fügen `nums[i]` NICHT zu unserer Teilfolge hinzu.

Für ein Array `[1, 2, 3]`:
- Nehmen wir 1? Ja -> Nehmen wir 2? Ja -> Nehmen wir 3? Ja. (Teilfolge: `[1, 2, 3]`)
- Nehmen wir 1? Ja -> Nehmen wir 2? Nein -> Nehmen wir 3? Ja. (Teilfolge: `[1, 3]`)
- Nehmen wir 1? Nein -> Nehmen wir 2? Nein -> Nehmen wir 3? Nein. (Teilfolge: `[]`)

Jede einzelne mögliche Kombination wird auf natürliche Weise durch das erschöpfende Durchsuchen beider Zweige dieses binären Entscheidungsbaums generiert!

**2. Der Rekursionszustand:**
Wir benötigen eine rekursive Funktion `recurse(index, current_path)`.
- `index` verfolgt, für welches Element in `nums` wir gerade die Entscheidung treffen.
- `current_path` ist ein Array (oder eine Liste), das die Elemente enthält, die wir bisher "genommen" haben.

**3. Der Induktionsanfang (Base Case):**
Wenn `index` die Länge `len(nums)` erreicht, haben wir für JEDES EINZELNE Element im Array eine "Nehmen/Weglassen"-Entscheidung getroffen.
Wir haben den Boden des Baums erreicht! `current_path` ist nun eine vollständig gebildete, gültige Teilfolge. Wir fügen eine *Kopie* von `current_path` zu unserem globalen Ergebnis-Array hinzu und kehren den Baum wieder nach oben zurück (`return`).

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for recursion_03: Print Subsequences.

For each position, branch on include/exclude. The recursion
tree has 2^n leaves; each leaf is a distinct subsequence.
Sorted so the verify can do a plain equality check.
"""


def solve(s, n):
    result = []

    def helper(i, path):
        if i == n:
            result.append("".join(path))
            return
        # Exclude s[i].
        helper(i + 1, path)
        # Include s[i].
        path.append(s[i])
        helper(i + 1, path)
        path.pop()

    helper(0, [])
    result.sort()
    return result
```

</details>

## Durchlauf

`nums = [1, 2]`. `results = []`.
Start: `recurse(0, [])`.

1. **`recurse(0, [])`** (Entscheidung für `1`):
   - TAKE-Zweig: Füge `1` hinzu. Path=`[1]`. Aufruf `recurse(1, [1])`.
2. **`recurse(1, [1])`** (Entscheidung für `2`):
   - TAKE-Zweig: Füge `2` hinzu. Path=`[1, 2]`. Aufruf `recurse(2, [1, 2])`.
3. **`recurse(2, [1, 2])`**:
   - `index == 2` (Induktionsanfang). Füge `[1, 2]` zu `results` hinzu. Zurückkehren.
4. Zurück in `recurse(1)`: Backtracking! `pop()`. Path ist wieder `[1]`.
   - LEAVE-Zweig: Nichts tun. Path=`[1]`. Aufruf `recurse(2, [1])`.
5. **`recurse(2, [1])`**:
   - `index == 2` (Induktionsanfang). Füge `[1]` zu `results` hinzu. Zurückkehren.
6. Zurück in `recurse(0)`: Backtracking! `pop()`. Path ist wieder `[]`.
   - LEAVE-Zweig: Nichts tun. Path=`[]`. Aufruf `recurse(1, [])`.
7. **`recurse(1, [])`** (Entscheidung für `2`):
   - TAKE-Zweig: Füge `2` hinzu. Path=`[2]`. Aufruf `recurse(2, [2])`.
8. **`recurse(2, [2])`**:
   - Induktionsanfang. Füge `[2]` hinzu. Zurückkehren.
9. Zurück in `recurse(1)`: Backtracking! `pop()`. Path ist wieder `[]`.
   - LEAVE-Zweig: Nichts tun. Path=`[]`. Aufruf `recurse(2, [])`.
10. **`recurse(2, [])`**:
    - Induktionsanfang. Füge `[]` hinzu. Zurückkehren.

Baum vollständig durchsucht!
`results = [[1, 2], [1], [2], []]`. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(N \cdot 2^N)$ | $O(N)$ |
| **Durchschnittlicher Fall** | $O(N \cdot 2^N)$ | $O(N)$ |
| **Schlechtester Fall** | $O(N \cdot 2^N)$ | $O(N)$ |

Für jedes Element in einem Array der Größe N verzweigen wir genau zweimal (Nehmen oder Weglassen). Dies erzeugt einen binären Rekursionsbaum mit genau $2^N$ Blattknoten. An jedem Blattknoten (dem Induktionsanfang) kopieren wir das `current_path`-Array, was $O(N)$ Zeit in Anspruch nimmt.
Daher beträgt die gesamte Zeitkomplexität $O(N \cdot 2^N)$. Dieser Algorithmus explodiert grundlegend für N > 20.
Die Platzkomplexität beträgt $O(N)$, um das `current_path`-Array und die Tiefe des Rekursions-Stacks zu speichern. (Ausgenommen der $O(N \cdot 2^N)$ Platz, der benötigt wird, um die Ausgabe `results` zu speichern).

## Varianten & Optimierungen

- **Subsets II (Umgang mit Duplikaten):** Wenn das Eingabe-Array Duplikate wie `[1, 2, 2]` enthält, erzeugt der Rekursionsbaum identische Teilmengen. Dies beheben Sie, indem Sie das Eingabe-Array zuerst sortieren und den "TAKE"-Zweig für jedes Element überspringen, das identisch mit dem vorherigen Element ist, WENN das vorherige Element "WEGGELASSEN" wurde!
- **Bitweise Teilfolgen (`bit_manipulation_04`):** Sie können alle $2^N$ Teilmengen vollständig iterativ unter Verwendung bitweiser Operationen generieren! Iterieren Sie i von 0 bis $2^N-1$. Die binäre Repräsentation von i (z. B. `101`) fungiert als Maske: schließe `nums[0]` ein, lasse `nums[1]` weg, schließe `nums[2]` ein.

## Anwendungen in der Praxis

- **Potenzmengen:** Generierung der mathematischen Potenzmenge $\mathcal{P}(S)$ einer gegebenen Menge, verwendet in Solvern für boolesche Erfüllbarkeitsprobleme und Algorithmen zur kombinatorischen Optimierung.

## Verwandte Algorithmen in cOde(n)

- **[backtracking_01 - Subsets](../backtracking/backtracking_01_subsets.md)** — Die Implementierung dieses exakten Algorithmus in der Kategorie Backtracking, strukturiert unter Verwendung einer `for`-Schleife anstelle von strikten "Nehmen/Weglassen"-Binärentscheidungen.
- **[recursion_01 - Power Sum](recursion_01_power-sum.md)** — Verwendet den identischen "Take it or Leave it"-Rekursionsbaum, summiert jedoch Zahlen, anstatt sie an Arrays anzuhängen.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) geschrieben wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitives Programmieren verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Seitenanfang. Quell-Repository: <https://github.com/dawei7/code_n>.*