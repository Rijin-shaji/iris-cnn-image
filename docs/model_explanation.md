# CNN Model Architecture

A custom Convolutional Neural Network (CNN) is used for multi-class image classification.

## Architecture
- Conv2D (32 filters) + ReLU
- MaxPooling
- Conv2D (64 filters) + ReLU
- MaxPooling
- Conv2D (128 filters) + ReLU
- MaxPooling
- Fully Connected Dense Layer
- Dropout for regularization
- Softmax output layer (3 classes)

## Loss Function
- Categorical Crossentropy

## Optimizer
- Adam

## Evaluation Metric
- Accuracy
