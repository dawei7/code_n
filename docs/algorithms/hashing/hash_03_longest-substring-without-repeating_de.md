# Longest Substring Without Repeating Characters

| | |
|---|---|
| **ID** | `hash_03` |
| **Kategorie** | hashing |
| **Komplexität (erforderlich)** | $O(n)$ |
| **Schwierigkeit** | 4/10 |
| **Relevanz für Vorstellungsgespräche** | 9/10 |
| **Wikipedia** | [Sliding window](https://en.wikipedia.org/wiki/Sliding_window) |

## Problemstellung

Gegeben ist ein String `s`. Finde die Länge des **längsten Teilstrings** (zusammenhängend) ohne sich wiederholende Zeichen.

**Eingabe:** ein String `s`.
**Ausgabe:** die Länge des längsten Teilstrings, der nur aus eindeutigen Zeichen besteht.

**Beispiel:**

| s | Antwort | Teilstring |
|---|---:|---|
| `"abcabcbb"` | 3 | `"abc"` |
| `"bbbbb"` | 1 | `"b"` |
| `"pwwkew"` | 3 | `"wke"` |
| `""` | 0 | `""` |
| `"abcdef"` | 6 | `"abcdef"` |
| `"aab"` | 2 | `"ab"` |

## Anwendung

- LeetCode #3. Das kanonische **Sliding Window + Hash Set** Problem. Wird in Telefoninterviews bei fast jedem Unternehmen abgefragt.
- Testet das **"expand right, contract left"** Sliding-Window-Muster, das in vielen anderen Problemen wiederkehrt (längstes Subarray mit Summe ≤ k, Minimum Window Substring, etc.).

## Ansatz

**Sliding Window** mit einem Hash Set, das die Zeichen im aktuellen Fenster verfolgt.

Wir verwalten ein Fenster `[left, right]` (beide inklusive) und ein Hash Set `in_window` mit den Zeichen innerhalb dieses Fensters.

Für jedes `right` von `0` bis `n-1`:
1. Während `s[right]` bereits in `in_window` enthalten ist (d. h. `s[right]` erscheint an einer Position ≥ `left`):
   - Entferne `s[left]` aus `in_window`.
   - Erhöhe `left` um 1.
2. Füge `s[right]` zu `in_window` hinzu.
3. Aktualisiere das Ergebnis: `ans = max(ans, right - left + 1)`.

**Warum es funktioniert:** Das Fenster enthält immer nur "eindeutige Zeichen", und wir erweitern es gierig (greedy). Wenn ein Duplikat eintreten würde, verkleinern wir das Fenster von links, bis das Duplikat entfernt wurde. Jedes Zeichen tritt höchstens einmal in das Fenster ein und verlässt es wieder, daher beträgt der Gesamtaufwand $O(n)$.

**Optimierung mit einer Hash Map (Index des letzten Vorkommens):** Anstatt eines Sets und einer While-Schleife speichern wir den letzten Index, an dem jedes Zeichen aufgetreten ist. Wenn wir `s[right]` hinzufügen würden, springen wir mit `left` auf `max(left, last_seen[s[right]] + 1)`. Dies ist $O(n)$ mit $O(1)$ Aufwand pro Zeichen (keine While-Schleife), aber konzeptionell äquivalent.

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for hash_03: Longest Substring Without Repeating.

Sliding window: extend the right end, record the last index of
each character seen. If a repeat sits inside the window, jump
the left end past the previous occurrence. O(n).
"""


def solve(s, n):
    if n == 0:
        return 0
    last = {}
    best = 0
    left = 0
    for right in range(n):
        ch = s[right]
        if ch in last and last[ch] >= left:
            left = last[ch] + 1
        last[ch] = right
        if right - left + 1 > best:
            best = right - left + 1
    return best
```

</details>

## Ablauf

`s = "abcabcbb"`. Erwartet: 3.

| right | ch | ch im Fenster? | Aktion | Fenster | in_window | best |
|---:|---:|---|---|---|---|---:|
| 0 | a | nein | hinzufügen | "a" | {a} | 1 |
| 1 | b | nein | hinzufügen | "ab" | {a, b} | 2 |
| 2 | c | nein | hinzufügen | "abc" | {a, b, c} | **3** |
| 3 | a | ja | entferne b, dann entferne a, dann füge a hinzu | "bca" | {b, c, a} | 3 |
| 4 | b | ja | entferne c, entferne a, entferne b? Nein — b ist an Pos 1, nach Entfernen von c (Pos 2) und a (Pos 3) wird das Fenster zu "b", dann füge b hinzu | "ab" | {a, b} | 3 |
| 5 | c | nein | hinzufügen | "abc" | {a, b, c} | 3 |
| 6 | b | ja | entferne a, entferne b, dann füge b hinzu | "cb" | {c, b} | 3 |
| 7 | b | ja | entferne c, entferne b, dann füge b hinzu | "b" | {b} | 3 |

Antwort: 3. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(n)$ | $O(min(n, σ)$) |
| **Durchschnittlicher Fall** | $O(n)$ | $O(min(n, σ)$) |
| **Schlechtester Fall** | $O(n)$ | $O(min(n, σ)$) |

`σ` = die Größe des Zeichensatzes (z. B. 26 für englische Kleinbuchstaben, 128 für ASCII, ~65k für vollständiges Unicode). Das Hash Set speichert höchstens `min(n, σ)` Zeichen.

Die Hash-Map-Variante verwendet ebenfalls $O(min(n, σ)$) Platz.

## Varianten & Optimierungen

- **Längster Teilstring mit höchstens K eindeutigen Zeichen** — gleiche Struktur, aber das Prädikat für die Gültigkeit des Fensters lautet "höchstens K eindeutige Zeichen", nicht "keine Duplikate". Die Kontraktion ist aufwendiger (Anzahl zählen, nicht nur Mitgliedschaft).
- **Längster Teilstring mit nur eindeutigen Vokalen** — gleiche Struktur, Einschränkung auf Vokale.
- **Minimum Window Substring** — finde das kleinste Fenster in `s`, das alle Zeichen von `t` enthält. Gleiches Sliding Window; das Prädikat lautet "enthält den Zeichensatz von t".
- **Längster Teilstring mit nicht mehr als K Ersetzungen** — füge einen Zähler für das am häufigsten vorkommende Zeichen hinzu; das Fenster ist gültig, wenn `window_size - max_freq <= k`.
- **Längste Ersetzung bei wiederholten Zeichen** — gleiche Struktur wie oben.

## Praxisanwendungen

- **String-Deduplizierung** — Finden der längsten Sequenz eindeutiger Zeichen (wird in der Kompression und Kodierung verwendet).
- **Eindeutigkeit von Cache-Line-Keys** — Finden der längsten zusammenhängenden Sequenz eindeutiger Keys in einem Speicherzugriffsprotokoll.
- **Bioinformatik** — Finden des längsten DNA-Abschnitts ohne wiederholte Basen innerhalb eines Fensters.
- **Kompression** — LZ77-artige Kompression sucht nach dem längsten bereits gesehenen Präfix; dies entspricht der gleichen Struktur.
- **Sliding-Window-Aggregationen** — Das gleiche Muster liegt vielen Problemen zugrunde, die nach dem "längsten / kürzesten / min / max Subarray mit Eigenschaft X" suchen.

## Verwandte Algorithmen in cOde(n)

- **[hash_01 — Two Sum](hash_01_two-sum.md)** — gleicher Hash-Map-Ansatz, anderes Problem. (d=4/10, r=9/10)
- **[hash_02 — Subarray Sum Equals K](hash_02_subarray-sum-equals-k.md)** — Präfixsumme + Hash Map. (d=4/10, r=9/10)
- **[hash_04 — Group Anagrams](hash_04_group-anagrams.md)** — Hash Map als Kategorisierungswerkzeug. (d=4/10, r=9/10)
- **[string_03 — Longest Substring Without Repeating](string_03_longest-substring-without-repeating.md)** — gleiches Problem in der Kategorie Strings. (d=4/10, r=7/10)

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) geschrieben wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitives Programmieren verwendet wird. Für den enzyklopädischen Standardeintrag folgen Sie dem Wikipedia-Link am Seitenanfang. Quell-Repository: <https://github.com/dawei7/code_n>.*