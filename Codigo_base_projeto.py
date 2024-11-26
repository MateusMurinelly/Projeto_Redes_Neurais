import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator, load_img, img_to_array
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.callbacks import ModelCheckpoint, ReduceLROnPlateau, EarlyStopping
from keras.preprocessing import image
from tensorflow.keras.utils import load_img
from keras.metrics import Accuracy, Precision, Recall


batch_size = 32
epochs = 15
input_shape = (150, 150, 3)  # Tamanho das imagens de entrada


data_generator = ImageDataGenerator(rescale=1./255, validation_split=(0.3))
path = '/content/drive/MyDrive/Pasta sem nome/train'

train_generator = data_generator.flow_from_directory(
    path,
    target_size=input_shape[:2],
    shuffle=True,
    batch_size=batch_size,
    class_mode='categorical',
    subset='training')

validation_generator = data_generator.flow_from_directory(
    path,
    target_size=input_shape[:2],
    shuffle=True,
    batch_size=batch_size,
    class_mode='categorical',
    subset='validation')


filepeath = 'transferlearning_weigths.hdf5'
checkpoint = ModelCheckpoint(filepeath, monitor='val_loss', verbose=1, save_best_only=True, mode='max')

lr_reduce = ReduceLROnPlateau(monitor= 'val_loss', factor=0.8, min_delta= 0.001, patience= 3, verbose=1)

early_stop = EarlyStopping(monitor='val_loss', min_delta=0.001, patience= 5, verbose=1, mode='min')

callbacks = [ lr_reduce, checkpoint, early_stop]


model = Sequential()

model.add(Conv2D(64, (3, 3), activation='relu', input_shape=input_shape ))
model.add(MaxPooling2D(pool_size=2))
model.add(Dropout(0.3))

model.add(Conv2D(128, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=2))
model.add(Dropout(0.3))

model.add(Flatten())

model.add(Dense(256, activation='relu'))
model.add(Dropout(0.4))

model.add(Dense(2, activation='sigmoid'))

model.summary()


model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy', Precision(), Recall()])


model.fit(train_generator,
          steps_per_epoch=train_generator.samples//batch_size,
          epochs=epochs,
          validation_data=validation_generator,
          validation_steps=validation_generator.samples//batch_size,
          callbacks = callbacks)



test_loss, test_accuracy, test_precision, test_recall = model.evaluate(validation_generator, verbose=1)

print('Perda de teste:', test_loss)
print('Acurácia de teste:', test_accuracy)
print('Precisão de teste:', test_precision)
print('Teste de Recall', test_recall)

f1_score_divisor= test_precision * test_recall
f1_score_dividendo = test_precision + test_recall

f1 = (2*f1_score_divisor) / f1_score_dividendo
print(f1)

