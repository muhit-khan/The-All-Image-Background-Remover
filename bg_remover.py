import cv2
import numpy as np
import os
from directory_works import create_directory

def remove_background(image_path, save_dir):
    image = cv2.imread(image_path)

    if image is None:
        print(f"Failed to load image: {image_path}")
        return None

    mask = np.zeros(image.shape[:2], dtype=np.uint8)
    bgdModel = np.zeros((1, 65), dtype=np.float64)
    fgdModel = np.zeros((1, 65), dtype=np.float64)
    rect = (1, 1, image.shape[1] - 1, image.shape[0] - 1)
    cv2.grabCut(image, mask, rect, bgdModel,
                fgdModel, 5, cv2.GC_INIT_WITH_RECT)
    mask = np.where((mask == 2) | (mask == 0), 0, 1).astype(np.uint8)
    result = image * mask[:, :, np.newaxis]

    # Create 'Background_Removed' directory inside the source directory
    save_dir = create_directory(save_dir)

    # Generate output image path with .png extension
    filename = os.path.splitext(os.path.basename(image_path))[0]
    output_image_path = os.path.join(save_dir, f"{filename}.png")

    cv2.imwrite(output_image_path, result)
    return save_dir
