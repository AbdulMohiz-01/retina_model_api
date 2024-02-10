import tensorflow as tf
from PIL import Image
from io import BytesIO
import numpy as np

def predict_image(image_file):
    # Load and preprocess the image for prediction
    img = Image.open(BytesIO(image_file.read()))
    img = img.resize((180, 180))  # Adjust size based on your model's input size
    img_array = np.array(img)
    img_array = np.expand_dims(img_array, axis=0)
    # img_array = img_array.astype('float32') / 255.0  # Normalize the image data

    # load the model
    model = tf.keras.models.load_model('./model/retina.h5')
    # Make predictions
    predictions = model.predict(img_array)

    # Assuming you have a classification model, you might want to decode the predictions
    class_labels = ['0', '1', '2', '3', '4', '5']  # Replace with your actual class labels
    predicted_class_index = np.argmax(predictions[0])
    predicted_class_name = class_labels[predicted_class_index]

    # Return the predictions
    return predicted_class_name, float(predictions[0][predicted_class_index]), predictions[0].tolist()
