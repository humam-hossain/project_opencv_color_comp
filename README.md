# Color Comparison with OpenCV in python

## Getting started

```
$ pip install opencv-contrib-python numpy matplotlib Pillow
$ cd src
$ python main.py
```

## Sample Output
![Output Sample](https://i.ibb.co/kgb6J90/output-tshirt-sample-2.png)
![Output Sample](https://i.ibb.co/48fsp74/output-tshirt-sample-1.png)
![Output Sample](https://i.ibb.co/C8wBj1j/output-sample.png)

## Limitations

The two input images must have the same size/dimensions and also suffers from a few problems including scaling, translations, rotations, and distortions. For images that do not have the same dimensions, we must switch from identifying pixel-similarity to object-similarity using deep-learning feature models instead of comparing individual pixel values.

### Noise
Noise exists in output

![Output Noise](https://i.ibb.co/7KPFjmN/output-noise.png)

### Complex sample
Doesn't work on complex samples

![Output complex sample](https://i.ibb.co/stvwZ25/output-complex.png)