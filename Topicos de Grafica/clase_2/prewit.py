
import numpy as np
import cv2

def prewit(imgTest,kernel):

    imgFilter = imgTest.copy()

    n , m = imgTest.shape
    nK, mK = kernel.shape
    ptoMiddle = nK//2

    for i in range(n - nK + 1):
        for j in range(m - mK + 1):
            slicing = imgTest[i:i+nK, j:j+mK]
            multiMatrix = np.multiply(slicing,kernel)
            sum = np.sum(multiMatrix) / (nK*mK)
            
            imgFilter[i+ptoMiddle][j+ptoMiddle] = sum
    return imgFilter




imgGray = cv2.imread('./img/monedas.png' ,0)
cv2.imshow("original", imgGray)



    
kernel = np.array([[-1,0,1],
                   [-1,0,1],
                   [-1,0,1]])

imgFilter = prewit(imgGray,kernel)
cv2.imshow("prewit", imgFilter)

filename = './img/' + 'prewit' + str(3) + 'x' + str(3) + 'monedas.jpg'
cv2.imwrite(filename, imgFilter)

cv2.waitKey(0)
