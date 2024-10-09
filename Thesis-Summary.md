# Thesis Title : Framework for Classifying Violence and Non-Violence Content using Deep Learning Model in Films for Sensitive Viewers
This project focuses on building a system that classifies movie scenes into two categories: **Violent** & **Non-Violent** based on visual content. My system is designed to assist both **content providers** & **sensitive viewers** by detecting **violent scenes** & offering **alerts** enabling more **informed viewing decisions**. This work leverages deep learning methods to **analyze frames** from short video sequences.

## Key Objectives
### 1. Scene Classification 
The system classifies movie scenes as either violent or non-violent based on universal cinema rules focusing primarily on gory, destructive & physically violent scenes.
### 2. Motivation 
Addressing the limitations of existing methods in violence detection, this system provides a more practical & efficient solution for content filtering & classification in the context of movie scenes.

## Methodology
### 1. Data Collection 
We compiled a dataset of **600 video sequences**. 300 for violent & for 300 non-violent from **350 movies** including Bollywood, Korean & Hollywood films. Each sequence lasts **2-5 seconds** with **5 frames** manually selected from each.

### 2. Model Architecture
The system uses a **Convolutional Neural Network (CNN)** feature extractor, specifically **InceptionV3** combined with **LSTM** to capture both **spatial** & **temporal features** from movie frames.

### 3. Training and Evaluation
The dataset was split into **training**, **validation** & **testing sets** maintaining class balance. The model was trained using forward and backward propagation, with **regularization techniques** like **dropout** to **prevent overfitting**.

## Workflow
The workflow of this project is as follows:

### 1. Data Collection
A dataset of 600 video sequences (300 violent and 300 non-violent) from 350 movies including Bollywood, Korean & Hollywood films was compiled. Each sequence was 2-5 seconds long with 5 manually selected frames.

### 2. Preprocessing 
Movie scenes were manually edited & frames were extracted for classification. These frames were then labeled as violent or non-violent & prepared for model training.

### 3. Feature Extraction 
**InceptionV3** was used to extract key spatial features from the frames.

### 4. Modeling 
A combination of **CNN** & **LSTM** was used to capture both **spatial** and **temporal features** from the movie scenes.

### 5. Training 
The dataset was split into training, validation, and testing sets. The model was trained using forward and backward propagation, with dropout to prevent overfitting.

### 6. Evaluation 
The model was evaluated using metrics like **accuracy** & **loss** along with **ROC curves**.

### Workflow Diagram
Below is the workflow diagram of the system, illustrating the complete process from data collection to scene classification:
<div align="center">
  <img src="Diagrams/Workflow.png" alt="Project Logo" width=100% height=30%/>
</div>
