from data_generator import get_generators
from model import build_model

EPOCHS = 25

train_data, val_data = get_generators()

model = build_model()
model.summary()

print("Training CNN model...")

model.fit(
    train_data,
    validation_data=val_data,
    epochs=EPOCHS
)

model.save("models/iris_cnn.h5")
print("Model saved as iris_cnn.h5")
