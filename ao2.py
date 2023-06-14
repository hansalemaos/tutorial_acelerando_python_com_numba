from numba_aot_compiler import compnumba #pip install numba-aot-compiler
import numpy as np
from numba import uint8, uint16


def search_colors(r, g, b, rgbs, divider):
    res = np.zeros(b.shape, dtype=np.uint16)
    res2 = np.zeros(b.shape, dtype=np.uint16)
    zaehler = 0
    for rgb in rgbs:
        rr, gg, bb = rgb
        for i in range(r.shape[0]):
            if r[i] == rr:
                if g[i] == gg:
                    if b[i] == bb:
                        dvquot, dvrem = divmod(i, divider)
                        res[zaehler] = dvquot
                        res2[zaehler] = dvrem
                        zaehler = zaehler + 1
    results = np.dstack((res[:zaehler], res2[:zaehler]))
    return results


compi2 = compnumba(
    fu=search_colors,
    funcname="search_colors",
    file="searchcolorsnumba",
    folder="locate_pixelcolor_numba2",
    signature=(uint8[:], uint8[:], uint8[:], uint8[:, :], uint16),
    parallel=True,
    fastmath=True,
    nogil=True,
)