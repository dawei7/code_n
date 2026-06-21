# Longest Common Prefix (Trie-Methode)

| | |
|---|---|
| **ID** | `trie_03` |
| **Kategorie** | trie |
| **Komplexität (erforderlich)** | $O(N \times M)$ Zeit, $O(N \times M)$ Platz |
| **Schwierigkeit** | 3/10 |
| **Relevanz für Vorstellungsgespräche** | 6/10 |
| **LeetCode-Äquivalent** | [Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/) |

## Problemstellung

Schreiben Sie eine Funktion, um den längsten gemeinsamen Präfix-String innerhalb eines Arrays von Strings zu finden.
Wenn kein gemeinsamer Präfix existiert, geben Sie einen leeren String `""` zurück.

*(Hinweis: Wir haben dies bereits in `string_11` mittels Horizontal Scanning in $O(N \times M)$ Zeit und $O(1)$ Platz gelöst. Dieses Dokument demonstriert die Trie-basierte Lösung, die in Vorstellungsgesprächen oft als Folgefrage gestellt wird, um Ihr Wissen über Tries zu prüfen).*

**Eingabe:** Ein Array von Strings `strs`.
**Ausgabe:** Ein String, der den längsten gemeinsamen Präfix repräsentiert.

## Wann man diese Methode verwendet

- In einem Vorstellungsgespräch, wenn der Interviewer sagt: "Großartig, Ihr $O(1)$ Platz-Horizontal-Scanning ist perfekt. Was aber, wenn das Array von Strings eine riesige Streaming-Datenbank ist, die sich ständig aktualisiert, und wir den Longest Common Prefix dynamisch abfragen müssen, ohne das gesamte Array neu zu scannen?"
- Ihre Antwort: "Wir bauen einen Trie!"

## Ansatz

**1. Die "Einzelkind"-Eigenschaft:**
Was passiert, wenn Sie ein Array von Strings in einen Trie einfügen?
Wenn alle Strings einen gemeinsamen Präfix teilen, wie `"flower"`, `"flow"` und `"flight"`, beginnen sie alle mit `"fl"`.
Betrachten Sie die Wurzel des Trie. Sie hat nur ein Kind: `'f'`.
Betrachten Sie den `'f'`-Knoten. Er hat nur ein Kind: `'l'`.
Betrachten Sie den `'l'`-Knoten. Er hat ZWEI Kinder! `'o'` und `'i'`!
Der Longest Common Prefix entspricht mathematisch dem einzelnen, unverzweigten Pfad von der Wurzel des Trie abwärts!

**2. Die Abbruchbedingungen:**
Wir fügen jeden String in den Trie ein. Dann starten wir an der Wurzel und verfolgen den Pfad nach unten.
Wir fügen Zeichen zu unserem Ergebnis-String hinzu, solange:
1. Der aktuelle Knoten GENAU 1 Kind hat. (Wenn er 2 Kinder hat, haben sich die Strings verzweigt! Stopp!)
2. Der aktuelle Knoten NICHT das Ende eines Wortes ist! (Wenn `"flow"` hier endet, können wir nicht fortfahren, selbst wenn der einzige Kind-Pfad zu `"flower"` weiterführt, da `"flow"` physisch keinen längeren Präfix als sich selbst haben kann!).

**3. Die Ausführung der Verfolgung:**
Wir verwalten unseren `current_node`. Wir prüfen `len(current_node.children)`. Wenn die Länge `1` ist, nehmen wir das Zeichen dieses einen Kindes, hängen es an unser Ergebnis an, bewegen unseren Pointer nach unten und wiederholen den Vorgang!

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for trie_03: Longest Common Prefix.

Walk the trie from the root. While the current node has
exactly one child and is not a word end, descend.
"""


def solve(words, n):
    if n == 0:
        return ""
    children = []
    is_end = []

    def new_node():
        children.append({})
        is_end.append(False)
        return len(children) - 1

    root = new_node()
    for w in words:
        cur = root
        for ch in w:
            nxt = children[cur].get(ch)
            if nxt is None:
                nxt = new_node()
                children[cur][ch] = nxt
            cur = nxt
        is_end[cur] = True
    out = []
    cur = root
    while len(children[cur]) == 1 and not is_end[cur]:
        ch, nxt = next(iter(children[cur].items()))
        out.append(ch)
        cur = nxt
    return "".join(out)
```

</details>

## Durchlauf

`strs = ["flower", "flow", "flight"]`.

**Aufbau des Trie:**
Wurzel -> `'f'` -> `'l'`.
Von `'l'` verzweigt es sich in:
- `'o'` -> `'w'` (Wortende) -> `'e'` -> `'r'` (Wortende).
- `'i'` -> `'g'` -> `'h'` -> `'t'` (Wortende).

**Verfolgung für LCP:**
1. Start bei `root`.
   - `len(children)` ist 1 (`'f'`).
   - Kein Wortende.
   - Hänge `'f'` an. `lcp = ["f"]`.
   - Gehe zu `'f'`.
2. Bei `'f'`:
   - `len(children)` ist 1 (`'l'`).
   - Kein Wortende.
   - Hänge `'l'` an. `lcp = ["f", "l"]`.
   - Gehe zu `'l'`.
3. Bei `'l'`:
   - `len(children)` ist 2 (`'o'` und `'i'`).
   - `len(curr.children) > 1` löst `break` aus!
4. Gib `"".join(["f", "l"])` zurück.

Ausgabe: `"fl"`. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(N \times M)$ | $O(N \times M)$ |
| **Durchschnittlicher Fall** | $O(N \times M)$ | $O(N \times M)$ |
| **Schlechtester Fall** | $O(N \times M)$ | $O(N \times M)$ |

Sei N die Anzahl der Strings und M die maximale Länge eines Strings.
Das Einfügen aller Strings in den Trie erfordert die Verarbeitung jedes Zeichens, was genau $O(N \times M)$ Zeit in Anspruch nimmt.
Das Verfolgen des Pfades nach unten benötigt maximal $O(M)$ Zeit.
Die gesamte Zeitkomplexität beträgt $O(N \times M)$.
Die Platzkomplexität beträgt $O(N \times M)$, da wir physisch einen massiven Trie im Speicher aufbauen, der jedes einzelne Zeichen des Arrays enthält (im Gegensatz zum Horizontal-Scanning-Ansatz, der $O(1)$ Platz benötigt).

## Varianten & Optimierungen

- **Dynamische Updates:** Dieser Ansatz ist für statische Arrays grundsätzlich schlechter als Horizontal Scanning. Wenn das Array jedoch dynamisch ist (Strings werden kontinuierlich hinzugefügt und entfernt), erfordert Horizontal Scanning jedes Mal einen $O(N \times M)$ Rescan! Ein Trie handhabt Einfügungen in $O(M)$ Zeit und Löschungen in $O(M)$ Zeit, und die Aktualisierung des LCP dauert $O(M)$ Zeit. Er ist für dynamische Datensätze exponentiell schneller!

## Anwendungen in der Praxis

- **Routing-Tabellen:** IP-Paket-Routing in Computernetzwerken verwendet spezialisierte Tries (Radix Trees / Patricia Tries), um den längsten passenden IP-Präfix-Subnetz-Eintrag dynamisch zu finden, während neue Router dem globalen Netzwerk beitreten oder es verlassen.

## Verwandte Algorithmen in cOde(n)

- **[string_11 - Longest Common Prefix](../strings/string_11_longest-common-substring.md)** — Der $O(1)$ Platz-Algorithmus, den Sie in Standard-Vorstellungsgesprächen tatsächlich verwenden sollten.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) verfasst wurde und sich an der kanonischen Struktur orientiert, die von Wettbewerbsprogrammierungs-Referenzseiten verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Seitenanfang. Quell-Repository: <https://github.com/dawei7/code_n>.*