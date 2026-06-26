# Anzahl der eindeutigen Elemente in jedem Fenster

| | |
|---|---|
| **ID** | `hash_05` |
| **Kategorie** | Hashing |
| **Komplexität (erforderlich)** | $O(N)$ Zeit, $O(K)$ Platz |
| **Schwierigkeit** | 4/10 |
| **Relevanz für Vorstellungsgespräche** | 6/10 |
| **GeeksForGeeks-Äquivalent** | [Count distinct elements in every window of size K](https://www.geeksforgeeks.org/count-distinct-elements-in-every-window-of-size-k/) |

## Problemstellung

Gegeben ist ein Array von Integern `nums` und ein Integer `K`. Bestimmen Sie die Anzahl der eindeutigen Elemente in jedem zusammenhängenden Sliding Window der Größe `K` von links nach rechts.

**Eingabe:** Ein Integer-Array `nums` der Größe `N` und eine Fenstergröße `K`.
**Ausgabe:** Ein Array von Integern, das die Anzahl der eindeutigen Elemente für jedes Fenster repräsentiert.

## Wann man es verwendet

- Um Hash Maps mit der Sliding-Window-Technik zu kombinieren.
- Wenn Sie eine laufende Häufigkeitszählung pflegen müssen, während Elemente dynamisch in Ihr aktives Sub-Array eintreten und es wieder verlassen.

## Ansatz

**1. Der Fehler bei Sets:**
Wenn wir nur die Anzahl der eindeutigen Elemente eines einzelnen Arrays bestimmen wollten, könnten wir alle Elemente in ein Hash Set werfen und `len(set)` zurückgeben.
Aber während das Fenster gleitet, fällt das Element `nums[i - K]` aus dem Fenster. Wenn wir einfach `set.remove(nums[i - K])` ausführen, könnten wir versehentlich eine Zahl löschen, die AUCH an einer anderen Stelle innerhalb des Fensters existiert! Wir müssen GENAU wissen, wie viele Kopien dieser Zahl sich aktuell im Fenster befinden.

**2. Die Häufigkeits-Map:**
Anstelle eines Sets verwenden wir eine Hash Map (Dictionary), wobei `Key = Zahl` und `Value = Häufigkeit`.
Die Anzahl der eindeutigen Elemente ist einfach die Anzahl der aktiven Keys in der Hash Map (d. h. `len(map)`).

**3. Das Sliding Window:**
1. **Initialisierung:** Fügen Sie manuell die ersten `K` Elemente in die Häufigkeits-Map ein. Speichern Sie `len(map)` als Antwort für das erste Fenster.
2. **Gleiten:** Iterieren Sie von `i = K` bis `N-1`.
   - **Neues Element hinzufügen:** `nums[i]` tritt in das Fenster ein. Erhöhen Sie dessen Häufigkeit in der Map.
   - **Altes Element entfernen:** `nums[i - K]` fällt aus dem Fenster. Verringern Sie dessen Häufigkeit in der Map.
   - **Entscheidende Bereinigung:** Wenn die Häufigkeit von `nums[i - K]` den Wert `0` erreicht, ist es vollständig aus dem Fenster verschwunden! Wir MÜSSEN `del map[nums[i - K]]` ausführen, um den Key vollständig zu löschen, damit `len(map)` korrekt die Anzahl der eindeutigen Elemente widerspiegelt!
3. Hängen Sie `len(map)` an das Ergebnis-Array an.

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for hash_05: Count Distinct Elements in Window.

For each window of size k, return the number of distinct
elements. Sliding window + count map: O(n) total.
"""


def solve(arr, k, n):
    if k <= 0 or k > n:
        return []
    counts = {}
    out = []
    for i in range(k):
        counts[arr[i]] = counts.get(arr[i], 0) + 1
    out.append(len(counts))
    for i in range(k, n):
        counts[arr[i]] = counts.get(arr[i], 0) + 1
        old = arr[i - k]
        counts[old] -= 1
        if counts[old] == 0:
            del counts[old]
        out.append(len(counts))
    return out
```

</details>

## Durchlauf

`nums = [1, 2, 1, 3, 4, 2, 3]`, `K = 4`.

1. **Initialisierung des ersten Fensters (Indizes 0 bis 3):** `[1, 2, 1, 3]`.
   - `freq_map = {1: 2, 2: 1, 3: 1}`.
   - `len(map) = 3`. `results = [3]`.
2. **Gleiten zu i=4 (eingehend 4, ausgehend 1):**
   - Füge `4` hinzu: `freq_map = {1: 2, 2: 1, 3: 1, 4: 1}`.
   - Entferne `nums[4-4] = nums[0] = 1`. `freq_map[1]` sinkt von 2 auf 1.
   - `freq_map = {1: 1, 2: 1, 3: 1, 4: 1}`.
   - `len(map) = 4`. `results = [3, 4]`.
3. **Gleiten zu i=5 (eingehend 2, ausgehend 2):**
   - Füge `2` hinzu: `freq_map[2]` wird 2.
   - Entferne `nums[5-4] = nums[1] = 2`. `freq_map[2]` sinkt zurück auf 1.
   - `freq_map = {1: 1, 2: 1, 3: 1, 4: 1}`.
   - `len(map) = 4`. `results = [3, 4, 4]`.
4. **Gleiten zu i=6 (eingehend 3, ausgehend 1):**
   - Füge `3` hinzu: `freq_map[3]` wird 2.
   - Entferne `nums[6-4] = nums[2] = 1`. `freq_map[1]` sinkt auf 0!
   - `del freq_map[1]`!
   - `freq_map = {2: 1, 3: 2, 4: 1}`.
   - `len(map) = 3`. `results = [3, 4, 4, 3]`.

Ergebnis: `[3, 4, 4, 3]`. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(N)$ | $O(K)$ |
| **Durchschnittlicher Fall** | $O(N)$ | $O(K)$ |
| **Schlechtester Fall** | $O(N)$ | $O(K)$ |

Wir iterieren genau einmal durch das Array der Länge N. Bei jedem Schritt benötigen das Einfügen in das Dictionary, das Dekrementieren und das Löschen von Keys jeweils amortisiert $O(1)$ Zeit. Die gesamte Zeitkomplexität ist strikt $O(N)$.
Die Platzkomplexität beträgt $O(K)$, da das Dictionary maximal K eindeutige Keys enthalten wird (die maximale Größe des Sliding Window).

## Varianten & Optimierungen

- **Sliding Window Maximum (`two_pointers_05`):** Wenn Sie aufgefordert werden, das *Maximum Element* in jedem Fenster der Größe K anstelle der *Anzahl der eindeutigen Elemente* zu finden, schlägt eine Hash Map fehl, da das Finden des `max()` der Keys $O(K)$ Zeit pro Fenster benötigt! Sie müssen eine Monotonic Deque verwenden.

## Anwendungen in der Praxis

- **Überwachung des Netzwerkverkehrs:** Erkennung von DDoS-Angriffen durch Aufrechterhaltung eines rollierenden Fensters der letzten 10.000 eingehenden IP-Adressen. Wenn die "Anzahl der eindeutigen Elemente" plötzlich sinkt, während das Paketvolumen hoch bleibt, überflutet eine einzelne IP den Server.

## Verwandte Algorithmen in cOde(n)

- **[hash_03 - Longest Substring Without Repeating](hash_03_longest-substring-without-repeating.md)** — Ein weiterer Algorithmus, der Hash Maps mit Sliding Windows kombiniert, jedoch mit einem dynamisch in der Größe anpassbaren Fenster anstelle einer festen Größe `K`.
- **[two_pointers_05 - Sliding Window Maximum](../two_pointers/two_pointers_05_sliding-window-maximum.md)** — Die Deque-basierte Variante zur Verfolgung von Extremwerten in einem festen Fenster.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) verfasst wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitive Programmierung verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Seitenanfang. Quell-Repository: <https://github.com/dawei7/code_n>.*