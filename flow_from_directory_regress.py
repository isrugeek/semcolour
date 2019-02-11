#* coding=utf-8 */
import tensorflow as tf
import os
import keras
from keras.preprocessing import image
from keras.layers import Dense, GlobalAveragePooling2D, Flatten,Dropout
from keras import backend as K
from keras.models import Model
#from keras.applications.resnet50 import ResNet50,preprocess_input
from keras.applications.inception_resnet_v2 import InceptionResNetV2, preprocess_input
import numpy as np
import math
from livelossplot import PlotLossesKeras
from os import walk
from keras.callbacks import ModelCheckpoint
import matplotlib.pyplot as plt

# customize keras old class


class DirectoryIterator(image.DirectoryIterator):
    def __init__(self,
                 directory,
                 image_data_generator,
                 target_size=(256, 256),
                 color_mode='rgb',
                 classes=None,
                 class_mode='categorical',
                 batch_size=32,
                 shuffle=True,
                 seed=None,
                 data_format=None,
                 save_to_dir=None,
                 save_prefix='',
                 save_format='png',
                 follow_links=False,
                 subset=None,
                 interpolation='nearest'):
        super(DirectoryIterator, self).__init__(
            directory,
            image_data_generator,
            target_size=target_size,
            color_mode=color_mode,
            classes=classes,
            class_mode=class_mode,
            batch_size=batch_size,
            shuffle=shuffle,
            seed=seed,
            data_format=data_format,
            save_to_dir=save_to_dir,
            save_prefix=save_prefix,
            save_format=save_format,
            follow_links=follow_links,
            subset=subset,
            interpolation=interpolation)
        self.batch_x_cb = None
        self.batch_y_cb = None

    def register_batch_process(self, batch_x_cb=None, batch_y_cb=None):
        self.batch_x_cb = batch_x_cb
        self.batch_y_cb = batch_y_cb

    def _get_batches_of_transformed_samples(self, index_array):
        batch_x = np.zeros((len(index_array),) + self.image_shape, dtype=K.floatx())
        grayscale = self.color_mode == 'grayscale'
        # build batch of image data
        for i, j in enumerate(index_array):
            fname = self.filenames[j]
            img = image.load_img(
                os.path.join(self.directory, fname),
                grayscale=grayscale,
                target_size=self.target_size,
                interpolation=self.interpolation)
            x = image.img_to_array(img, data_format=self.data_format)
            x = self.image_data_generator.random_transform(x)
            x = self.image_data_generator.standardize(x)
            batch_x[i] = x
        # optionally save augmented images to disk for debugging purposes
        if self.save_to_dir:
            for i, j in enumerate(index_array):
                img = image.array_to_img(batch_x[i], self.data_format, scale=True)
                fname = '{prefix}_{index}_{hash}.{format}'.format(
                    prefix=self.save_prefix,
                    index=j,
                    hash=np.random.randint(1e7),
                    format=self.save_format)
                img.save(os.path.join(self.save_to_dir, fname))
        # build batch of labels
        invalid_mode = False
        if self.class_mode == 'input':
            batch_y = batch_x.copy()
        elif self.class_mode == 'sparse':
            batch_y = self.classes[index_array]
        elif self.class_mode == 'binary':
            batch_y = self.classes[index_array].astype(K.floatx())
        elif self.class_mode == 'categorical':
            batch_y = np.zeros((len(batch_x), self.num_classes), dtype=K.floatx())
            for i, label in enumerate(self.classes[index_array]):
                batch_y[i, label] = 1.
        # Add Regression Support
        else:
            batch_y = None
            invalid_mode = True
        if self.batch_x_cb:
            batch_x = self.batch_x_cb(batch_x, self.filenames, index_array)
        if batch_y is not None and self.batch_y_cb:
            batch_y = self.batch_y_cb(batch_y, self.filenames, index_array)
        if invalid_mode:
            return batch_x
        return batch_x, batch_y


class ImageDataGeneratorReg(image.ImageDataGenerator):
    def flow_from_directory(self,
                            directory,
                            target_size=(256, 256),
                            color_mode='rgb',
                            classes=None,
                            class_mode='categorical',
                            batch_size=32,
                            shuffle=True,
                            seed=None,
                            save_to_dir=None,
                            save_prefix='',
                            save_format='png',
                            follow_links=False,
                            subset=None,
                            interpolation='nearest'):

        return DirectoryIterator(
            directory,
            self,
            target_size=target_size,
            color_mode=color_mode,
            classes=classes,
            class_mode=class_mode,
            data_format=self.data_format,
            batch_size=batch_size,
            shuffle=shuffle,
            seed=seed,
            save_to_dir=save_to_dir,
            save_prefix=save_prefix,
            save_format=save_format,
            follow_links=follow_links,
            subset=subset,
            interpolation=interpolation)
