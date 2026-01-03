import os
import shutil
import random

SOURCE_DIR = r"F:/archive (2)"
DEST_DIR = "data/processed/iris_dataset_split"

CLASSES = ["setosa", "versicolor", "virginica"]
TRAIN_RATIO = 0.7
VAL_RATIO = 0.15
TEST_RATIO = 0.15

random.seed(42)

print(" Counting images in each class:")
total_images = 0
for cls in CLASSES:
    count = len(os.listdir(os.path.join(SOURCE_DIR, cls)))
    total_images += count
    print(f"{cls}: {count}")
print(f"Total images: {total_images}\n")

print("Splitting dataset...")

for split in ["train", "val", "test"]:
    for cls in CLASSES:
        os.makedirs(os.path.join(DEST_DIR, split, cls), exist_ok=True)

for cls in CLASSES:
    images = os.listdir(os.path.join(SOURCE_DIR, cls))
    random.shuffle(images)

    total = len(images)
    train_end = int(total * TRAIN_RATIO)
    val_end = train_end + int(total * VAL_RATIO)

    for img in images[:train_end]:
        shutil.copy(os.path.join(SOURCE_DIR, cls, img),
                    os.path.join(DEST_DIR, "train", cls, img))

    for img in images[train_end:val_end]:
        shutil.copy(os.path.join(SOURCE_DIR, cls, img),
                    os.path.join(DEST_DIR, "val", cls, img))

    for img in images[val_end:]:
        shutil.copy(os.path.join(SOURCE_DIR, cls, img),
                    os.path.join(DEST_DIR, "test", cls, img))

print(" Dataset split completed")
