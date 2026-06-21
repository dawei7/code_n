# Wortzählung mit Präfix

| | |
|---|---|
| **ID** | `trie_02` |
| **Kategorie** | trie |
| **Komplexität (erforderlich)** | $O(M)$ Zeit, $O(M)$ Platz |
| **Schwierigkeit** | 3/10 |
| **Relevanz für Vorstellungsgespräche** | 7/10 |
| **GeeksForGeeks Äquivalent** | [Find the count of words with a given prefix](https://www.geeksforgeeks.org/find-count-of-words-with-a-given-prefix/) |

## Problemstellung

Gegeben ist eine Liste von Strings (ein Wörterbuch) und ein `prefix`-String. Ermitteln Sie die Gesamtzahl der gültigen Wörter im Wörterbuch, die mit dem gegebenen `prefix` beginnen.
Sie müssen in der Lage sein, diese Abfrage tausende Male effizient durchzuführen.

**Eingabe:** Ein Wörterbuch von Strings und ein Ziel-`prefix`.
**Ausgabe:** Eine Ganzzahl, die die Anzahl der Wörter repräsentiert, die auf das Präfix passen.

## Wann man es verwendet

- Zur Optimierung von Echtzeit-Auto-Complete-Systemen, bei denen dem Benutzer angezeigt werden soll, wie viele Ergebnisse mit seiner aktuell eingegebenen Suchanfrage übereinstimmen, bevor er die Eingabetaste drückt.
- Eine elegante Demonstration, wie Tries mit mathematischen Zuständen erweitert werden können.

## Ansatz

**1. Der naive Ansatz ($O(N \times M)$):**
Man könnte über alle N Wörter im Wörterbuch iterieren und `.startswith(prefix)` verwenden. Dies benötigt $O(M)$ Zeit pro Wort.
Wenn das Wörterbuch 100.000 Wörter enthält, verbraucht dies für eine einzige Abfrage enorme CPU-Zyklen.

**2. Die ineffiziente Trie-Suche ($O(V)$):**
Man könnte alle Wörter in einen Standard-Trie einfügen. Man traversiert den `prefix` hinunter. Wenn man das Ende des Präfixes erreicht, führt man eine umfangreiche Tiefensuche (DFS) durch alle verbleibenden Kindknoten durch und zählt explizit jeden Knoten, bei dem `is_end_of_word == True` gilt.
Dies ist schneller als der naive Ansatz, erfordert aber immer noch das Traversieren hunderter Knoten, wenn das Präfix auf tausende Wörter passt!

**3. Der erweiterte Trie ($O(M)$):**
Wenn wir wissen wollen, wie viele Wörter im Teilbaum unterhalb eines bestimmten Knotens existieren, warum behalten wir das nicht einfach im Auge, wenn wir den Baum aufbauen?!
Wir erweitern unsere `TrieNode`-Klasse um eine neue Ganzzahl-Eigenschaft: `prefix_count`.
Wenn wir ein Wort wie `"apple"` einfügen, inkrementieren wir beim Traversieren der Knoten `'a'`, `'p'`, `'p'`, `'l'`, `'e'` physisch `prefix_count += 1` auf JEDEM EINZELNEN KNOTEN, den wir passieren!
Wenn wir später `"app"` abfragen, traversieren wir bis zu `'p'`. Wir führen KEINE DFS durch! Wir geben einfach `curr.prefix_count` zurück! Dies verrät uns sofort, wie viele Wörter während des Einfügens diesen Knoten passiert haben!

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for trie_02: Word Count with Prefix.

Count the words in the trie that start with prefix.
"""


def solve(words, n, prefix):
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
    cur = root
    for ch in prefix:
        if ch not in children[cur]:
            return 0
        cur = children[cur][ch]
    count = 0

    def dfs(i):
        nonlocal count
        if is_end[i]:
            count += 1
        for nxt in children[i].values():
            dfs(nxt)

    dfs(cur)
    return count
```

</details>

## Durchlauf

Wörterbuch: `["apple", "apply", "ape", "bat"]`.

**Aufbau des Trie:**
- `insert("apple")`: 
  `'a'` (count 1) -> `'p'` (count 1) -> `'p'` (count 1) -> `'l'` (count 1) -> `'e'` (count 1).
- `insert("apply")`: 
  `'a'` (count 2) -> `'p'` (count 2) -> `'p'` (count 2) -> `'l'` (count 2) -> `'y'` (count 1).
- `insert("ape")`: 
  `'a'` (count 3) -> `'p'` (count 3) -> `'e'` (count 1).
- `insert("bat")`: 
  `'b'` (count 1) -> `'a'` (count 1) -> `'t'` (count 1).

**Abfrage:**
`count_prefix("ap")`
- Gehe zu `'a'`.
- Gehe zu `'p'`.
- Der Knoten `'p'` hat `prefix_count = 3`.
- Gibt sofort `3` zurück! ✓ (Passt auf "apple", "apply", "ape").

`count_prefix("appl")`
- Gehe zu `'a'`, `'p'`, `'p'`, `'l'`.
- Der Knoten `'l'` hat `prefix_count = 2`.
- Gibt sofort `2` zurück! ✓ (Passt auf "apple", "apply").

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(M)$ | $O(1)$ |
| **Durchschnittlicher Fall** | $O(M)$ | $O(M)$ |
| **Schlechtester Fall** | $O(M)$ | $O(M)$ |

Das Einfügen benötigt $O(M)$ Zeit, wobei M die Länge des Strings ist.
Die Abfrage benötigt $O(P)$ Zeit, wobei P die Länge des Präfixes ist.
Es gibt während der Abfragephase absolut keine Abhängigkeit von der Größe des Wörterbuchs (N)! Eine Abfragezeit von $O(M)$ ist mathematisch optimal und erfolgt sofort.
Die Platzkomplexität beträgt $O(M)$ pro eingefügtem Wort für den Aufbau der Knoten, aber Abfragen benötigen $O(1)$ Platz.

## Varianten & Optimierungen

- **Wortlöschung:** Wenn Sie das Entfernen von Wörtern aus dem Wörterbuch unterstützen müssen, verfolgen Sie einfach das Wort und dekrementieren Sie `prefix_count -= 1` auf jedem Knoten! (Siehe `trie_04`).
- **Beliebtestes Auto-Complete:** Anstatt eine Ganzzahl zu speichern, speichern Sie einen `max_score` und einen `popular_string`! Wenn Sie Wörter einfügen und deren Beliebtheitswert höher ist als der `max_score` des Knotens, überschreiben Sie den Knoten mit dem neuen besten String. Wenn ein Benutzer ein Präfix abfragt, können Sie den #1 beliebtesten Auto-Complete-Vorschlag in exakt $O(1)$ Zeit zurückgeben, nachdem Sie das Präfix verfolgt haben!

## Anwendungen in der Praxis

- **SQL `LIKE 'app%'` Analytik:** Optimierung von Backend-Abfrageplanern bei der Ermittlung der Gesamthäufigkeit von Datensätzen in Textspalten, die mit einem bestimmten Teilstring beginnen.

## Verwandte Algorithmen in cOde(n)

- **[trie_01 - Trie Insert/Search](trie_01_trie-insert-and-search.md)** — Die grundlegende Datenstruktur, die diese Erweiterung ermöglicht.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) verfasst wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitives Programmieren verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Seitenanfang. Quell-Repository: <https://github.com/dawei7/code_n>.*