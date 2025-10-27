import numpy as np
import tensorflow as tf
from tensorflow.keras import datasets

fashion_mnist=tf.keras.datasets.fashion_mnist
(x_train,train_label),(x_test,test_label)=fashion_mnist.load_data()

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

model=tf.keras.Sequential([
   tf.keras.layers.Flatten(input_shape=(28,28)),
   tf.keras.layers.Dense(128,activation='relu'),
   tf.keras.layers.Dense(10)
   ])
model.compile(loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              optimizer='Adam',
              metrics=['accuracy'])
model.fit(x_train,train_label)
p_model=tf.keras.Sequential([model,
                             tf.keras.layers.Softmax()
                             ])

loss,acc=model.evaluate(x_test,test_label,verbose=2)
predictions=p_model.predict(x_test)
