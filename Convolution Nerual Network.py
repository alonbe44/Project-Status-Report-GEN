#  Copyright (c) 2023. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia accumsan.
#  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
#  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget metus.
#  Vestibulum commodo. Ut rhoncus gravida arcu.
import time

import  numpy as np
import scipy.signal
import PIL
from PIL import Image
import requests
from io import BytesIO
from PIL import ImageFilter
from PIL import ImageEnhance
from IPython.display import display
import numpy as np

def convolotionfun():
    conv =np.convolve([1, 2, 3], [4, 5, 6])
    print(conv)

    arr1=np.random.random(100000)
    arr2=np.random.random(100000)
    st=time.time()
    avr=np.convolve(arr1,arr2)
    end=time.time()
    print(end-st)
    st=time.time()

    avr=scipy.signal.fftconvolve(arr1,arr2)
    end=time.time()
    print(end-st)

def imageprc():
    img = Image.open("C:/Users/Abdelrahman.Rasem/PycharmProjects/Project-Status-Report-GEN/pair_plot.png")
    print(img.mode)
    print(img.size)
    print(img.format)
    print(img.is_animated)
    print(img.n_frames)
    print(img.getpixel((0, 0)))
    kernel = np.array([[1/9, 1/9, 1/9],
                       [1/9, 1/9, 1/9],
                       [1/9, 1/9, 1/9]])
    # Iterate through the pixels and print their color information

    image_height, image_width = img.size[0],img.size[1]
    kernel_height, kernel_width = kernel.shape
    output = np.zeros((image_height, image_width))
    for i in range(0, img.size[0]):
        for j in range(0, img.size[1]):
            # Apply the convolution operation at pixel (i, j)
            value = 0
            for m in range(kernel_height):
                for n in range(kernel_width):
                    if i - m >= 0 and i - m < image_height and j - n >= 0 and j - n < image_width:
                        value += img[i - m, j - n] * kernel[m, n]
            output[i, j] = value
            # pixel = img.getpixel((i, j))
            # if pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0 and pixel[3] == 255:
            #     print(f"Pixel at ({i}, {j}) is opaque black: R={pixel[0]}, G={pixel[1]}, B={pixel[2]}, A={pixel[3]}")
            # elif pixel[0] == 255 and pixel[1] == 255 and pixel[2] == 255 and pixel[3] == 255:
            #     a=1
            #    # print(f"Pixel at ({i}, {j}) is opaque white: R={pixel[0]}, G={pixel[1]}, B={pixel[2]}, A={pixel[3]}")
            # else:
            #     print(
            #         f"Pixel at ({i}, {j}) is neither opaque black nor opaque white: R={pixel[0]}, G={pixel[1]}, B={pixel[2]}, A={pixel[3]}")
            print(output)




import keras
from keras.datasets import mnist
from keras import models
from keras import layers

(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

network=models.Sequential()
network.add(layers.Dense(512, activation='relu', input_shape=(28 * 28,)))
network.add(layers.Dense(10, activation='softmax'))

network.compile(optimizer='rmsprop',
                loss='categorical_crossentropy',
                metrics=['accuracy'])

train_images = train_images.reshape((60000, 28 * 28))
train_images = train_images.astype('float32') / 255

test_images = test_images.reshape((10000, 28 * 28))
test_images = test_images.astype('float32') / 255

from keras.utils import to_categorical

train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)

network.fit(train_images, train_labels, epochs=5, batch_size=128)
test_loss, test_acc = network.evaluate(test_images, test_labels)
print('test_acc:', test_acc*100)
