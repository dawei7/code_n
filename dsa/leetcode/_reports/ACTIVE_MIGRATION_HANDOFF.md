# Active LeetCode Migration Handoff

Updated: 2026-07-16

This work is active. It is neither complete nor globally blocked. The full
goal remains the canonical migration of every problem through frontend ID
3985. This handoff records the current live boundary for a new Codex session;
the worktree and freshly generated reports remain authoritative if anything
below has drifted.

## Full goal

Migrate every canonical LeetCode package in `C:\dawei7\code_n`, in ascending
numeric frontend-ID order through problem 3985, to the reviewed Two Sum
standard. A completed package needs:

1. an original, source-faithful `doc.md`;
2. visible samples, trials, and meaningful hidden correctness cases;
3. complexity verification: normally exactly three ordered,
   complexity-sensitive benchmark tiers, or a strictly validated non-scaling
   `complexity_certificate.json` when the legal contract cannot support an
   honest scaling verdict;
4. an optimal app-local solution for every runnable supported environment;
5. a separate exact LeetCode-native submission artifact;
6. remote Accepted verification where account access and execution semantics
   permit it;
7. regression checks; and
8. durable progress or blocker documentation.

Preserve all existing changes. If one problem is genuinely blocked, document
the problem-specific reason and continue to the next numeric frontend ID.

## Repository and branch state

- Repository: `C:\dawei7\code_n`
- Current local branch: `main`
- Current committed migration checkpoint:
  `97717019379cb191b141940935075f9667ece6c4`, which completes and delivers
  frontend IDs 1481 through 1489.
- The worktree contains the completed local package changes for frontend IDs
  1490 through 1499, the bounded-domain certificate regression for 1491, and
  refreshed generated reports. Preserve them and any later local changes unless
  inspection proves they are unrelated.
- The four-digit directory migration remains based on
  `1fc55b6e7ff0e808e207376bc663ea60cb2cb798`.
- `main` and `origin/main` are at checkpoint `97717019` before the uncommitted
  frontend ID 1490 package changes.
- The current commit-and-push authorization is consumed by this checkpoint.
  Do not commit, push, merge, or release without a new explicit user request.

Canonical problem directories now use four-digit frontend-ID prefixes, for
example `dsa/leetcode/0001_two-sum` and
`dsa/leetcode/0824_goat-latin`. All 3985 canonical package directories were
renamed and the padding migration was hash-verified. Lexicographic directory
order now equals numeric frontend-ID order. Personal user-data paths are a
separate compatibility surface and intentionally remain unpadded, for example
`dsa/leetcode/1_two-sum/user_solutions/...` under the user-data root.

## Authorities to read completely before acting

Read these files in full, in this order:

1. `AGENTS.md`
2. `BENCHMARKING.md`
3. `LEETCODE_SUBMISSIONS.md`
4. `dsa/leetcode/_template.md`
5. `dsa/leetcode/_reports/ORIGINAL_18_BLOCKER_PLAYBOOK.md`
6. `dsa/leetcode/_reports/ACTIVE_MIGRATION_HANDOFF.md`
7. `dsa/leetcode/_reports/two_sum_migration_progress.md`

Then refresh the migration audit and inspect the next package's
`metadata.json` and every existing artifact. Do not infer the current frontier
from chat history or this file alone.

## Problem-statement writing convention

- Use `Goal`, `Function Contract`, `Examples`, and `Required Complexity`, in
  that order.
- The Goal must be original prose, not a copied LeetCode statement. It should
  nevertheless stay close to the public problem's intent, logical order,
  technical vocabulary, semantic coverage, and proportionate length. A long
  or nuanced source problem should not collapse into a generic short summary.
- Rephrase to improve clarity, sequencing, or completeness, not merely to make
  the words different. Preserve already-clear mathematical and technical
  terms. In particular, never replace `ascending` with `non-decreasing`, or
  interchange `strictly increasing`, `subarray`, `subsequence`, `at most`,
  `exactly`, or similar terms merely as stylistic variation.
- State every operation rule, guarantee, boundary condition, output condition,
  and distinction that changes how the problem is solved.
- Use only public problem facts needed to author an independent summary. Do
  not copy full LeetCode statements, examples, editorials, or proprietary
  solution prose. The metadata table owns the only official external problem
  link and labels it `LeetCode`.
- Do not add `Solution` or `Reference Implementations` sections to `doc.md`.
  Implementations belong under `solutions/`.

## Mathematical notation versus executable code

This distinction is a durable requirement for all reviewed documents, not a
problem-820-only cleanup.

- Write abstract mathematics in LaTeX: `$n$`, `$x = yz$`,
  `$1 \le n \le 1000$`, `$10^9 + 7$`, `$O(n^2)$`, and sums or recurrences.
- Prefer a display definition when a long expression would make a rendered
  line unreadable. Define a short symbol once and use it in the bounds. For
  example:

  $$
  S = \sum_{w \in \texttt{words}} \lvert w \rvert.
  $$

  Then write the relevant bound as `$O(S)$`, not the full summation twice.
- Define every problem-specific complexity symbol before using it. Standard
  input-size symbols such as `$n$` must still be tied to the concrete input,
  for example "Let `$n$` be the length of `arr`."
- Keep executable calculations and language syntax in code spans rather than
  converting them to LaTeX. This includes assignments, indexing, slices,
  function calls, pointer changes, and programming-language operators. Correct
  examples are `nums[a] = target - nums[b]`, `ways[root] += ...`, `arr[i:j]`,
  `left += 1`, and `solve(arr)`.
- Strings, serialized values, identifiers used as literal program objects, and
  input/output fragments also remain code. Use `\texttt{...}` inside LaTeX
  only when the identifier genuinely participates in an abstract mathematical
  definition, as `words` does in the displayed definition of `$S$` above.
- `Required Complexity` is notation-only and has exactly this form, with no
  explanatory prose in that section:

  ```markdown
  - **Time:** $O(...)$
  - **Space:** $O(...)$
  ```

The corpus-wide mathematical-notation review through problem 822 is complete.
Problem 820 now defines the total input-character count with the displayed
symbol `$S$` before using `$O(S)$`. The documentation tests, dataset checker,
full Python regression suite, Ruff, web build, Electron build, and diff checks
for that pass and the directory-padding migration were completed successfully
before problem 823 began.

## Approach-section convention

- Only `Approach` is collapsible.
- Inside Approach, use exactly these three level-four headings, in this order:
  `General`, `Complexity detail`, and `Alternatives and edge cases`.
- Do not add any other Markdown headings inside Approach.
- Use optional, problem-specific bold signposts inside `General` when they
  improve navigation, such as `**Why the unique pair must be found**`. They are
  bold paragraphs, not headings and not a repeated mini-template.
- Documentation quality and completeness take priority over brevity or token
  conservation. Never shorten `doc.md` merely to save model tokens or finish a
  package faster; make it as extensive as the problem's semantics, constraints,
  algorithm, and correctness reasoning require.
- Use as many problem-specific bold signposts inside `General` as the distinct
  reasoning stages need. Substantial explanations should normally expose their
  derivation, state or transition logic, endpoint conditions, and correctness
  reasoning as navigable ideas instead of hiding them in an undifferentiated
  block. Do not force extra signposts when a genuinely simple observation has
  no additional idea to separate.
- Derive the algorithm from the problem's constraints and integrate the reason
  it is correct with the idea being explained. Do not insert generic repeated
  `Correctness`, invariant, trace, proof, or fixed-count slots when they do not
  improve that particular explanation.
- Match depth to difficulty. Simple observations may be concise; complex
  algorithms need the state definitions, transitions, examples, and reasoning
  necessary to teach them accurately.
- Write `Alternatives and edge cases` entirely as a bullet list. Bold-name each
  genuine alternative and state its tradeoff or failure mode, for example
  `- **Visited matrix plus direction changes:** ...`. Give each material edge
  case or semantic trap a separate bullet. Do not use free-text paragraphs or
  force a fixed number of bullets.

## Identity and submission rules

- Preserve the numeric frontend ID, title slug, official URL, language,
  category, and source-native execution semantics.
- LeetCode's backend `question_id` is not the frontend ID and may legitimately
  differ. For example, frontend problem 497 has internal question ID 914.
  Record both values from the authoritative metadata; never overwrite the
  internal ID merely because the frontend ID looks more familiar.
- Keep the app-local `solve(...)` implementation and the native artifact side
  by side. The native file must retain the platform declaration and exact
  method signature, such as `class Solution`.
- A candidate remains unverified until the exact native source is remotely
  Accepted. Local correctness alone never promotes `submission.json`.
- The user has already authorized in-scope remote verification submissions for
  this continuing migration through the existing Electron credential bridge.
  Do not ask for a separate confirmation for every problem when the execution
  environment permits the direct command. Do not add approval-escalation
  flags. If the host UI itself enforces a confirmation, that policy cannot be
  bypassed from repository code. The user cannot answer further approval
  prompts: if such an interaction or the current `safeStorage.decryptString`
  failure prevents verification, record an exact package blocker and continue
  to the next frontend ID.
- If work is paused only by the transient message "Selected model is at
  capacity", retry after about five minutes and continue from the live audit.

## Per-package completion loop

For each package in ascending numeric frontend-ID order:

1. Confirm public identity, contract facts, access class, supported language,
   and the exact native declaration or query interface from the official
   LeetCode page or live GraphQL metadata when needed.
2. Create the exact platform-native source and candidate manifest, and perform
   minimal contract-focused sanity checks.
3. Submit that exact native artifact early and promote the manifest only on
   remote Accepted evidence. If remote verification is unavailable, record the
   exact blocker before continuing local authoring.
4. Use the Accepted source as the semantic and algorithmic anchor for the
   separate app-local implementation and independent document.
5. Author visible samples, trials, and meaningful hidden correctness cases. If
   multiple outputs are valid, use or add a semantic validator; never reject a
   valid output solely because its serialization differs.
6. Normally author exactly three increasing benchmark tiers with one
   consistent `size` meaning, unique positive sizes, and at least a fourfold
   total span. If and only if the source contract meets a reviewed non-scaling
   condition, author `complexity_certificate.json` and every required
   replacement check instead.
7. For a benchmark, the reference and a separate implementation in the
   required complexity class must pass. A correct principal slower-class
   implementation must return every expected output and fail only the
   complexity verdict whenever the legal domain permits such a distinction.
   A safety-cap failure is not an acceptable substitute for scaling evidence.
   For a certificate, strict schema validation and method-specific bounded,
   proof, semantic, scheduler, or deadlock regressions must pass; certificates
   are never reported as runtime measurements.
8. If any source changes after acceptance, rerun correctness and calibration.
   If a rejection or later discovery exposes misunderstood semantics, revise
   the document, cases, expected outputs, both solution forms, and affected
   benchmark or complexity claims together; never patch only the submission.
9. Refresh the audit and dataset report, run focused regression tests, and run
   `git diff --check`.
10. Record a genuine blocker with exact evidence and continue numerically.

## Current authoritative checkpoint

The refreshed migration audit after completing and remotely verifying package
work through 1613 reports:

- 3985 canonical packages;
- 1613 locally complete;
- 1566 packages fully complete and remotely verified;
- 1582 completed three-tier scaling benchmarks;
- 31 strictly validated complexity certificates;
- 1613 packages with complete complexity verification;
- 47 recorded remote-verification blockers. Frontend IDs 1413 through 1426
  are locally complete but Electron `safeStorage.decryptString` fails with
  Windows error `0x8009000B`. Frontend IDs 1463 through 1495 are locally
  complete but Chrome was not running; the Chrome-control policy requires an
  explicit confirmation before launching it, while the user instructed the
  migration to record blockers rather than request input;
- frontend ID 1614, Maximum Nesting Depth of the Parentheses, as the first
  actionable incomplete package.

There are 2372 locally incomplete packages after this checkpoint. The forty-seven
recorded blockers affect only remote Accepted verification; per the user's
instruction, record the exact failure for each affected package and continue
numerically without waiting for user input. Use the generated report for the
live check combination rather than relying on older grouped counts here.

The thirteen former benchmark blockers are frontend IDs 401, 405, 479, 999,
1108, 1114, 1118, 1134, 1137, 1154, 1165, 1188, and 1226. Their certificates
record bounded-domain, bounded-concurrency, or asymptotic-optimality evidence.
The other five original blockers are frontend IDs 1115, 1116, 1117, 1195,
and 1242; their source-native concurrency contracts support the reviewed
three-tier scaling workloads. The per-ID recovery procedure is in
`dsa/leetcode/_reports/ORIGINAL_18_BLOCKER_PLAYBOOK.md`. The generated audit is
authoritative if these counts drift.

## Historical problem 823 checkpoint

Problem 823, Binary Trees With Factors, is complete on the current uncommitted
branch:

- Package: `dsa/leetcode/0823_binary-trees-with-factors`
- LeetCode frontend ID: 823
- LeetCode internal question ID: 843
- Native entrypoint: `Solution.numFactoredBinaryTrees`
- App-local and native algorithms: sorted dynamic programming with a value-to-
  count map; `$O(n^2)$` time and `$O(n)$` auxiliary space.
- Correctness suite: 12 ordinary cases plus 3 benchmark cases, 15 total.
- Benchmark sizes: 32, 128, and 512 unique values, a 16-fold span. Each is a
  prefix of the sorted nonunit divisors of 73513440 so the tiers contain a
  dense lattice of valid factor dependencies.
- The canonical implementation and an independently structured quadratic
  factor-pair implementation passed every case and the scaling verdict.
- For calibration, the correct slower implementation linearly materialized
  prior pair products with `list(map(left.__mul__, previous))`. It returned all
  15 expected outputs and failed only scaling: relative extra growth `+0.53`
  exceeded `0.15`, and its largest reference ratio was `9.32x`.
- Exact native source remotely Accepted as LeetCode submission `2066667507`.
  `submission.json` was promoted to `verified` by the verifier.

Fresh audit after that acceptance:

- 3985 canonical packages
- 820 locally complete
- 820 fully complete and remotely verified
- 3 documented fixed-domain benchmark blockers
- 823 documents complete under the migration audit
- 1484 correctness-case packages complete
- 820 benchmark packages complete
- 1679 optimal app-local solutions complete
- 823 native submissions complete
- First actionable incomplete package: frontend ID 824, Goat Latin, at
  `dsa/leetcode/0824_goat-latin`

The separate dataset completion report currently records 2192 documents as
manually complete and 1793 as needing authoring. It is a broader documentation
inventory, not permission to skip the audit's first actionable package.

The fixed-domain records described above were historical blockers. They are now
represented by strictly validated non-scaling certificates; current state is
recorded in `dsa/leetcode/_reports/two_sum_migration_progress.md`.

## Verification evidence at this boundary

The complexity-certificate and concurrency-runtime batch remains green. The
latest completed packages add this evidence:

- problem 1268, Search Suggestions System, was remotely Accepted as submission
  `2068233787`;
- problem 1269, Number of Ways to Stay in the Same Place After Some Steps, was
  remotely Accepted as submission `2068243061`;
- problem 1270, All People Report to the Given Manager, was remotely Accepted
  as MySQL submission `2068251502`;
- problem 1271, Hexspeak, was remotely Accepted as submission `2068259331`;
- problem 1272, Remove Interval, was remotely Accepted as submission
  `2068263023`;
- problem 1273, Delete Tree Nodes, was remotely Accepted as submission
  `2068268130`;
- problem 1274, Number of Ships in a Rectangle, was remotely Accepted as
  submission `2068282593`; its app-local judge now supplies LeetCode-compatible
  `Point` objects through a hidden `Sea` oracle and enforces the 400-query cap;
- problem 1275, Find Winner on a Tic Tac Toe Game, was remotely Accepted as
  submission `2068286486`;
- problem 1276, Number of Burgers with No Waste of Ingredients, was remotely
  Accepted as submission `2068292171`;
- problem 1277, Count Square Submatrices with All Ones, was remotely Accepted
  as submission `2068298023`;
- problem 1278, Palindrome Partitioning III, was remotely Accepted as
  submission `2068302137`;
- problem 1279, Traffic Light Controlled Intersection, was remotely Accepted
  as submission `2068306159`; its source-native concurrency runner validates
  green-light changes, crossing exclusivity, red-road crossings, and deadlock;
- problem 1280, Students and Examinations, was remotely Accepted as MySQL
  submission `2068311399`;
- problem 1281, Subtract the Product and Sum of Digits of an Integer, was
  remotely Accepted as submission `2068315469`;
- problem 1282, Group the People Given the Group Size They Belong To, was
  remotely Accepted as submission `2068318505`;
- problem 1283, Find the Smallest Divisor Given a Threshold, was remotely
  Accepted as submission `2068324305`;
- problem 1284, Minimum Number of Flips to Convert Binary Matrix to Zero
  Matrix, was remotely Accepted as submission `2068327463`;
- problem 1285, Find the Start and End Number of Continuous Ranges, was
  remotely Accepted as MySQL submission `2068331983`;
- problem 1286, Iterator for Combination, was remotely Accepted as submission
  `2068335476`;
- problem 1287, Element Appearing More Than 25% In Sorted Array, was remotely
  Accepted as submission `2068337962`;
- problem 1288, Remove Covered Intervals, was remotely Accepted as submission
  `2068341518`;
- problem 1289, Minimum Falling Path Sum II, was remotely Accepted as
  submission `2068345447`;
- problem 1290, Convert Binary Number in a Linked List to Integer, was
  remotely Accepted as submission `2068348444`;
- problem 1291, Sequential Digits, was remotely Accepted as submission
  `2068351238`;
- problem 1292, Maximum Side Length of a Square with Sum Less than or Equal to
  Threshold, was remotely Accepted as submission `2068356607`;
- problem 1293, Shortest Path in a Grid with Obstacles Elimination, was
  remotely Accepted as submission `2068362101`;
- problem 1294, Weather Type in Each Country, was remotely Accepted as MySQL
  submission `2068365190`;
- problem 1295, Find Numbers with Even Number of Digits, was remotely Accepted
  as submission `2068368120`;
- problem 1296, Divide Array in Sets of K Consecutive Numbers, was remotely
  Accepted as submission `2068376168`;
- problem 1297, Maximum Number of Occurrences of a Substring, was remotely
  Accepted as submission `2068380987`;
- problem 1298, Maximum Candies You Can Get from Boxes, was remotely Accepted
  as submission `2068386935`;
- problem 1299, Replace Elements with Greatest Element on Right Side, was
  remotely Accepted as submission `2068389895`;
- problem 1300, Sum of Mutated Array Closest to Target, was remotely Accepted
  as submission `2068393866`;
- problem 1301, Number of Paths with Max Score, was remotely Accepted as
  submission `2068416253` after submission `2068399383` exposed a reachable
  100-by-100 board whose optimal-path count is zero modulo $10^9+7$;
- problem 1302, Deepest Leaves Sum, was remotely Accepted as submission
  `2068419488`;
- problem 1303, Find the Team Size, was remotely Accepted as MySQL submission
  `2068423014`;
- problem 1304, Find N Unique Integers Sum up to Zero, was remotely Accepted
  as submission `2068429171`;
- problem 1305, All Elements in Two Binary Search Trees, was remotely Accepted
  as submission `2068432556`;
- problem 1306, Jump Game III, was remotely Accepted as submission
  `2068436843`;
- problem 1307, Verbal Arithmetic Puzzle, was remotely Accepted as submission
  `2068444942`;
- problem 1308, Running Total for Different Genders, was remotely Accepted as
  MySQL submission `2068448664`;
- problem 1309, Decrypt String from Alphabet to Integer Mapping, was remotely
  Accepted as submission `2068452085`;
- problem 1310, XOR Queries of a Subarray, was remotely Accepted as submission
  `2068455042`;
- problem 1311, Get Watched Videos by Your Friends, was remotely Accepted as
  submission `2068458760`;
- problem 1312, Minimum Insertion Steps to Make a String Palindrome, was
  remotely Accepted as submission `2068461613`;
- problem 1313, Decompress Run-Length Encoded List, was remotely Accepted as
  submission `2068464551`;
- problem 1314, Matrix Block Sum, was remotely Accepted as submission
  `2068467426`;
- problem 1315, Sum of Nodes with Even-Valued Grandparent, was remotely
  Accepted as submission `2068470451`;
- problem 1316, Distinct Echo Substrings, was remotely Accepted as submission
  `2068474022`;
- problem 1317, Convert Integer to the Sum of Two No-Zero Integers, was
  remotely Accepted as submission `2068482128`; its semantic validator accepts
  any positive zero-free pair with the required sum;
- problem 1318, Minimum Flips to Make a OR b Equal to c, was remotely Accepted
  as submission `2068484550`;
- problem 1319, Number of Operations to Make Network Connected, was remotely
  Accepted as submission `2068487705`;
- problem 1320, Minimum Distance to Type a Word Using Two Fingers, was remotely
  Accepted as submission `2068490064`;
- problem 1321, Restaurant Growth, was remotely Accepted as MySQL submission
  `2068493367`;
- problem 1322, Ads Performance, was remotely Accepted as MySQL submission
  `2068495154`;
- problem 1323, Maximum 69 Number, was remotely Accepted as submission
  `2068497164`;
- problem 1324, Print Words Vertically, was remotely Accepted as submission
  `2068499185`;
- problem 1325, Delete Leaves With a Given Value, was remotely Accepted as
  submission `2068502569`;
- problem 1326, Minimum Number of Taps to Open to Water a Garden, was remotely
  Accepted as submission `2068505103`;
- problem 1327, List the Products Ordered in a Period, was remotely Accepted as
  MySQL submission `2068507227`;
- problem 1328, Break a Palindrome, was remotely Accepted as submission
  `2068509703`; its live backend `question_id` is 1252 rather than a sequential
  value near the frontend ID;
- problem 1329, Sort the Matrix Diagonally, was remotely Accepted as submission
  `2068587798`;
- problem 1330, Reverse Subarray To Maximize Array Value, was remotely Accepted
  as submission `2068590962`; its live backend `question_id` is 1255;
- problem 1331, Rank Transform of an Array, was remotely Accepted as submission
  `2068593034`;
- problem 1332, Remove Palindromic Subsequences, was remotely Accepted as
  submission `2068596166`; its live backend `question_id` is 1454;
- problem 1333, Filter Restaurants by Vegan-Friendly, Price and Distance, was
  remotely Accepted as submission `2068599010`;
- problem 1334, Find the City With the Smallest Number of Neighbors at a
  Threshold Distance, was remotely Accepted as submission `2068603266`;
- problem 1335, Minimum Difficulty of a Job Schedule, was remotely Accepted as
  submission `2068607058`;
- problem 1336, Number of Transactions per Visit, was remotely Accepted as
  MySQL submission `2068611403`; its live backend `question_id` is 1467;
- problem 1337, The K Weakest Rows in a Matrix, was remotely Accepted as
  submission `2068614061`; its live backend `question_id` is 1463;
- problem 1338, Reduce Array Size to The Half, was remotely Accepted as
  submission `2068617518`;
- problem 1339, Maximum Product of Splitted Binary Tree, was remotely Accepted
  as submission `2068620361`;
- problem 1340, Jump Game V, was remotely Accepted as submission
  `2068623413`;
- problem 1341, Movie Rating, was remotely Accepted as MySQL submission
  `2068627841`; its live backend `question_id` is 1480. An initial native
  query timed out as submission `2068627115`, so the exact candidate was
  replaced with direct grouped derived tables before verification;
- problem 1342, Number of Steps to Reduce a Number to Zero, was remotely
  Accepted as submission `2068632131`; its live backend `question_id` is 1444;
- problem 1343, Number of Sub-arrays of Size K and Average Greater than or
  Equal to Threshold, was remotely Accepted as submission `2068634512`; its
  live backend `question_id` is 1445;
- problem 1344, Angle Between Hands of a Clock, was remotely Accepted as
  submission `2068638706`; its live backend `question_id` is 1446;
- problem 1345, Jump Game IV, was remotely Accepted as submission
  `2068643211`; its live backend `question_id` is 1447;
- problem 1346, Check If N and Its Double Exist, was remotely Accepted as
  submission `2068648353`; its live backend `question_id` is 1468;
- problem 1347, Minimum Number of Steps to Make Two Strings Anagram, was
  remotely Accepted as submission `2068650593`; its live backend
  `question_id` is 1469;
- problem 1348, Tweet Counts Per Frequency, was remotely Accepted as
  submission `2068655262`; its live backend `question_id` is 1470;
- problem 1349, Maximum Students Taking Exam, was remotely Accepted as
  submission `2068657927`; its live backend `question_id` is 1471;
- problem 1350, Students With Invalid Departments, was remotely Accepted as
  MySQL submission `2068665038`; its live backend `question_id` is 1481;
- problem 1351, Count Negative Numbers in a Sorted Matrix, was remotely
  Accepted as submission `2068667545`; its live backend `question_id` is 1476;
- problem 1352, Product of the Last K Numbers, was remotely Accepted as
  submission `2068670862`; its live backend `question_id` is 1477;
- problem 1353, Maximum Number of Events That Can Be Attended, was remotely
  Accepted as submission `2068673964`; its live backend `question_id` is 1478;
- problem 1354, Construct Target Array With Multiple Sums, was remotely
  Accepted as submission `2068678764`; its live backend `question_id` is 1479;
- problem 1355, Activity Participants, was remotely Accepted as MySQL
  submission `2068682973`; its live backend `question_id` is 1494;
- problem 1356, Sort Integers by The Number of 1 Bits, was remotely Accepted as
  submission `2068685420`; its live backend `question_id` is 1458;
- problem 1357, Apply Discount Every n Orders, was remotely Accepted as
  submission `2068693366`; its live backend `question_id` is 1459;
- problem 1358, Number of Substrings Containing All Three Characters, was
  remotely Accepted as submission `2068702496`; its live backend `question_id`
  is 1460;
- problem 1359, Count All Valid Pickup and Delivery Options, was remotely
  Accepted as submission `2068705667`; its live backend `question_id` is 1461;
- problem 1360, Number of Days Between Two Dates, was remotely Accepted as
  submission `2068709078`; its live backend `question_id` is 1274;
- problem 1361, Validate Binary Tree Nodes, was remotely Accepted as submission
  `2068711780`; its live backend `question_id` is 1275;
- problem 1362, Closest Divisors, was remotely Accepted as submission
  `2068717432`; its live backend `question_id` is 1276;
- problem 1363, Largest Multiple of Three, was remotely Accepted as submission
  `2068720826`; its live backend `question_id` is 1277;
- problem 1364, Number of Trusted Contacts of a Customer, was remotely Accepted
  as MySQL submission `2068725201`; its live backend `question_id` is 1495;
- problem 1365, How Many Numbers Are Smaller Than the Current Number, was
  remotely Accepted as submission `2068728074`; its live backend `question_id`
  is 1482;
- problem 1366, Rank Teams by Votes, was remotely Accepted as submission
  `2068731697`; its live backend `question_id` is 1483;
- problem 1367, Linked List in Binary Tree, was remotely Accepted as submission
  `2068736760`; its live backend `question_id` is 1484;
- problem 1368, Minimum Cost to Make at Least One Valid Path in a Grid, was
  remotely Accepted as submission `2068741550`; its live backend `question_id`
  is 1485;
- problem 1369, Get the Second Most Recent Activity, was remotely Accepted as
  MySQL submission `2068748473`; its live backend `question_id` is 1504;
- problem 1370, Increasing Decreasing String, was remotely Accepted as
  submission `2068752614`; its live backend `question_id` is 1472;
- problem 1371, Find the Longest Substring Containing Vowels in Even Counts,
  was remotely Accepted as submission `2068755255`; its live backend
  `question_id` is 1473;
- problem 1372, Longest ZigZag Path in a Binary Tree, was remotely Accepted as
  submission `2068758149`; its live backend `question_id` is 1474;
- problem 1373, Maximum Sum BST in Binary Tree, was remotely Accepted as
  submission `2068763101`; its live backend `question_id` is 1475;
- problem 1374, Generate a String With Characters That Have Odd Counts, was
  remotely Accepted as submission `2068766105`; its live backend `question_id`
  is 1490;
- problem 1375, Number of Times Binary String Is Prefix-Aligned, was remotely
  Accepted as submission `2068768445`; its live backend `question_id` is 1491;
- problem 1376, Time Needed to Inform All Employees, was remotely Accepted as
  submission `2068771174`; its live backend `question_id` is 1492;
- problem 1377, Frog Position After T Seconds, was remotely Accepted as
  submission `2068774179`; its live backend `question_id` is 1493;
- problem 1378, Replace Employee ID With The Unique Identifier, was remotely
  Accepted as MySQL submission `2068779941`; its live backend `question_id` is
  1509;
- problem 1379, Find a Corresponding Node of a Binary Tree in a Clone of That
  Tree, was remotely Accepted as submission `2068787062`; its live backend
  `question_id` is 1498;
- problem 1380, Lucky Numbers in a Matrix, was remotely Accepted as submission
  `2068789419`; its live backend `question_id` is 1496;
- problem 1381, Design a Stack With Increment Operation, was remotely Accepted
  as submission `2068793772`; its live backend `question_id` is 1497;
- problem 1382, Balance a Binary Search Tree, was remotely Accepted as
  submission `2068800587`; its live backend `question_id` is 1285;
- problem 1383, Maximum Performance of a Team, was remotely Accepted as
  submission `2068804058`; its live backend `question_id` is 1499;
- problem 1384, Total Sales Amount by Year, was remotely Accepted as MySQL
  submission `2068809662`; its live backend `question_id` is 1518;
- problem 1385, Find the Distance Value Between Two Arrays, was remotely
  Accepted as submission `2068812262`; its live backend `question_id` is 1486;
- problem 1386, Cinema Seat Allocation, was remotely Accepted as submission
  `2068814945`; its live backend `question_id` is 1487;
- problem 1269's benchmark uses $N=\texttt{steps}\,w$ at sizes 840, 5100, and
  31500. The reference and independent same-class implementation passed; a
  correct full-array implementation returned every expected output and failed
  only scaling with extra growth `+0.51` and a `6.88x` largest ratio;
- problem 1270's benchmark uses employee-row counts 16, 64, and 256. The
  reference and recursive-CTE same-class query passed; a correct Cartesian
  product query returned every expected row and failed only scaling with extra
  growth `+0.72` and a `7.22x` largest ratio;
- problem 1271 uses a `bounded_domain` certificate because $n \le 10^{12}$
  yields at most ten hexadecimal digits. Its independent oracle covers values
  1 through 4096, powers of sixteen, valid letter forms, and upper boundaries;
- problem 1272's benchmark sizes are 512, 2048, and 8192 retained intervals.
  A second linear implementation passed; a correct repeated-list-rebuild
  implementation failed only scaling at `+0.51` and `4.20x`;
- problem 1273's benchmark sizes are 256, 1024, and 4096 nodes in a chain. A
  second postorder implementation passed; correct full-subtree member-list
  materialization failed only scaling at `+0.29` and `4.14x`;
- problem 1274 uses a `bounded_domain` certificate. The maximum-ship full-grid
  regression used 313 of 400 oracle calls, and the focused judge test verifies
  inclusive rectangles, `Point` identity, and hard budget enforcement;
- problem 1275 uses a `bounded_domain` certificate for the fixed 3-by-3 board;
  regression checks every reachable valid game state against an independent
  board-line oracle;
- problem 1276's benchmark sizes are 200, 400, and 800 burgers. The $O(1)$
  reference passed, while correct linear enumeration returned every answer,
  completed normally, and failed only scaling with extra growth `+0.71`;
- problem 1277's all-one matrix benchmark uses 36, 144, and 576 cells. A
  correct square-enumeration implementation completed normally and failed
  only scaling at `+0.54` and `12.60x`;
- problem 1278's benchmark uses $kn^2$ sizes 1250, 5000, and 20000. A correct
  substring-rescanning implementation completed normally and failed only
  scaling at `+0.43` and `10.32x`;
- problem 1279 uses a `bounded_concurrency` certificate backed by scheduler,
  semantic-validator, and deadlock regressions;
- problem 1280's SQL benchmark uses $R+E$ sizes 8, 32, and 128. A correct
  Cartesian-product query completed normally and failed only scaling at
  `+1.96` and `305.39x`;
- problem 1281 uses a `bounded_domain` certificate because legal inputs have
  at most six digits; regression exhaustively checks all 100000 legal values;
- problem 1282's benchmark uses 32, 128, and 500 people. Correct quadratic
  list removal completed normally and failed only scaling at `+0.18` and
  `2.01x`;
- problem 1283's benchmark uses 32, 128, and 512 array values. A correct
  selection-sort-plus-binary-search implementation completed normally and
  failed only scaling at `+0.86` and `22.98x`;
- problem 1284 uses a `bounded_domain` certificate for at most nine cells;
  regression checks every binary state for every legal matrix shape against
  independent exhaustive flip-subset enumeration;
- problem 1285's SQL benchmark uses 32, 128, and 512 log rows. A correct
  start/end anti-join completed normally and failed only scaling at `+2.11`
  and `806.23x`;
- problem 1286's benchmark uses 16, 64, and 256 successive iterator results.
  A correct restart-enumeration iterator completed normally and failed only
  scaling at `+0.69` and `5.53x`;
- problem 1287's benchmark uses 512, 2048, and 8192 sorted values. A correct
  linear run scan completed normally and failed only scaling at `+0.88` and
  `47.86x`;
- problem 1288's benchmark uses 30, 120, and 480 disjoint intervals. Correct
  pairwise coverage testing completed normally and failed only scaling at
  `+1.30` and `165.20x`;
- problem 1289's benchmark uses 576, 2304, and 9216 grid cells. The correct
  cubic predecessor scan completed normally and failed only scaling at
  `+0.54` and `26.36x`;
- problem 1290 uses a `bounded_domain` certificate for at most 30 linked-list
  nodes; regression exhaustively checks every bit pattern through length 12
  and independent maximum-length boundaries through the real list adapter;
- problem 1291 uses a `bounded_domain` certificate for the fixed 36
  sequential-digit candidates; regression checks every interval formed by
  candidate-adjacent legal boundaries;
- problem 1292's all-one square-matrix benchmark uses 576, 2304, and 9216
  cells. Correct all-side prefix enumeration completed normally and failed
  only scaling at `+0.46` and `5.31x`;
- problem 1293's open-grid benchmark uses state-space sizes 32, 128, and 512.
  Correct unsorted-list Dijkstra completed normally and failed only scaling at
  `+0.86` and `32.93x`;
- problem 1294's SQL benchmark uses 32, 128, and 512 total country and weather
  rows. A correct correlated-average query completed normally and failed only
  scaling at `+0.60` and `5.60x`;
- problem 1295's benchmark uses 32, 128, and 500 values. Correct selection-sort
  preprocessing completed normally and failed only scaling at `+1.35` and
  `199.30x`;
- problem 1296's unique-singleton benchmark uses 256, 1024, and 4096 values.
  Correct repeated minimum-map scanning completed normally and failed only
  scaling at `+0.48` and `6.50x`;
- problem 1297's pseudorandom-string benchmark uses lengths 64, 128, and 256.
  Correct pairwise minimum-window recounting completed normally and failed
  only scaling at `+1.12` and `25.64x`;
- problem 1298's descending dependency-chain benchmark uses 16, 64, and 256
  boxes. Correct repeated global rescanning completed normally and failed only
  scaling at `+0.92` and `28.28x`;
- problem 1299's descending-array benchmark uses 32, 128, and 512 values.
  Correct suffix rescanning completed normally and failed only scaling at
  `+1.34` and `121.63x`;
- problem 1300's joint array-length and cap-range benchmark uses sizes 16, 64,
  and 256. A correct selection-sort prefix derivation completed normally and
  failed only scaling at `+0.93` and `21.09x`;
- problem 1301's all-nine board benchmark uses side lengths 16, 50, and 100.
  Correct immutable anti-diagonal score/count snapshots completed every case,
  including the modulo-zero remote regression, and failed only scaling at
  `+0.21`;
- problem 1302's right-skewed-tree benchmark uses 32, 128, and 512 nodes.
  Correct repeated subtree-height recursion completed normally and failed
  only scaling at `+1.13` and `155.44x`;
- problem 1303's single-team SQL benchmark uses 32, 128, and 512 employee rows.
  A correct correlated count subquery completed normally and failed only
  scaling at `+0.84` and `10.51x`;
- problem 1304's construction benchmark uses output lengths 64, 256, and 1000.
  Correct repeated membership checks completed normally and failed only
  scaling at `+0.61`;
- problem 1305's interleaved skewed-tree benchmark uses 32, 128, and 512 total
  nodes. Correct repeated sorted insertion completed normally and failed only
  scaling at `+1.04` and `39.68x`;
- problem 1306's unit-jump-chain benchmark uses lengths 32, 128, and 512.
  Correct explicit linear scans of the visited list completed normally and
  failed only scaling at `+0.94` and `40.82x`;
- problem 1307 uses a `bounded_domain` certificate because at most ten distinct
  letters can receive digits. An independent coefficient-and-permutation
  oracle checks smaller alphametics, while satisfiable and impossible
  ten-letter boundary cases exercise the complete digit domain;
- problem 1308's two-partition SQL benchmark uses 32, 128, and 512 score rows.
  A correct correlated prefix-sum query completed normally and failed only
  scaling at `+0.86` and `11.39x`;
- problem 1309's marked-token benchmark uses encoded lengths 30, 120, and 480.
  Correct repeated prefix validation completed normally, including the
  separate 1000-character ordinary boundary, and failed only scaling at
  `+1.25` and `146.65x`;
- problem 1310's balanced array-and-query benchmark uses combined sizes 64,
  256, and 1024. Correct direct range scans completed normally and failed only
  scaling at `+1.39` and `205.39x`;
- problem 1311's distinct-title benchmark uses 32, 128, and 512 target-level
  video entries. Correct repeated full-list frequency scans completed normally
  and failed only scaling at `+1.55` and `617.64x`;
- problem 1312's all-distinct-string benchmark uses lengths 4, 8, and 16.
  Correct unmemoized interval recursion completed normally and failed only
  scaling at `+3.96` and `259.10x`;
- problem 1313's growing-run benchmark uses output lengths 144, 576, and 2304.
  Correct repeated accumulated-result copying completed normally and failed
  only scaling at `+1.27` and `185.47x`;
- problem 1314's growing-radius square-matrix benchmark uses 64, 256, and 1024
  cells. Correct direct clipped-block enumeration completed normally and
  failed only scaling at `+0.86` and `14.96x`;
- problem 1315's even-valued right-chain benchmark uses 24, 96, and 384 nodes.
  Correct repeated root searches for parent and grandparent completed normally
  and failed only scaling at `+1.15` and `261.16x`;
- problem 1316's repeated-character benchmark uses lengths 24, 48, and 96.
  Correct exact half comparisons completed normally and failed only scaling at
  `+0.74`;
- problem 1317's target-value benchmark uses 24, 96, and 384. Correct
  exhaustive enumeration of both positive addends completed normally, returned
  semantically valid pairs, and failed only scaling at `+1.83` and `569.63x`;
- problem 1318's significant-bit benchmark uses widths 4, 12, and 28. Correct
  repeated lower-bit rescanning completed normally and failed only scaling at
  `+0.48`;
- problem 1319's connected-path benchmark uses combined vertex-and-edge sizes
  15, 63, and 255. Correct repeated reachability traversals completed normally
  and failed only scaling at `+1.21` and `82.21x`;
- problem 1320's distinct-letter benchmark uses word lengths 4, 8, and 16.
  Correct no-memo two-finger assignment recursion completed normally and failed
  only scaling at `+4.32` and `123.18x`;
- problem 1321's consecutive-date SQL benchmark uses 32, 128, and 512 customer
  rows. A correct correlated seven-day aggregation completed normally and
  failed only scaling at `+1.12` and `35.59x`;
- problem 1322's distinct-ad SQL benchmark uses 32, 128, and 512 rows. Correct
  correlated per-ad counts completed normally and failed only scaling at
  `+0.80` and `14.39x`;
- problem 1323 uses a `bounded_domain` certificate because every legal number
  has at most four digits. Regression exhaustively checks all legal 6/9 digit
  strings against independent enumeration of no change and every single flip;
- problem 1324's padded-rectangle benchmark uses 32, 128, and 512 cells.
  Correct repeated sentence splitting and rescanning completed normally and
  failed only scaling at `+0.84` and `27.42x`;
- problem 1325's target-valued skew-chain benchmark uses 16, 64, and 256 nodes.
  Correct repeated current-leaf deletion passes completed normally and failed
  only scaling at `+1.18` and `96.28x`;
- problem 1326's unit-radius garden benchmark uses lengths 32, 128, and 512.
  Correct explicit insertion sorting followed by greedy interval cover
  completed normally and failed only scaling at `+1.11` and `141.86x`;
- problem 1327's product-and-order SQL benchmark uses combined row counts 64,
  256, and 1024. A correct correlated per-product sum completed normally and
  failed only scaling at `+0.81` and `10.35x`;
- problem 1328's all-a palindrome benchmark uses lengths 24, 96, and 384.
  Correct candidate enumeration with explicit palindrome checks completed
  normally and failed only scaling at `+1.51` and `252.04x`;
- problem 1329's descending-diagonal square-matrix benchmark uses 64, 256, and
  1024 cells. Correct per-diagonal selection sorting completed normally and
  failed only scaling at `+0.58` and `8.55x`;
- problem 1330's mixed-value benchmark uses array lengths 24, 96, and 384.
  Correct exhaustive reversal-boundary enumeration completed normally and
  failed only scaling at `+1.18` and `198.53x`;
- problem 1331's descending-distinct benchmark uses array lengths 32, 128, and
  512. Correct selection sorting completed normally and failed only scaling at
  `+1.48` and `215.87x`;
- problem 1332's late-mismatch binary-string benchmark uses lengths 32, 128,
  and 512. Correct longest-palindromic-subsequence dynamic programming
  completed normally and failed only scaling at `+1.88` and `1827.51x`;
- problem 1333's all-eligible restaurant benchmark uses 32, 128, and 512
  records. Correct selection sorting completed normally and failed only
  scaling at `+1.26` and `109.79x`;
- problem 1334's dense-graph benchmark uses 4, 8, and 16 cities. Correct
  all-sources Bellman-Ford completed every tier and failed only scaling at
  `+1.27`; larger draft tiers were rejected during calibration because the
  slower implementation reached the safety cap rather than producing a valid
  scaling verdict;
- problem 1335's five-day scheduling benchmark uses 16, 32, and 64 jobs.
  Correct explicit segment-maximum recomputation completed normally and failed
  only scaling at `+0.88` and `17.24x`;
- problem 1336's visit-and-transaction benchmark uses combined row counts 32,
  128, and 512. A correct correlated-count query completed normally and failed
  only scaling at `+0.77`;
- problem 1337's square-matrix benchmark uses 256, 1024, and 4096 cells.
  Correct explicit row summation completed normally and failed only scaling at
  `+0.36`;
- problem 1338's all-distinct benchmark uses array lengths 32, 128, and 512.
  Correct linear-search frequency counting completed normally and failed only
  scaling at `+1.48` and `347.15x`;
- problem 1339's right-skewed-tree benchmark uses 32, 128, and 512 nodes.
  Correct repeated subtree summation completed normally and failed only
  scaling at `+1.04` and `67.74x`;
- problem 1340's descending-chain benchmark uses 16, 64, and 256 positions.
  Correct repeated jump relaxation completed normally and failed only scaling
  at `+1.20` and `228.40x`; a larger draft tier was rejected because it
  reached the safety cap instead of producing scaling evidence;
- problem 1341's SQL benchmark uses 48, 192, and 768 combined user, movie, and
  rating rows. A correct correlated-query alternative completed normally and
  failed only scaling at `+0.67`;
- problem 1342's benchmark uses values 128, 1024, and 4096. Correct dynamic
  programming from zero through the input completed normally and failed only
  scaling at `+0.79` and `29.44x`; larger draft tiers were rejected because
  the slower implementation reached the safety cap;
- problem 1343's benchmark uses array lengths 32, 128, and 512 with half-array
  windows. Correct explicit rescanning of every window completed normally and
  failed only scaling at `+1.32` and `88.96x`;
- problem 1344 uses a `bounded_domain` certificate because the legal input has
  only 720 clock states. Regression exhaustively checks all of them against an
  independent exact-arithmetic oracle expressed in half-degree units;
- problem 1345's repeated-value benchmark uses array lengths 32, 128, and 512.
  Correct repeated equal-value bucket scanning completed normally and failed
  only scaling at `+1.01` and `82.41x`;
- problem 1346's odd-value benchmark uses array lengths 32, 128, and 500.
  Correct exhaustive pair testing completed normally and failed only scaling
  at `+1.24` and `158.53x`;
- problem 1347's reversed character-block benchmark uses common string lengths
  128, 512, and 2048. Correct repeated list search and removal completed
  normally and failed only scaling at `+0.41`;
- problem 1348's record-and-bucket benchmark uses combined sizes 64, 256, and
  1024. Correct per-bucket rescanning completed normally and failed only
  scaling at `+1.11` and `89.31x`;
- problem 1349's open-room row-mask benchmark uses required-work sizes 32, 768,
  and 16384. Correct recursive row-sequence enumeration without memoization
  completed normally and failed only scaling at `+0.57` and `28.53x`;
- problem 1350's SQL benchmark uses combined department-and-student row counts
  32, 128, and 512. A correct de-indexed correlated existence query completed
  normally and failed only scaling at `+0.50`;
- problem 1351's diagonal-boundary matrix benchmark uses $m+n$ sizes 50, 100,
  and 200. Correct full-cell scanning completed normally and failed only
  scaling at `+1.14` and `19.78x`;
- problem 1352's balanced addition-and-query benchmark uses operation counts
  32, 128, and 512. Correct raw suffix multiplication completed normally and
  failed only scaling at `+0.83` and `11.81x`;
- problem 1353's shared-interval event benchmark uses 32, 128, and 512 events.
  Correct repeated linear deadline selection completed normally and failed
  only scaling at `+0.98` and `100.65x`;
- problem 1354's modulo-compression benchmark uses maximum-value bit lengths 3,
  7, and 13. Correct single-subtraction reversal completed normally and failed
  only scaling at `+3.12` and `124.53x`; an earlier 21-bit tier was rejected
  because it reached the safety cap;
- problem 1355's SQL benchmark uses combined activity-and-friend row counts 32,
  128, and 512. A correct de-indexed correlated-count query completed normally
  and failed only scaling at `+0.93` and `12.83x`;
- problem 1356's descending-distinct benchmark uses array lengths 32, 128, and
  500. Correct selection sorting by population count and value completed
  normally and failed only scaling at `+1.50` and `228.28x`;
- problem 1357's repeated full-catalog bills use total catalog-plus-line-item
  sizes 816, 16064, and 200200. A correct implementation rebuilding the product
  map for every line item completed normally and failed only scaling at
  `+0.24`;
- problem 1358's late-completion strings use lengths 10, 500, and 10000. A
  correct implementation materializing and searching every suffix completed
  normally and failed only scaling at `+0.68` and `154.02x`;
- problem 1359's labeled-order tiers use $n=10$, $40$, and $100$. A correct
  pickup/delivery state DP completed normally and failed only scaling at
  `+1.54` and `224.08x`;
- problem 1360's legal date gaps use 365, 3650, and 36500 days. Correct
  day-by-day calendar advancement completed normally and failed only scaling
  at `+0.94` and `511.28x`;
- problem 1361's valid right-chain tiers use 100, 1000, and 10000 nodes. Correct
  repeated full-array parent counting completed normally and failed only
  scaling at `+0.52` and `11.57x`;
- problem 1362's deep-divisor tiers use larger products 83, 1523, and 9818. A
  correct exhaustive factor enumerator completed normally and failed only
  scaling at `+0.73` and `77.14x`;
- problem 1363's mixed-digit tiers use lengths 50, 500, and 5000. Correct
  repeated-maximum ordering completed normally and failed only scaling at
  `+0.39`;
- problem 1364's SQL tiers use 4, 16, and 64 rows in each of Customers,
  Contacts, and Invoices. Correct de-indexed correlated counts completed
  normally and failed only scaling at `+0.24`;
- problem 1365's bounded-value tiers use lengths 125, 250, and 500. Correct
  repeated sorted first-index lookup completed normally and failed only
  scaling at `+0.42`;
- problem 1366 holds 624 ballots fixed while scaling teams 4, 12, and 26. A
  correct bubble comparator that recounts tied position columns completed
  normally and failed only scaling at `+0.68`;
- problem 1367's repeated-prefix chains use reference-work sizes 550, 1200,
  and 2250. Correct restart-at-every-node matching completed normally and
  failed only scaling at `+1.40`;
- problem 1368's zero-cost snake grids use 81, 625, and 2401 cells. Correct
  unsorted-frontier Dijkstra completed normally and failed only scaling at
  `+0.20`;
- problem 1369's SQL tiers use 16, 64, and 256 activity rows. A correct
  correlated recount completed normally and failed only scaling at `+0.83`;
- problem 1370's repeated-character tiers use lengths 125, 250, and 500. A
  correct direct list simulation completed normally and failed only scaling
  at `+0.31`;
- problem 1371's consonant-only tiers use lengths 500, 2000, and 8000. Correct
  repeated prefix vowel counting completed normally and failed only scaling
  at `+0.15` beyond the exact threshold;
- problem 1372's alternating-chain tiers use 20, 40, and 80 tree nodes. Correct
  path matching restarted at every node completed normally and failed only
  scaling at `+1.19` and `41.59x`;
- problem 1373's increasing right-chain tiers use 20, 40, and 80 tree nodes.
  Correct independent validation and summation of every subtree completed
  normally and failed only scaling at `+0.87`;
- problem 1374 spans its full legal output range with lengths 125, 250, and
  500. Correct repeated string prepending completed normally and failed only
  scaling at `+0.70`;
- problem 1375's adjacent-pair flip tiers use lengths 500, 2000, and 8000.
  Correct prefix rescanning with slicing and `all` completed normally and
  failed only scaling at `+0.72` and `14.50x`; an explicit Python-loop draft
  was rejected because it reached the safety cap;
- problem 1376's reporting-chain tiers use 500, 2000, and 8000 employees.
  Correct repeated manager-array searches completed normally and failed only
  scaling at `+0.46` and `8.76x`;
- problem 1377's binary-heap tree tiers use the full legal range of 25, 50,
  and 100 vertices. Correct raw-edge rescanning completed normally and failed
  only scaling at `+1.21` and `32.48x`;
- problem 1378's SQL tiers use 32, 128, and 512 combined employee and mapping
  rows. A correct de-indexed correlated lookup completed normally and failed
  only scaling at `+0.31`;
- problem 1379's left-chain tiers use 20, 40, and 80 nodes. Correct replay of
  every original node's path in the cloned tree completed normally and failed
  only scaling at `+1.15` and `19.31x`;
- problem 1380's square-matrix tiers use 100, 625, and 2500 cells. Correct
  per-cell row-minimum and column-maximum recomputation completed normally and
  failed only scaling at `+0.20`;
- problem 1381's full-depth stack workloads use 60, 240, and 960 operations.
  Correct eager bottom-element increments completed normally and failed only
  scaling at `+0.91` and `16.52x`;
- problem 1382's increasing right-chain tiers use 625, 2500, and 10000 nodes.
  Correct repeated prefix fingerprinting and copying completed normally and
  failed only scaling at `+0.34`; a lighter prefix-copy draft was rejected
  because framework overhead left it at the scaling threshold;
- problem 1383's nonmonotone-speed tiers use 250, 1000, and 4000 engineers.
  Correct repeated sorting of every efficiency prefix completed normally and
  failed only scaling at `+0.93` and `25.88x`;
- problem 1384's SQL tiers use 32, 128, and 512 combined product-and-sales
  rows. Correct de-indexed correlated product-year scans completed normally
  and failed only scaling at `+0.61`;
- problem 1385's all-far array tiers use combined lengths 250, 500, and 1000.
  Correct exhaustive pair comparison completed normally and failed only
  scaling at `+0.96` and `95.06x`;
- problem 1386's sparse-cinema tiers use 1000, 10000, and 100000 rows with one
  irrelevant reservation. Correct full-row scanning completed normally and
  failed only scaling at `+0.92` and `5660.05x`;
- problem 1382 extended the balanced-BST validator with an explicit
  `values_from_tree` mode so alternate valid balanced shapes are checked
  against the inorder values of a level-order input tree;
- problem 1384's first two native submissions exposed an omitted required
  `product_id` output column. Documentation, fixtures, both SQL artifacts, and
  calibration were corrected together before the Accepted submission;
- problem 1379 required a source-native cloned-tree fixture: the judge now
  constructs distinct original and cloned trees while passing `target` as the
  exact selected object inside `original`. Its focused regression passed as
  part of 105 validated-case tests;
- the dynamic complexity parser now recognizes canonical LaTeX
  `$O(n \log n)$` as linearithmic, with a focused regression test;
- problem 1387 was remotely Accepted as submission `2068821263`; its Collatz
  tiers use range sizes 100, 300, and 600, and a correct uncached alternative
  completed normally and failed only scaling at `+0.38`;
- problem 1388 was remotely Accepted as submission `2068824739`; its circular
  pizza tiers use 30, 120, and 480 slices, and correct endpoint-rescanning DP
  completed normally and failed only scaling at `+0.28`;
- problem 1389 was remotely Accepted as submission `2068827730`; its full
  legal insertion tiers use 25, 50, and 100 operations, and correct repeated
  rebuilding completed normally and failed only scaling at `+1.65` and
  `34.70x`;
- problem 1390 was remotely Accepted as submission `2068833742`; its prime-
  cube divisor-search tiers use sizes 11, 70, and 225, and correct full divisor
  enumeration completed normally and failed only scaling at `+1.23` and
  `60.13x`;
- problem 1391 was remotely Accepted as submission `2068841616`; its valid-
  street tiers use 20, 80, and 281 cells, and a correct traversal with a
  redundant full-size scan per visited cell completed normally and failed only
  scaling at `+0.83` and `19.32x`;
- problem 1392 was remotely Accepted as submission `2068848081`; its KMP
  prefix tiers use lengths 32, 80, and 160, and correct explicit border
  comparison completed normally and failed only scaling at `+1.04` and
  `16.71x`;
- problem 1393 was remotely Accepted as MySQL submission `2068851797`; its
  stock-operation tiers use 16, 64, and 256 rows, and correct de-indexed
  correlated aggregation completed normally and failed only scaling at
  `+0.47`;
- problem 1394 was remotely Accepted as submission `2068855506`; its distinct-
  value tiers use lengths 125, 250, and 500, and correct repeated counting
  completed normally and failed only scaling at `+0.95`;
- problem 1395 was remotely Accepted as submission `2068858629`; its monotone
  rating tiers use 10, 20, and 40 soldiers, and correct triple enumeration
  completed normally and failed only scaling at `+1.17`;
- problem 1396 was remotely Accepted as submission `2068862234`; its stateful
  workloads use 60, 240, and 960 calls, and correct duration-list re-summing
  completed normally and failed only scaling at `+1.02` and `33.29x`;
- problem 1397 was remotely Accepted as submission `2068868699`; its bounded
  KMP digit-DP tiers use lengths 4, 8, and 16. Correct lexicographic enumeration
  completed normally and failed only scaling at `+2.94`; larger draft ranges
  were rejected because they reached the safety cap;
- problem 1398 was remotely Accepted as MySQL submission `2068872192`; its
  customer-and-order tiers use 24, 96, and 384 rows, and correct de-indexed
  correlated A/B/C checks completed normally and failed only scaling at
  `+0.54`;
- problem 1399 was remotely Accepted as submission `2068876229`; its digit-sum
  tiers use upper bounds 32, 64, and 128, and correct repeated group rescanning
  completed normally and failed only scaling at `+1.02` and `29.68x`;
- problem 1400 was remotely Accepted as submission `2068879728`; its repeated-
  character tiers use lengths 125, 500, and 2000, and correct repeated full-
  string counting completed normally and failed only scaling at `+0.98` and
  `34.65x`;
- problem 1401 was remotely Accepted as submission `2068886036`; it uses a
  strictly validated `asymptotic_optimality` certificate because constant-time
  closest-point geometry already matches the problem-level lower bound;
- problem 1402 was remotely Accepted as submission `2068889803`; correct
  repeated maximum selection completed normally and failed only scaling at
  `+0.32`;
- problem 1403 was remotely Accepted as submission `2068893384`; correct
  repeated maximum selection and removal completed normally and failed only
  scaling at `+0.47`;
- problem 1404 was remotely Accepted as submission `2068897433`; correct
  immutable binary-string simulation completed normally and failed only
  scaling at `+0.20`;
- problem 1405 was remotely Accepted as submission `2068903132`; its semantic
  validator accepts any longest valid happy string with the required character
  counts, and correct exhaustive memoization failed only scaling at `+2.18`
  and `490.28x`;
- problem 1406 was remotely Accepted as submission `2068907802`; correct
  absolute-score dynamic programming with repeated suffix copies completed
  normally and failed only scaling at `+0.22`;
- problem 1407 was remotely Accepted as MySQL submission `2068911553`; a
  correct de-indexed correlated aggregation completed normally and failed only
  scaling at `+0.40`;
- problem 1408 was remotely Accepted as submission `2068915174`; correct
  redundant full-answer recomputation completed normally and failed only
  scaling at `+1.37` and `11.16x`;
- problem 1409 was remotely Accepted as submission `2068923846`; correct
  permutation prefix replay completed normally and failed only scaling at
  `+1.22` and `37.20x`;
- problem 1410 was remotely Accepted as submission `2068931727`; correct
  redundant decoded-prefix rescanning completed normally and failed only
  scaling at `+0.26`; its live backend `question_id` is 1526;
- problem 1411 was remotely Accepted as submission `2068939568`; correct
  repeated row-history rebuilding completed normally and failed only scaling
  at `+0.30`;
- problem 1412 was remotely Accepted as MySQL submission `2069002090`; its
  live backend `question_id` is 1546, and a correct correlated-extrema query
  completed normally and failed only scaling at `+0.69`;
- problem 1413 is locally complete; correct repeated prefix recomputation
  failed only scaling at `+1.46` and `62.33x`, but remote verification is
  blocked by Electron credential decryption error `0x8009000B`;
- problem 1414 is locally complete; correct repeated Fibonacci-list scanning
  failed only scaling at `+0.41` and `68.27x`, but remote verification is
  blocked by the same credential error;
- problem 1415 is locally complete; correct ordered backtracking failed only
  scaling at `+1.72` and `104.48x`, but remote verification is blocked by
  the same credential error;
- problem 1416 is locally complete; correct unmemoized restoration
  backtracking failed only scaling at `+3.60` and `1345.45x`, but remote
  verification is blocked by the same credential error;
- problem 1417 is locally complete; its new semantic validator accepts any
  character-preserving letter-digit alternation, 114 focused tests pass, and
  correct repeated search and removal failed only scaling at `+0.85` and
  `21.10x`; remote verification is blocked by the credential error;
- problem 1418 is locally complete; correct per-cell order rescanning failed
  only scaling at `+1.13` and `42.03x`, but remote verification is blocked
  by the same credential error;
- problem 1419 is locally complete; correct per-frog stage tracking completed
  normally and failed only scaling at `+0.23`, but remote verification is
  blocked by the same credential error;
- problem 1420 is locally complete; correct direct smaller-maximum summation
  failed only scaling at `+0.35` and `9.40x`, but remote verification is
  blocked by the same credential error;
- problem 1421 is locally complete; a correct correlated NPV lookup completed
  normally and failed only scaling at `+0.33`, but remote verification is
  blocked by the same credential error;
- problem 1422 is locally complete; correct repeated split slicing and
  recounting failed only scaling at `+1.02` and `37.31x`, but remote
  verification is blocked by the same credential error;
- problem 1423 is locally complete; correct enumeration of every left/right
  card distribution failed only scaling at `+0.62` and `13.74x`, but
  remote verification is blocked by the same credential error;
- problem 1424 is locally complete; its sparse-coordinate diagonal benchmark
  replaces an invalid dense-square draft, and correct diagonal-by-diagonal row
  rescanning failed only scaling at `+1.06` and `44.55x`; remote
  verification is blocked by the same credential error;
- problem 1425 is locally complete; correct direct previous-window DP failed
  only scaling at `+0.69`, but remote verification is blocked by the same
  credential error;
- problem 1426 is locally complete; correct list-membership counting failed
  only scaling at `+0.83`, but remote verification is blocked by the same
  credential error;
- problem 1427 was remotely Accepted as submission `2069064960`; correct
  one-character-at-a-time shifting completed normally and failed scaling at
  `+0.61` and `76.05x`;
- problem 1428 was remotely Accepted as submission `2069069965`; the reusable
  `BinaryMatrix` judge adapter and regression were added, and correct per-row
  binary search completed within the 1000-query limit but failed scaling at
  `+0.45`;
- problem 1429 was remotely Accepted as submission `2069073389`; correct
  arrival-history rescanning completed normally and failed scaling at `+0.63`;
- problem 1430 was remotely Accepted as submission `2069077262`; correct
  root-to-leaf path materialization completed normally and failed scaling at
  `+0.86` and `28.31x`;
- problem 1431 was remotely Accepted as submission `2069079343`; its invalid
  zero-extra hidden case and legacy one-tier benchmark were replaced, and
  correct repeated `max` computation failed scaling at `+0.21`;
- problem 1432 was remotely Accepted as submission `2069082111`; its strict
  nine-digit bounded-domain certificate is backed by an independent digit-pair
  oracle over inputs 1 through 9999 plus upper-bound cases;
- problem 1433 was remotely Accepted as submission `2069084354`; correct
  insertion sorting completed normally and failed scaling at `+1.16` and
  `124.40x`;
- problem 1434 was remotely Accepted as submission `2069087010`; its inherited
  third sample was corrected from 8 to 11, and factorial backtracking completed
  normally and failed scaling at `+1.23`;
- problem 1435 was remotely Accepted as submission `2069089789`; correct
  correlated SQL completed normally and failed scaling at `+1.04` and
  `27.26x` while preserving all four duration bins;
- problem 1436 was remotely Accepted as submission `2069091570`; correct
  repeated starting-city scans completed normally and failed scaling at
  `+1.26` and `22.56x`;
- problem 1437 was remotely Accepted as submission `2069093475`; its largest
  tier was reduced after a safety-cap calibration, and correct all-pairs
  checking then completed normally and failed scaling at `+1.22` and
  `178.80x`;
- problem 1438 was remotely Accepted as submission `2069095512`; correct
  repeated min/max scans completed normally and failed scaling at `+0.65`;
- problem 1439 was remotely Accepted as submission `2069097610`; the reference
  was upgraded to a bounded pair-sum heap merge, and correct full cross-product
  sorting failed scaling at `+1.16`;
- problem 1440 was remotely Accepted as submission `2069099669`; correct
  correlated operand lookups completed normally and failed scaling at `+0.79`
  and `11.05x`;
- problem 1441 was remotely Accepted as submission `2069101763`; an optimized
  built-in membership candidate was explicitly rejected as an uncalibrated
  counterexample, while a correct explicit repeated target scan completed
  normally and failed scaling at `+0.93`;
- problem 1442 was remotely Accepted as submission `2069150164`; its linear
  matching-prefix aggregation passed alongside an independently structured
  linear implementation, while correct quadratic outer-endpoint enumeration
  completed normally and failed only scaling at `+1.14` and `65.26x`;
- problem 1443 was remotely Accepted as submission `2069151267`; its iterative
  postorder avoids recursion depth on legal chains, an independent linear
  leaf-pruning method passed, and correct per-apple ancestor walking completed
  normally and failed only scaling at `+0.97` and `67.58x`;
- problem 1444 was remotely Accepted as submission `2069152814`; its
  suffix-sum memoized DP preserves the directional giving semantics and exact
  `k`, an independent bottom-up DP passed, and correct per-state rectangle
  rescanning completed normally and failed only scaling at `+0.49` and
  `8.96x`. A slower draft that reached the safety cap was rejected as invalid
  calibration rather than counted as a complexity failure;
- problem 1445 was remotely Accepted as MySQL submission `2069155302`; its
  conditional aggregation passed alongside an independently structured linear
  aggregation, while correct correlated per-date lookups completed normally
  and failed only scaling at `+0.92` and `25.81x`;
- problem 1446 was remotely Accepted as submission `2069157201`; its one-pass
  run counter and an independent run-boundary scan passed, while correct
  quadratic run expansion completed normally and failed only scaling at
  `+1.32` and `135.98x`;
- problem 1447 was remotely Accepted as submission `2069158331`; its Euclidean
  GCD enumeration and an independently structured comprehension using the
  same complexity primitive passed, while correct trial-divisor enumeration
  completed normally and failed only scaling at `+1.23` and `29.82x`. A
  Python-level hand-written Euclid comparison that did not match the calibrated
  primitive was rejected rather than counted as same-class evidence;
- problem 1448 was remotely Accepted as submission `2069159432`; its iterative
  path-maximum DFS and an independent BFS passed, while correct full-path
  rescanning completed normally and failed only scaling at `+0.38`;
- problem 1449 was remotely Accepted as submission `2069160966`; its
  integer-length knapsack DP and an independent forward-state DP passed, while
  the prior correct string-valued DP completed normally and failed only
  scaling at `+0.40`;
- problem 1450 was remotely Accepted as submission `2069161957`; its direct
  interval predicate and an independent index scan passed, while correct
  time-unit simulation completed normally and failed only scaling at `+1.42`
  and `24.40x`;
- problem 1451 was remotely Accepted as submission `2069163111`; its stable
  key sort and an independently written stable key sort passed, while correct
  stable insertion completed normally and failed only scaling at `+1.67` and
  `438.29x`. The initial 2048-word insertion tier hit the safety cap and was
  replaced by legal 64/256/640 tiers; indexed tuple sorting and Python-level
  buckets with mismatched curves were rejected as same-class evidence;
- problem 1452 was remotely Accepted as submission `2069164103`; invalid
  duplicate-list cases were removed because the source guarantees distinct
  favorite-company sets. Two set-containment implementations passed, while
  correct list-membership checks completed normally and failed only scaling at
  `+1.02`;
- problem 1453 was remotely Accepted as submission `2069165700`; its angular
  sweep and an independently wrapped sweep passed, while correct direct
  pair-center enumeration completed normally and failed only scaling at
  `+0.68`;
- problem 1454 was remotely Accepted as MySQL submission `2069166953`; its
  gaps-and-islands query deduplicates login dates, and an independent `LAG`
  formulation passed, while correct correlated window counting completed
  normally and failed only scaling at `+1.19` and `65.43x`;
- problem 1455 was remotely Accepted as submission `2069168170`; its direct
  word-boundary scan and an independent linear split scan passed, while a
  correct implementation that repeatedly recounted preceding words completed
  normally and failed only scaling at `+0.81`;
- problem 1456 was remotely Accepted as submission `2069169780`; its fixed-
  width sliding window and an independent constant-space scan passed, while
  correct full-window recounting completed normally and failed only scaling at
  `+1.23` and `54.00x`;
- problem 1457 was remotely Accepted as submission `2069171315`; its iterative
  parity-mask DFS and an independent iterative traversal passed. Restoring the
  canonical `**Inputs**` marker repaired binary-tree fixture conversion, and
  correct explicit path reconstruction completed normally and failed only
  scaling at `+1.12` and `97.51x`;
- problem 1458 was remotely Accepted as submission `2069172396`; its rolling-
  row and full-table dynamic programs passed. A hidden order-sensitive case
  was corrected after validation exposed a better legal pairing, while correct
  predecessor rescanning completed normally and failed only scaling at `+2.32`
  and `73.07x`;
- problem 1459 was remotely Accepted as Premium MySQL submission `2069173889`;
  its direct self-join and an independent cross join passed on output-sensitive
  all-valid-pair tiers, while a correct correlated full-table rescan completed
  normally and failed only scaling at `+0.56`;
- problem 1460 was remotely Accepted as submission `2069175019`; its fixed-
  domain balance array and an independent frequency map passed. Incremental
  nonzero-balance tracking removed a fixed-scan calibration artifact, while
  correct repeated list removal completed normally and failed only scaling at
  `+0.51`;
- problem 1461 was remotely Accepted as submission `2069176461`; its rolling
  bitmask and an independent rolling integer set passed. A native substring-
  search draft was rejected as an uncalibrated counterexample, while correct
  exhaustive code-by-window scanning completed normally and failed only
  scaling at `+1.12` and `33.30x`;
- problem 1462 was remotely Accepted as submission `2069177679`; its reverse-
  topological set closure and an independent bitset closure passed, while
  correct per-query DFS completed normally and failed only scaling at `+1.42`
  and `33.59x`;
- problem 1463 is locally complete. Its rolling joint-column dynamic program
  passed scaling at extra exponent `+0.01`; correct redundant recomputation
  returned every expected output, completed normally, and failed only scaling
  at `+1.16` and `12.57x`. Remote verification is blocked because Chrome is
  not running and policy requires explicit launch confirmation;
- problem 1464 is locally complete. Its one-pass two-maxima scan passed at
  `+0.00`; correct pair enumeration returned every expected output, completed
  normally, and failed only scaling at `+1.21` and `34.11x`. It has the same
  Chrome launch blocker;
- problem 1465 is locally complete. Its sort-and-gap scan passed at `-0.01`;
  correct predecessor rescanning returned every expected output, completed
  normally, and failed only scaling at `+1.04` and `21.36x`. It has the same
  Chrome launch blocker;
- problem 1466 is locally complete. Its direction-marked iterative tree
  traversal passed at `+0.01`; correct repeated frontier scans returned every
  expected output, completed normally, and failed only scaling at `+0.99` and
  `15.47x`. It has the same Chrome launch blocker;
- problem 1467 is locally complete. Its exact rolling combinatorial DP over
  ball count and distinct-color difference passed at `+0.01`; correct
  allocation-vector enumeration returned every float-validated answer,
  completed normally, and failed only scaling at `+2.78` and `51.03x`. It has
  the same Chrome launch blocker;
- problem 1468 is locally complete. Its grouped company-maximum scan plus join
  passed SQL scaling at `+0.01`; a correct correlated maximum query returned
  every expected row, completed normally, and failed only scaling at `+0.70`.
  It has the same Chrome launch blocker;
- problem 1469 is locally complete. Its parent-local iterative tree traversal
  passed at `+0.00`; correct repeated parent searches returned every unordered
  result, completed normally, and failed only scaling at `+0.90` and `14.89x`.
  It has the same Chrome launch blocker;
- problem 1470 is locally complete. Its direct two-half interleaving passed at
  `+0.01`; correct explicit prefix reconstruction returned every expected
  output, completed normally, and failed only scaling at `+0.84` and `10.91x`.
  The audit also caught and prompted repair of a 54-word Goal narrative before
  completion. It has the same Chrome launch blocker;
- problem 1471 is locally complete. Its sorted two-pointer endpoint selection
  passed every correctness case and scaling with a flat `-0.00` extra exponent
  and `1.01x` largest-tier ratio. Correct repeated strongest-occurrence
  scanning completed normally, returned every expected multiset, and failed
  only scaling at `+1.42` and `192.58x`. An initial 256/1024/4096
  calibration was rejected because the slower implementation reached the
  Python step guard; the final legal 32/128/512 tiers preserve the 16x span
  while producing a genuine scaling verdict. It has the same Chrome launch
  blocker;
- problem 1472 is locally complete. Its valid-prefix array with independent
  current and logical-end indices passed every operation sequence and scaling
  at `-0.01` with a `0.98x` largest-tier ratio. Correct explicit retained-
  prefix copying completed normally, returned every expected result, and
  failed only scaling at `+0.97` and `22.97x`. It has the same Chrome
  launch blocker;
- problem 1473 is locally complete. Its rolling neighborhood-and-last-color
  dynamic program uses per-neighborhood smallest and second-smallest
  predecessor colors, passed every case, and passed scaling at `-0.01` with
  a `1.00x` largest-tier ratio. The correct standard transition that scans
  all predecessor colors completed normally, returned every expected optimum,
  and failed only scaling at `+0.93`. Validation also exposed and repaired one
  hand-authored hidden expected cost from `6` to the independently brute-
  forced optimum `3`. It has the same Chrome launch blocker;
- problem 1474 is locally complete. Its one-pass in-place linked-list rewiring
  passed every case and scaling at `-0.01` with a `0.99x` largest-tier
  ratio. Correct positional rescanning completed normally, returned every
  expected retained chain, and failed only scaling at `+1.21` and `91.03x`.
  LeetCode's anonymous Premium API withheld prose but confirmed backend ID
  `1618`, the `deleteNodes` signature, and the first two official testcase
  inputs. It has the same Chrome launch blocker;
- problem 1475 is locally complete. Its unresolved-index monotonic stack
  passed every case and scaling at `-0.00` with a `1.00x` largest-tier
  ratio. Correct rightward scanning completed normally, returned every final
  price, and failed only scaling at `+1.37` and `104.49x`. It has the same
  Chrome launch blocker;
- problem 1476 is locally complete. Its object-owned matrix with direct
  inclusive cell assignments passed every operation trace and scaling at
  `-0.01` with a `1.00x` largest-tier ratio. Correct full-matrix copying
  before each update completed normally, returned every expected trace, and
  failed only scaling at `+1.04` and `13.65x`. It has the same Chrome launch
  blocker;
- problem 1477 is locally complete. Its positive-value sliding window with
  shortest-prefix partner lengths passed every case and scaling at `+0.00`
  with a `1.00x` largest-tier ratio. Correct target-interval enumeration
  completed normally, returned every optimum, and failed only scaling at
  `+1.16` and `136.86x`. It has the same Chrome launch blocker;
- problem 1478 is locally complete. Its median-pair interval-cost recurrence
  plus rolling mailbox-partition DP passed every case and scaling at `+0.01`
  with a `1.00x` largest-tier ratio. Correct cubic interval re-summing
  completed normally, returned every optimum, and failed only scaling at
  `+0.32`. One hand-authored cluster fixture was independently recalculated
  from `13` to the true optimum `11` before runtime validation. It has the
  same Chrome launch blocker;
- problem 1479 is locally complete. Its SQLite conditional-aggregation query
  and separate native MySQL weekday pivot returned every expected category,
  including unsold categories, on the official and hidden relational cases.
  Three 8/32/128 category tiers exercise the one-pass grouped join against the
  correlated-subquery alternative. The source-native route does not emit a
  measured scaling verdict because this legacy metadata marks the SQL package
  non-runnable, but the authored benchmark passes structural audit. It has the
  same Chrome launch blocker;
- problem 1480 is locally complete. Its carried-prefix implementation passed
  every correctness case and all 32/128/512 benchmark tiers with an extra
  growth exponent of `-0.00` and a `1.00x` largest-tier ratio. The correct
  quadratic prefix-recomputation candidate completed normally, returned every
  expected running sum, and failed only scaling at `+1.44` and `132.50x`. It
  has the same Chrome launch blocker;
- problem 1481 is locally complete. Its frequency-counting and ascending-cost
  greedy implementation passed all samples, the visible trial, hidden boundary
  cases, and the 32/128/512 benchmark tiers at `+0.01` with a `1.01x`
  largest-tier ratio. The correct repeated-frequency-count candidate completed
  normally, returned every optimum, and failed only scaling at `+1.48` and
  `470.80x`. It has the same Chrome launch blocker;
- problem 1482 is locally complete. Its monotone-feasibility binary search
  passed all samples, the visible adjacency trial, hidden boundary cases, and
  the legal 8/32/128 tiers at `-0.00` with a `0.99x` largest-tier ratio. The
  correct candidate that scans sorted distinct bloom days completed normally,
  returned every minimum day, and failed only scaling at `+0.81` and `12.00x`.
  The smaller tiers avoid a safety-cap failure while retaining a 16x span. It
  has the same Chrome launch blocker;
- problem 1483 is locally complete. Its binary-lifting table and stateful
  operation wrapper passed the official sequence, visible chain trial, hidden
  tree-shape cases, and the legal 8/32/128 tiers at `-0.08` with a `0.74x`
  largest-tier ratio. Correct direct parent walking completed normally,
  returned every query answer, and failed only scaling at `+0.67`. It has the
  same Chrome launch blocker;
- problem 1484 is locally complete. Its SQLite distinct-pair aggregation and
  separate native MySQL ordered `GROUP_CONCAT` artifact cover duplicate sale
  rows, independent date groups, and lexicographic product order. The grouped
  query passed all five correctness cases and the legal 8/32/128 tiers at
  `+0.01` with a `0.99x` largest-tier ratio. Correct correlated subqueries
  completed normally, returned every expected relation, and failed only
  scaling at `+0.61` and `8.69x`. It has the same Chrome launch blocker;
- problem 1485 is locally complete. Its documented app contract explicitly
  distinguishes encoded relationship equivalence from native object identity.
  The linear encoded clone passed all official, visible, hidden, and legal
  16/64/256 tiers at `-0.04` with a `0.89x` largest-tier ratio. Correct linear
  target-index searching completed normally, returned every relationship, and
  failed only scaling at `+1.32` and `53.05x`. The separate native artifact
  performs an identity-map `Node` to `NodeCopy` graph clone. It has the same
  Chrome launch blocker;
- problem 1486 is locally complete. Its constant-time parity split and
  four-case prefix-XOR formula passed all cases and the legal 64/256/1000 tiers
  at `+0.00` with a `0.99x` largest-tier ratio. Direct linear XOR accumulation
  completed normally, returned every result, and failed only scaling at
  `+0.51`. It has the same Chrome launch blocker;
- problem 1487 is locally complete. Its next-suffix hash-map invariant covers
  literal parenthesized names, preoccupied gaps, generated-name collisions,
  and nested suffixes. It passed all cases and the legal 16/64/256 tiers at
  `+0.00` with a `1.00x` largest-tier ratio. Correct suffix searching that
  restarts at one completed normally, returned every exact assigned name, and
  failed only scaling at `+1.18` and `39.34x`. It has the same Chrome launch
  blocker;
- problem 1488 is locally complete. Its future-occurrence queues, live-deadline
  map, and earliest-deadline heap correctly handle alternate valid schedules,
  stale heap entries after refill, unusable early dry days, and impossible
  sequences. It passed all cases and the legal 64/256/1024 tiers at `-0.00`
  with a `0.93x` largest-tier ratio. Correct linear dry-day scanning completed
  normally, produced valid schedules for every feasible case, and failed only
  scaling at `+0.75`. It has the same Chrome launch blocker;
- problem 1489 is locally complete. Its equal-weight component contraction and
  Tarjan multigraph bridge classification run in $O(E \log E)$ and correctly
  handle cheaper internal paths, parallel contracted edges, mixed bridge/cycle
  groups, and original edge indices. A new
  `ordered_groups_unordered_items` validator preserves the critical versus
  pseudo-critical category positions while accepting any index order within
  each category, with focused regression coverage. The reference passed all
  cases and the legal 8/32/128 tiers at `-0.00` with a `0.98x` largest-tier
  ratio. Correct exclude/force Kruskal completed normally and failed only
  scaling at `+1.08` and `48.76x`. It has the same Chrome launch blocker;
- problem 1490 is locally complete. Its explicit stack carries corresponding
  original/copy N-ary node pairs, allocates every child exactly once, and
  preserves ordered child lists without recursion-depth risk or an unnecessary
  identity map. The reference passed every correctness case and the legal
  625/2500/10000 wide-tree tiers at `-0.00` with a `1.00x` largest-tier
  ratio. Correct repeated child-list concatenation completed normally, returned
  every exact cloned tree, and failed only scaling at `+0.43`. It has the
  same Chrome launch blocker;
- problem 1491 is locally complete. Its one-pass sum/minimum/maximum aggregation
  returns the average after removing exactly the two unique extremes in
  $O(N)$ time and $O(1)$ auxiliary space. Because the official domain caps
  $N$ at 100, the package uses a strict `bounded_domain` certificate rather
  than pretending optimized sorting can be distinguished by stable scaling.
  An independent sort-and-slice oracle checks every legal length from 3 through
  100, varied orders, value boundaries, and fractional results. The certificate
  suite passed 18 tests and 27 certificate-route subtests. It has the same
  Chrome launch blocker;
- problem 1492 is locally complete. Its two integer-square-root scans enumerate
  small divisors upward and paired large divisors upward via a reverse scan,
  skip the duplicate square root, and use $O(1)$ auxiliary space. It passed
  all cases and the legal prime 61/251/997 tiers at `+0.00` with a `1.01x`
  largest-tier ratio. Correct linear divisor enumeration completed normally,
  returned every answer, and failed only scaling at `+0.41`. It has the same
  Chrome launch blocker;
- problem 1493 is locally complete. Its at-most-one-zero sliding window encodes
  the mandatory deletion as `right - left`, covering all-ones, all-zeros,
  boundary-zero, and repeated-shrink cases in $O(N)$ time and $O(1)$ space.
  It passed all cases and the legal 64/256/1024 repeated-run tiers at `-0.00`
  with a `1.00x` largest-tier ratio. A direct nested-loop draft was rejected
  as invalid calibration after reaching the safety cap; a correct quadratic
  try-every-deletion implementation using finishable built-in rescans returned
  every expected answer and failed only scaling at `+0.88` and `16.42x`.
  It has the same Chrome launch blocker;
- problem 1494 is locally complete. Its completed-course-mask DP precomputes
  prerequisite masks, takes all available courses when capacity does not bind,
  and generates only exact-$k$ combinations when selection matters. A
  no-prerequisite closed form avoids unnecessary exponential work on the
  official 11-course sample. The reference passed all cases and the
  64/256/1024 state-space tiers at `-0.01` with a `0.99x` largest-tier
  ratio. A correct full-universe subset baseline completed normally and failed
  only scaling at `+0.85` and `22.50x`. It has the same Chrome launch
  blocker;
- problem 1495 is locally complete. Its portable SQL joins schedule and content
  metadata, applies independent kid/movie predicates, uses the half-open June
  timestamp interval, and deduplicates titles. It passed all cases and the
  32/128/512 content-row tiers at `+0.01` with a `1.00x` largest-tier
  ratio. A correct correlated `EXISTS` formulation completed normally,
  returned every title, and failed only scaling at `+0.63`. It is paid SQL,
  remote submission is standing-authorized, and it has the same Chrome launch
  blocker;
- problem 1496 is complete and remotely verified as submission `2069341486`.
  Its 625/2500/10000 straight-path tiers passed both linear hash-set
  implementations. Correct list membership returned every answer and failed
  only scaling at `+0.85` with a `22.29x` largest-tier ratio;
- problem 1497 is complete and remotely verified as submission `2069349686`.
  Its sparse remainder-count implementation handles the legal maximum divisor
  without exhausting the ordinary-case step guard. Correct repeated
  complement search completed the 256/512/1024 tiers and failed only scaling
  at `+1.26` and `104.02x`;
- problem 1498 is complete and remotely verified as submission `2069354834`.
  Its sort-and-two-pointer counting passed the 128/256/512 tiers. Correct
  restarted right-end search returned every modulo count and failed only
  scaling at `+1.15` and `106.60x`;
- problem 1499 is complete and remotely verified as submission `2069359603`.
  Its monotonic deque and an independent linear queue both passed the
  128/256/512 all-eligible tiers. Correct all-pairs enumeration completed
  normally and failed only scaling at `+1.11` and `88.02x`;
- problem 1500 is complete and remotely verified as submission `2069377610`.
  Its sparse bidirectional ownership maps and reusable-ID min-heap passed the
  16/64/256 high-ID-reuse tiers. Correct linear ID search returned every
  output and failed only scaling at `+0.93` with a `22.65x` largest ratio;
- problem 1501 is complete and remotely verified as MySQL submission
  `2069382920`. Its accepted endpoint-expansion query anchors the app-local
  SQLite query, correctness cases, and 32/128/512 country tiers. A correct
  correlated per-country rescan returned every result and failed only scaling
  at `+0.87` with an `11.74x` largest ratio;
- problem 1502 is complete and remotely verified as submission `2069390999`.
  Its accepted linear spacing-and-hash-set source anchors the app-local
  solution and 64/256/1000 descending-progression tiers. An independently
  structured set-congruence implementation passed; correct repeated list
  membership returned every answer and failed only scaling at `+0.45`;
- problem 1503 is complete and remotely verified as submission `2069396697`.
  Its collision/pass-through equivalence anchors a constant-space linear scan
  and 32/128/512 dense-occupancy tiers. The independent native-style extrema
  implementation passed; correct second-by-second pass-through simulation
  returned every answer and failed only scaling at `+1.42` with a `233.62x`
  largest ratio;
- problem 1504 is complete and remotely verified as submission `2069404571`.
  Its accepted histogram/minimum-sum monotonic stack anchors the app-local
  source and 5/20/80 all-one square tiers. An independent index-stack dynamic
  program passed; the correct per-row leftward histogram scan returned every
  count and failed only scaling at `+0.78` with a `9.06x` largest ratio;
- problem 1505 is complete and remotely verified as submission `2069411408`.
  Its accepted digit-position queues and Fenwick tree source anchors the
  app-local solution and 64/256/1024 repeated reverse-digit tiers. An
  independently structured Fenwick implementation passed; correct greedy
  removal from a mutable list returned every answer and failed only scaling
  at `+0.19`;
- problem 1506 is complete and remotely verified as submission `2069419267`.
  Its accepted XOR cancellation source anchors the constant-space app-local
  solution and 128/512/2048 wide-tree tiers with the root last. An independent
  child-value hash-set implementation passed; correct repeated membership in
  the flattened child list returned every root and failed only scaling at
  `+0.46`;
- problem 1507 is complete and remotely verified as submission `2069426510`.
  Its accepted fixed-format parser anchors the app-local source and ten
  ordinary cases. Because every valid source input has at most thirteen
  characters, a strict `bounded_domain` certificate replaces artificial
  scaling; its regression exhaustively checks every valid date from 1900
  through 2100 with the proper ordinal suffix;
- problem 1508 is complete and remotely verified as submission `2069432165`.
  Its accepted threshold counting and prefix-of-prefix source anchors the
  app-local solution and 64/250/1000 all-rank tiers. An independently derived
  sliding aggregate passed; correct materialization and sorting returned every
  answer and failed only scaling at `+0.84`;
- problem 1509 is complete and remotely verified as submission `2069440199`.
  Its accepted fixed-size extreme heaps anchor the linear app-local source and
  64/256/1024 shuffled-consecutive tiers. An independent bounded sorted-list
  scan passed; correct retained-interval enumeration returned every answer and
  failed only scaling at `+1.14` with a `46.17x` largest ratio;
- problem 1510 is complete and remotely verified as submission `2069447412`.
  Its accepted bottom-up winning-state recurrence anchors the app-local source
  and 128/512/4096 pile-size tiers. An independent descending-square recurrence
  passed; correct enumeration of every possible removal returned every answer
  and failed only scaling at `+0.26`;
- problem 1511 is complete and remotely verified as MySQL submission
  `2069457310`. Its accepted joined conditional aggregation anchors the
  app-local SQL and 32/128/512 customer tiers. An independent monthly CTE
  passed; correct correlated monthly subqueries returned every row and failed
  only scaling at `+0.82` with a `12.55x` largest ratio;
- problem 1512 is complete and remotely verified as submission `2069465467`.
  Its accepted streaming frequency invariant anchors the app-local source and
  legal 6/25/100 all-equal tiers. An independent frequency-combination method
  passed; correct direct pair enumeration returned every answer and failed
  only scaling at `+1.04` with a `20.65x` largest ratio;
- problem 1513 is complete and remotely verified as submission `2069472420`.
  Its accepted right-endpoint run accumulation anchors the app-local source and
  64/256/1024 all-one tiers. An independent triangular run calculation passed;
  correct prefix-pair enumeration returned every answer and failed only
  scaling at `+1.29` with a `378.80x` largest ratio;
- problem 1514 is complete and remotely verified as submission `2069479831`.
  Its accepted max-probability Dijkstra source anchors the app-local adapter
  and 16/64/256 reverse-ordered chain tiers. An independent negative-log
  Dijkstra passed; correct Bellman-Ford relaxation returned every answer and
  failed only scaling at `+1.11` with a `46.59x` largest ratio;
- problem 1515 is complete and remotely verified as submission `2069487983`.
  Its accepted nested ternary search uses seventy iterations per coordinate;
  the app-local adapter uses forty-five iterations per coordinate to remain
  within the traced execution budget while retaining better than the required
  precision. It and an independent shrinking-step hill climb passed the legal
  4/16/48 balanced-corner tiers. Correct over-refinement with
  `45 + floor(n / 2)` iterations returned every answer and failed only scaling
  at `+0.31`;
- problem 1516 is complete and remotely verified as submission `2069506271`.
  Its accepted parent-map pointer rewiring anchors the app-local ordered-record
  adapter, and the two forms matched on 2,000 randomized trees. It and an
  independent descendant-set traversal passed the legal 32/128/512 deep-chain
  tiers. Correct repeated parent rescans returned every adjusted tree and
  failed only scaling at `+1.00` with a `31.42x` largest ratio;
- problem 1517 is complete and remotely verified as MySQL submission
  `2069514846`. Its accepted case-sensitive anchored regular expression
  anchors the app-local SQLite glob predicate, and the two semantics matched
  on 10,000 randomized addresses. It and an independent parsed-prefix query
  passed the 64/256/1024 user tiers. A correct grouped cross join returned
  every qualifying user and failed only scaling at `+1.30` with a `205.64x`
  largest ratio;
- problem 1518 is complete and remotely verified as submission `2069522926`.
  Its accepted constant-time net-empty formula matched direct simulation for
  all 9,900 legal input pairs. A strict `bounded_domain` certificate records
  the complete finite domain and the exhaustive replacement regression;
- problem 1519 is complete and remotely verified as submission `2069527776`.
  Its accepted iterative enter/exit counter-difference traversal matched a
  brute subtree oracle on 1,500 randomized trees and passed the 32/128/512
  all-equal chain tiers with an independent postorder frequency-vector method.
  Correct per-subtree traversal returned every count and failed only scaling
  at `+0.99` with a `54.00x` largest ratio;
- problem 1520 is complete and remotely verified as submission `2069533580`.
  Its accepted first/last-occurrence closure greedy matched interval dynamic
  programming for every `abc` string through length eight. It and an
  independent sorted-interval greedy passed the 32/128/512 full-closure tiers;
  correct repeated whole-string rescans returned the optimum and failed only
  scaling at `+0.92` with a `29.78x` largest ratio;
- problem 1521 is complete and remotely verified as submission `2069538119`.
  Its accepted distinct-ending-AND state compression matched direct subarray
  enumeration on 5,000 randomized arrays. It and an independent sorted-state
  implementation passed the 32/128/512 no-early-exit tiers; correct all-range
  enumeration returned the minimum difference and failed only scaling at
  `+0.93` with a `23.56x` largest ratio;
- problem 1522 is complete and remotely verified as submission `2069543443`.
  Its accepted iterative postorder-height source matched two-sweep diameter on
  3,000 randomized N-ary trees. It and an independent two-sweep implementation
  passed the recalibrated 16/64/256 chain tiers; correct all-source distance
  traversal completed every tier and failed only scaling at `+1.05` with a
  `78.03x` largest ratio;
- problem 1523 is complete and remotely verified as submission `2069547887`.
  Its accepted prefix-count formula matched direct counting over every interval
  through 100 and 10,000 randomized legal intervals. It and an independent
  endpoint-parity formula passed the legal 1000/4000/16000 width tiers; correct
  direct enumeration completed every tier and failed only scaling at `+0.96`
  with a `137.24x` largest ratio;
- problem 1524 is complete and remotely verified as submission `2069552475`.
  Its accepted opposite-parity prefix product matched direct enumeration on
  5,000 randomized arrays. It and an independent ending-state recurrence
  passed the 32/128/512 alternating-parity tiers; correct nested subarray
  enumeration completed every tier and failed only scaling at `+1.23` with a
  `183.50x` largest ratio;
- problem 1525 is complete and remotely verified as submission `2069555850`.
  Its accepted incremental left-set/right-frequency scan matched direct split
  checking on 10,000 randomized strings. It and independent prefix/suffix
  distinct-count arrays passed the 64/256/1024 repeated-alphabet tiers; correct
  per-boundary set rebuilding completed every tier and failed only scaling at
  `+0.54`;
- problem 1526 is complete and remotely verified as submission `2069559814`.
  Its accepted positive-rise layer count matched per-height run counting on
  5,000 randomized targets. It and an independent reverse drop-count scan
  passed the 16/64/256 unique-height zigzag tiers; correct compressed
  height-band run counting completed every tier and failed only scaling at
  `+1.45` with a `292.79x` largest ratio;
- problem 1527 is complete and remotely verified as MySQL submission
  `2069565144`. Its accepted two-boundary `LIKE` filter anchors the app-local
  deterministic SQLite query and the 64/256/1024 all-matching patient tiers.
  An independent prepended-boundary filter passed; a correct grouped cross
  join returned every qualifying row and failed only scaling at `+1.32` with
  a `242.50x` largest ratio;
- problem 1528 is complete and remotely verified as submission `2069574023`.
  Its accepted direct destination placement matched a sorted-pair oracle on
  5,000 randomized legal permutations. It and an independent indexed
  placement loop passed the legal 6/25/100 reverse-permutation tiers; correct
  repeated Python scans for each destination completed every tier and failed
  only scaling at `+1.00` with an `18.57x` largest ratio;
- problem 1529 is complete and remotely verified as submission `2069578266`.
  Its accepted effective-bit transition scan matched breadth-first minimum
  distances for every binary target through length eight. It and an
  independent adjacent-transition count passed the 32/128/512 alternating
  tiers; correct explicit suffix simulation completed every tier and failed
  only scaling at `+1.34` with a `151.64x` largest ratio;
- problem 1530 is complete and remotely verified as submission `2069583223`.
  Its accepted iterative bounded-distance histogram matched a brute-force
  oracle on 1,960 randomized trees and handled a legal 1,024-node chain. It
  and an independent recursive histogram passed the 31/127/511 complete-tree
  tiers; correct all-leaf-pairs root-path comparison completed every tier and
  failed only scaling at `+0.88`;
- problem 1531 is complete and remotely verified as submission `2069589037`.
  Its accepted first-run dynamic program matched exhaustive deletion on 1,000
  randomized strings. It and an independent memoized formulation passed the
  legal 8/16/32 interleaved tiers; a correct interval-rescan dynamic program
  with a uniform-string base case completed every tier and failed only scaling
  at `+0.34`;
- problem 1532 is complete and remotely verified as MySQL submission
  `2069600087`. Its accepted partitioned row-number query anchors the app-local
  SQLite form and the 64/256/1024 single-customer order tiers. An independent
  rank window passed; a correct correlated newer-order count completed every
  tier and failed only scaling at `+1.10` with a `31.65x` largest ratio;
- problem 1533 is complete and remotely verified as submission `2069607131`.
  Its accepted equal-half search matched all exceptional positions through
  length 1,000 and 5,000 randomized legal arrays. The app-local hidden
  `ArrayReader` enforces the 20-call limit, including a 500,000-element
  boundary regression. A strict `asymptotic_optimality` certificate records
  the matching $\Omega(\log n)$ information lower bound and $O(\log n)$ upper
  bound, because the query cap excludes an honest slower scaling class;
- problem 1534 is complete and remotely verified as submission `2069620174`.
  Its accepted pruned cubic enumeration matched an independent combinations
  oracle on 5,000 randomized arrays. It and a separate combinations
  implementation passed the legal 25/50/100 all-equal tiers; a correct
  per-triplet sixteen-fold array-materialization control completed every tier
  and failed only scaling at `+0.20`;
- problem 1535 is complete and remotely verified as submission `2069627756`.
  Its accepted champion scan matched literal deque simulation on 5,000
  randomized games. It and an independent maximum-aware scan passed the
  32/128/512 increasing tiers with legal `k = n^2`; correct deque simulation
  with a two-element base case completed every tier and failed only scaling at
  `+1.36` with a `397.96x` largest ratio;
- problem 1536 is complete and remotely verified as submission `2069634458`.
  Its accepted trailing-zero capacity greedy matched adjacent-swap BFS on
  2,100 randomized grids. It and an independent stable-selection method passed
  the legal 25/100/200 reverse-capacity tiers; correct physical-row simulation
  with fixed eight-fold snapshots completed every tier and failed only scaling
  at `+0.19`;
- problem 1537 is complete and remotely verified as submission `2069645143`.
  Its Accepted two-pointer score merge matched all official examples and an
  exhaustive-path oracle on 5,000 randomized array pairs. It and an
  independently structured segment accumulator passed the legal 64/256/1024
  disjoint interleaved tiers; a correct repeated linear-membership method
  completed every tier and failed only scaling at `+1.09` with a `94.14x`
  largest ratio;
- problem 1538 is complete and remotely verified as Premium submission
  `2069658953`. Its Accepted relative-query classifier passed every binary
  array through length 12, 1,000 randomized arrays, and maximum-length
  boundary checks. The app-local hidden `ArrayReader` enforces the exact
  distribution API and $2n$ query cap, while semantic validation accepts any
  majority index. The Accepted implementation and an independent balance
  formulation passed the legal 65/257/1025 alternating tiers; correct
  256-fold proportional snapshot work preserved the legal $n$ queries,
  completed every tier, and failed only scaling at `+0.73` with a `9.23x`
  largest ratio;
- problem 1539 is complete and remotely verified as submission `2069668925`.
  Its Accepted missing-count binary search matched exhaustive small
  combinations and 10,000 randomized legal inputs. It and an independent
  upper-bound search passed the legal 64/256/1000 dense-prefix tiers with
  maximum `k`; the correct linear rank-adjustment scan completed every tier
  and failed only scaling at `+0.53`;
- problem 1540 is complete and remotely verified as submission `2069674585`.
  Its Accepted residue scheduler matched exhaustive small strings and 20,000
  randomized schedules. It and an independent maximum-occurrence formulation
  passed the legal 32/128/384 repeated-shift tiers; the correct prefix-rescan
  scheduler completed every tier and failed only scaling at `+1.24` with a
  `96.01x` largest ratio;
- problem 1541 is complete and remotely verified as submission `2069680468`.
  Its Accepted outstanding-close greedy matched exhaustive balanced
  supersequences through length eight and 20,000 randomized token scans. It
  and an independent token-consumption formulation passed the legal
  1024/8192/65536 all-closing tiers; correct snapshotting literal list repair
  completed every tier and failed only scaling at `+0.60` with a `24.69x`
  largest ratio;
- problem 1542 is complete and remotely verified as submission `2069688798`.
  Its Accepted ten-bit prefix-parity scan matched every ternary string through
  length nine and 10,000 randomized decimal strings. It and an independent
  earliest-mask map passed the legal 20/80/320 repeated-decimal tiers; the
  correct full substring parity scan completed every tier and failed only
  scaling at `+0.97` with a `16.14x` largest ratio;
- problem 1543 is complete and remotely verified as MySQL submission
  `2069695334`. The SQLite adapter anchored to that Accepted query and an
  independent normalized CTE passed all ten correctness cases and the legal
  16/64/256 tiers. A correct correlated normalized-product/month recount
  completed every tier and failed only scaling, with relative runtime ratios
  of `2.60x`, `13.27x`, and `82.52x`;
- problem 1544 is complete and remotely verified as submission `2069702856`.
  Its live backend `question_id` is `1666`. The Accepted stack and an
  independent ASCII-case stack agreed with exhaustive restart reduction over
  every `aAbB` string through length eight and passed the legal 16/48/96
  nested-cancellation tiers. Correct restart-and-splice reduction completed
  every tier and failed only scaling at `+0.74`, with a `4.47x` largest ratio;
- problem 1545 is complete and remotely verified as submission `2069708049`.
  Its Accepted recursive symmetry lookup passed every position through level
  seven, while an independent iterative reflection passed all authored cases
  and the legal 4/10/20 level tiers. Correct full-string construction using
  native translation completed every tier and failed only scaling at `+1.30`,
  with an `8.81x` largest ratio;
- problem 1546 is complete and remotely verified as submission `2069713462`.
  Its live backend `question_id` is `1649`. The Accepted earliest-finish
  prefix-set greedy matched exhaustive dynamic programming for every ternary
  array through length seven. It and an independent prefix-map DP passed the
  legal 32/128/512 all-one tiers; the correct interval DP completed every tier
  and failed only scaling at `+1.30`, with a `168.62x` largest ratio;
- problem 1547 is complete and remotely verified as submission `2069720258`.
  Its live backend `question_id` is `1669`. The Accepted bottom-up interval DP
  matched exhaustive cut-order search for all tested subsets through stick
  length nine. It and an independent memoized recurrence passed the legal
  6/12/24-cut tiers; the correct quartic transition evaluator completed every
  tier and failed only scaling at `+0.89`, with a `6.24x` largest ratio;
- problem 1548 is complete and remotely verified as submission `2069726269`.
  Its live backend `question_id` is `1687`. The Accepted layered graph DP
  passed 1,400 randomized connected instances. A new semantic validator accepts
  any legal minimum-mismatch path and rejects invalid or suboptimal paths. The
  Accepted source and an independent edge-relaxation DP passed the legal
  3/6/12 target-length tiers; correct exhaustive walk enumeration completed
  every tier and failed only scaling at `+3.13`, with an `84.08x` largest ratio;
- problem 1549 is complete and remotely verified as MySQL submission
  `2069733378`. Its live backend `question_id` is `1688`. The Accepted
  `DENSE_RANK` query and an independent grouped-maximum join passed all ten
  correctness cases and the legal 64/256/1024 order tiers. A correct correlated
  maximum query completed every tier and failed only scaling at `+1.13`, with
  a `34.61x` largest ratio;
- problem 1550 is complete and remotely verified as submission `2069738369`.
  Its live backend `question_id` is `1293`. The Accepted streak scan matched
  every parity pattern through length ten. It and an independent constant-window
  scan passed the legal 64/256/1000 all-even tiers; correct prefix rescanning
  completed every tier and failed only scaling at `+0.40`, with a `4.13x`
  largest ratio;
- problem 1551 is complete and remotely verified as submission `2069743661`.
  Its live backend `question_id` is `1674`. The Accepted closed form matched
  direct deficit sums for every legal `n` through 10000. It and an independent
  half-product formula passed the legal 625/2500/10000 tiers; correct direct
  summation completed every tier and failed only scaling at `+0.81`, with a
  `23.09x` largest ratio;
- problem 1552 is complete and remotely verified as submission `2069747390`.
  Its live backend `question_id` is `1675`. The Accepted binary search matched
  exhaustive placement for all tested subsets of up to seven baskets. It and
  an independent tight-bound search passed the legal 16/64/256 all-basket
  tiers; correct restart-scan feasibility completed every tier and failed only
  scaling at `+1.16`, with a `41.59x` largest ratio;
- problem 1553 is complete and remotely verified as submission `2069752628`.
  Its live backend `question_id` is `1676`. The Accepted memoized recurrence
  matched bottom-up DP for every `n` through 10000. It and an independent
  cached recurrence passed the legal 127/2047/32767 tiers; correct unmemoized
  recursion completed every tier and failed only scaling at `+0.58`, with a
  `33.57x` largest ratio;
- problem 1554 is complete and remotely verified as submission `2069759643`.
  Its live backend `question_id` is `1697`. Submission `2069758383` exposed
  `O(q*l)` retained exact signatures as a memory-limit failure, and the
  column-wise exact-integer revision `2069758915` then timed out. The Accepted
  source uses column-wise double rolling hashes with exact collision
  verification; it passed bounded exhaustive and 10,000 randomized dictionaries.
  It and an independent prefix/suffix-ID method passed the legal 16/64/256-word
  tiers; correct pairwise Hamming comparison completed every tier and failed
  only scaling at `+0.78`;
- problem 1555 is complete and remotely verified as MySQL submission
  `2069766835`. Its live backend `question_id` is `1702`. The Accepted signed
  flow aggregation and an independent dual-aggregate query passed all ten
  correctness cases and the legal 32/128/512 user-and-transfer tiers. Correct
  per-user correlated sums completed every tier and failed only scaling at
  `+0.95`, with a `16.59x` largest ratio;
- problem 1556 is complete and remotely verified as submission `2069772868`.
  Its live backend `question_id` is `1660`; the early remote check corrected
  the initially guessed backend ID before package authoring. The Accepted
  right-to-left grouping source passed 100,001 consecutive values, every
  legal decimal-width transition, the upper bound, and 10,000 deterministic
  full-range values against an independent forward-grouping oracle. Its strict
  bounded-domain certificate records the ten-digit source maximum instead of
  claiming an unstable fixed-width timing verdict;
- problem 1557 is complete and remotely verified as submission `2069776826`.
  Its live backend `question_id` is `1661`. The Accepted Boolean indegree scan
  and an independent destination-set implementation passed all correctness
  cases and the legal 512/2048/8192-vertex chain tiers. A correct tuple-count
  edge-rescan implementation completed every tier and failed only scaling at
  `+0.97`, with a `33.53x` largest ratio;
- problem 1558 is complete and remotely verified as submission `2069783015`.
  Its live backend `question_id` is `1662`. The Accepted population-count
  formula and an independent binary-string bit scan passed all correctness
  cases and the legal 512/2048/8192-entry maximum-width tiers. A correct
  repeated-prefix-maximum implementation completed every tier and failed only
  scaling at `+0.82`, with a `44.02x` largest ratio;
- problem 1559 is complete and remotely verified as submission `2069788767`.
  Its live backend `question_id` is `1663`. The Accepted parent-aware iterative
  DFS matched exhaustive binary grids through `3x3`; it and an independent
  union-find implementation passed all cases and the legal 64/256/1024-cell
  alternating-row tiers. Correct repeated component traversal completed every
  tier and failed only scaling at `+0.51`, with an `18.58x` largest ratio;
- problem 1560 is complete and remotely verified as submission `2069793551`.
  Its live backend `question_id` is `1682`; early verification corrected the
  initially guessed backend ID before package authoring. The Accepted endpoint
  arc and an independent modular-distance implementation passed all cases and
  the complete legal 4/20/100-sector tiers. Correct visit-by-visit simulation
  completed every tier and failed only scaling at `+1.47`, with a `146.30x`
  largest ratio;
- problem 1561 is complete and remotely verified as submission `2069798426`.
  Its live backend `question_id` is `1683`. The Accepted ascending rank scan
  matched exhaustive optimal grouping for every multiset through six piles
  over values 1 through 5. It and an independent descending-rank scan passed
  all cases and the legal 384/1536/6144-pile tiers. Correct repeated extrema
  extraction completed every tier and failed only scaling at `+1.63`, with a
  `1177.16x` largest ratio;
- problem 1562 is complete and remotely verified as submission `2069803480`.
  Its live backend `question_id` is `1684`. The Accepted boundary-length merge
  matched every permutation through `n=7` for every legal target size. It and
  an independent union-find implementation passed all cases and the legal
  512/2048/8192-position odd-then-even tiers. Correct full-bitstring rescanning
  completed every tier and failed only scaling at `+0.86`, with a `9.48x`
  largest ratio;
- problem 1563 is complete and remotely verified as submission `2069809632`.
  Its live backend `question_id` is `1685`. The Accepted first-crossing
  monotone DP matched the direct cubic recurrence exhaustively through length
  eight over values 1 through 4. It and an independent last-not-greater
  monotone formulation passed all cases and the legal 16/32/64-stone balanced
  tiers. Correct cubic interval DP completed every tier and failed only scaling
  at `+0.87`;
- problem 1564 is complete and remotely verified as submission `2069815797`.
  Its live backend `question_id` is `1703`. The remotely Accepted prefix-
  clearance greedy and an independently structured prefix-minimum matcher
  passed all eleven correctness cases and the legal 256/1024/4096 descending-
  clearance tiers. A correct implementation that recomputes every prefix
  minimum from a fresh slice completed every tier and failed only scaling at
  `+0.64`;
- problem 1565 is complete and remotely verified as MySQL submission
  `2069823481`. Its live backend `question_id` is `1712`. The Accepted strict-
  threshold monthly aggregation and an independent substring-key aggregation
  passed all ten correctness cases and the legal 32/128/512 distinct-month
  tiers. A correct correlated monthly-rescan query completed every tier and
  failed only scaling at `+0.98`, with a `30.25x` largest ratio;
- problem 1566 is complete and remotely verified as submission `2069828346`.
  Its live backend `question_id` is `1689`. The Accepted offset-equality streak
  and an independent grouped-equality scan passed all eleven correctness cases
  and the legal 8/32/100-value distinct-array tiers. A correct direct region
  verifier completed every tier and failed only scaling at `+0.86`, with a
  `10.81x` largest ratio;
- problem 1567 is complete and remotely verified as submission `2069833033`.
  Its live backend `question_id` is `1690`. The Accepted two-sign ending-state
  DP matched exhaustive brute force on all 9,840 sign arrays through length
  eight. It and an independent zero-delimited parity scan passed all twelve
  correctness cases and the legal 32/128/512 all-positive tiers. A correct
  exhaustive subarray scan completed every tier and failed only scaling at
  `+1.17`, with a `266.51x` largest ratio;
- problem 1568 is complete and remotely verified as submission `2069837609`.
  Its live backend `question_id` is `1691`. The Accepted implicit-grid low-link
  DFS matched brute force for every binary grid through `3x3`. It and an
  independent explicit-graph articulation implementation passed all twelve
  correctness cases and the legal 16/36/64-cell solid-square tiers. Correct
  remove-and-recount scanning completed every final tier and failed only
  scaling at `+0.99`, with a `21.09x` largest ratio. Larger draft tiers were
  discarded because the slower implementation reached the safety cap;
- problem 1569 is complete and remotely verified as submission `2069845927`.
  Its live backend `question_id` is `1692`. An initially Accepted quadratic
  partition source was superseded by the final linear Cartesian-tree source,
  then resubmitted. The final source matched all 46,233 permutations through
  length eight. It and an independent reverse union-find formulation passed
  all twelve correctness cases and the legal 32/128/512-key increasing-chain
  tiers. Correct recursive root partitioning completed every tier and failed
  only scaling at `+0.89`;
- problem 1570 is complete and remotely verified as submission `2069851041`.
  Its live backend `question_id` is `1713`. The Accepted smaller-map lookup and
  an independent sorted two-pointer intersection passed all twelve correctness
  cases and the legal 32/128/512-coordinate full-support tiers. Correct
  pairwise sparse-entry matching completed every tier and failed only scaling
  at `+1.17`, with a `228.36x` largest ratio;
- problem 1571 is complete and remotely verified as MySQL submission
  `2069854873`. Its live backend `question_id` is `1718`. The Accepted direct
  join-and-group query and an independent precomputed-unit-volume aggregation
  passed all ten correctness cases and the legal 32/128/512-row distinct-
  warehouse tiers. A correct correlated warehouse rescan completed every tier
  and failed only scaling at `+0.80`, with a `12.74x` largest ratio;
- problem 1572 is complete and remotely verified as submission `2069859153`.
  Its live backend `question_id` is `1677`. The Accepted two-index diagonal
  scan and an independent two-sum formulation passed all twelve correctness
  cases and the legal 8/32/100-dimension all-one tiers. Correct full-matrix
  scanning completed every tier and failed only scaling at `+1.25`, with a
  `37.42x` largest ratio. The Accepted source also exposed and corrected a
  stale hidden expected result after an out-of-contract zero was replaced;
- problem 1573 is complete and remotely verified as submission `2069863817`.
  Its live backend `question_id` is `1678`. The Accepted four-boundary scan
  matched every binary string from length three through twelve. It and an
  independent constant-space gap scan passed all twelve correctness cases and
  the legal 32/128/512-character all-zero tiers. Correct prefix-count cut-pair
  enumeration completed every tier and failed only scaling at `+1.87`, with a
  `2160.71x` largest ratio. The audit initially withheld completion until the
  Goal narrative was expanded past the source-fidelity threshold;
- problem 1574 is complete and remotely verified as submission `2069870124`.
  Its live backend `question_id` is `1679`. The Accepted prefix/suffix merge
  matched a brute-force removal oracle on all 87,380 arrays over values zero
  through three and lengths one through eight. It and an independent linear
  suffix-first scan passed all thirteen correctness cases and the legal
  32/128/512-element incompatible-sorted-halves tiers. Correct removal-interval
  enumeration completed every tier and failed only scaling at `+1.09`, with a
  `428.41x` largest ratio. The first bridge launch inherited
  `ELECTRON_RUN_AS_NODE=1`; clearing it restored Electron secure-storage access
  before the unchanged candidate was submitted;
- problem 1575 is complete and remotely verified as submission `2069876316`.
  Its live backend `question_id` is `1680`. The Accepted memoized recurrence,
  an independent bottom-up table, and a direct recursive oracle matched all
  17,780 small distinct-coordinate contracts. The Accepted and bottom-up forms
  passed all thirteen correctness cases and the legal 16/64/200-fuel tiers.
  Correct repeated table construction completed every ordinary and benchmark
  case and failed only scaling at `+0.97`, with a `191.46x` largest ratio. An
  initially considered exponential route enumerator was rejected as invalid
  calibration because it could not reasonably complete the official fuel-40
  case; no safety-cap result was counted as complexity evidence;
- problem 1576 is complete and remotely verified as submission `2069885198`.
  Its live backend `question_id` is `1698`. A new semantic validator accepts
  any valid completion while checking length, fixed-letter preservation,
  lowercase replacements, and unequal adjacent characters; its focused
  regression test covers alternate valid outputs and invalid mutations. The
  Accepted mutable-list scan, an independent linear construction, and correct
  immutable rebuild-and-rescan scanning passed all thirteen cases, the legal
  16/64/100-character all-placeholder tiers, and 983 exhaustive valid source
  strings. The quadratic candidate completed every tier and failed only
  scaling at `+0.90`, with a `13.16x` largest ratio;
- problem 1577 is complete and remotely verified as submission `2069890487`.
  Its live backend `question_id` is `1699`. The Accepted pair-product counter,
  an independent square-frequency formulation, and direct triplet enumeration
  matched all 115,600 small array-pair contracts. All three passed thirteen
  correctness cases and the final legal 8/24/64-element duplicate tiers. The
  cubic enumerator completed and failed only scaling at `+1.19`, with a
  `41.66x` largest ratio. Exhaustive checking corrected one duplicate-sensitive
  expected result from four to three. A draft 100-element tier was discarded
  because the slower implementation reached the execution safety cap;
- problem 1578 is complete and remotely verified as submission `2069896899`.
  Its live backend `question_id` is `1700`. The Accepted streaming greedy scan,
  an independent run-sum formulation, and correct repeated-run recomputation
  matched 21,844 exhaustive small contracts and passed all thirteen ordinary
  cases plus the legal 16/64/256-balloon single-run tiers. The quadratic
  recomputation completed every tier and failed only scaling at `+1.20`, with
  a `178.17x` largest ratio;
- problem 1579 is complete and remotely verified as submission `2069902982`.
  Its live backend `question_id` is `1701`. The Accepted ranked,
  path-compressed DSU, an independent optimized DSU, and a correct uncompressed
  DSU matched a brute-force retained-subset oracle on all 511 nonempty typed
  three-node graphs and passed all thirteen cases plus the legal 32/128/512-node
  shared-chain-and-chord tiers. The uncompressed candidate completed every tier
  and failed only scaling at `+0.70`, with a `10.03x` largest ratio;
- problem 1580 is complete and remotely verified through Premium access as
  submission `2069909471`. Its live backend `question_id` is `1719`. The
  Accepted directional-capacity matching and an independent two-ended greedy
  formulation matched 1,860,496 small box/warehouse contracts and passed all
  thirteen cases plus the legal 32/128/256-item all-fit tiers. Correct
  quadratic smallest-fitting-box selection completed every tier and failed
  only scaling at `+1.03`, with a `41.71x` largest ratio;
- problem 1581 is complete and remotely verified as MySQL submission
  `2069914477`. Its live backend `question_id` is `1724`. The Accepted left
  anti-join and an independent uncorrelated `NOT IN` materialization passed all
  ten fixtures and the legal 32/128/512-visit tiers. A correct correlated
  transaction-count query completed every tier and failed only scaling at
  `+0.62`, with a `5.12x` largest ratio. Empty-table drafts were replaced by
  semantically neutral transactional rows because the local SQL fixture loader
  needs one row to infer an empty table's columns; an unindexed correlated
  `NOT EXISTS` draft was rejected as the independent passing candidate after
  it also showed slower growth;
- problem 1582 is complete and remotely verified as submission `2069920845`.
  Its live backend `question_id` is `1704`. The Accepted row/column-count scan,
  an independent transpose-count formulation, and correct full recounting
  matched 74,954 exhaustive binary matrices and passed all thirteen ordinary
  cases plus the legal 64/1024/4096-cell dense tiers. The slower recount
  completed every tier and failed only scaling at `+0.51`, with a `42.36x`
  largest ratio;
- problem 1583 is complete and remotely verified as submission `2069926627`.
  Its live backend `question_id` is `1705`. The Accepted dense rank table, an
  independent inverse-rank-map formulation, and explicit linear rank searches
  matched all 3,888 four-friend preference/pairing contracts and passed all
  thirteen ordinary cases plus the final legal 16/32/64-friend stable tiers.
  Explicit rank scanning completed every tier and failed only scaling at
  `+0.56`. Exhaustive checking corrected one asymmetric expected result from
  two to zero. A built-in `list.index` draft was discarded because optimized
  C-level scans did not yield a calibrated slower trend;
- problem 1584 is complete and remotely verified as submission `2069936240`.
  Its live backend `question_id` is `1706`. The Accepted dense Prim method, an
  independent set-based Prim formulation, and a Kruskal oracle matched all 465
  distinct point subsets of sizes one through six from a 3-by-3 grid. They
  passed all 13 cases and the legal 16/32/64-point collinear tiers. Correct
  full-cut scanning completed every tier and failed only scaling at `+1.04`,
  with an `11.97x` largest ratio. An earlier purported independent Prim draft
  was discarded after calibration exposed its accidental cubic refresh loop;
- problem 1585 is complete and remotely verified as submission `2069945934`.
  Its live backend `question_id` is `1707`. The Accepted ten-position-list
  greedy, an independent queue-front formulation, and exhaustive substring-sort
  reachability matched all 66,429 source/target pairs of lengths one through
  five over digits zero through two. They passed all 15 cases and the legal
  125/500/2000-character descending-cycle tiers. Correct repeated search,
  prefix checking, and removal completed every tier and failed only scaling at
  `+0.95`, with a `28.20x` largest ratio. A draft 8,000-character top tier was
  discarded because the slower implementation reached the Python step safety
  cap;
- problem 1586 is complete and remotely verified as submission `2069956982`.
  Its live backend `question_id` is `1729`, and authenticated verification
  confirmed the Premium-only `BSTIterator` interface. The Accepted lazy
  inorder stack with cursor history and an independent eager inorder iterator
  matched 873 BST insertion orders across 20,952 randomized valid operations.
  They passed all 10 cases and the legal 8/32/128-node right-chain tiers.
  Correct full-inorder recomputation on every move completed every tier and
  failed only scaling at `+0.99`, with an `18.76x` largest ratio. Draft 512-
  and 256-node top tiers were discarded because amplified defensive deep copies
  of the skewed fixtures exceeded Python's recursion limit before measurement;
- problem 1587 is complete and remotely verified as submission `2069967098`.
  Its live backend `question_id` is `1734`. The Accepted join/group query and
  an independent aggregate-first query matched all nine authored cases and 200
  randomized signed-balance fixtures. They passed the legal 32/128/512-user
  tiers, including exact-threshold accounts. Correct correlated scalar sums
  completed every tier and failed only scaling at `+0.79`, with a `9.26x`
  largest ratio;
- problem 1588 is complete and remotely verified as submission `2069973851`.
  Its live backend `question_id` is `1693`. The Accepted per-index contribution
  count, an independent parity-state recurrence, and direct enumeration matched
  all 10 authored cases and all 21,844 arrays of lengths one through seven over
  values one through four. They passed the legal 6/25/100-element maximum-value
  tiers. Correct running-sum enumeration completed every tier and failed only
  scaling at `+1.11`, with a `31.72x` largest ratio. An earlier independent DP
  draft was discarded after its redundant state bookkeeping measured `+0.17`,
  just outside the same-class cutoff;
- problem 1589 is complete and remotely verified as submission `2069981421`.
  Its live backend `question_id` is `1695`. The Accepted difference-array
  coverage method, an independent endpoint-event sweep, and direct range
  increments matched all 11 authored cases and 1,394 brute-force permutation
  contracts. They passed the legal 32/128/512-element tiers with the same
  number of full-array requests. Correct direct range increments completed
  every tier and failed only scaling at `+1.05`, with a `58.85x` largest ratio;
- problem 1590 is complete and remotely verified as submission `2069987107`.
  Its live backend `question_id` is `1694`. The Accepted forward prefix map, an
  independent reverse suffix map, and full subarray enumeration matched all 11
  authored cases and 32,790 exhaustive array/divisor contracts. They passed the
  legal 32/128/512-element tiers where only removing the forbidden whole array
  matches. Correct enumeration completed every tier and failed only scaling at
  `+1.12`, with a `217.27x` largest ratio. Exhaustive checking corrected an
  initially authored interior-removal fixture whose total was already divisible;
- problem 1591 is complete and remotely verified as submission `2069996162`.
  Its live backend `question_id` is `1696`. The Accepted dependency graph, an
  independent DFS cycle detector, synchronous rectangle peeling, and explicit
  bounding-rectangle render orders matched all 11 authored cases and 1,352
  exhaustive small grids. They passed the legal 8/16/32-side nested-layer
  tiers. Correct synchronous peeling completed every tier and failed only
  scaling at `+0.89`, with a `3.98x` largest ratio;
- problem 1592 is complete and remotely verified as submission `2070002890`.
  Its live backend `question_id` is `1714`. The Accepted split/count/join
  method, an independent length-minus-joined-words formulation, and explicit
  repeated-prefix copying matched all 10 authored cases and 2,036 exhaustive
  legal text shapes. They passed the legal 8/32/100-character tiers. Correct
  repeated copying completed every tier and failed only scaling at `+0.27`,
  with a `2.16x` largest ratio. A Python-level manual tokenizer draft was
  discarded because its interpreter overhead did not calibrate as same-class;
- problem 1593 is complete and remotely verified as submission `2070012003`.
  Its live backend `question_id` is `1715`. The Accepted short-first
  branch-and-bound search matched a brute-force boundary-mask oracle for all
  9,840 strings over `abc` through length 8. It and an independent
  branch-and-bound formulation passed the legal 3/6/12-character distinct-text
  tiers. Correct exhaustive mask enumeration with pairwise uniqueness checks
  completed every tier and failed only scaling at `+3.92`, with a `276.85x`
  largest ratio;
- problem 1594 is complete and remotely verified as submission `2070022007`.
  Its live backend `question_id` is `1716`. The Accepted full-table min/max
  product DP matched exhaustive path enumeration across 33,130 small matrices;
  an independent rolling-row DP passed the legal 9/36/81-cell tiers. Correct
  full path enumeration completed every tier and failed only scaling at
  `+2.27`, with a `131.43x` largest ratio;
- problem 1595 is complete and remotely verified as submission `2070026636`.
  Its live backend `question_id` is `1717`. The Accepted memoized bitmask DP
  matched exhaustive edge-subset enumeration on all 729 two-by-three matrices
  with costs in $\{0,1,2\}$. An independent reverse-order memoized formulation
  passed the legal 3/6/12-row tiers twice. Correct endpoint-assignment
  enumeration completed every tier and failed only scaling at `+3.33`, with an
  `85.59x` largest ratio;
- problem 1596 is complete and remotely verified as Premium SQL submission
  `2070033400`. Its live backend `question_id` is `1735`. The Accepted grouped
  dense-rank query matched the official fixture and 500 randomized frequency
  oracles. An independent aggregate/max-join query passed the legal
  32/128/512-order tiers. Correct correlated recounting completed every tier
  and failed only scaling at `+1.32`, with a `67.28x` largest ratio;
- problem 1597 is complete and remotely verified as Premium submission
  `2070039849`. Its live backend `question_id` is `1736`. The Accepted two-stack
  expression-tree builder preserved LeetCode's platform `Node` declaration and
  matched an independent shunting-yard oracle on the official inputs, targeted
  parenthesized cases, and 5,184 exhaustive flat expressions. An independent
  Pratt parser passed the legal 7/31/99-character tiers. Correct recursive
  lowest-precedence rescanning completed every tier and failed only scaling at
  `+0.86`, with a `14.52x` largest ratio;
- problem 1598 is complete and remotely verified as submission `2070047085`.
  Its live backend `question_id` is `1720`. The Accepted depth counter matched
  a stack oracle on 87,380 exhaustive operation sequences. An independent
  explicit stack passed the legal 32/128/512-operation tiers. Correct explicit
  front shifting completed every tier and failed only scaling at `+1.17`, with
  a `105.13x` largest ratio;
- problem 1599 is complete and remotely verified as submission `2070052406`.
  Its live backend `question_id` is `1721`. The Accepted cumulative simulation
  matched an independent profit-history oracle on 23,430 arrival-and-cost
  contracts. An independent marginal-profit simulation passed the legal
  32/128/512-arrival tiers. Correct prefix resimulation completed every tier
  and failed only scaling at `+1.01`, with a `63.41x` largest ratio;
- problem 1600 is complete and remotely verified as submission `2070058534`.
  Its live backend `question_id` is `1722`. The Accepted stateful class matched
  the official trace and 1,000 randomized histories. An independent
  adjacency/preorder design passed the legal 32/128/512-person traces. Correct
  eager order rebuilding completed every tier and failed only scaling at
  `+1.15`, with an `85.04x` largest ratio;
- problem 1601 is complete and remotely verified as submission `2070066042`.
  Its live backend `question_id` is `1723`. The Accepted branch-and-bound
  search matched a subset oracle on the official examples and 5,000 randomized
  request sets. An independent iterative bounded search passed the legal
  3/6/12-request tiers. Correct full-mask balance rebuilding completed every
  tier and failed only scaling at `+4.16`, with a `343.93x` largest ratio;
- problem 1602 is complete and remotely verified as Premium submission
  `2070072807`. Its live backend `question_id` is `1745`. The actual native
  declaration is `Solution.findNearestRightNode`; the metadata's
  `findNeartestRightNode` spelling is stale. The Accepted identity-based BFS
  matched 5,000 randomized trees and targets. An independent frontier BFS
  passed the legal 31/127/511-node tiers. Correct repeated root-to-node depth
  searches completed every tier and failed only scaling at `+1.19`, with a
  `244.20x` largest ratio;
- problem 1603 is complete and remotely verified as submission `2070080564`.
  Its live backend `question_id` is `1708`. The Accepted counter class matched
  the official trace and 10,000 randomized parking histories. An independent
  dictionary counter passed the legal 32/128/512-call tiers. Correct
  individual-slot scanning completed every tier and failed only scaling at
  `+1.28`, with a `106.69x` largest ratio;
- problem 1604 is complete and remotely verified as submission `2070087650`.
  Its live backend `question_id` is `1709`. The Accepted grouped-timestamp
  method passed exact-60 and 61-minute boundary checks plus 4,800 randomized
  brute-force comparisons. An independent global record sort passed the legal
  64/256/512-record tiers. Correct per-name filtering completed every tier and
  failed only scaling at `+1.05`, with a `124.00x` largest ratio;
- problem 1605 is complete and remotely verified as submission `2070097822`.
  Its live backend `question_id` is `1711`. The Accepted margin-greedy method
  passed four boundary examples and 5,000 randomized matrix-margin checks. A
  new `matrix_margins` semantic validator accepts every valid non-negative
  integer matrix rather than one exact arrangement. An independent cumulative
  interval construction passed the legal 64/256/1024-cell tiers. Correct
  row-major repeated-margin summation completed every tier and failed only
  scaling at `+0.93`, with a `23.70x` largest ratio;
- problem 1606 is complete and remotely verified as submission `2070105431`.
  Its live backend `question_id` is `1710`. The Accepted Fenwick-tree plus
  busy-heap scheduler matched four fixed scenarios and 10,000 randomized
  brute-force schedules. An independent segment tree passed the legal
  64/256/1024-request saturation tiers. Correct circular linear scanning
  completed every tier and failed only scaling at `+0.90`, with a `13.25x`
  largest ratio;
- problem 1607 is complete and remotely verified as Premium MySQL submission
  `2070113289`. Its live backend `question_id` is `1749`. The Accepted
  `NOT EXISTS` query passed the official fixture, no-order coverage,
  alphabetical ordering, and both inclusive 2020 endpoints. The app-local
  distinct-ID anti-join and independent conditional aggregation passed the
  legal 32/128/512-row tiers. Correct correlated counting completed every tier
  and failed only scaling at `+0.77`, with a `7.66x` largest ratio;
- problem 1608 is complete and remotely verified as submission `2070120538`.
  Its live backend `question_id` is `1730`. The Accepted sorting-boundary
  method passed five targeted examples and 20,000 randomized brute-force
  comparisons. An independent capped-frequency suffix count passed the legal
  6/24/96-element tiers. Correct repeated candidate counting completed every
  tier and failed only scaling at `+1.18`, with a `37.28x` largest ratio;
- problem 1609 is complete and remotely verified as submission `2070128099`.
  Its live backend `question_id` is `1731`. The Accepted level-order validator
  passed four targeted trees and 10,000 randomized comparisons with an
  independent DFS-level oracle. An independent DFS with per-depth state passed
  the legal 31/127/511-node perfect-tree tiers. Correct all-pairs comparison
  within each level completed every tier and failed only scaling at `+0.87`,
  with a `23.93x` largest ratio;
- problem 1610 is complete and remotely verified as submission `2070134095`.
  Its live backend `question_id` is `1733`. The Accepted doubled-angle sliding
  window passed six targeted scenarios and 10,000 randomized circular-angle
  oracle checks. An independent sorted-angle binary-search window passed the
  legal 32/128/512-point duplicate-ray tiers. Correct orientation-by-orientation
  recounting completed every tier and failed only scaling at `+1.03`, with an
  `81.05x` largest ratio;
- problem 1611 is complete and remotely verified as submission `2070140470`.
  Its live backend `question_id` is `1732`. The Accepted inverse-Gray suffix
  XOR matched an independent legal-operation BFS for all 2,048 states below
  2048 and the $10^9$ boundary. An independent highest-bit recurrence passed
  the legal 2/8/30-bit tiers. Correct $O(b^2)$ suffix recomputation completed
  every ordinary case and tier and failed only scaling at `+0.56`, with a
  `4.97x` largest ratio;
- problem 1612 is complete and remotely verified as Premium submission
  `2070149283`. Its live backend `question_id` is `1750`. The Accepted signed
  variable-frequency traversal passed both live samples, two leaf boundaries,
  and 10,000 randomized basis-evaluation checks. An independent fixed-array
  iterative traversal passed the legal 30/126/510-total-node tiers. Correct
  unmatched-position scanning completed every tier and failed only scaling at
  `+0.78`, with a `14.18x` largest ratio;
- problem 1613 is complete and remotely verified as Premium MySQL submission
  `2070158984`. Its live backend `question_id` is `1759`. The Accepted
  recursive-range anti-join passed the official fixture plus no-gap,
  missing-prefix, and mixed-gap checks. An independent materialized membership
  query passed the legal 32/128/512-ID tiers. Correct correlated counting
  completed every tier and failed only scaling at `+0.73`, with a `7.30x`
  largest ratio;
- the refreshed migration audit: 1613 locally complete, 1566 fully verified,
  47 blocked, 1582 scaling benchmarks, 31 certificates, and frontend ID 1614
  next;
- the dataset checker after problem 1613: 3985 documents, 2597 manually
  complete, and 1388 still needing authoring;
- the dataset checker after problem 1612: 3985 documents, 2596 manually
  complete, and 1389 still needing authoring;
- the dataset checker after problem 1611: 3985 documents, 2595 manually
  complete, and 1390 still needing authoring;
- the dataset checker after problem 1610: 3985 documents, 2594 manually
  complete, and 1391 still needing authoring;
- the dataset checker after problem 1609: 3985 documents, 2594 manually
  complete, and 1391 still needing authoring;
- the dataset checker after problem 1608: 3985 documents, 2593 manually
  complete, and 1392 still needing authoring;
- the dataset checker after problem 1607: 3985 documents, 2593 manually
  complete, and 1392 still needing authoring;
- the dataset checker after problem 1606: 3985 documents, 2592 manually
  complete, and 1393 still needing authoring;
- the dataset checker after problem 1605: 3985 documents, 2592 manually
  complete, and 1393 still needing authoring;
- the dataset checker after problem 1604: 3985 documents, 2592 manually
  complete, and 1393 still needing authoring;
- the dataset checker after problem 1603: 3985 documents, 2592 manually
  complete, and 1393 still needing authoring;
- the dataset checker after problem 1602: 3985 documents, 2591 manually
  complete, and 1394 still needing authoring;
- the dataset checker after problem 1600: 3985 documents, 2590 manually
  complete, and 1395 still needing authoring;
- the dataset checker after problem 1597: 3985 documents, 2589 manually
  complete, and 1396 still needing authoring;
- the dataset checker after problem 1596: 3985 documents, 2588 manually
  complete, and 1397 still needing authoring;
- the dataset checker after problem 1593: 3985 documents, 2587 manually
  complete, and 1398 still needing authoring;
- the dataset checker after problem 1592: 3985 documents, 2586 manually
  complete, and 1399 still needing authoring;
- the dataset checker after problem 1591: 3985 documents, 2585 manually
  complete, and 1400 still needing authoring;
- the dataset checker after problem 1590: 3985 documents, 2585 manually
  complete, and 1400 still needing authoring;
- the dataset checker after problem 1589: 3985 documents, 2585 manually
  complete, and 1400 still needing authoring;
- the dataset checker after problem 1588: 3985 documents, 2585 manually
  complete, and 1400 still needing authoring;
- the dataset checker after problem 1587: 3985 documents, 2585 manually
  complete, and 1400 still needing authoring;
- the dataset checker after problem 1586: 3985 documents, 2584 manually
  complete, and 1401 still needing authoring;
- the dataset checker after problem 1585: 3985 documents, 2583 manually
  complete, and 1402 still needing authoring;
- the dataset checker after problem 1584: 3985 documents, 2582 manually
  complete, and 1403 still needing authoring;
- the dataset checker after problem 1583: 3985 documents, 2582 manually
  complete, and 1403 still needing authoring;
- the dataset checker after problem 1582: 3985 documents, 2582 manually
  complete, and 1403 still needing authoring;
- the dataset checker after problem 1581: 3985 documents, 2582 manually
  complete, and 1403 still needing authoring;
- the dataset checker after problem 1580: 3985 documents, 2581 manually
  complete, and 1404 still needing authoring;
- the dataset checker after problem 1579: 3985 documents, 2580 manually
  complete, and 1405 still needing authoring;
- the dataset checker after problem 1578: 3985 documents, 2579 manually
  complete, and 1406 still needing authoring;
- the dataset checker after problem 1577: 3985 documents, 2579 manually
  complete, and 1406 still needing authoring;
- the dataset checker after problem 1576: 3985 documents, 2579 manually
  complete, and 1406 still needing authoring;
- the dataset checker after problem 1575: 3985 documents, 2578 manually
  complete, and 1407 still needing authoring;
- the dataset checker after problem 1574: 3985 documents, 2578 manually
  complete, and 1407 still needing authoring;
- the dataset checker after problem 1573: 3985 documents, 2578 manually
  complete, and 1407 still needing authoring;
- the dataset checker after problem 1572: 3985 documents, 2577 manually
  complete, and 1408 still needing authoring;
- the dataset checker after problem 1571: 3985 documents, 2577 manually
  complete, and 1408 still needing authoring;
- the dataset checker after problem 1570: 3985 documents, 2576 manually
  complete, and 1409 still needing authoring;
- the dataset checker after problem 1569: 3985 documents, 2575 manually
  complete, and 1410 still needing authoring;
- the dataset checker after problem 1568: 3985 documents, 2575 manually
  complete, and 1410 still needing authoring;
- the dataset checker after problem 1567: 3985 documents, 2575 manually
  complete, and 1410 still needing authoring;
- the dataset checker after problem 1566: 3985 documents, 2575 manually
  complete, and 1410 still needing authoring;
- the dataset checker after problem 1565: 3985 documents, 2575 manually
  complete, and 1410 still needing authoring;
- the dataset checker after problem 1564: 3985 documents, 2574 manually
  complete, and 1411 still needing authoring;
- the dataset checker after problem 1563: 3985 documents, 2573 manually
  complete, and 1412 still needing authoring;
- the dataset checker after problem 1562: 3985 documents, 2573 manually
  complete, and 1412 still needing authoring;
- the dataset checker after problem 1561: 3985 documents, 2573 manually
  complete, and 1412 still needing authoring;
- the dataset checker after problem 1560: 3985 documents, 2573 manually
  complete, and 1412 still needing authoring;
- the dataset checker after problem 1559: 3985 documents, 2573 manually
  complete, and 1412 still needing authoring;
- the dataset checker after problem 1558: 3985 documents, 2573 manually
  complete, and 1412 still needing authoring;
- the dataset checker after problem 1557: 3985 documents, 2573 manually
  complete, and 1412 still needing authoring;
- the dataset checker after problem 1556: 3985 documents, 2572 manually
  complete, and 1413 still needing authoring;
- the dataset checker after problem 1555: 3985 documents, 2571 manually
  complete, and 1414 still needing authoring;
- the dataset checker after problem 1554: 3985 documents, 2570 manually
  complete, and 1415 still needing authoring;
- the dataset checker after problem 1553: 3985 documents, 2569 manually
  complete, and 1416 still needing authoring;
- the dataset checker after problem 1552: 3985 documents, 2568 manually
  complete, and 1417 still needing authoring;
- the dataset checker after problem 1551: 3985 documents, 2568 manually
  complete, and 1417 still needing authoring;
- the dataset checker after problem 1550: 3985 documents, 2567 manually
  complete, and 1418 still needing authoring;
- the dataset checker after problem 1549: 3985 documents, 2567 manually
  complete, and 1418 still needing authoring;
- the dataset checker after problem 1548: 3985 documents, 2566 manually
  complete, and 1419 still needing authoring;
- the dataset checker after problem 1547: 3985 documents, 2565 manually
  complete, and 1420 still needing authoring;
- the dataset checker after problem 1546: 3985 documents, 2565 manually
  complete, and 1420 still needing authoring;
- the dataset checker after problem 1545: 3985 documents, 2565 manually
  complete, and 1420 still needing authoring;
- the dataset checker after problem 1544: 3985 documents, 2564 manually
  complete, and 1421 still needing authoring;
- the dataset checker after problem 1543: 3985 documents, 2563 manually
  complete, and 1422 still needing authoring;
- the combined complexity-certificate, validated-case, and dynamic-document
  suite after problem 1556 passed 140 tests and 31 certificate-route subtests,
  with only the existing Starlette `httpx` deprecation warning;
- the focused validated-case and dynamic-documentation suite after problem
  1557 passed 117 tests, with only the existing Starlette `httpx` deprecation
  warning;
- the focused validated-case and dynamic-documentation suite after problem
  1558 passed 117 tests, with only the existing Starlette `httpx` deprecation
  warning;
- the focused validated-case and dynamic-documentation suite after problem
  1559 passed 117 tests, with only the existing Starlette `httpx` deprecation
  warning;
- the focused validated-case and dynamic-documentation suite after problem
  1560 passed 117 tests, with only the existing Starlette `httpx` deprecation
  warning;
- the focused validated-case and dynamic-documentation suite after problem
  1561 passed 117 tests, with only the existing Starlette `httpx` deprecation
  warning;
- the focused validated-case and dynamic-documentation suite after problem
  1562 passed 117 tests, with only the existing Starlette `httpx` deprecation
  warning;
- the focused validated-case and dynamic-documentation suite after problem
  1563 passed 117 tests, with only the existing Starlette `httpx` deprecation
  warning;
- the combined complexity-certificate, validated-case, and dynamic-document
  suite after problem 1564 passed 140 tests and 31 certificate-route subtests,
  with only the existing Starlette `httpx` deprecation warning;
- the combined complexity-certificate, validated-case, and dynamic-document
  suite after problem 1565 passed 140 tests and 31 certificate-route subtests,
  with only the existing Starlette `httpx` deprecation warning;
- the combined complexity-certificate, validated-case, and dynamic-document
  suite after problem 1566 passed 140 tests and 31 certificate-route subtests,
  with only the existing Starlette `httpx` deprecation warning;
- the combined complexity-certificate, validated-case, and dynamic-document
  suite after problem 1567 passed 140 tests and 31 certificate-route subtests,
  with only the existing Starlette `httpx` deprecation warning;
- the combined complexity-certificate, validated-case, and dynamic-document
  suite after problem 1568 passed 140 tests and 31 certificate-route subtests,
  with only the existing Starlette `httpx` deprecation warning;
- the combined complexity-certificate, validated-case, and dynamic-document
  suite after problem 1569 passed 140 tests and 31 certificate-route subtests,
  with only the existing Starlette `httpx` deprecation warning;
- the combined complexity-certificate, validated-case, and dynamic-document
  suite after problem 1570 passed 140 tests and 31 certificate-route subtests,
  with only the existing Starlette `httpx` deprecation warning;
- the combined complexity-certificate, validated-case, and dynamic-document
  suite after problem 1571 passed 140 tests and 31 certificate-route subtests,
  with only the existing Starlette `httpx` deprecation warning;
- the combined complexity-certificate, validated-case, and dynamic-document
  suite after problem 1572 passed 140 tests and 31 certificate-route subtests,
  with only the existing Starlette `httpx` deprecation warning;
- the combined complexity-certificate, validated-case, and dynamic-document
  suite after problem 1573 passed 140 tests and 31 certificate-route subtests;
  after the Goal-only repair, the dynamic-document suite passed 7 tests, with
  only the existing Starlette `httpx` deprecation warning;
- the combined complexity-certificate, validated-case, and dynamic-document
  suite after problem 1574 passed 140 tests and 31 certificate-route subtests,
  with only the existing Starlette `httpx` deprecation warning;
- the combined complexity-certificate, validated-case, and dynamic-document
  suite after problem 1575 passed 140 tests and 31 certificate-route subtests,
  with only the existing Starlette `httpx` deprecation warning;
- the combined complexity-certificate, validated-case, and dynamic-document
  suite after problem 1576 passed 141 tests and 31 certificate-route subtests,
  with only the existing Starlette `httpx` deprecation warning;
- the combined complexity-certificate, validated-case, and dynamic-document
  suite after problem 1577 passed 141 tests and 31 certificate-route subtests,
  with only the existing Starlette `httpx` deprecation warning;
- the combined complexity-certificate, validated-case, and dynamic-document
  suite after problem 1578 passed 141 tests and 31 certificate-route subtests,
  with only the existing Starlette `httpx` deprecation warning;
- the combined complexity-certificate, validated-case, and dynamic-document
  suite after problem 1579 passed 141 tests and 31 certificate-route subtests,
  with only the existing Starlette `httpx` deprecation warning;
- the combined complexity-certificate, validated-case, and dynamic-document
  suite after problem 1580 passed 141 tests and 31 certificate-route subtests,
  with only the existing Starlette `httpx` deprecation warning;
- the combined complexity-certificate, validated-case, and dynamic-document
  suite after problem 1581 passed 141 tests and 31 certificate-route subtests,
  with only the existing Starlette `httpx` deprecation warning;
- the combined complexity-certificate, validated-case, and dynamic-document
  suite after problem 1582 passed 141 tests and 31 certificate-route subtests,
  with only the existing Starlette `httpx` deprecation warning;
- the combined complexity-certificate, validated-case, and dynamic-document
  suite after problem 1583 passed 141 tests and 31 certificate-route subtests,
  with only the existing Starlette `httpx` deprecation warning;
- the combined complexity-certificate, validated-case, and dynamic-document
  suite after problem 1584 passed 141 tests and 31 certificate-route subtests,
  with only the existing Starlette `httpx` deprecation warning;
- the combined complexity-certificate, validated-case, and dynamic-document
  suite after problem 1585 passed 141 tests and 31 certificate-route subtests,
  with only the existing Starlette `httpx` deprecation warning;
- the combined complexity-certificate, validated-case, and dynamic-document
  suite after problem 1586 passed 141 tests and 31 certificate-route subtests,
  with only the existing Starlette `httpx` deprecation warning;
- the combined complexity-certificate, validated-case, and dynamic-document
  suite after problem 1587 passed 141 tests and 31 certificate-route subtests,
  with only the existing Starlette `httpx` deprecation warning;
- the combined complexity-certificate, validated-case, and dynamic-document
  suite after problem 1588 passed 141 tests and 31 certificate-route subtests,
  with only the existing Starlette `httpx` deprecation warning;
- the combined complexity-certificate, validated-case, and dynamic-document
  suite after problem 1589 passed 141 tests and 31 certificate-route subtests,
  with only the existing Starlette `httpx` deprecation warning;
- the combined complexity-certificate, validated-case, and dynamic-document
  suite after problem 1590 passed 141 tests and 31 certificate-route subtests,
  with only the existing Starlette `httpx` deprecation warning;
- the combined complexity-certificate, validated-case, and dynamic-document
  suite after problem 1591 passed 141 tests and 31 certificate-route subtests,
  with only the existing Starlette `httpx` deprecation warning;
- the combined complexity-certificate, validated-case, and dynamic-document
  suite after problem 1592 passed 141 tests and 31 certificate-route subtests,
  with only the existing Starlette `httpx` deprecation warning;
- the combined complexity-certificate, validated-case, and dynamic-document
  suite after problem 1543 passed 138 tests and 30 certificate-route subtests,
  with only the existing Starlette `httpx` deprecation warning;
- the dataset checker after problem 1542: 3985 documents, 2562 manually
  complete, and 1423 still needing authoring;
- the dataset checker after problem 1541: 3985 documents, 2561 manually
  complete, and 1424 still needing authoring;
- the dataset checker after problem 1540: 3985 documents, 2560 manually
  complete, and 1425 still needing authoring;
- the dataset checker after problem 1539: 3985 documents, 2559 manually
  complete, and 1426 still needing authoring;
- the dataset checker after problem 1538: 3985 documents, 2559 manually
  complete, and 1426 still needing authoring;
- the dataset checker after problem 1537: 3985 documents, 2558 manually
  complete, and 1427 still needing authoring;
- the dataset checker after problem 1536: 3985 documents, 2558 manually
  complete, and 1427 still needing authoring;
- the dataset checker after problem 1535: 3985 documents, 2558 manually
  complete, and 1427 still needing authoring;
- the dataset checker after problem 1534: 3985 documents, 2558 manually
  complete, and 1427 still needing authoring;
- the dataset checker after problem 1533: 3985 documents, 2558 manually
  complete, and 1427 still needing authoring;
- the dataset checker after problem 1532: 3985 documents, 2557 manually
  complete, and 1428 still needing authoring;
- the dataset checker after problem 1531: 3985 documents, 2556 manually
  complete, and 1429 still needing authoring;
- the dataset checker after problem 1530: 3985 documents, 2555 manually
  complete, and 1430 still needing authoring;
- the dataset checker after problem 1529: 3985 documents, 2554 manually
  complete, and 1431 still needing authoring;
- the dataset checker after problem 1528: 3985 documents, 2553 manually
  complete, and 1432 still needing authoring;
- the dataset checker after problem 1527: 3985 documents, 2553 manually
  complete, and 1432 still needing authoring;
- the dataset checker after problem 1525: 3985 documents, 2552 manually
  complete, and 1433 still needing authoring;
- the dataset checker after problem 1524: 3985 documents, 2551 manually
  complete, and 1434 still needing authoring;
- the dataset checker after problem 1523: 3985 documents, 2551 manually
  complete, and 1434 still needing authoring;
- the dataset checker after problem 1522: 3985 documents, 2550 manually
  complete, and 1435 still needing authoring;
- the dataset checker after problem 1521: 3985 documents, 2549 manually
  complete, and 1436 still needing authoring;
- the dataset checker after problem 1520: 3985 documents, 2549 manually
  complete, and 1436 still needing authoring;
- the dataset checker after problem 1519: 3985 documents, 2548 manually
  complete, and 1437 still needing authoring;
- the dataset checker after problem 1518: 3985 documents, 2547 manually
  complete, and 1438 still needing authoring;
- the dataset checker after problem 1517: 3985 documents, 2546 manually
  complete, and 1439 still needing authoring;
- the dataset checker after problem 1516: 3985 documents, 2545 manually
  complete, and 1440 still needing authoring;
- the dataset checker after problem 1515: 3985 documents, 2544 manually
  complete, and 1441 still needing authoring;
- the dataset checker after problem 1513: 3985 documents, 2544 manually
  complete, and 1441 still needing authoring;
- the dataset checker after problem 1511: 3985 documents, 2543 manually
  complete, and 1442 still needing authoring;
- the dataset checker after problem 1510: 3985 documents, 2542 manually
  complete, and 1443 still needing authoring;
- the dataset checker after problem 1508: 3985 documents, 2541 manually
  complete, and 1444 still needing authoring;
- the dataset checker after problem 1507: 3985 documents, 2541 manually
  complete, and 1444 still needing authoring;
- the dataset checker after problem 1506: 3985 documents, 2540 manually
  complete, and 1445 still needing authoring;
- the dataset checker after problem 1505: 3985 documents, 2539 manually
  complete, and 1446 still needing authoring;
- the dataset checker after problem 1504: 3985 documents, 2538 manually
  complete, and 1447 still needing authoring;
- the dataset checker after problem 1503: 3985 documents, 2538 manually
  complete, and 1447 still needing authoring;
- the dataset checker after problem 1502: 3985 documents, 2538 manually
  complete, and 1447 still needing authoring;
- the dataset checker after problem 1501: 3985 documents, 2538 manually
  complete, and 1447 still needing authoring;
- the dataset checker after problem 1499: 3985 documents, 2536 manually
  complete, and 1449 still needing authoring;
- the dataset checker after problem 1495: 3985 documents, 2535 manually
  complete, and 1450 still needing authoring;
- the dataset checker after problem 1494: 3985 documents, 2534 manually
  complete, and 1451 still needing authoring;
- the dataset checker after problem 1492: 3985 documents, 2533 manually
  complete, and 1452 still needing authoring;
- the combined complexity-certificate, validated-case, dynamic-documentation,
  and submission suite after problem 1493 passed 141 tests and 27 certificate
  subtests, with only the existing Starlette `httpx` deprecation warning;
- the dataset checker after problem 1490: 3985 documents, 2532 manually
  complete, and 1453 still needing authoring;
- the focused validated-case, dynamic-documentation, and submission suite after
  problem 1490 passed 123 tests, with only the existing Starlette `httpx`
  deprecation warning;
- the dataset checker after problem 1478: 3985 documents, 2526 manually
  complete, and 1459 still needing authoring;
- the focused validated-case, dynamic-documentation, and submission suite after
  problem 1478 passed 122 tests, with only the existing Starlette `httpx`
  deprecation warning;
- the focused validated-case, dynamic-documentation, and submission suite after
  problem 1471 passed 122 tests, with only the existing Starlette `httpx`
  deprecation warning;
- the focused validated-case, dynamic-documentation, and submission suite after
  problem 1470 passed 122 tests, with only the existing Starlette `httpx` deprecation
  warning;
- the focused validated-case and dynamic-documentation suite after problem
  1434 passed 115 tests, with only the existing Starlette `httpx` deprecation
  and pytest-cache permission warnings;
- the certificate suite after problem 1432 passed 17 tests and 26 routed
  subtests, with the same existing warnings;
- the focused validated-case and dynamic-documentation suite after problem
  1420 passed 114 tests, with only the existing Starlette `httpx` deprecation
  and pytest-cache permission warnings;
- the focused validated-case and dynamic-documentation suite after problem
  1377 passed 111 tests, with only the existing Starlette `httpx` deprecation
  and pytest-cache permission warnings;
- the focused validated-case and dynamic-documentation suite after problem
  1386 passed 112 tests, with only the existing Starlette `httpx` deprecation
  and pytest-cache permission warnings;
- the combined certificate and dynamic-documentation suite after problem 1323
  passed 21 tests and 23 certificate-route subtests, with only the existing
  Starlette `httpx` deprecation warning;
- the focused dynamic-documentation suite after problem 1322 passed 7 tests,
  with only the existing Starlette `httpx` deprecation warning;
- the focused validated-case and dynamic-documentation suite after problem
  1317 passed 111 tests, with only the existing Starlette `httpx` deprecation
  warning;
- the focused dynamic-documentation suite after problem 1318 passed 7 tests,
  with only the existing Starlette `httpx` deprecation warning;
- the focused validated-case and dynamic-documentation suite after problem
  1315 passed 110 tests, with only the existing Starlette `httpx` deprecation
  warning;
- the combined certificate, validated-case, and dynamic-documentation suite
  after problem 1307 passed 123 tests and 22 certificate-route subtests, with
  only the existing Starlette `httpx` deprecation warning;
- the focused validated-case and dynamic-documentation suite after problem
  1310 passed 110 tests, with only the existing Starlette `httpx` deprecation
  warning;
- the focused validated-case and dynamic-documentation suite after problem
  1306 passed 110 tests, with only the existing Starlette `httpx` deprecation
  warning;
- the focused validated-case and dynamic-documentation suite after problem
  1297 passed 110 tests, with only the existing Starlette `httpx` deprecation
  warning;
- the combined certificate, validated-case, and dynamic-doc suite after
  problem 1291 passed 121 tests with 21 certificate-route subtests, with only the
  existing Starlette `httpx` deprecation warning;
- the combined complexity-certificate, validated-case, and dynamic-document
  suite after problem 1604 passed 141 tests and 31 certificate-route subtests,
  with only the existing Starlette `httpx` deprecation warning;
- the combined complexity-certificate, validated-case, and dynamic-document
  suite after problem 1605 passed 142 tests and 31 certificate-route subtests,
  with only the existing Starlette `httpx` deprecation warning;
- the combined complexity-certificate, validated-case, and dynamic-document
  suite after problem 1606 passed 142 tests and 31 certificate-route subtests,
  with only the existing Starlette `httpx` deprecation warning;
- the combined complexity-certificate, validated-case, and dynamic-document
  suite after problem 1607 passed 142 tests and 31 certificate-route subtests,
  with only the existing Starlette `httpx` deprecation warning;
- the combined complexity-certificate, validated-case, and dynamic-document
  suite after problem 1608 passed 142 tests and 31 certificate-route subtests,
  with only the existing Starlette `httpx` deprecation warning;
- the combined complexity-certificate, validated-case, and dynamic-document
  suite after problem 1609 passed 142 tests and 31 certificate-route subtests,
  with only the existing Starlette `httpx` deprecation warning;
- the combined complexity-certificate, validated-case, and dynamic-document
  suite after problem 1610 passed 142 tests and 31 certificate-route subtests,
  with only the existing Starlette `httpx` deprecation warning;
- the combined complexity-certificate, validated-case, and dynamic-document
  suite after problem 1611 passed 142 tests and 31 certificate-route subtests,
  with only the existing Starlette `httpx` deprecation warning;
- the combined complexity-certificate, validated-case, and dynamic-document
  suite after problem 1612 passed 142 tests and 31 certificate-route subtests,
  with only the existing Starlette `httpx` deprecation warning;
- the combined complexity-certificate, validated-case, and dynamic-document
  suite after problem 1613 passed 142 tests and 31 certificate-route subtests,
  with only the existing Starlette `httpx` deprecation warning; and
- `git diff --check` passed apart from non-failing line-ending notices.

The earlier full-suite, Ruff, web-build, and Electron-build evidence still
belongs to the concurrency/certificate batch; rerun those repository-wide
checks after the next substantial batch or before final handoff.

## Exact restart sequence

Start in the existing checkout and keep its uncommitted changes:

```powershell
Set-Location C:\dawei7\code_n
git branch --show-current
git status --short --branch
git rev-parse HEAD
.\.venv\Scripts\python.exe tools\audit_leetcode_migration.py
Get-Content dsa\leetcode\_reports\two_sum_migration_progress.md
```

The expected branch is `main`, and the expected committed migration checkpoint is
`97717019379cb191b141940935075f9667ece6c4`. The refreshed first actionable
package should be
`dsa/leetcode/1614_maximum-nesting-depth-of-the-parentheses`. If
any of those facts differ, trust the live worktree and refreshed audit,
investigate the drift, and preserve rather than discard changes.

After completing each package, use at least:

```powershell
.\.venv\Scripts\python.exe tools\audit_leetcode_migration.py
.\.venv\Scripts\python.exe tools\check_leetcode_dataset.py
.\.venv\Scripts\python.exe -m pytest server\tests\test_validated_cases.py server\tests\test_dynamic_docs.py -q
git diff --check
```

For the next native candidate, replace the frontend ID in:

```powershell
$env:ELECTRON_RUN_AS_NODE=$null
npx.cmd --prefix electron electron electron/scripts/verify-leetcode-candidate.cjs lc_1614
```

## Exact prompt for a new Codex session

Copy and paste this entire block into the new session:

> Resume the active canonical LeetCode migration in `C:\dawei7\code_n` with
> the full goal of completing every problem through frontend ID 3985. Stay on
> the existing local branch `main` and preserve every local change, including
> the separate visualization framework work. Before
> changing anything, read `AGENTS.md`, `BENCHMARKING.md`,
> `LEETCODE_SUBMISSIONS.md`, `dsa/leetcode/_template.md`,
> `dsa/leetcode/_reports/ORIGINAL_18_BLOCKER_PLAYBOOK.md`,
> `dsa/leetcode/_reports/ACTIVE_MIGRATION_HANDOFF.md`, and
> `dsa/leetcode/_reports/two_sum_migration_progress.md` completely. Then run a
> fresh migration audit and treat the live worktree and generated reports as
> authoritative. Problems through frontend ID 1613 are locally complete;
> 1566 packages are remotely verified. Problems 1413 through 1426 have
> recorded Electron credential-decryption blockers, while 1463 through 1495
> have recorded Chrome-not-running launch-policy blockers. The expected first
> actionable package is
> `dsa/leetcode/1614_maximum-nesting-depth-of-the-parentheses`,
> but follow
> the refreshed audit if it differs.
> Continue autonomously in numeric frontend-ID order and do not stop after
> planning. For each package, follow the early-verification order in
> `LEETCODE_SUBMISSIONS.md`: confirm contract and native interface, minimally
> sanity-check the exact native source, obtain remote Accepted evidence, then
> use that accepted source to anchor the app-local adapter, comprehensive
> cases, and complexity calibration. If rejection reveals misunderstood
> semantics, revise the document, cases, expected outputs, both solution forms,
> and affected benchmark together rather than patching only the submission.
> If any of the original eighteen complexity blockers reappears,
> follow the playbook's reviewed per-ID recovery path and do not stop at the
> stale blocker record. For every problem, finish the source-faithful original
> documentation, correctness cases, complexity verification through exactly
> three complexity-sensitive benchmark tiers or a strictly validated
> non-scaling certificate when the legal contract cannot support scaling,
> optimal app-local solution, separate native LeetCode
> artifact, remote Accepted verification where permitted, regression checks,
> and progress or blocker documentation. Keep canonical package directory
> prefixes four digits, while leaving personal user-data paths unpadded. In
> `Goal`, preserve the source's technical vocabulary, logical order, semantic
> detail, and proportionate length; rephrase only to improve clarity or remain
> independently written, never for variation alone and never by changing terms
> such as `ascending` into `non-decreasing`. Use LaTeX for abstract mathematics
> and complexity, define long expressions with a short mathematical symbol,
> and keep executable assignments, indexing, function calls, slices, pointer
> changes, operators, strings, and serialized values in code spans rather than
> LaTeX. `Required Complexity` must contain only `- **Time:** $O(...)$` and
> `- **Space:** $O(...)$`, with any problem-specific symbols defined earlier.
> Inside Approach, use only `General`, `Complexity detail`, and `Alternatives
> and edge cases` as real headings. Use problem-specific bold signposts inside
> substantial General explanations without creating another repeated prose
> template. Documentation quality and completeness take priority over brevity
> or token conservation: never shorten `doc.md` to save tokens or finish a
> package faster, and use as many problem-specific bold signposts as its
> distinct reasoning stages require. Keep `Alternatives and edge cases`
> entirely as bullets: bold-name
> each alternative and give separate bullets for material edge cases. Preserve
> LeetCode frontend IDs separately from backend `question_id` values. Use the
> existing Electron credential bridge for the in-scope remote submissions
> already authorized by the user without asking for per-problem confirmation
> when the environment permits it. For benchmarked packages, a correct
> slower-class candidate must return all expected outputs and fail the scaling
> verdict, not a safety cap. A certificate is allowed only under the reviewed
> rules in `BENCHMARKING.md`. If a problem is genuinely blocked, record exact
> evidence and move on.
> Do not commit, push, merge, or release unless the user explicitly authorizes
> that new external change. If model capacity temporarily pauses the session,
> retry after about five minutes and continue from the refreshed audit.
