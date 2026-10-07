
#!/usr/bin/python3

import numpy as np

            
def Gauss_Edge(Img, width, sigma):
    new_size = [Img.shape[0]+2*width,Img.shape[1]+2*width]
    new_img = np.zeros(new_size)
    new_img[width:Img.shape[0]+width,width:Img.shape[1]+width] = Img
    # up left region
    Xul = np.arange(-width, 0, 1.0)
    Yul = np.arange(-width, 0, 1.0)
    X1, Y1 = np.meshgrid(Xul, Yul)
    gauss_ul = Img[0][0]*np.exp(-(X1**2+Y1**2)/(2*sigma**2))
    new_img[0:width,0:width] = gauss_ul
    # up right region
    Xur = np.arange(0, width, 1.0)
    Yur = np.arange(0, width, 1.0)
    X2, Y2 = np.meshgrid(Xur, Yul)
    gauss_ur = Img[0][-1]*np.exp(-(X2**2+Y2**2)/(2*sigma**2))
    new_img[0:width,Img.shape[0]+width:Img.shape[0]+2*width] = gauss_ur
    # down left region
    X3, Y3 = np.meshgrid(Xul, Yur)
    gauss_dl = Img[-1][0]*np.exp(-(X3**2+Y3**2)/(2*sigma**2))
    new_img[Img.shape[0]+width:Img.shape[0]+2*width,0:width] = gauss_dl
    # down right region
    X4, Y4 = np.meshgrid(Xur, Yur)
    gauss_dr = Img[-1][-1]*np.exp(-(X4**2+Y4**2)/(2*sigma**2))
    new_img[Img.shape[0]+width:Img.shape[0]+2*width,Img.shape[0]+width:Img.shape[0]+2*width] = gauss_dr
    
    # up&down region
    Xu = Img[0,:]
    Xd = Img[-1,:]
    Yc = np.arange(0, width, 1.0)
    Y_exp = np.exp(-Yc**2/(2*sigma**2))
    invY = Y_exp[::-1]
    xx1,yy1 = np.meshgrid(Xu,Y_exp[::-1])
    up_region = xx1*yy1
    #up_region_new = np.outer(Xu,invY)
    xx2,yy2 = np.meshgrid(Xd,Y_exp)
    down_region = xx2*yy2
    new_img[0:width,width:Img.shape[0]+width] = up_region
    new_img[Img.shape[0]+width:Img.shape[0]+2*width,width:Img.shape[0]+width] = down_region
    # left&right region
    Yu = Img[:,0]
    Yd = Img[:,-1]
    Xc = np.arange(0, width, 1.0)
    X_exp = np.exp(-Xc**2/(2*sigma**2))
    xx3,yy3 = np.meshgrid(X_exp[::-1],Yu)
    left_region = xx3*yy3
    xx4,yy4 = np.meshgrid(X_exp,Yd)
    right_region = xx4*yy4
    new_img[width:Img.shape[0]+width,0:width] = left_region
    new_img[width:Img.shape[0]+width,Img.shape[0]+width:Img.shape[0]+2*width] = right_region
    return new_img

    