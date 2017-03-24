import  numpy
import cv2
import PIL
from PIL import Image


def resizeImage(matrix):
    print matrix.shape
    im = PIL.Image.fromarray(numpy.uint8(matrix))
    img = im.resize((256, 256), PIL.Image.ANTIALIAS)
    img.save('testq.png')
    img.show()

def matchSize(matrix):
     height = matrix.shape[0]
     width = matrix.shape[1]
     diff = abs(height - width)
     if(height == width) :
         resizeImage(matrix)
     else :
         if(height > width):
             for num in range(diff/2) :
                 matrix = numpy.delete(matrix,0, 0)
                 matrix = numpy.delete(matrix,matrix.shape[0]-1, 0)
                 print num
             matchSize(matrix)
         else :
             for num in range(diff / 2):
                 matrix = numpy.delete(matrix, 0, 1)
                 matrix = numpy.delete(matrix, matrix.shape[1] - 1, 1)
                 print num

             matchSize(matrix)

numpy.set_printoptions(threshold=numpy.inf)
matrix = numpy.asarray(Image.open('black.jpg').convert('L'))
print matrix.shape
matchSize(matrix)



