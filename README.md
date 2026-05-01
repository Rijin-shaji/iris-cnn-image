# iris-cnn-image
CNN-based image classification system for identifying Iris flower species from images.
CNN-based image classification system to identify Iris flower species (Setosa, Versicolor, Virginica) using deep learning. The project includes dataset splitting, image augmentation, CNN training, evaluation, and single-image prediction.

---

## Iris Flower Image Classification Using CNN

### Overview
This project builds an end-to-end Convolutional Neural Network (CNN) pipeline to classify Iris flower images into three species: **Setosa**, **Versicolor**, and **Virginica**. The system handles dataset preparation, model training, and inference using TensorFlow and Keras.

---

## Objectives
- Automatically split raw image data into train, validation, and test sets
- Apply image augmentation to improve generalization
- Train a CNN model for multi-class image classification
- Save the trained model for reuse
- Perform single-image prediction with confidence score

---

## Classes
- Setosa
- Versicolor
- Virginica

---

## Model Architecture
- Convolutional Layers: 32 → 64 → 128 filters
- MaxPooling layers for spatial reduction
- Fully connected Dense layer with Dropout
- Softmax output layer for 3-class classification

---

## Tech Stack
- Python  
- TensorFlow / Keras  
- OpenCV  
- NumPy  
- ImageDataGenerator  

---

## Project Structure

iris-cnn-image-classification/
│
├── README.md
├── requirements.txt
├── .gitignore
│
├── data/
│ ├── raw/
│ │ └── iris/
│ │ ├── setosa/
│ │ ├── versicolor/
│ │ └── virginica/
│ │
│ └── processed/
│ └── dataset_split/
│ ├── train/
│ ├── val/
│ └── test/
│
├── src/
│ ├── data_split.py # Dataset splitting logic
│ ├── data_generator.py # Image augmentation
│ ├── model.py # CNN architecture
│ ├── train.py # Model training pipeline
│ └── predict.py # Single image prediction
│
├── notebooks/
│ ├── data_exploration.ipynb
│ ├── image_visualization.ipynb
│ ├── cnn_experiments.ipynb
│ └── training_analysis.ipynb
│
├── models/
│ └── iris_cnn.h5
│
├── results/
│ └── training_logs.txt
│
└── docs/
├── data_description.md
├── model_explanation.md
└── project_workflow.md


---

## Workflow
1. Load raw Iris images
2. Split dataset into train, validation, and test sets
3. Apply image augmentation on training data
4. Train CNN model
5. Save trained model
6. Predict Iris species from a single image

---

## Results
- Successful multi-class image classification
- Robust training using data augmentation
- Accurate prediction with confidence score
- Model saved for future inference

---

## Installation
Clone the repository and install dependencies:

```bash
git clone https://github.com/Rijin-shaji/iris-cnn-image.git
cd iris-cnn-image-classification
pip install -r requirements.txt

