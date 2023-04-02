import numpy 
import cv2


''' 
    with numpy we can create 1,2,3 dimentional arraies, 
    and we can reshape the arrays to any dimentional way we need.
'''
a = numpy.arange(27)
type(a)
a= a.reshape(3,9)
print(a)
n = numpy.asarray([[1,2,3,4,5],[1,2,6,7,8],[1,2,10,11,12]])
# print(n)
# print("new")
# print(n[1:3,2:])


'''
    Reading imgs as an array, it prints the rows and columns 
    0 : read it in gray scale, 1: colorful as BRG
'''
#READING
img = cv2.imread("img.png",0)
#print(img)

#WRITING AN IMG
cv2.imwrite("newImg.png",img)
img[0:2,0:3]

# for i in img:
#     print(i)
    
# for i in img.T:
    

    
# for i in img.flat:
#     print (i)
stacking = numpy.vstack(([1,2,3],[4,5,6]))
# stacking = numpy.vstack(([1,2,3],[4,5,6]))
print(stacking)
print()

ar1= numpy.hsplit(stacking,3)
# ar1= numpy.vsplit(stacking,2)
print(ar1)