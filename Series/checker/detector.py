import numpy as np
from PIL import Image
from Macros.ModelMacros import SERIES_LIST, MIN_CONFIDENCE, NOTHING_VALUE
from keras.utils import img_to_array
from Macros.ModelMacros import PIC_SIZE
from tensorflow import image
from tensorflow import keras


def detect_serie(image: Image) -> str:
    from .model import model
    image_array = img_to_array(image)
    image_array = np.expand_dims(image_array, axis=0)
    image_array /= 255.

    # Make predictions on the image
    predictions = model.predict(image_array, verbose=0)
    # Print the predicted class name and confidence level
    predicted_class_index = np.argmax(predictions)
    predicted_class_name = SERIES_LIST[predicted_class_index]
    confidence = predictions[0][predicted_class_index] * 100
    return predicted_class_name if confidence >= MIN_CONFIDENCE else NOTHING_VALUE


if __name__ == '__main__':
    img = Image.open(r'C:\Users\Eliad\Projects\Spoiled\Server\Series\checker\the-good-place-season-4-1.jpeg')
    img = keras.utils.array_to_img(image.resize(img, PIC_SIZE))
    print(detect_serie(img))  # passing the image object here
