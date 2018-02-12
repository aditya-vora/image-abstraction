# Image Abstraction

This python package creates an abstraction (cartoon) of an image given as input using bilateral filter.  

### Prerequisities

Packages required to run the code:  

* OpenCV 2.4.11
* Python Numpy
* Python Scipy

## Steps to run the code
* Clone the repository to your machine. 
```
cd folder
git clone https://github.com/aditya-vora/image-abstraction
cd image-abstraction
```

* Store the test images in the images folder
* Run the main script from terminal  

```
python main.py ./images/image.jpg 
python main.py ./images/image.jpg --kernel_size 5 --kernel_sigma [4,2] --q_level 10 --sigmaE 0.5 --phiE 1.0 --T 0.98 
```

## Referances

1. Winnemöller, Holger, Sven C. Olsen, and Bruce Gooch. "Real-time video abstraction." ACM Transactions On Graphics (TOG).      Vol. 25. No. 3. ACM, 2006. 

2. Tomasi, Carlo, and Roberto Manduchi. "Bilateral filtering for gray and color images." Computer Vision, 1998. Sixth            International Conference on. IEEE, 1998.

