# img-processing
Set of algorithms in developed in Image Processing class in Federal University of Tocantins

### List of implemented algorithms
* Interpolation (Nearest Neighbor, Bilinear, Bicubic)
```
$ python3 main.py -i <path> -a <algorithm> -f <float> -o <name>
```
* Labeling
```
$ python3 main.py -i <path> -a labeling -o <name>
```
* Histogram Processing (equalize)
```
$ python3 main.py -i <path> -a equalize -o <name>
```
* Intensity Transformation (Logarithmic and PowerLow)
```
$ python3 main.py -i <path> -a <algorithm> -f <float> [<float>] -o <name>
```
* Operators (arithmetic: add, subtract, division*, mltipy* and geometric: mirrorH, mirrorV, rotate*)
```
$ python3 main.py -i <path1> <path2> [<float1>, <float2>] -a <algorithm> -o <name>
```
* Morphology (binary: dilation, erosion, extractContours, opening*, ending* and gray: dilationGray3, dilationGray5, erosionGray3, erosionGray5)
```
$ python3 main.py -i <path> -a <algorithm> -e <path> -o <name>
```

*still in development

### Prerequisites
Python3.6
```
$ sudo apt install python3.6
```
Virtualenv
```
$ sudo apt-get install python3-pip
$ sudo pip3 install virtualenv 
```

### Installing
Create a new environment 
```
$ virtualenv <env_name>
```
Running environment 
```
$ source <env_name>/bin/activate
```
Install the requirements (in environment)
```
$ pip3 install -r requirements.txt
```

### Running the tests
For run the application is necessary run the encironment and inform:
```
$ source <env_name>/bin/activate
$ python3 main.py -h
Usage: main.py -i <path> -a <algorithm> [args]

Options:
  --version             show program's version number and exit
  -h, --help            show this help message and exit
  -i path, --image=path
                        path of the image to be used.
  -a name, --algorithm=name
                        Algorithm name to be used. List in README.md
  -f float, --factor=float
                        Increase/decrease for interpolation and constant for
                        the logarithmic transformation algorithm.
  -o name.png, --output=name.png
                        Name of output image. e.g: lena.png
  -m name, --mask=name  Mask name of filtering algorithms
  -e path, --structElement=path
                        Structuring element for morphology algorithms.
```
Example of run a test:
```
$ python3 main.py -i img/lena.png -a bicubic -f 1.7 -o lena-1.7.png
algortihm used: bicubic
path of image: img/lena.png
Size of origin image: (512,512)

Function: bicubic(img_input, factor):
        New size of image: (870,870)

Time running: 8.0866s
Output image saved in: ./output/lena-1.7.png
```

## Authors
* **Felipe Rodrigues Costa** - [FelipeFRC](https://github.com/FelipeFRC)
* **Rafael da Costa Silva** - [RafaelSilva7](https://github.com/RafaelSilva7)

## License
This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/RafaelSilva7/img-processing/blob/master/LICENSE) file for details
