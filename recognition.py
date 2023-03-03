from tensorflow.python.ops.control_flow_ops import case_v2
from IPython.lib.display import isfile
import numpy as np
import os
from google.colab.patches import cv2_imshow
import cv2
import matplotlib as plt
import tensorflow as tf

# mnist = tf.keras.datasets.mnist
# (x_train, y_train), (x_test, y_test) = mnist.load_data()
# x_train = tf.keras.utils.normalize(x_train, axis=1)
# x_test = tf.keras.utils.normalize(x_test, axis=1)

# model = tf.keras.models.Sequential()
# model.add(tf.keras.layers.Flatten(input_shape=(28, 28)))
# model.add(tf.keras.layers.Dense(128, activation='relu'))
# model.add(tf.keras.layers.Dense(128, activation='relu'))
# model.add(tf.keras.layers.Dense(10, activation='softmax'))

# model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# model.fit(x_train, y_train, epochs=3)
# model.save('language_recognition.model')

model = tf.keras.models.load_model('language_recognition.model')
# loss, accuracy = model.evaluate(x_test, y_test)

#print(loss)
#print(accuracy)
image_number = 1
while os.path.isfile(f"English_digits/digit{image_number}.png"):
    try:
        img = cv2.imread(f"English_digits/digit{image_number}.png")[:,:,0]
        img = np.invert(np.array([img]))
        prediction = model.predict(img)
        print(f"This is probably an english digit of {np.argmax(prediction)}")
        cv2_imshow(img[0])
        #plt.show()
    except:
        print("Error!")
    finally:
        image_number += 1







