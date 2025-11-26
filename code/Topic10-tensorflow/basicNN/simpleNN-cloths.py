# simple neural network using tensor flow to interpretfashion items
# 
# Author: Andrew Beatty

#### Libraries
# My libraries
import utils

# Third-party libraries
from tensorflow import keras
import tensorflow as tf


# Helper libraries
import numpy as np


class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

def run_neural_net():
    fashion_mnist = keras.datasets.fashion_mnist  # load dataset

    (train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()  # split into tetsing and training
    
    # I used this code to inspect the data
    #image_num = 100
    #print (f"{train_images[image_num]},\n label: {train_labels[image_num]}")
    #utils.show_image(train_images[image_num], train_labels[image_num],class_names[train_labels[image_num]])
 
    # build the net
    model = keras.Sequential([
        keras.layers.Flatten(input_shape=(784,1)),  # input layer (1)
        keras.layers.Dense(128, activation='relu'),  # hidden layer (2)
        keras.layers.Dense(10, activation='softmax')  # output layer (3)
    ])

    model.compile(optimizer='adam',
                loss='sparse_categorical_crossentropy',
                metrics=['accuracy'])

    # I put in an epock of 1 to speed this up but we can run it more times if required
    model.fit(train_images, train_labels, epochs=1)

    validation_loss, validation_acc = model.evaluate(test_images,  test_labels, verbose=1)
    print(f'Validation accuracy:{validation_acc}\nloss: {validation_loss}')

    # make predictions
    print("\n\nnow ready to run predictions")
    predictions = model.predict(test_images)

    max = len(test_images)
    num = num = utils.get_number(max)
    while num != -1:
        #image = test_data[num][0]
        image= test_images[num]
        label = test_labels[num]
        guess = np.argmax(predictions[num])
        utils.show_image(image, f"{label} {class_names[label]}" , f"{guess} {class_names[guess]}")
        num = utils.get_number(max)


if __name__ == '__main__':
    run_neural_net()
