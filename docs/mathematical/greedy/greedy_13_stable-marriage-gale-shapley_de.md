# Formale mathematische Spezifikation: Stable Marriage Problem (Gale-Shapley)

## 1. Definitionen und Notation

Sei $M = \{m_1, m_2, \dots, m_n\}$ die Menge der $n$ Männer und $W = \{w_1, w_2, \dots, w_n\}$ die Menge der $n$ Frauen.

*   **Präferenzrelationen:** Für jeden $m \in M$ existiert eine strikte totale Ordnung $\succ_m$ über $W$. Analog existiert für jede $w \in W$ eine strikte totale Ordnung $\succ_w$ über $M$. Wir schreiben $w_i \succ_m w_j$, wenn Mann $m$ Frau $w_i$ gegenüber $w_j$ bevorzugt.
*   **Matching:** Ein Matching $\mu$ ist eine Bijektion $\mu: M \cup W \to M \cup W$, sodass für alle $m \in M$ gilt $\mu(m) \in W$, und für alle $w \in W$ gilt $\mu(w) \in M$, wobei $\mu(\mu(x)) = x$ erfüllt ist.
*   **Stabilität:** Ein Matching $\mu$ ist **stabil**, wenn kein Paar $(m, w)$ existiert, für das gilt:
    1. $w \succ_m \mu(m)$ (Mann $m$ bevorzugt Frau $w$ gegenüber seiner aktuellen Partnerin).
    2. $m \succ_w \mu(w)$ (Frau $w$ bevorzugt Mann $m$ gegenüber ihrem aktuellen Partner).
    Ein solches Paar $(m, w)$ wird als **Blockierendes Paar** bezeichnet.
*   **Zustandsraum:** Der Zustand des Algorithmus in Iteration $k$ ist definiert durch das Tupel $\mathcal{S}_k = (\text{free\_men}_k, \text{engaged}_k, \text{next\_proposal}_k)$, wobei $\text{engaged}_k \subset M \times W$ die Menge der aktuellen vorläufigen Verlobungen repräsentiert.

## 2. Algebraische Charakterisierung

Der Gale-Shapley-Algorithmus konstruiert ein Matching $\mu$ durch eine Sequenz von Vorschlägen. Sei $P_m \subseteq W$ die Menge der Frauen, denen Mann $m$ bereits einen Vorschlag gemacht hat.

**Invariante:** Zu jedem Zeitpunkt des Algorithmus gilt: Wenn $m$ nicht verlobt ist, dann ist für alle $w \in P_m$ die Frau $w$ aktuell mit einem $m' \in M$ verlobt, für den $m' \succeq_w m$ gilt.

**Übergangsfunktion:**
Sei $m$ ein freier Mann. Sei $w = \text{argmax}_{\succ_m} \{W \setminus P_m\}$. Der Übergang $\mathcal{S}_k \to \mathcal{S}_{k+1}$ ist definiert als:
1. Wenn $w$ nicht zugeordnet ist: $\mu(m) = w$.
2. Wenn $w$ mit $m'$ verlobt ist:
   - Wenn $m \succ_w m'$, dann $\mu(m) = w$ und $m'$ wird frei.
   - Wenn $m' \succ_w m$, dann bleibt $m$ frei und $P_m = P_m \cup \{w\}$.

**Konvergenz:**
Der Algorithmus terminiert, wenn die Menge der freien Männer leer ist. Die Anzahl der Vorschläge ist durch $n^2$ beschränkt, da jeder Mann jeder Frau höchstens einmal einen Vorschlag macht. Da sich die Menge der verlobten Paare für die Empfänger (Frauen) hinsichtlich ihrer Präferenzrangfolgen monoton verbessert und die Antragsteller (Männer) ihre Präferenzlisten abarbeiten, muss der Prozess in einem stabilen Matching $\mu^*$ terminieren.

## 3. Komplexitätsanalyse

### Zeitkomplexität
Die Zeitkomplexität wird durch die Anzahl der Vorschläge bestimmt.
*   **Obere Schranke:** Jeder Mann $m \in M$ hat eine Präferenzliste der Länge $n$. Im Schlechtesten Fall macht jeder Mann jeder Frau genau einmal einen Vorschlag. Somit ist die Gesamtzahl der Vorschläge durch $N^2$ beschränkt.
*   **Kosten pro Vorschlag:** Durch Vorberechnen der inversen Präferenzmatrix $R_w \in \mathbb{Z}^{n \times n}$, wobei $R_w[m]$ den Rang von Mann $m$ für Frau $w$ zurückgibt, reduziert sich der Vergleich $m \succ_w m'$ auf einen Zugriff in konstanter Zeit: $R_w[m] < R_w[m']$.
*   **Gesamtzeit:** Der Algorithmus führt $O(N^2)$ Vorschläge aus, wobei jeder $O(1)$ Zeit für den Präferenzvergleich und die Pointer-Aktualisierungen benötigt. Somit beträgt die gesamte Zeitkomplexität $T(N) = O(N^2)$.

### Platzkomplexität
*   **Präferenzmatrizen:** Das Speichern von `men_prefs` und `women_prefs` erfordert $O(N^2)$ Platz.
*   **Inverse Präferenzmatrix:** Die `woman_rank`-Matrix erfordert $O(N^2)$ Platz, um einen Zugriff in $O(1)$ zu ermöglichen.
*   **Hilfsstrukturen:** Die Arrays `next_w`, `woman_engaged_to` und `man_engaged_to` erfordern jeweils $O(N)$ Platz.
*   **Gesamtplatz:** Der dominierende Term ist die Speicherung der Präferenz- und Rangmatrizen, was zu einer gesamten Platzkomplexität von $S(N) = O(N^2)$ führt.