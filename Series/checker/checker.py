from keras.models import load_model
import numpy as np
from keras.utils import load_img, img_to_array
from os import walk
from Macros.SeriesList import SERIES_LIST, DIR_PATH

f = []

for (dirpath, dirnames, filenames) in walk(DIR_PATH):
    f.extend(filenames)
    break

# load your model
loaded_model = load_model('27_full_model.h5')

# Load and preprocess the image
for file in f:
    img_path = DIR_PATH
    image = load_img(img_path+file, target_size=(224, 224))
    image_array = img_to_array(image)
    image_array = np.expand_dims(image_array, axis=0)
    image_array /= 255.

    # Make predictions on the image
    predictions = loaded_model.predict(image_array, verbose=0)
    # Print the predicted class name and confidence level
    predicted_class_index = np.argmax(predictions)
    predicted_class_name = SERIES_LIST[predicted_class_index]
    confidence = predictions[0][predicted_class_index] * 100

def