# Formale mathematische Spezifikation: Christofides-TSP (1,5-Approximation)

## 1. Definitionen und Notation

Sei $G = (V, E, w)$ ein vollständiger, ungerichteter, gewichteter Graph, wobei:
*   $V = \{v_1, v_2, \dots, v_n\}$ die Menge der Knoten ist, die die Städte repräsentieren, mit $|V| = n$.
*   $E = \{\{u, v\} \mid u, v \in V, u \neq v\}$ die Menge der Kanten ist, mit $|E| = \frac{n(n-1)}{2}$.
*   $w: E \to \mathbb{R}_{\ge 0}$ eine symmetrische Gewichtsfunktion ist, die jeder Kante einen nicht-negativen reellen Wert zuweist. Der Einfachheit halber schreiben wir $w(u, v)$ anstelle von $w(\{u, v\})$.

### Die metrische Eigenschaft
Die Gewichtsfunktion $w$ erfüllt die **Dreiecksungleichung** (metrische Eigenschaft):
$$\forall u, v, z \in V, \quad w(u, z) \le w(u, v) + w(v, z)$$

### Teilgraphen und Bäume
*   **Spanning Tree (Spannbaum):** Ein Teilgraph $T = (V, E_T)$ von $G$, der zusammenhängend und azyklisch ist.
*   **Minimum Spanning Tree (MST):** Ein Spannbaum $T$, der das gesamte Kantengewicht minimiert:
    $$w(T) = \sum_{e \in E_T} w(e)$$
*   **Induzierter Teilgraph:** Für eine Teilmenge von Knoten $U \subseteq V$ enthält der induzierte Teilgraph $G[U] = (U, E_U, w|_{E_U})$ nur die Knoten in $U$ und die Kanten aus $E$, deren Endpunkte beide zu $U$ gehören.

### Matchings und Schaltkreise
*   **Perfektes Matching:** Gegeben ein Graph $H = (V_H, E_H)$, ist ein Matching $M \subseteq E_H$ perfekt, wenn jeder Knoten $v \in V_H$ inzident zu genau einer Kante in $M$ ist. Dies erfordert, dass $|V_H|$ gerade ist.
*   **Minimum-Weight Perfect Matching (MWPM):** Ein perfektes Matching $M$ auf $H$, das $\sum_{e \in M} w(e)$ minimiert.
*   **Multigraph:** Ein Graph $H' = (V, E_{H'})$, bei dem $E_{H'}$ eine Multimenge von Kanten ist, was mehrere Kanten zwischen demselben Knotenpaar erlaubt. Wir bezeichnen die Vereinigung von Multimengen mit $\uplus$.
*   **Euler-Zyklus:** Ein geschlossener Pfad in einem Multigraphen, der jede Kante in der Multimenge genau einmal durchläuft.
*   **Hamilton-Zyklus (TSP-Tour):** Ein geschlossener Pfad in $G$, der jeden Knoten in $V$ genau einmal besucht und zum Startknoten zurückkehrt. Sei $\mathcal{H}$ die Menge aller Hamilton-Zyklen in $G$.
*   **Optimale TSP-Tour:** Ein Hamilton-Zyklus $H^* \in \mathcal{H}$, sodass:
    $$w(H^*) = \min_{H \in \mathcal{H}} w(H)$$

---

## 2. Algebraische Charakterisierung

Der Christofides-Algorithmus konstruiert einen Hamilton-Zyklus $H$ durch eine Sequenz graphentheoretischer Transformationen.

```
                  [ Input Graph G ]
                          │
                          ▼
               [ Step 1: Compute MST T ]
                          │
                          ▼
         [ Step 2: Identify Odd-Degree Vertices O ]
                          │
                          ▼
       [ Step 3: Compute MWPM M on Induced Subgraph G[O] ]
                          │
                          ▼
         [ Step 4: Form Multigraph H' = T ⊎ M ]
                          │
                          ▼
            [ Step 5: Find Eulerian Circuit C ]
                          │
                          ▼
            [ Step 6: Shortcut C to Tour H ]
```

### Schritt 1: Konstruktion des Minimum Spanning Tree
Wir berechnen einen MST $T = (V, E_T)$ von $G$.
$$\text{Minimiere } \sum_{e \in E_T} w(e) \quad \text{unter der Bedingung, dass } (V, E_T) \text{ ein Spannbaum ist.}$$

#### Lemma 1 (MST-untere Schranke)
Das Gewicht des MST $T$ ist strikt kleiner als das Gewicht der optimalen TSP-Tour $H^*$:
$$w(T) < w(H^*)$$

*Beweis:* Sei $H^*$ der optimale Hamilton-Zyklus. Das Entfernen einer beliebigen Kante aus $H^*$ ergibt einen spannenden Pfad $P$. Da ein spannender Pfad ein Spannbaum ist und $T$ der *minimale* Spannbaum ist, gilt:
$$w(T) \le w(P) < w(H^*)$$
Die strikte Ungleichung gilt, da Kantengewichte nicht-negativ sind und $H^*$ mindestens eine Kante enthält, die nicht in $P$ enthalten ist, mit einem Gewicht $w(e) \ge 0$.

### Schritt 2: Auswahl der Knoten mit ungeradem Grad
Sei $O \subseteq V$ die Menge der Knoten mit ungeradem Grad in $T$:
$$O = \{ v \in V \mid \deg_T(v) \equiv 1 \pmod 2 \}$$

#### Lemma 2 (Korollar zum Handschlag-Lemma)
Die Kardinalität von $O$ ist gerade: $|O| \equiv 0 \pmod 2$.

*Beweis:* Nach dem Handschlag-Lemma ist die Summe der Grade aller Knoten in jedem Graphen gerade:
$$\sum_{v \in V} \deg_T(v) = 2|E_T|$$
Wir unterteilen die Summe in Knoten mit geradem und ungeradem Grad:
$$\sum_{v \in V} \deg_T(v) = \sum_{v \in O} \deg_T(v) + \sum_{v \notin O} \deg_T(v) \equiv 0 \pmod 2$$
Da $\sum_{v \notin O} \deg_T(v)$ eine Summe gerader Zahlen ist, ist sie gerade. Somit muss $\sum_{v \in O} \deg_T(v)$ gerade sein. Da jeder Term in $\sum_{v \in O} \deg_T(v)$ ungerade ist, muss die Anzahl der Terme $|O|$ gerade sein.

### Schritt 3: Minimum-Weight Perfect Matching (MWPM)
Wir konstruieren den induzierten Teilgraphen $G[O]$ und berechnen ein Minimum-Weight Perfect Matching $M$ auf $G[O]$.

#### Lemma 3 (Matching-obere Schranke)
Das Gewicht des Minimum-Weight Perfect Matching $M$ auf $G[O]$ ist durch die Hälfte des Gewichts der optimalen TSP-Tour $H^*$ beschränkt:
$$w(M) \le \frac{1}{2} w(H^*)$$

*Beweis:* Sei $H^*$ der optimale Hamilton-Zyklus auf $G$. Wir konstruieren einen Zyklus $H^*_O$ auf der Knotenmenge $O$, indem wir $H^*$ durchlaufen und alle Knoten überspringen, die nicht in $O$ liegen. Aufgrund der Dreiecksungleichung erhöht das Überspringen (Shortcutting) das Gesamtgewicht nicht:
$$w(H^*_O) \le w(H^*)$$
Da $|O|$ gerade ist, besteht der Zyklus $H^*_O$ aus einer geraden Anzahl von Kanten. Wir können die Kanten von $H^*_O$ in zwei disjunkte perfekte Matchings $M_1$ und $M_2$ unterteilen, sodass:
$$E(H^*_O) = M_1 \cup M_2 \quad \text{und} \quad M_1 \cap M_2 = \emptyset$$
Somit ist die Summe ihrer Gewichte:
$$w(M_1) + w(M_2) = w(H^*_O) \le w(H^*)$$
Da $M$ das *minimale* perfekte Matching auf $G[O]$ ist, muss sein Gewicht kleiner oder gleich dem Gewicht von sowohl $M_1$ als auch $M_2$ sein:
$$w(M) \le \min(w(M_1), w(M_2))$$
Daher gilt:
$$2 w(M) \le w(M_1) + w(M_2) \le w(H^*) \implies w(M) \le \frac{1}{2} w(H^*)$$

### Schritt 4: Multigraph-Vereinigung
Wir definieren den Multigraphen $H' = (V, E_{H'})$ mit $E_{H'} = E_T \uplus M$.

#### Lemma 4 (Euler-Eigenschaft)
Jeder Knoten in $H'$ hat einen geraden Grad und $H'$ ist zusammenhängend.

*Beweis:* Für jeden Knoten $v \in V$ ist sein Grad in $H'$:
$$\deg_{H'}(v) = \deg_T(v) + \deg_M(v)$$
*   Wenn $v \in O$, dann ist $\deg_T(v)$ ungerade und $\deg_M(v) = 1$. Somit ist $\deg_{H'}(v)$ gerade.
*   Wenn $v \notin O$, dann ist $\deg_T(v)$ gerade und $\deg_M(v) = 0$. Somit ist $\deg_{H'}(v)$ gerade.

Da $T$ ein Spannbaum ist, verbindet er alle Knoten in $V$. Das Hinzufügen der Matching-Kanten $M$ erhält die Zusammenhangseigenschaft. Da $H'$ zusammenhängend ist und alle Knoten einen geraden Grad haben, enthält $H'$ einen Euler-Zyklus.

### Schritt 5: Euler-Zyklus und Shortcutting
Sei $C = (u_1, u_2, \dots, u_m, u_1)$ ein Euler-Zyklus in $H'$, wobei $m = |E_T| + |M| = n - 1 + \frac{|O|}{2}$.
Wir konstruieren einen Hamilton-Zyklus $H = (v_1, v_2, \dots, v_n, v_1)$, indem wir $C$ vom Anfang bis zum Ende durchlaufen und jeden Knoten überspringen, der bereits besucht wurde.

Sei $\sigma: C \to H$ dieser Shortcutting-Operator. Aufgrund der Dreiecksungleichung gilt für jede Sequenz übersprungener Knoten:
$$w(v_i, v_{i+1}) \le \sum_{j=a}^{b} w(u_j, u_{j+1})$$
wobei $u_a = v_i$ und $u_{b+1} = v_{i+1}$. Die Summation über den gesamten Zyklus ergibt:
$$w(H) \le w(C)$$

### Schritt 6: Beweis des Approximationsverhältnisses
Durch Kombination der Schranken aus den vorherigen Schritten erhalten wir:
$$w(H) \le w(C) = w(T) + w(M)$$
Unter Anwendung von Lemma 1 ($w(T) < w(H^*)$) und Lemma 3 ($w(M) \le \frac{1}{2} w(H^*)$):
$$w(H) < w(H^*) + \frac{1}{2} w(H^*) = 1,5 \cdot w(H^*)$$
Dies vervollständigt den Beweis, dass der Algorithmus eine 1,5-Approximation garantiert.

---

## 3. Komplexitätsanalyse

### Zeitkomplexität

Die gesamte Zeitkomplexität des Christofides-Algorithmus wird durch den Schritt des Minimum-Weight Perfect Matching dominiert.

#### 1. Minimum Spanning Tree (Prim-Algorithmus)
Unter Verwendung einer Adjazenzmatrix-Repräsentation für einen vollständigen Graphen $G$:
*   Das Finden der Kante mit dem minimalen Gewicht in jedem Schritt benötigt $O(V)$ Zeit.
*   Die Wiederholung für $V - 1$ Knoten ergibt:
    $$T_{\text{MST}}(V) = \sum_{i=1}^{V-1} O(V) = O(V^2)$$

#### 2. Identifikation der Knoten mit ungeradem Grad
Das Scannen der Grade der Knoten in $T$ zur Konstruktion der Menge $O$:
$$T_{\text{odd}}(V) = O(V)$$

#### 3. Minimum-Weight Perfect Matching (MWPM)
*   **Exakte Formulierung (Edmonds' Blossom-Algorithmus):**
    Um das 1,5-Approximationsverhältnis zu garantieren, müssen wir das exakte Minimum-Weight Perfect Matching auf dem vollständigen Graphen $G[O]$ finden. Der für gewichtete Graphen angepasste Blossom-Algorithmus von Edmonds läuft in:
    $$T_{\text{MWPM}}(|O|) = O(|O|^3) \le O(V^3)$$
*   **Heuristische Approximation (Greedy Matching):**
    Die bereitgestellte Python-Implementierung verwendet eine Greedy-Matching-Heuristik (wiederholtes Auswählen der günstigsten Kante zwischen nicht gematchten ungeraden Knoten). Diese Heuristik läuft in $O(|O|^2 \log |O|)$ oder $O(V^2)$, garantiert jedoch **nicht** in allen metrischen Räumen das 1,5-Approximationsverhältnis. Für eine mathematisch rigorose Garantie ist der $O(V^3)$ Blossom-Algorithmus erforderlich.

#### 4. Euler-Zyklus (Hierholzer-Algorithmus)
Der Hierholzer-Algorithmus findet einen Euler-Zyklus, indem er jede Kante in $H'$ genau einmal durchläuft.
*   Anzahl der Knoten: $|V| = n$.
*   Anzahl der Kanten in $H'$: $|E_{H'}| = |E_T| + |M| = (n - 1) + \frac{|O|}{2} < 1,5n$.
*   Unter Verwendung einer Adjazenzliste mit effizienter Kantenentfernung beträgt die Zeitkomplexität:
    $$T_{\text{Euler}}(V) = O(|V| + |E_{H'}|) = O(V)$$

#### 5. Shortcutting
Das Durchlaufen des Euler-Zyklus der Länge $O(V)$ und das Überspringen von Duplikaten mittels einer Lookup-Tabelle (Hash-Set oder boolesches Array) der Größe $V$:
$$T_{\text{shortcut}}(V) = O(V)$$

#### Gesamte Zeitkomplexität
Summierung der Komponenten:
$$T_{\text{total}}(V) = T_{\text{MST}}(V) + T_{\text{odd}}(V) + T_{\text{MWPM}}(V) + T_{\text{Euler}}(V) + T_{\text{shortcut}}(V)$$
$$T_{\text{total}}(V) = O(V^2) + O(V) + O(V^3) + O(V) + O(V) = O(V^3)$$

---

### Platzkomplexität

Die Platzkomplexität wird hinsichtlich des zusätzlichen Speicherbedarfs (Auxiliary Space) und des Gesamtspeichers analysiert.

#### 1. Input-Repräsentation
Die Input-Kostenmatrix erfordert das Speichern von $n \times n$ Distanzen:
$$S_{\text{input}}(V) = \Theta(V^2)$$

#### 2. Zusätzlicher Speicherbedarf
*   **MST-Repräsentation:** Das Eltern-Array und das Array zur Gradverfolgung benötigen $O(V)$ Speicher.
*   **Menge $O$ der Knoten mit ungeradem Grad:** Das Speichern der Indizes der Knoten mit ungeradem Grad erfordert $O(V)$ Speicher.
*   **Multigraph $H'$:** Die Adjazenzlisten-Repräsentation von $H'$ enthält $V$ Knoten und maximal $1,5V$ Kanten, was $O(V)$ Speicher erfordert.
*   **Stack für den Euler-Zyklus:** Der Rekursions-Stack oder ein expliziter Stack für den Hierholzer-Algorithmus speichert maximal $|E_{H'}| + 1$ Knoten:
    $$S_{\text{stack}}(V) = O(V)$$
*   **Shortcutting-Status:** Ein boolesches Array oder Hash-Set der Größe $V$ zur Verfolgung besuchter Knoten:
    $$S_{\text{visited}}(V) = O(V)$$

#### Gesamte Platzkomplexität
*   **Zusätzlicher Speicherbedarf:** $O(V)$
*   **Gesamtspeicher (inklusive Input-Matrix):** $O(V^2)$