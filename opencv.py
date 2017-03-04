import cv2
import glob
import random
import os
def createFolder(path):
    os.makedirs(path)

def flipAndRotate(minangle, maxangle, flip,) :
    for img in glob.glob("*.jpg"):
        imagename = os.path.splitext(img)[0]
        img = cv2.imread(img, 1)
        createFolder(imagename)
        for i in range(0, 5):
            rows, cols ,zdim = img.shape
            angle = random.randint(minangle, maxangle)
            # cv2.getRotationMatrix2D(center, angle, scale)
            M = cv2.getRotationMatrix2D((cols / 2, rows / 2), angle, 1)
            # wrapAlline(source,martrix,size)
            # verticleflip = 1, horixontalflip = 0
            dst = cv2.warpAffine(img, M, (cols, rows))
            resultimage = cv2.flip(dst, flip)
            resultpath = imagename + "/"+imagename + str(i) + ".jpeg"
            cv2.imwrite(resultpath, resultimage)


def takeInputArguments () :
    print "arguments: minangle ,maxangle, flip "
    print "verticleflip = 1, horixontalflip = 0"
    flipAndRotate(int(input('minangle')), int(input('maxangle')), int(input('flip')))

takeInputArguments()
