import numpy as np  
import pandas as pd  
import os,sys,inspect
from support_functions import *


def read_and_train(read_func):
    # Read the data
    AnomalyData, data_train, data_test, labels_train, labels_test=read_func()

    # Merge the data
    data = np.concatenate((data_train, data_test))
    labels = np.concatenate((labels_train, labels_test))

    if AnomalyData.replicate_for_training >0:# If we only has very few data, we replicates the data before training
        data = np.tile(data, (AnomalyData.replicate_for_training,1))
        labels = np.tile(labels, AnomalyData.replicate_for_training)


    ## Compile and Train the model
    # Specify the model config
    encoder_layers_size, decoder_layers_size = get_deep_model_config(data.shape[1],AnomalyData.n_layers,AnomalyData.multiplier)

    # Training
    autoencoder,encoder = train_autoencoder(AnomalyData,data, labels,encoder_layers_size,decoder_layers_size,save_model = True)

    # Delete the data to release the space
    del data
    del labels
    del data_train
    del data_test
    del labels_train
    del labels_test
    dir()

# Update models according to the list
#read_and_train(read_mnist_data)
#read_and_train(get_yale_faces_data)
read_and_train(read_synthetic_data('Synthetic/'))
read_and_train(read_synthetic_data('Synthetic_2/'))
read_and_train(read_synthetic_data('Synthetic_3/'))
read_and_train(read_synthetic_data('Synthetic_4/'))
