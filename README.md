# Anomaly Detection with PCA and Deep Autoencoder
This repository hosts my work on the performance evaluation of four types of anomaly detectors on different datasets. 

## Methods of Anoamly Detection

Four methods of Anomaly Detection are implemented and evaluated on each of the dataset
- **PCA based Reconstruction Error Method**: The dataset is reconstructed with [Principal Component Analysis](https://en.wikipedia.org/wiki/Principal_component_analysis) method, and the anomalous data points are detected based on the reconstruction error, or the orthorgonal distance between the original and reconstructed representation.
- **PCA based Multivariate Gaussian Method**: The dataset is encoded with PCA method, and the anomalous data points are detected by applying a Multivariate Gaussian Distribution on the encoded dataset. 
- **Deep Autoencoder based Reconstruction Error Method**: A deep autoencoder is trained with the normal dataset with the goal to fully represent the original dataset. Then the dataset is reconstructed with the Deep Autoencoder model, and the anomalous data points are detected based on the distance between the original and reconstructed representation.
- **Deep Autoencoder based Multivariate Gaussian Method**: The dataset is encoded with the trained Deep Autoencoder model, and the anomalous data points are detected by applying a Multivariate Gaussian Distribution on the encoded dataset.

## Datasets
- [**Yale Faces Dataset**](/Yale_Faces_Data): [Faces dataset from Computer Vision Lab](http://vision.ucsd.edu/~iskwak/ExtYaleDatabase/ExtYaleB.html) in Yale University. The dataset contains photos of different subjects under 9 poses and 64 illumination conditions. The anomalies in the dataset are all photos of people with mustache
- [**MNIST**](/MNIST): the photos of handwritten digits released by [Yann LeCun](http://yann.lecun.com/exdb/mnist/). The anomalies in the dataset are all photos of the digit 2
- [**Synthetic Dataset 1**](/Synthetic): artificial dataset synthesized by myself. It is a binary dataset with dimension of 16 and generated with a multivariate gaussian distribution. The anomalies are vectors whose total number of '1s' in th vector is less than the threshold (4).
- [**Synthetic Dataset 2**](/Synthetic_2): It is also a binary dataset with dimension of 16 and generated with a multivariate gaussian distribution. The anomalies are vectors whose sum of the right n-1 digits is even and the left-most digit is odd (1)
- [**Synthetic Dataset 3**](/Synthetic_3): It is a binary dataset with dimension of 16 and generated with three multivariate gaussian distributions. The data generated with one distribution is treated and normal, and the data generated by the other two distribution is treated as anomalous.
- [**Synthetic Dataset 4**](/Synthetic_4): It is a binary dataset with dimension of 16 and generated with two multivariate gaussian distributions. The anomalies are vectors whose total number of '1s' in th vector is less than the threshold (4).

### Examples of the Datasets
Below is an example of the [**Yale Faces Dataset**](/Yale_Faces_Data). Subjects with mustache are defined as anomaly, just like the bottom right photo:
![Dataset_Faces](/Reports/Screenshots/dataset_faces.png)

Below is an example of the [**MNIST Dataset**](/MNIST). Photos of the number 2 are defined as anomlay:
![Dataset_MNIST](/Reports/Screenshots/dataset_mnist.png)

The table below shows the characteristics of the synthetic datasets:
![Table_Dataset_Synthetic](/Reports/Screenshots/dataset_synthetic.png)

Below explains how the [**Synthetic Dataset 1**](/Synthetic_1) was generated: 
![Dataset_Synthetic1](/Reports/Screenshots/dataset_synthetic1.png)

Below explains how the [**Synthetic Dataset 2**](/Synthetic_2) was generated: 
![Dataset_Synthetic2](/Reports/Screenshots/dataset_synthetic2.png)

## Results for each type of anomaly detector
I applied each of the Anomaly Detectors on all of the dataset. Here I used two metrics in evaluation:
- [R-Precision](https://en.wikipedia.org/wiki/Information_retrieval#R-Precision): The precision of the top *R* results, where *R* is the total number of positive results.
- [Precision @ K](https://en.wikipedia.org/wiki/Information_retrieval#Precision_at_K): The precision of the top *k* results. 

![Results_Evaluation_Table](/Reports/Screenshots/Results_Evaluation_Table.png)

Some findings:
- There is no single anomaly detector that excel in all the datasets.
- Autoencoder-based methods work better than PCA-based methods in general. 
- Gaussian-based methods fail in most of the dataset, partially due to the correlation between latent dimensions after encoding. However, the Autoencoder + Gaussian method succeeded in Synthetic dataset #1, where the anomaly 

> Autoencoder-based methods work better than PCA-based methods in general

![Results_Evaluation_1](/Reports/Screenshots/Results_Evaluation_1.png)

> Autoencoder + Gaussian method succeeds in synthetic #1

![Results_Evaluation_2](/Reports/Screenshots/Results_Evaluation_2.png)

## Some Visualization
> The project has not finished yet, so I only show a few visualization here for presentation purpose. The results and conclusions are coming soon.

#### PCA - Eigenfaces generated from the Face Database
![Faces_PCA_EIGEN](/Reports/Screenshots/rm_faces_eigenfaces.png)


#### PCA - Reconstructed photos from the Face Database
![Faces_PCA_RC](/Reports/Screenshots/rm_faces_rc.png)

#### Deep Autoencoder - Reconstructed photos from the MNIST Database
![MNIST_DA_RC](/Reports/Screenshots/rm_mnist_rc.png)

#### Deep Autoencoder - Result with the Reconstruction Error Method on the MNIST Database
![MNIST_DA_RE](/Reports/Screenshots/rm_mnist_da_re_result.png)

#### Comparison between PCA and Deep Autoencoder - Reconstructed Data from the Synthetic Dataset 3
##### Reconstruction with PCA
![S3_PCA_RE](/Reports/Screenshots/rm_PCA_REC_PLOT_SD3.png)
##### Reconstruction with Deep Autoencoder
![S3_DA_RE](/Reports/Screenshots/rm_AUT_REC_PLOT_SD3.png)

#### PCA - Result with the Reconstruction Error Method on the Synthetic Dataset 3
![S3_PCA_RE_RESULT](/Reports/Screenshots/rm_PCA_REC_SD3.png)

