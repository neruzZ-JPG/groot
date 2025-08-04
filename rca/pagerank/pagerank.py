import networkx as nx

__all__ = ["pagerank", "google_matrix"]

def pagerank(
    G,
    alpha=0.85,
    personalization=None,
    max_iter=100,
    tol=1.0e-6,
    nstart=None,
    weight="weight",
    dangling=None,
):
    
    return _pagerank_scipy(
        G, alpha, personalization, max_iter, tol, nstart, weight, dangling
    )



def _pagerank_scipy(
    G,
    alpha=0.85,
    personalization=None,
    max_iter=100,
    tol=1.0e-6,
    nstart=None,
    weight="weight",
    dangling=None,
):
    import numpy as np
    #import scipy as sp
    from .. import sparse_matrix
    from .. import errors

    N = len(G)
    if N == 0:
        return {}

    nodelist = list(G)
    # todo
    A = to_scipy_sparse_array(G, nodelist=nodelist, weight=weight, dtype=float)
    print(A)
    S = A.sum_axis(axis=1)
    print(S)
    S[S != 0] = 1.0 / S[S != 0]
    # TODO: csr_array
    Q = sparse_matrix.CSRSparseMatrix(sparse_matrix.spdiags(S.T, 0, *A.shape))
    A = Q @ A

    # initial vector
    if nstart is None:
        x = np.repeat(1.0 / N, N)
    else:
        x = np.array([nstart.get(n, 0) for n in nodelist], dtype=float)
        x /= x.sum()

    # Personalization vector
    if personalization is None:
        p = np.repeat(1.0 / N, N)
    else:
        p = np.array([personalization.get(n, 0) for n in nodelist], dtype=float)
        if p.sum() == 0:
            raise ZeroDivisionError
        p /= p.sum()
    # Dangling nodes
    if dangling is None:
        dangling_weights = p
    else:
        # Convert the dangling dictionary into an array in nodelist order
        dangling_weights = np.array([dangling.get(n, 0) for n in nodelist], dtype=float)
        dangling_weights /= dangling_weights.sum()
    is_dangling = np.where(S == 0)[0]

    # power iteration: make up to max_iter iterations
    for _ in range(max_iter):
        xlast = x
        x = alpha * (x @ A + sum(x[is_dangling]) * dangling_weights) + (1 - alpha) * p
        # check convergence, l1 norm
        err = np.absolute(x - xlast).sum()
        if err < N * tol:
            return dict(zip(nodelist, map(float, x)))
    raise errors.PowerIterationFailedConvergence(max_iter)

def to_scipy_sparse_array(G, nodelist=None, dtype=None, weight="weight", format="csr"):
    #import scipy as sp
    from .. import sparse_matrix
    from .. import errors
    
    if len(G) == 0:
        raise errors.NetworkXError("Graph has no nodes or edges")

    if nodelist is None:
        nodelist = list(G)
        nlen = len(G)
    else:
        nlen = len(nodelist)
        if nlen == 0:
            raise errors.NetworkXError("nodelist has no nodes")
        nodeset = set(G.nbunch_iter(nodelist))
        if nlen != len(nodeset):
            for n in nodelist:
                if n not in G:
                    raise errors.NetworkXError(f"Node {n} in nodelist is not in G")
            raise errors.NetworkXError("nodelist contains duplicates.")
        if nlen < len(G):
            G = G.subgraph(nodelist)

    index = dict(zip(nodelist, range(nlen)))
    coefficients = zip(
        *((index[u], index[v], wt) for u, v, wt in G.edges(data=weight, default=1))
    )
    try:
        row, col, data = coefficients
    except ValueError:
        # there is no edge in the subgraph
        row, col, data = [], [], []

    if G.is_directed():
        A = sparse_matrix.COOSparseMatrix(data, row, col, shape=(nlen, nlen), dtype=dtype)
    else:
        # symmetrize matrix
        d = data + data
        r = row + col
        c = col + row
        # selfloop entries get double counted when symmetrizing
        # so we subtract the data on the diagonal
        selfloops = list(nx.selfloop_edges(G, data=weight, default=1))
        if selfloops:
            diag_index, diag_data = zip(*((index[u], -wt) for u, v, wt in selfloops))
            d += diag_data
            r += diag_index
            c += diag_index
        A = sparse_matrix.COOSparseMatrix(d, r, c, shape=(nlen, nlen), dtype=dtype)
    try:
        return A.asformat(format)
    except ValueError as err:
        raise errors.NetworkXError(f"Unknown sparse matrix format: {format}") from err
    

def selfloop_edges(G, data=False, keys=False, default=None):
    if data is True:
        if G.is_multigraph():
            if keys is True:
                return (
                    (n, n, k, d)
                    for n, nbrs in G.adj.items()
                    if n in nbrs
                    for k, d in nbrs[n].items()
                )
            else:
                return (
                    (n, n, d)
                    for n, nbrs in G.adj.items()
                    if n in nbrs
                    for d in nbrs[n].values()
                )
        else:
            return ((n, n, nbrs[n]) for n, nbrs in G.adj.items() if n in nbrs)
    elif data is not False:
        if G.is_multigraph():
            if keys is True:
                return (
                    (n, n, k, d.get(data, default))
                    for n, nbrs in G.adj.items()
                    if n in nbrs
                    for k, d in nbrs[n].items()
                )
            else:
                return (
                    (n, n, d.get(data, default))
                    for n, nbrs in G.adj.items()
                    if n in nbrs
                    for d in nbrs[n].values()
                )
        else:
            return (
                (n, n, nbrs[n].get(data, default))
                for n, nbrs in G.adj.items()
                if n in nbrs
            )
    else:
        if G.is_multigraph():
            if keys is True:
                return (
                    (n, n, k) for n, nbrs in G.adj.items() if n in nbrs for k in nbrs[n]
                )
            else:
                return (
                    (n, n)
                    for n, nbrs in G.adj.items()
                    if n in nbrs
                    for i in range(len(nbrs[n]))  # for easy edge removal (#4068)
                )
        else:
            return ((n, n) for n, nbrs in G.adj.items() if n in nbrs)
