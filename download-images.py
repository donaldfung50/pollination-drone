import urllib.request
import cv2
import numpy as np
import os

def dl_negatives():
	#other image urls
	#people: http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n00007846
	#animals: http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n00015388
    neg_imgs = 'http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n03545756'   
    neg_urls = urllib.request.urlopen(neg_imgs).read().decode()
    num = 1651
    
    if not os.path.exists('neg'):
        os.makedirs('neg')
        
    for i in neg_urls.split('\n'):
        try:
            print(i)
            urllib.request.urlretrieve(i, "neg/"+str(num)+".jpg")
            img = cv2.imread("neg/"+str(num)+".jpg",cv2.IMREAD_GRAYSCALE)
            resized_image = cv2.resize(img, (100, 100))
            cv2.imwrite("neg/"+str(num)+".jpg",resized_image)
            num += 1
            
        except Exception as e:
            print(str(e))  

dl_negatives()