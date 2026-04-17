import tensorflow as tf
import os
import sys

# ----------------------------
# Suppress TF warnings
# ----------------------------
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# ----------------------------
# Print current working directory
# ----------------------------
print(f"Current Working Directory: {os.getcwd()}")

# ----------------------------
# Path to your .keras model
# ----------------------------
keras_model_path = "plant_model_4.keras"

if not os.path.exists(keras_model_path):
    print(f"ERROR: Keras model file not found at {keras_model_path}")
    sys.exit(1)

# ----------------------------
# Load Keras model
# ----------------------------
print(f"Loading Keras model from: {keras_model_path}")
try:
    model = tf.keras.models.load_model(keras_model_path)
    print("Model loaded successfully!")
    model.summary()
except Exception as e:
    print(f"ERROR: Failed to load model! {e}")
    sys.exit(1)

# ----------------------------
# Path to save TensorFlow SavedModel
# ----------------------------
# Note: Adding a version number (e.g., /1/) is required by TF Serving
saved_model_path = "./models/plant_models/4"

# Ensure target directory exists
os.makedirs(os.path.dirname(saved_model_path), exist_ok=True)
print(f"Exporting model to: {saved_model_path}")

# ----------------------------
# Export in SavedModel format
# ----------------------------
try:
    # In Keras 3, 'export' is used for SavedModel (pb/variables)
    # whereas 'save' is used for .keras files.
    model.export(saved_model_path)
    print(f"\nSUCCESS: Model exported at: {saved_model_path}")
except Exception as e:
    print("\nERROR: Failed to export model!")
    print(e)
    sys.exit(1)

# ----------------------------
# Verify contents
# ----------------------------
if os.path.exists(saved_model_path):
    print("\nSavedModel directory contents:")
    print(os.listdir(saved_model_path))
