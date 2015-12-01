__author__ = 'Xin'
def rec_dfs(G, s, S=None):
    if S is None: S = set()
    S.add(s)
    for u in G[s]:
        if u in S: continue
        rec_dfs(G, u, S)

def iter_dfs(G, s):
    S, Q = set(), []
    Q.append(s)
    while Q:
        u = Q.pop()
        if u in S: continue
        S.add(u)
        Q.extend(G[u])
        yield u

a, b, c, d, e, f, g, h = range(8)
N= [{b, c, d, e, f},  {c, e}, {d}, {e},  {f},  {c, g, h},  {f, h},  {f, g}]
print(list(iter_dfs(N,a)))


# Listing 5-7. Depth-First Search with Timestamps
def dfs(G, s, d, f, S=None, t=0):
    if S is None: S = set()
    d[s] = t; t += 1
    S.add(s)
    for u in G[s]:
        if u in S: continue
        t = dfs(G, u, d, f, S, t)
    f[s] = t; t += 1
    return t
# Initialize the history
# Set discover time
# We've visited s
# Explore neighbors
# Already visited. Skip
# Recurse; update timestamp
# Set finish time
# Return timestamp