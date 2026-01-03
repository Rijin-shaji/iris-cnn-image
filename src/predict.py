import cv2
import numpy as np
import tensorflow as tf

IMG_SIZE = 128
CLASS_NAMES = ['setosa', 'versicolor', 'virginica']

def predict_iris(image_path):
    model = tf.keras.models.load_model("models/iris_cnn.h5")

    img = cv2.imread(image_path)
    if img is None:
        print("Image not found")
        return

    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
    img = img / 255.0
    img = np.expand_dims(img, axis=0)

    preds = model.predict(img)[0]
    class_id = np.argmax(preds)

    print(f"Predicted Class: {CLASS_NAMES[class_id]}")
    print(f"Confidence: {preds[class_id]:.2f}")

predict_iris(r"F:/123.jpg")
