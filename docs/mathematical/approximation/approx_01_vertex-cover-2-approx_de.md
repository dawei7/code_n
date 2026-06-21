# Formale mathematische Spezifikation: Vertex-Cover (2-Approximation)

## 1. Definitionen und Notation

Sei $G = (V, E)$ ein ungerichteter, einfacher Graph, wobei:
*   $V = \{v_1, v_2, \dots, v_n\}$ die endliche Menge der Knoten ist, mit $|V| = n$.
*   $E \subseteq \{\{u, v\} \mid u, v \in V, u \neq v\}$ die Menge der ungerichteten Kanten ist, mit $|E| = m$.

### Definition 1.1: Vertex-Cover
Eine Teilmenge von Knoten $C \subseteq V$ ist ein **Vertex-Cover** von $G$ genau dann, wenn jede Kante in $E$ zu mindestens einem Knoten in $C$ inzident ist:
$$\forall \{u, v\} \in E, \quad \{u, v\} \cap C \neq \emptyset$$

### Definition 1.2: Minimales Vertex-Cover
Ein Vertex-Cover $C^* \subseteq V$ ist ein **minimales Vertex-Cover** von $G$, wenn es die Kardinalität des Covers minimiert:
$$C^* \in \arg\min \{ |C| \mid C \subseteq V \text{ ist ein Vertex-Cover von } G \}$$
Wir bezeichnen die Größe des optimalen Vertex-Covers als $\tau(G) = |C^*|$. Das Finden von $\tau(G)$ ist NP-schwer.

### Definition 1.3: Matching
Eine Teilmenge von Kanten $M \subseteq E$ ist ein **Matching** in $G$, wenn keine zwei Kanten in $M$ einen gemeinsamen Knoten teilen:
$$\forall e_1, e_2 \in M \text{ mit } e_1 \neq e_2, \quad e_1 \cap e_2 = \emptyset$$
Ein Matching $M$ ist **maximal**, wenn es nicht durch Hinzufügen einer weiteren Kante aus $E$ erweitert werden kann, ohne die Eigenschaft der paarweisen Disjunktheit zu verletzen.

### Definition 1.4: Zustandsraum des Approximationsalgorithmus
Die Ausführung des 2-Approximationsalgorithmus kann als zeitdiskretes Übergangssystem modelliert werden. Der Zustandsraum $\mathcal{S}$ ist definiert als:
$$\mathcal{S} = \{ (C, E') \mid C \subseteq V, \, E' \subseteq E \}$$
wobei:
*   $C$ die Menge der Knoten repräsentiert, die aktuell für das Vertex-Cover ausgewählt wurden.
*   $E'$ die Menge der aktiven, noch nicht abgedeckten Kanten im Graphen repräsentiert.

---

## 2. Algebraische Charakterisierung und Korrektheit

### 2.1. Algorithmisches Übergangssystem
Sei $(C_k, E_k) \in \mathcal{S}$ der Zustand des Algorithmus zum Schritt $k \ge 0$.

*   **Anfangszustand ($k = 0$):**
    $$C_0 = \emptyset, \quad E_0 = E$$

*   **Zustandsübergang ($k \to k+1$):**
    Falls $E_k \neq \emptyset$, wähle eine beliebige Kante $e_k = \{u_k, v_k\} \in E_k$. Der nächste Zustand $(C_{k+1}, E_{k+1})$ ist durch die Übergangsrelationen definiert:
    $$C_{k+1} = C_k \cup \{u_k, v_k\}$$
    $$E_{k+1} = \{ \{x, y\} \in E_k \mid \{x, y\} \cap \{u_k, v_k\} = \emptyset \}$$

*   **Abbruchbedingung:**
    Der Algorithmus terminiert zum Schritt $T$, wenn $E_T = \emptyset$. Das Ergebnis ist die Menge $C = C_T$.

> **Anmerkung zur Code-Diskrepanz:** Der bereitgestellte Python-Code implementiert eine Greedy-Heuristik basierend auf dem maximalen Knotengrad, was eine $O(\log |V|)$-Approximation liefert. Die mathematische Spezifikation unten formalisiert den *Edge-Picking 2-Approximation*-Algorithmus, der im Text beschrieben ist und eine strikte 2-Approximation garantiert.

---

### 2.2. Schleifeninvarianten
Um die Korrektheit und das Approximationsverhältnis des Algorithmus zu beweisen, definieren wir die Menge der gewählten Kanten zum Schritt $k$ als:
$$M_k = \{ e_i \in E \mid 0 \le i < k \}$$

#### Lemma 2.1: Matching-Invariante
*Für jeden Schritt $k \ge 0$ ist die Menge $M_k$ ein Matching in $G$.*

**Beweis (durch vollständige Induktion):**
*   **Induktionsanfang ($k=0$):** $M_0 = \emptyset$, was trivialerweise ein Matching ist.
*   **Induktionsschritt:** Angenommen, $M_k$ ist ein Matching. Zum Schritt $k$ wählen wir $e_k = \{u_k, v_k\} \in E_k$. Aufgrund der Definition der Übergangsrelation enthält $E_k$ nur Kanten, die keine Knoten mit den zuvor in $M_k$ gewählten Kanten teilen (da alle inzidenten Kanten in vorherigen Schritten entfernt wurden). Somit gilt $\forall e \in M_k, e \cap e_k = \emptyset$. Folglich ist $M_{k+1} = M_k \cup \{e_k\}$ ein Matching. $\blacksquare$

#### Lemma 2.2: Überdeckungsinvariante
*Für jeden Schritt $k \ge 0$ ist die Menge der Knoten $C_k$ exakt die Menge der Endpunkte der Kanten in $M_k$:*
$$C_k = \bigcup_{e \in M_k} e$$

**Beweis:**
Dies folgt direkt aus den Übergangsregeln: $C_0 = \emptyset$, und in jedem Schritt fügen wir beide Endpunkte von $e_k$ zu $C_k$ hinzu. Da $M_k$ ein Matching ist, sind die Endpunkte aller $e \in M_k$ paarweise disjunkt, was $|C_k| = 2|M_k|$ impliziert. $\blacksquare$

---

### 2.3. Beweis der Korrektheit und des Approximationsverhältnisses

#### Theorem 2.3: Gültigkeit des Ergebnis-Covers
*Nach der Terminierung zum Schritt $T$ ist die Ergebnismenge $C_T$ ein gültiges Vertex-Cover von $G$.*

**Beweis:**
Nehmen wir durch Widerspruch an, $C_T$ sei kein Vertex-Cover. Dann existiert eine Kante $e = \{u, v\} \in E$ derart, dass $\{u, v\} \cap C_T = \emptyset$. 
Da $e \in E = E_0$ und $e \notin E_T$ (da $E_T = \emptyset$), muss es einen Schritt $k < T$ geben, in dem $e$ aus $E_k$ entfernt wurde. 
Gemäß der Übergangsregel wird eine Kante $e$ aus $E_k$ genau dann entfernt, wenn $e \cap \{u_k, v_k\} \neq \emptyset$. 
Da $\{u_k, v_k\} \subseteq C_{k+1} \subseteq C_T$, folgt daraus $e \cap C_T \neq \emptyset$, was unserer Annahme widerspricht. Somit ist $C_T$ ein gültiges Vertex-Cover. $\blacksquare$

#### Theorem 2.4: 2-Approximationsverhältnis
*Die Größe des Vertex-Covers $C_T$, das vom Algorithmus zurückgegeben wird, ist höchstens doppelt so groß wie die Größe des minimalen Vertex-Covers $C^*$:*
$$|C_T| \le 2 \cdot |C^*|$$

**Beweis:**
1.  Sei $M_T$ das Matching, das vom Algorithmus bei Terminierung konstruiert wurde. Nach Lemma 2.2 gilt $|C_T| = 2|M_T|$.
2.  Sei $C^*$ ein beliebiges optimales Vertex-Cover von $G$. Nach Definition 1.1 muss $C^*$ jede Kante in $G$ abdecken.
3.  Da $M_T \subseteq E$ ein Matching ist, sind die enthaltenen Kanten paarweise knotendisjunkt. Um die Kanten in $M_T$ abzudecken, muss daher jedes gültige Vertex-Cover (einschließlich $C^*$) für jede Kante in $M_T$ mindestens einen eindeutigen Knoten auswählen:
    $$\forall e \in M_T, \quad |e \cap C^*| \ge 1$$
4.  Da die Kanten in $M_T$ keine Knoten teilen, können wir diese Ungleichungen summieren:
    $$|C^*| \ge \sum_{e \in M_T} |e \cap C^*| \ge |M_T|$$
5.  Durch Kombination von $|C_T| = 2|M_T|$ und $|M_T| \le |C^*|$ erhalten wir:
    $$|C_T| \le 2 \cdot |C^*|$$
Dies vervollständigt den Beweis, dass der Algorithmus eine 2-Approximation garantiert. $\blacksquare$

---

## 3. Komplexitätsanalyse

### 3.1. Zeitkomplexität

Um eine optimale Zeitkomplexität von $O(|V| + |E|)$ zu erreichen, wird der Algorithmus unter Verwendung einer Adjazenzliste für $G$ zusammen mit einem zusätzlichen booleschen Array zur Verfolgung der abgedeckten Knoten implementiert.

#### Formale Herleitung:
Sei $G = (V, E)$ als Adjazenzliste $Adj$ repräsentiert. Wir führen:
1.  Ein boolesches Array $\text{visited}$ der Größe $|V|$, initialisiert mit $\text{False}$.
2.  Eine Ergebnismenge $C$, initialisiert mit $\emptyset$.

Der Algorithmus iteriert über die Kantenmenge $E$. Für jede Kante $e = \{u, v\} \in E$:
$$\text{Aufwand pro Kante } e = \{u, v\}: \begin{cases} 
O(1) & \text{falls } \text{visited}[u] = \text{True} \text{ oder } \text{visited}[v] = \text{True} \\
O(1) \text{ Updates} & \text{falls } \text{visited}[u] = \text{False} \text{ und } \text{visited}[v] = \text{False}
\end{cases}$$

Im zweiten Fall führen wir die folgenden Operationen mit konstantem Zeitaufwand aus:
*   Hinzufügen von $u$ und $v$ zu $C$.
*   Setzen von $\text{visited}[u] = \text{True}$ und $\text{visited}[v] = \text{True}$.

Die gesamte Zeitkomplexität $T(|V|, |E|)$ lässt sich ausdrücken als:
$$T(|V|, |E|) = \Theta(|V|) + \sum_{e \in E} O(1) = \Theta(|V| + |E|)$$

Somit ist die Zeitkomplexität im Schlechtesten Fall, Durchschnittlichen Fall und Bestfall:
$$\mathcal{O}(|V| + |E|)$$

---

### 3.2. Platzkomplexität

#### Hilfsspeicher:
Der Hilfsspeicher besteht aus den Datenstrukturen, die zur Ausführung der Approximationslogik erforderlich sind, exklusive des Eingabegraphen:
1.  Die Vertex-Cover-Menge $C$: speichert höchstens $|V|$ Knoten, was $O(|V|)$ Speicherplatz erfordert.
2.  Das Tracking-Array $\text{visited}$: erfordert $O(|V|)$ Speicherplatz.

$$\text{Hilfsspeicher} = \Theta(|V|)$$

#### Gesamtspeicher:
Die gesamte Platzkomplexität beinhaltet die Repräsentation des Eingabegraphen. Bei Verwendung einer Adjazenzliste erfordert der Graph $\Theta(|V| + |E|)$ Speicherplatz.

$$\text{Gesamtspeicher} = \Theta(|V| + |E|)$$