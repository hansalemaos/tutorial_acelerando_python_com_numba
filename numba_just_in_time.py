path = r"C:\Users\hansc\Downloads\pexels-alex-andrews-2295744.jpg"
from PIL import Image
from time import perf_counter
from numba import njit
import numpy as np
img = Image.open(path)
img = img.convert("RGB")
datas = np.array(img.getdata())
datalen = len(datas)
width, height = img.size

@njit(parallel=True)
def get_coords_with_pil(col):
    resultdata = []
    for index, item in enumerate(datas):
        if (item[0] == col[0] and item[1] ==
                col[1] and item[2] == col[2]):
            resultdata.append(divmod(index, width))
    return resultdata
@njit(parallel=True)
def get_coords_with_pilall(colors):
    resultdata = []
    for index, item in enumerate(datas):
        for col in colors:
            if (item[0] == col[2] and item[1] ==
                    col[1] and item[2] == col[0]):
                resultdata.append(divmod(index, width))
    return resultdata


colorsone = [(255,255,255)]
start = perf_counter()
ba0 = get_coords_with_pilall(colors=colorsone)
print(perf_counter()-start)

colorsall = [(66, 71, 69), (62, 67, 65), (144, 155, 153), (52, 57, 55),
             (127, 138, 136), (53, 58, 56), (51, 56, 54), (32, 27, 18),
             (24, 17, 8), ]
start = perf_counter()
ba = get_coords_with_pilall(colors=colorsall)
print(perf_counter()-start)

