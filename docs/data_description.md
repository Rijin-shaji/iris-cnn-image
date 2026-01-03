# Dataset Description

This project uses an image-based dataset for classification.

## Classes
- Setosa
- Versicolor
- Virginica

## Data Source
Images are organized into class-wise folders.

## Data Organization
data/
└── raw/
    └── iris/
        ├── setosa/
        ├── versicolor/
        └── virginica/

## Preprocessing Steps
- Image resizing to 128 × 128
- Normalization (pixel values scaled to 0–1)
- Data augmentation applied to training data
