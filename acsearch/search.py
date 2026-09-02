"""Search algorithms on the AC graph."""
from __future__ import annotations
import heapq
from collections import deque
from typing import Callable, Dict, List, Optional, Tuple
from .words import Word, cyclic_canonical
from .moves import ac_neighbors, apply_move, cyclic_neighbors, Move
from .presentation import Presentation, symmetry_canonical, standard_key


def _is_standard(rels: Tuple[Word, ...], n: int) -> bool:
    return tuple(sorted(cyclic_canonical(r) for r in rels)) == standard_key(n)


def greedy_search(p: Presentation, max_rel_len: int, max_nodes: int = 1_000_000,
                  key: Callable[[Tuple[Word, ...]], object] | None = None,
                  include_inverse: bool = True,
                  target: Callable[[Tuple[Word, ...]], bool] | None = None
                  ) -> Optional[List[Move]]:
    """Best-first (greedy) search ordered by total relator length, as in
    Shehper et al. 2024.  Returns a certificate path of elementary moves from
    ``p`` to a presentation whose relators are (conjugates/inverses of) the
    generators, or None if the node budget is exhausted.
    """
    n = p.n
    key = key or (lambda r: tuple(sorted(cyclic_canonical(x) for x in r)))
    target = target or (lambda r: _is_standard(r, n))
    start = p.rels
    if target(start):
        return []
    parent: Dict[object, Tuple[object, Move, Tuple[Word, ...]]] = {}
    seen = {key(start)}
    heap = [(sum(map(len, start)), 0, start)]
    counter = 1
    visited = 0
    while heap and visited < max_nodes:
        _, _, rels = heapq.heappop(heap)
        visited += 1
        for mv, new in ac_neighbors(rels, n, max_rel_len, include_inverse):
            k = key(new)
            if k in seen:
                continue
            seen.add(k)
            parent[k] = (key(rels), mv, rels)
            if target(new):
                # reconstruct
                path = [mv]
                cur = key(rels)
                while cur in parent:
                    pk, pmv, prels = parent[cur]
                    path.append(pmv)
                    cur = pk
                path.reverse()
                return path
            heapq.heappush(heap, (sum(map(len, new)), counter, new))
            counter += 1
    return None


def bfs_closure(start: Tuple[Word, ...], n: int, max_total: int,
                limit: int | None = None, use_symmetry: bool = True,
                slack: int = 0, verbose: bool = False) -> Dict[Tuple[Word, ...], int]:
    """Breadth-first closure of ``start`` in the cyclic-word AC graph with
    total length <= max_total.  Returns dict state -> distance.  States are
    sorted tuples of cyclic canonical words (optionally canonical under signed
    generator permutations).
    """
    canon = (lambda r: symmetry_canonical(Presentation(n, r))) if use_symmetry \
        else (lambda r: tuple(sorted(cyclic_canonical(x) for x in r)))
    s0 = canon(start)
    dist = {s0: 0}
    q = deque([s0])
    while q:
        cur = q.popleft()
        d = dist[cur]
        for nb in cyclic_neighbors(cur, n, max_total, slack):
            c = canon(nb)
            if c not in dist:
                dist[c] = d + 1
                q.append(c)
                if limit and len(dist) >= limit:
                    return dist
        if verbose and len(dist) % 10000 < 1:
            print(len(dist), len(q))
    return dist
