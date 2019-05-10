# img-processing
Set of algorithms in developed in Image Processing class in Federal University of Tocantins

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
Usage: main.py [option] arg1

Options:
  --version             show program's version number and exit
  -h, --help            show this help message and exit
  -i PATH, --image=PATH
                        path of the image to be used.
  -t TYPE, --type=TYPE  Type of interpolation to be used. {neighbor, bilinear,
                        bicubic, labeling}
  -s FACTOR, --scale=FACTOR
                        Increase/decrease factor. It is must be greater than
                        0.25 or 25%. Can't use with --type = labeling [0 = 0%,
                        1.5 = 150%]
  -o OUTPUT, --output=OUTPUT
                        Name of output image. e.g: lena.png
```
Example of run a test:
```
$ python3 main.py -i img/lena.png -t bicubic -s 1.7 -o lena-1.7.png
algortihm used: bicubic
path of image: img/lena.png
Size of origin image: (512,512)

Function: bicubic(img_input, factor):
        New size of image: (870,870)

Time running: 8.0866s
Output image saved in: ./output/lena-1.7.png
```

## Authors
* **Felipe Rodrigues Costa**
* **Rafael da Costa Silva** - [RafaelSilva7](https://github.com/RafaelSilva7)

## License
This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/RafaelSilva7/img-processing/blob/master/LICENSE) file for details
