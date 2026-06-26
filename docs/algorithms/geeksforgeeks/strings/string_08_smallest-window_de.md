# Kleinstes Fenster, das alle Zeichen enthält

| | |
|---|---|
| **ID** | `string_08` |
| **Kategorie** | strings |
| **Komplexität (erforderlich)** | $O(N)$ Zeit, $O(1)$ Platz |
| **Schwierigkeit** | 8/10 |
| **Relevanz für Vorstellungsgespräche** | 9/10 |
| **LeetCode-Äquivalent** | [Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/) |

## Problemstellung

Gegeben sind zwei Strings `s` und `t` mit den Längen `m` bzw. `n`.
Geben Sie den **Minimum Window Substring** von `s` zurück, sodass jedes Zeichen in `t` (einschließlich Duplikaten) im Fenster enthalten ist.
Falls kein solcher Substring existiert, geben Sie den leeren String `""` zurück.

**Eingabe:** Ein String `s` und ein String `t`.
**Ausgabe:** Ein String, der das kleinste Fenster repräsentiert.

## Wann man es verwendet

- Der absolute Höhepunkt der **Sliding Window**-Probleme in technischen Vorstellungsgesprächen.
- Wenn Sie das kürzeste zusammenhängende Segment finden müssen, das eine komplexe Häufigkeitsanforderung erfüllt.

## Ansatz

**1. Das "Expand and Shrink" Sliding Window:**
Wir verwalten ein physisches Fenster, das durch einen `left`-Pointer und einen `right`-Pointer definiert ist.
- **Expand:** Wir bewegen den `right`-Pointer nach rechts und nehmen Zeichen in unser Fenster auf, bis unser Fenster schließlich alle erforderlichen Zeichen von `t` enthält.
- **Shrink:** Sobald wir ein gültiges Fenster haben, könnte es unnötig lang sein (z. B. `"AxxxBxxxC"`). Wir versuchen es zu verkleinern, indem wir den `left`-Pointer nach rechts bewegen! Wir entfernen nacheinander Zeichen vom Anfang des Fensters und protokollieren jedes Mal die Fenstergröße, BIS das Entfernen eines Zeichens unser gültiges Fenster zerstört!
- Sobald das Fenster ungültig wird, setzen wir die Erweiterung mit dem `right`-Pointer fort, um das fehlende Zeichen erneut zu finden.

**2. Verfolgung von Häufigkeiten (Die Hash Maps):**
Wie wissen wir effizient, ob unser Fenster alle Zeichen von `t` enthält?
Wir verwenden zwei Hash Maps (oder Arrays fester Größe für 128 ASCII-Zeichen):
- `t_count`: Speichert die absolute Häufigkeit der benötigten Zeichen (z. B. `{'A': 1, 'B': 1, 'C': 1}`).
- `window_count`: Speichert die Häufigkeit der Zeichen, die sich aktuell in unserem Sliding Window befinden.

**3. Die `have` vs `need` Optimierung:**
Das Überprüfen, ob zwei Hash Maps perfekt übereinstimmen, benötigt $O(26)$ oder $O(128)$ Zeit. Dies bei jedem Schritt des Sliding Windows zu tun, ist langsam.
Stattdessen verwalten wir zwei Integer-Zähler: `have` und `need`.
- `need` ist die Gesamtzahl der EINZIGARTIGEN Zeichen in `t`.
- `have` beginnt bei 0. Jedes Mal, wenn wir ein Zeichen zu unserem Fenster hinzufügen, aktualisieren wir `window_count`. Wenn `window_count[char]` exakt `t_count[char]` entspricht, erhöhen wir `have`!
- In dem Moment, in dem `have == need` gilt, wissen wir, dass unser Fenster zu 100 % gültig ist, ohne jemals über die Hash Maps iterieren zu müssen!

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for string_08: Smallest Window.

Sliding window: smallest substring of s containing all chars of p.
"""


def solve(s, p):
    n = len(s)
    if not p or not s:
        return ""
    need = set(p)
    best = ""
    left = 0
    have = set()
    for right in range(n):
        if s[right] in need:
            have.add(s[right])
        while True:
            # Check if we have everything in the current window.
            covered = all((c in have) for c in need) if have else False
            if not covered or left > right:
                break
            window = s[left:right + 1]
            if not best or len(window) < len(best):
                best = window
            if s[left] in need:
                pass
            left += 1
            have = set()
            for k in range(left, right + 1):
                if s[k] in need:
                    have.add(s[k])
    return best
```

</details>

## Durchlauf

`s = "ADOBECODEBANC"`, `t = "ABC"`.
`t_count = {'A':1, 'B':1, 'C':1}`. `need = 3`.

1. **Expand `right`:**
   - Füge `A` hinzu. `have=1`.
   - Füge `D, O, B` hinzu. `have=2`.
   - Füge `E, C` hinzu. `have=3`.
2. **Gültiges Fenster gefunden!** `have == need`.
   - Fenster: `"ADOBEC"` (Indizes 0 bis 5). Länge 6.
   - **Shrink `left`:** Entferne `A`.
   - `window_count['A']` fällt auf 0. `have` fällt auf 2! Schleife bricht ab.
   - `left` bewegt sich auf 1.
3. **Expand `right`:**
   - Füge `O, D, E, B, A` hinzu.
   - `A` hinzugefügt! `have` kehrt auf 3 zurück!
4. **Gültiges Fenster gefunden!**
   - Fenster: `"DOBECODEBA"` (Indizes 1 bis 10). Länge 10. (Länge > 6, daher speichern wir es nicht).
   - **Shrink `left`:** Entferne `D, O, B, E, C`.
   - Das Entfernen von `C` lässt `have` auf 2 fallen. Schleife bricht ab.
   - `left` ist nun bei Index 6.
5. **Expand `right`:**
   - Füge `N, C` hinzu.
   - `C` hinzugefügt! `have` kehrt auf 3 zurück!
6. **Gültiges Fenster gefunden!**
   - Fenster: `"ODEBANC"` (Indizes 6 bis 12).
   - **Shrink `left`:** Entferne `O, D, E`.
   - Fenster ist `"BANC"` (Indizes 9 bis 12). Länge 4! Neuer Rekord!
   - Entferne `B`. `have` fällt auf 2. Schleife bricht ab.

Ende des Strings. Gib `"BANC"` zurück. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(N)$ | $O(1)$ |
| **Durchschnittlicher Fall** | $O(N)$ | $O(1)$ |
| **Schlechtester Fall** | $O(N)$ | $O(1)$ |

Der `right`-Pointer beginnt bei Index 0 und bewegt sich bis Index N-1, wobei er N Schritte ausführt.
Der `left`-Pointer beginnt bei Index 0 und bewegt sich bis Index N-1, wobei er N Schritte ausführt.
Ein Pointer bewegt sich NIEMALS rückwärts. Die Zeichen werden genau einmal zum Fenster hinzugefügt und genau einmal entfernt.
Gesamtoperationen = 2N. Die Zeitkomplexität ist strikt $O(N)$.
Die Platzkomplexität ist technisch $O(1)$ konstante Zeit, da die Zeichen des Strings ASCII (oder Unicode) sind, was bedeutet, dass die Hash Maps niemals eine maximale Größe von 128 (oder 256) Schlüsseln überschreiten, unabhängig davon, ob der String 10 Millionen Zeichen lang ist!

## Varianten & Optimierungen

- **Längster Substring ohne wiederholende Zeichen (`string_11`):** Die exakt gleiche "Expand and Shrink"-Logik, aber die Bedingung zum Verkleinern lautet einfach: "Solange das neu hinzugefügte Zeichen bereits in der Hash Map enthalten ist".
- **Alle Anagramme in einem String finden:** Die gleiche Logik, aber die Fenstergröße ist strikt auf `len(t)` festgelegt. Anstatt dynamisch zu expandieren und zu schrumpfen, bewegt sich `left` exakt im Gleichschritt mit `right`.

## Anwendungen in der Praxis

- **Netzwerk-Paketanalyse:** Finden des engsten Übertragungsfensters in einem kontinuierlichen Strom von TCP-Paketen, bei dem alle erforderlichen Header-Flags erfolgreich protokolliert wurden, bevor ein Fehler auftrat.

## Verwandte Algorithmen in cOde(n)

- **[two_pointers_01 - Two Sum Sorted](../two_pointers/two_pointers_01_two-sum-sorted.md)** — Die einfachere Version von Two Pointers, bei der die Pointer an entgegengesetzten Enden starten. Sliding Window ist eine Teilmenge von Two Pointers, bei der sich beide Pointer in die gleiche Richtung bewegen.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) verfasst wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitives Programmieren verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Seitenanfang. Quell-Repository: <https://github.com/dawei7/code_n>.*