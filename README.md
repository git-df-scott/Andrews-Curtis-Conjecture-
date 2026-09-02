# Andrews-Curtis Conjecture: search framework and literature status

`acsearch` is a small Python package for studying balanced presentations of the
trivial group under Andrews-Curtis (AC) moves:

- `acsearch.words` - free-group words, reduction, cyclic canonical forms
- `acsearch.presentation` - presentations, canonical forms modulo signed
  generator permutations (a subgroup of Aut(F_n), under which AC-triviality is
  invariant)
- `acsearch.moves` - elementary AC moves (certificate moves) and the
  length-bounded cyclic-word move set used for exhaustive closure
- `acsearch.search` - greedy best-first search (Shehper et al. 2024 style) and
  breadth-first closure of the standard presentation within a length bound
- `acsearch.verify` - certificate replay and Todd-Coxeter check that a
  candidate really presents the trivial group (via sympy)
- `acsearch.candidates` - Akbulut-Kirby AK(n), Miller-Schupp MS(n,w), the
  classical two- and three-generator candidates, and the six length-14
  Miller-Schupp presentations that resisted greedy search

Run the tests with `python3 -m pytest tests`.

Status of the conjecture itself (checked September 2026): open. No
counterexample is known; see the literature notes in `docs/` as they are added.
