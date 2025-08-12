<!-- @format -->

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

Below is the workflow diagram of the system, illustrating the complete process from data collection to scene classification:

<div align="center">
  <img src="Diagrams/Workflow.png" alt="Project Logo" width=100% height=30%/>
  <img src="Diagrams/Workflow.png" alt="Project Logo" width=100%>
  <br>
  <em>Figure 01 : Workflow</em>
</div>

### 1. Data Collection

A dataset of 600 video sequences (300 violent and 300 non-violent) from 350 movies including Bollywood, Korean & Hollywood films was compiled. Each sequence was 2-5 seconds long with 5 manually selected frames.

### 2. Splitting Dataset into Train, Test & Validation Sets

Once the data is collected it is split into **training**, **testing** & **validation** sets. This systematic splitting ensures balanced classes (violent and non-violent scenes) in each subset allowing for robust training and evaluation of the model.

### 3. Data Preprocessing

During preprocessing, several important steps are performed:

- **Scene Cutting and Frame Selection**: Each video sequence is cut into specific scenes & **high-quality frames** are selected for processing.
- **Quality Control**: Ensuring that all frames meet quality standards for clear feature extraction.
- **Loading and Resizing Frames**: Frames are loaded and resized to a **consistent resolution** suitable for feature extraction.
- **Data Labeling**: Frames are labeled as **'Violence'** or **'Non-Violence'** according to their content.
- **Data Encoding**: Labels are encoded into a format suitable for model processing.
- **Data Normalization**: Frame data is normalized to standardize input features & improving the efficiency of training.

### 4. Feature Extraction Using InceptionV3

Using a **pre-trained InceptionV3 model** features are extracted from the preprocessed frames. These features capture the spatial details necessary for classifying scenes as violent or non-violent.

### 5. Model Training

With the extracted features the model is trained. A combination of **forward propagation**, **backward propagation** & **dropout techniques** is employed to optimize the model's performance.

### 6. Hyperparameter Tuning

The **hyperparameters** of the model are **fine-tuned** to enhance its accuracy and generalization. This process includes **optimizing parameters** like **learning rate**, **dropout rates** & **batch size**.

### 7. Classification

Once the model is trained, it classifies new scenes into **'Violence'** or **'Non-Violence'** based on the visual content of the frames.

### 8. Model Evaluation

After classification, the model is **evaluated** using **testing** and **validation data**. Metrics like **accuracy**, **loss** & **ROC curves** are used to assess its performance.

## Model Architecture

This model architecture combines **InceptionV3** for **feature extraction** with **LSTM layers** for **temporal analysis** **culminating in a classification output**.

Below is the Model Architecture of the system.

<div align="center">
  <img src="Diagrams/Model-Architecture.png" alt="Project Logo" width=100% height=30%/>
  <img src="Diagrams/Model-Architecture.png" alt="Project Logo" width=100%>
  <br>
  <em>Figure 02 : Model Architecture</em>
</div>

Here is short description of Model Architecture

- **InceptionV3** as the **base model** for feature extraction.
- **Time Distributed Layer** to handle frame sequences.
- **Flatten Layer** to reduce dimensionality.
- **Batch Normalization Layer** to stabilize and accelerate training.
- **LSTM Layer** for temporal sequence learning.
- **Dropout Layer** for regularization.
- **Batch Normalization Layer** to maintain normalization.
- **Dense Layer** for final feature representation.
- **Batch Normalization Layer** for further stabilization.
- **Output Layer** for scene classification.

## Dataset Sample

The dataset includes scenes from 350 movies featuring **violent films** such as **Fight Club**, **The Night Comes for Us**, **Saw (1 to 7)** & Punisher etc. alongside **non-violent films** like **La La Land**, **The Lunchbox** & **Beauty and the Beast** etc. This diverse selection provides a balanced mix of action-packed and calm scenes for accurate classification.

Below are a few sample images from the dataset used for the movie scene classification:

### Violence Scene Sample

![Project Logo](Diagrams/Model-Architecture.png)

<div align="center">

  <img src="Diagrams/Violence_Sample1.jpg" alt="Project Logo" width=45% height=30%/>
  <img src="Diagrams/Violence_Sample02.jpg" alt="Project Logo" width=45% height=30%/>
  <img src="Diagrams/Violence_Sample1.jpg" alt="Project Logo" width=45%>
  <img src="Diagrams/Violence_Sample02.jpg" alt="Project Logo" width=45%>
  <br>
  <em>Figure 03 : Violence Scenes</em>
</div>

### Non Violence Scene Sample

<div align="center">

  <img src="Diagrams/NonVio_1.jpg" alt="Project Logo" width=45% height=30%/>
  <img src="Diagrams/NonVio_02.jpg" alt="Project Logo" width=45% height=30%/>
  <img src="Diagrams/NonVio_1.jpg" alt="Project Logo" width=45%>
  <img src="Diagrams/NonVio_02.jpg" alt="Project Logo" width=45%>
  <br>
  <em>Figure 04 : Non Violence Scenes</em>
</div>

## Result

### Violence Scene Classification Result with Alert Message

In below showing the results generated by the system

<div align="center">
  <img src="Diagrams/Violence-Result0.png " alt="Project Logo" width=45% height=30%/>
  <img src="Diagrams/Violence-Result01.png" alt="Project Logo" width=45% height=30%/>
  <img src="Diagrams/Violence-Result0.png " alt="Project Logo" width=45%>
  <img src="Diagrams/Violence-Result01.png" alt="Project Logo" width=45%>
  <br>
  <em>Figure 05 : Violence Result</em>
</div>

### Non Violence Scene Classification Result with Note

In below showing the results generated by the system

<div align="center">
  <img src="Diagrams/Non-Violence-Result01.png " alt="Project Logo" width=45% height=30%/>
  <img src="Diagrams/Non-Violence-Result02.png" alt="Project Logo" width=45% height=30%/>
  <img src="Diagrams/Non-Violence-Result01.png " alt="Project Logo" width=45%>
  <img src="Diagrams/Non-Violence-Result02.png" alt="Project Logo" width=45%/>
  <br>
  <em>Figure 06 : Non-Violence Result</em>
</div>

## Applications

The system has multiple real-world applications, such as:

1.  **Content Filtering :** Platforms like **Amazon Prime**, **Netflix** or **Picurify** can implement this system to filter violent content for sensitive viewers.

2.  **Movie Recommendations :** Services like **Movie Lens** can use the system to recommend appropriate content for viewers based on their sensitivity to violent scenes.

## Challenges

1.  **Data Collection:** Obtaining movies and scenes with violent content required extensive manual effort.

2.  **Motion Handling :** The system currently has limitations in handling fast-paced scenes with rapid movements.

## Contributions

This project presents a novel approach to scene classification offering a unique blend of **CNN** & **LSTM** for movie scene analysis. It contributes toward making content viewing safer and more informed particularly for viewers sensitive to violent content.
This project presents a novel approach to scene classification offering a unique blend of **CNN** & **LSTM** for movie scene analysis. It contributes toward making content viewing safer and more informed particularly for viewers sensitive to violent content.
