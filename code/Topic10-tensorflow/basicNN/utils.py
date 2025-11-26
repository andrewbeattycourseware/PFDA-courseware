import tensorflow as tf
from tensorflow import keras

# Helper libraries
import numpy as np
import matplotlib.pyplot as plt


def show_image(data, label, guess):
    #print (len(data))
    #print (sqrt(len(data)))
    tensor = tf.Variable(data, dtype=tf.float32)
    img = tf.reshape(tensor, [28, -1])

    plt.figure()
    plt.imshow(img, cmap=plt.cm.binary)
    plt.title(f"Expected: { label}")
    plt.xlabel(f"Guess: { guess}")
    plt.colorbar()
    plt.grid(False)
    plt.show()


def get_number(max):
    while True:
        num = input("Pick a number(non digit to quit): ")
        if num.isdigit():
            num = int(num)
            if num <= max:
                return int(num)
            else:
                print(f"Try again..less than {max}")
        else:
            return -1
