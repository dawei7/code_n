# Formale mathematische Spezifikation: Word Break II (Backtracking)

Dieses Dokument liefert eine rigorose mathematische Spezifikation des **Word Break II**-Algorithmus unter Verwendung von Backtracking. Während das grundlegende Entscheidungsproblem (Word Break I) bestimmt, ob eine gültige Segmentierung existiert, erfordert Word Break II die Generierung der vollständigen Menge aller gültigen Segmentierungen.

---

## 1. Definitionen und Notation

### 1.1 Alphabete und Strings
Sei $\Sigma$ eine endliche, nicht-leere Menge von Zeichen, genannt *Alphabet*.
* Ein *String* $s$ der Länge $N \in \mathbb{N}_0$ ist eine Sequenz von Zeichen $(s_0, s_1, \dots, s_{N-1}) \in \Sigma^N$. Wir schreiben $s \in \Sigma^*$, um auszudrücken, dass $s$ zur Kleene-Hülle von $\Sigma$ gehört.
* Die Länge von $s$ wird als $|s| = N$ bezeichnet.
* Der leere String wird als $\epsilon$ bezeichnet, wobei $|\epsilon| = 0$.
* Für $0 \le i \le j \le N$ ist der *Substring* $s[i:j]$ definiert als:
  $$s[i:j] = \begin{cases} 
  s_i s_{i+1} \dots s_{j-1} & \text{falls } i < j \\
  \epsilon & \text{falls } i = j 
  \end{cases}$$

### 1.2 Das Wörterbuch
Sei $D \subset \Sigma^+$ eine endliche Menge nicht-leerer Strings, die das *Wörterbuch* repräsentiert, wobei $\Sigma^+ = \Sigma^* \setminus \{\epsilon\}$.

### 1.3 Konkatenation und Verknüpfung
* Sei $\cdot : \Sigma^* \times \Sigma^* \to \Sigma^*$ der Operator für die String-Konkatenation, wobei $u \cdot v$ (oder einfach $uv$) die Konkatenation der Strings $u$ und $v$ darstellt.
* Für eine Sequenz von Strings $\alpha = (w_1, w_2, \dots, w_k) \in (\Sigma^*)^k$ definieren wir das Konkatenationsprodukt:
  $$\prod_{m=1}^k w_m = w_1 \cdot w_2 \cdots w_k$$
* Wir definieren den Operator für die Verknüpfung mit Leerzeichen $\text{join} : (\Sigma^*)^k \to \Sigma^*$ als:
  $$\text{join}(w_1, w_2, \dots, w_k) = \begin{cases}
  w_1 & \text{falls } k = 1 \\
  w_1 \cdot \text{" "} \cdot \text{join}(w_2, \dots, w_k) & \text{falls } k > 1
  \end{cases}$$

### 1.4 Der Lösungsraum
Gegeben ein Eingabestring $s \in \Sigma^*$ der Länge $N$ und ein Wörterbuch $D$, ist die Menge aller gültigen Segmentierungen $\mathcal{P}(s, D)$ definiert als:
$$\mathcal{P}(s, D) = \left\{ (w_1, w_2, \dots, w_k) \in D^k \;\middle|\; k \ge 1, \;\; \prod_{m=1}^k w_m = s \right\}$$

Das Zielergebnis des Word Break II-Algorithmus ist die Menge der durch Leerzeichen getrennten Sätze $\mathcal{O}(s, D)$, definiert als:
$$\mathcal{O}(s, D) = \left\{ \text{join}(\mathbf{w}) \;\middle|\; \mathbf{w} \in \mathcal{P}(s, D) \right\}$$

---

## 2. Algebraische Charakterisierung

Der Backtracking-Algorithmus durchsucht systematisch den Suchraum der Präfixe, um $\mathcal{O}(s, D)$ zu konstruieren. Dies kann rekursiv unter Verwendung von mengenwertigen Funktionen und Zustandsraumübergängen modelliert werden.

### 2.1 Rekursive Formulierung
Sei $S(i)$ die Menge aller gültigen Segmentierungen des Suffixes $s[i:N]$ für $0 \le i \le N$. Wir definieren $S(i)$ rekursiv als:

$$S(i) = \begin{cases} 
\{ () \} & \text{falls } i = N \\
\bigcup_{j=i+1}^{N} \left\{ (s[i:j]) \cdot \sigma \;\middle|\; s[i:j] \in D \land \sigma \in S(j) \right\} & \text{falls } i < N 
\end{cases}$$

wobei $()$ die leere Sequenz ist und für ein Wort $w \in D$ und eine Sequenz von Wörtern $\sigma = (u_1, \dots, u_p)$ die Operation $w \cdot \sigma$ das Voranstellen von $w$ an die Sequenz bezeichnet, was $(w, u_1, \dots, u_p)$ ergibt.

Die vollständige Menge gültiger Segmentierungen für den gesamten String ist gegeben durch $S(0) = \mathcal{P}(s, D)$.

### 2.2 Zustandsraumdarstellung
Die Backtracking-Ausführung kann als Tiefensuche (DFS) über einen gerichteten azyklischen Graphen (DAG) der Zustandsübergänge $\mathcal{G} = (\mathcal{V}, \mathcal{E})$ formalisiert werden.

* **Zustandsraum ($\mathcal{V}$):** Ein Zustand ist ein Tupel $(i, \alpha) \in \mathcal{V}$, wobei:
  * $i \in \{0, 1, \dots, N\}$ den aktuellen Grenzindex in $s$ repräsentiert.
  * $\alpha = (w_1, \dots, w_m) \in D^m$ die Sequenz der Wörter ist, die erfolgreich aus dem Präfix $s[0:i]$ geparst wurden, sodass $\prod_{r=1}^m w_r = s[0:i]$.
* **Anfangszustand:** $s_{\text{start}} = (0, ())$.
* **Endzustände:** $\mathcal{T} = \{ (N, \alpha) \in \mathcal{V} \}$. Für jeden Endzustand $(N, \alpha)$ ist die Sequenz $\alpha$ eine gültige Segmentierung von $s$, und $\text{join}(\alpha) \in \mathcal{O}(s, D)$.
* **Übergangsrelation ($\mathcal{E}$):** Eine gerichtete Kante existiert vom Zustand $(i, \alpha)$ zum Zustand $(j, \beta)$ genau dann, wenn:
  $$i < j \le N \quad \land \quad s[i:j] \in D \quad \land \quad \beta = \alpha \cdot (s[i:j])$$

Da $j > i$ für jeden Übergang gilt, enthält der Graph $\mathcal{G}$ keine Zyklen, was sicherstellt, dass die Backtracking-Suche terminiert.

### 2.3 Memoized algebraische Formulierung (DP-Hybrid)
Um redundante Untersuchungen identischer Suffixe zu vermeiden, definieren wir eine memoized Funktion $f: \{0, \dots, N\} \to \mathcal{P}(\Sigma^*)$, die jeden Suffix-Index $i$ auf seine Menge gültiger, durch Leerzeichen getrennter Suffix-Segmentierungen abbildet:

$$f(i) = \begin{cases}
\{ \epsilon \} & \text{falls } i = N \\
\bigcup_{\substack{j=i+1 \\ s[i:j] \in D}}^{N} \left\{ s[i:j] \cdot \Phi(\sigma) \;\middle|\; \sigma \in f(j) \right\} & \text{falls } i < N
\end{cases}$$

wobei der Formatierungsoperator $\Phi: \Sigma^* \to \Sigma^*$ definiert ist als:
$$\Phi(\sigma) = \begin{cases} 
\epsilon & \text{falls } \sigma = \epsilon \\
\text{" "} \cdot \sigma & \text{sonst}
\end{cases}$$

---

## 3. Komplexitätsanalyse

Sei $N = |s|$ die Länge des Eingabestrings und $M = |D|$ die Anzahl der Wörter im Wörterbuch. Sei $L$ die maximale Länge eines Wortes in $D$.

### 3.1 Zeitkomplexität

#### Analyse des Schlechtesten Falls (Ohne Memoization)
Betrachten wir den Schlechtesten Fall mit der Eingabe $s = a^N$ (ein String aus $N$ identischen Zeichen) und einem Wörterbuch, das alle möglichen Präfixe enthält:
$$D = \{a, a^2, a^3, \dots, a^N\}$$

Unter diesen Bedingungen ist jeder Substring $s[i:j]$ ein gültiges Wörterbuchwort.
1. **Anzahl der gültigen Segmentierungen:**
   Die Anzahl der Möglichkeiten, einen String der Länge $N$ zu partitionieren, entspricht dem Setzen einer binären Entscheidung (Schnitt oder kein Schnitt) an jeder der $N-1$ internen Zeichengrenzen. Somit ist die Gesamtzahl der gültigen Segmentierungen:
   $$|\mathcal{P}(s, D)| = 2^{N-1}$$

2. **Arbeitsaufwand durch Backtracking:**
   Der Rekursionsbaum hat $2^{N-1}$ Blattknoten. An jedem Blattknoten konstruiert der Algorithmus einen durch Leerzeichen getrennten String der Länge $O(N)$, indem die gewählten Wörter verbunden werden. Diese String-Konstruktion benötigt $\Theta(N)$ Zeit.
   Die gesamte Zeitkomplexität zur Generierung und Ausgabe aller Lösungen ist:
   $$T(N) = \sum_{k=1}^{N} \binom{N-1}{k-1} \cdot O(N) = O(N \cdot 2^N)$$

#### Analyse des Schlechtesten Falls (Mit Memoization / DP-Hybrid)
Wenn der String nicht segmentiert werden kann (z. B. $s = a^N$ und $D = \{b\}$), kann reines Backtracking ohne Memoization immer noch exponentielle Zeit benötigen, falls es überlappende Teilübereinstimmungen gibt.

Mit Memoization:
1. Es gibt $N+1$ eindeutige Zustände (Indizes $0$ bis $N$).
2. Für jeden Zustand $i$ iterieren wir über $j \in \{i+1, \dots, \min(i+L, N)\}$, führen einen Substring-Slice der Länge maximal $L$ und ein Wörterbuch-Lookup durch. Unter Verwendung eines Hash Set oder Trie benötigt das Lookup $O(L)$ Zeit.
3. Wenn keine gültige Segmentierung existiert, wird der Zustandsraum beschnitten und der Algorithmus terminiert in:
   $$T_{\text{fail}}(N) = O(N \cdot L^2) \subseteq O(N^2) \text{ Zeit}$$
4. Wenn gültige Segmentierungen existieren, müssen wir dennoch die Ausgabe konstruieren. Die Zeitkomplexität wird durch die Größe der Ergebnismenge dominiert, welche im Schlechtesten Fall bei $O(N \cdot 2^N)$ bleibt.

Somit ist die gesamte Zeitkomplexität im Schlechtesten Fall:
$$\Theta(N^2 + N \cdot 2^N)$$

### 3.2 Platzkomplexität

#### Hilfsspeicher (Rekursions-Stack)
Die maximale Tiefe des Rekursionsbaums tritt auf, wenn der String in $N$ einzelne Zeichen der Länge $1$ segmentiert wird. Die maximale Tiefe des Aufruf-Stacks ist:
$$S_{\text{stack}}(N) = O(N)$$

#### Hilfsspeicher (Memoization-Tabelle)
Die Memoization-Tabelle speichert die Menge der gültigen Suffix-Segmentierungen $f(i)$ für jeden Index $i \in \{0, \dots, N\}$.
Im Schlechtesten Fall ($s = a^N$, $D = \{a, \dots, a^N\}$) ist die Größe der Menge $f(i)$ gleich $2^{N-1-i}$, und jeder String in $f(i)$ hat eine durchschnittliche Länge von $O(N-i)$.
Der gesamte Speicherbedarf für die Memoization-Tabelle ist:
$$S_{\text{memo}}(N) = \sum_{i=0}^{N} |f(i)| \cdot O(N-i) = \sum_{i=0}^{N} 2^{N-1-i} \cdot O(N-i) = O(2^N)$$

#### Gesamte Platzkomplexität
Unter Einbeziehung des Speichers, der für die endgültige Ausgabeliste $\mathcal{O}(s, D)$ benötigt wird, welche $2^{N-1}$ Sätze mit einer durchschnittlichen Länge von $O(N)$ enthält, ergibt sich die gesamte Platzkomplexität zu:
$$S_{\text{total}}(N) = O(N + 2^N) \text{ Hilfsspeicher (exklusive Ausgabe)}$$
$$S_{\text{total}}(N) = O(N \cdot 2^N) \text{ Gesamtspeicher (inklusive Ausgabe)}$$