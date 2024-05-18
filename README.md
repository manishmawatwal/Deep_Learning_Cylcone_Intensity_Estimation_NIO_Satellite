# An End-to-End Deep Learning Framework for Cyclone Intensity Estimation in North Indian Ocean Region using Satellite Imagery

## Abstract
Prediction of Tropical cyclones (TCs), particularly intensity prediction, has always been challenging for climate researchers due to the complicated physical mechanisms in TC dynamics and the way it interacts with upper ocean and atmospheric circulation. Furthermore, the available data set over the North Indian Ocean (NIO) is also very limited for Machine Learning (ML) model development. Here, we demonstrated a simple yet robust hybrid architecture leveraging Convolutional Neural Network (CNN) for automated prediction of the intensity of the cyclone based on IR satellite imagery of 2000-2022. The model comprises a binary classifier, a multiclass classifier, a YOLOv3 based cyclone detector and a regression module. The paper also highlights the discrepancy between the results of independent testing wherein training is done on 2000 to 2019 dataset and tested on 2020 to 2022 dataset, as well as the outcomes of a stratified train-test split performed over the entire dataset using a 70:15:15 ratio for training, validation and testing, respectively. The model is tuned for the NIO region with binary classification accuracy score of 98.4% (± 0.003), multiclass classification accuracy of 63.83% (± 1.3) and RMSE of 16.2 (± 0.9) knots on stratified split. The results highlight the careful interpretation of the DL model’s performance when applied to time series problems. Additionally, it discusses the limitations stemming from the dataset's small size and the challenges posed by the 5 kt resolution of the best track intensity estimation from Indian Meteorological Department (IMD). The internal representations learned by the model through feature maps analysis were studied, shedding light on the model’s decision-making process. The study underscores the need for further data accumulation and highlights avenues for enhancing model performance in the future.

# Methodology
![new](https://github.com/manishmawatwal/NIO-Cyclone/assets/56023675/c63bdb40-54ce-4ff7-8858-0c9905fdd20b)

# Results

![index](https://github.com/manishmawatwal/NIO-Cyclone/assets/56023675/1a85afa4-1ba9-435b-8dfc-a64a9253f768)


This repository is a part of the research being conducted at IIT Indore, Department of Astronomy, Astrophysics and Space Enginerering.

PI - Dr. Saurabh Das, RemoteWave Propagation Lab.

Researchers - Manish Mawatwal

Contact - saurabh.das@iiti.ac.in

This repository is also a part of the research work titled - 
1. "An End-to-End Deep Learning Framework for Cyclone Intensity Estimation in North Indian Ocean Region using Satellite Imagery". (Submitted and accepted) to URSI-RCRS 2022, IIT Indore.
2. "An End-to-End Deep Learning Framework for Cyclone Intensity Estimation in North Indian Ocean Region using Satellite Imagery". (In review)


Cyclone Detection, Classification and Intensity Estimation

Note - Some image files in binary_data.zip and regression_data.zip file have been deleted, adhering to the policy of restricting file uploads to 25MB on GitHub
