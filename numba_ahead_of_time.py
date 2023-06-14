from time import perf_counter

from locate_pixelcolor_numba2 import search_colors as search_colors2
import cv2
import numpy as np
def search_colors(pic, colors):
    if not isinstance(colors,np.ndarray):
        colors = np.array(colors,dtype=np.uint8)

    r = np.ascontiguousarray(pic[..., 0].flatten())
    g = np.ascontiguousarray(pic[..., 1].flatten())
    b = np.ascontiguousarray(pic[..., 2].flatten())
    divider =np.uint16(pic.shape[1])
    return search_colors2(r,g,b,colors,divider)
path = r"C:\Users\hansc\Downloads\pexels-alex-andrews-2295744.jpg"
pic = cv2.imread(path)

colors = np.array([(66,  71,  69),(62,  67,  65),(144, 155, 153),
                   (52,  57,  55),(127, 138, 136),(53,  58,  56),
                   (51,  56,  54),(32,  27,  18),(24,  17,   8),],dtype=np.uint8)
start = perf_counter()
ba=search_colors(pic,colors)
print(perf_counter() - start)

onecolor = np.array([(255,255,255)],dtype=np.uint8)
start = perf_counter()
ba0=search_colors(pic,colors)
print(perf_counter() - start)
