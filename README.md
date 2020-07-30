# pollination-drone
Files used to create a Haar Cascade that recognizes sunflowers. Cascade was then put on a Raspberry Pi and used on a proof-of-concept pollination drone. Code was lightly modified from the following tutorial: https://pythonprogramming.net/haar-cascade-object-detection-python-opencv-tutorial/

Download-images.py is used to download negative images from ImageNet. It also resizes the images to 100x100 and grayscales them. The actual training used over 2000 negative images. Sample negative images can be found in the sample-neg folder. 

Delete-uglies.py then finds the images that are pictures of nothing and deletes them. These images are downloaded when the original link to the image from ImageNet are no longer valid. Example uglies can be found in the uglies folder.

Create-descriptor.py is used to create the negative image descriptor file bg.txt. This is used later on to create the positive samples.

Once all the files are downloaded and created, the opencv_createsamples command is used to create the positive images. This is done by taking sunflower.png and transplanting it in different positions on the negative images. Again, the actual training used over 2000 positive images and examples can be found in the sample-pos folder. THe same command is then run one more time to create the positives.vec file.

After all the positive images are created, the actual training can be done. Using the opencv_traincascade command, the sunflower Haar Cascade is completed. Since the number of images used in this particular training was relatively small at ~2000, the cascade was created in only 8 stages. Run-cascade.py uses the connected webcam and the sunflower cascade to box any sunflowers seen in the video stream. Code was then used with an Arduino to control a vibration motor. Whenever the Raspberry Pi cam saw a sunflower, it sent a signal to the Arduino which would in turn power the motor. This can be viewed in the following video: https://youtu.be/oDJAULfGk7A.
