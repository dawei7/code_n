# Formale mathematische Spezifikation: Word Count mit Präfix

## 1. Definitionen und Notation

Sei $\Sigma$ ein endliches Alphabet. Ein Wörterbuch $D$ ist eine endliche Menge von Strings $D = \{s_1, s_2, \dots, s_N\}$, wobei jedes $s_i \in \Sigma^*$ ist. 

Wir definieren einen **Trie** als einen gewurzelten Baum $T = (V, E)$, wobei:
*   $V$ die Menge der Knoten ist. Jeder Knoten $v \in V$ repräsentiert ein Präfix $p \in \Sigma^*$.
*   $E \subseteq V \times V$ die Menge der gerichteten Kanten ist, wobei eine mit $\sigma \in \Sigma$ beschriftete Kante $(u, v)$ existiert, falls das durch $v$ repräsentierte Präfix $p_u \cdot \sigma$ ist.
*   $\text{root} \in V$ die leere Zeichenkette $\epsilon$ repräsentiert.
*   $\text{count}(v): V \to \mathbb{N}_0$ eine Augmentierungsfunktion ist, die jeden Knoten $v$ auf die Anzahl der Strings in $D$ abbildet, die das mit $v$ assoziierte Präfix besitzen.

Gegeben ein Anfrage-Präfix $q \in \Sigma^*$, ist das Ziel, die Funktion $f(q)$ zu berechnen:
$$f(q) = |\{s \in D \mid q \text{ ist ein Präfix von } s\}|$$

## 2. Algebraische Charakterisierung

Die Korrektheit des Algorithmus beruht auf der induktiven Definition der Augmentierungsfunktion $\text{count}(v)$. 

Für jeden Knoten $v$, der das Präfix $p$ repräsentiert, sei $S_v = \{s \in D \mid p \text{ ist ein Präfix von } s\}$. Per Definition gilt $\text{count}(v) = |S_v|$. 

**Basis:**
Für den Wurzelknoten $r$, der $\epsilon$ repräsentiert:
$$\text{count}(r) = |D|$$

**Rekursionsschritt:**
Für einen Knoten $u$ und seinen durch die Kante $(u, v)$ verbundenen Nachfolger $v$, welche mit $\sigma$ beschriftet ist:
$$\text{count}(v) = \sum_{s \in S_u} \mathbb{I}(s \text{ beginnt mit } p_u \cdot \sigma)$$
wobei $\mathbb{I}(\cdot)$ die Indikatorfunktion ist. 

**Einfüge-Invariante:**
Beim Einfügen eines Wortes $w = \sigma_1\sigma_2\dots\sigma_m$ in den Trie definieren wir einen Pfad von Knoten $v_0, v_1, \dots, v_m$, wobei $v_0 = \text{root}$ und $v_i$ dem Präfix $w[1 \dots i]$ entspricht. Die Aktualisierungsregel für jeden Knoten $v_i$ auf dem Pfad lautet:
$$\text{count}(v_i) \leftarrow \text{count}(v_i) + 1$$
Dies stellt sicher, dass für jeden Knoten $v$, der das Präfix $p$ repräsentiert, $\text{count}(v)$ genau der Anzahl entspricht, wie oft der Einfügepfad durch $v$ verlaufen ist. Dies ist äquivalent zur Anzahl der Wörter in $D$, die $p$ als Präfix haben.

**Formulierung der Anfrage:**
Gegeben eine Anfrage $q = \sigma_1\sigma_2\dots\sigma_k$, sei $v_q$ der Knoten, der durch das Traversieren des Tries ausgehend von der Wurzel entlang der Zeichenfolge in $q$ erreicht wird. Falls der Pfad existiert, ist das Ergebnis:
$$f(q) = \text{count}(v_q)$$
Falls der Pfad nicht existiert, gilt $f(q) = 0$.

## 3. Komplexitätsanalyse

### Zeitkomplexität
Sei $M = |q|$ die Länge des Anfrage-Präfixes.

1.  **Vorverarbeitung (Einfügen):** Für jedes Wort $s_i \in D$ mit der Länge $L_i$ führen wir $L_i$ Knotentraversierungen und Aktualisierungen durch. Die Gesamtzeitkomplexität für den Aufbau des Tries beträgt $O(\sum_{i=1}^N L_i)$.
2.  **Anfrage:** Der Anfrage-Algorithmus durchläuft einen Pfad der Länge $M$. In jedem Schritt $j \in \{1, \dots, M\}$ führen wir eine Wörterbuch-Suchoperation in den Nachfolgern des aktuellen Knotens durch, was im Durchschnitt $O(1)$ (unter Verwendung einer Hash Map) oder $O(\log |\Sigma|)$ (unter Verwendung eines balancierten BST) benötigt. 
    *   Gesamtzeit der Anfrage: $O(M)$.

Da $M$ unabhängig von der Wörterbuchgröße $N$ ist, ist die Anfragezeit optimal.

### Platzkomplexität
Die Platzkomplexität wird durch die Anzahl der Knoten im Trie bestimmt. 
*   Im schlechtesten Fall, in dem keine zwei Wörter ein Präfix teilen, beträgt die Anzahl der Knoten $|V| = 1 + \sum_{i=1}^N L_i$.
*   Jeder Knoten speichert eine Map der Nachfolger und einen Integer-Wert `count`. 
*   Gesamter Speicherplatz: $O(\sum_{i=1}^N L_i)$, was sich zu $O(M_{total})$ vereinfacht, wobei $M_{total}$ die Summe der Längen aller Strings im Wörterbuch ist. 
*   Der Hilfsspeicher für eine einzelne Anfrage beträgt $O(1)$, da wir nur einen Zeiger auf den aktuellen Knoten verwalten.
