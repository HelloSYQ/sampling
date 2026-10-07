
import matplotlib.pyplot as plt
import cv2
import numpy as np
from matplotlib.colors import BoundaryNorm
from matplotlib.ticker import MaxNLocator
from scipy.integrate import quad
from scipy.linalg import inv
from scipy.linalg import det
from astropy.io import fits

dfu = fits.open("hsttest001.fits")
data = dfu[0].data
print(np.min(data))

im = plt.imshow(data,cmap='gray')
plt.colorbar()
plt.savefig('hsttest001.png',dpi=300)
