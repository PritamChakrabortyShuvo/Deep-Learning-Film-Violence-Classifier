# Define class names
class_names = ['violence', 'non-violence']

# Define the function to get class indices from one-hot encoding
def one_hot_to_labels(y_one_hot):
    return np.argmax(y_one_hot, axis=1)

# Load the model and training history
model = load_model('/content/drive/MyDrive/inception_lstm_16_50.h5')

with open('/content/drive/MyDrive/training_history_16_50.pkl', 'rb') as file:
    loaded_history = pickle.load(file)

# Evaluate model on the test dataset
# Ensure that X_test and y_test are loaded and preprocessed correctly
# X_test, y_test should be preprocessed similar to X_train, y_train

# For demonstration, assuming X_test and y_test are already defined
# model evaluation
test_loss, test_accuracy = model.evaluate(X_test, y_test, verbose=1)
print(f"Test Loss: {test_loss}")
print(f"Test Accuracy: {test_accuracy}")

# Predictions
y_pred_probs = model.predict(X_test)
y_pred = np.argmax(y_pred_probs, axis=1)
y_true = one_hot_to_labels(y_test)

# Classification report
report = classification_report(y_true, y_pred, target_names=class_names)
print("Classification Report:")
print(report)

# Save the classification report to a file
with open('/content/drive/MyDrive/classification_report.txt', 'w') as f:
    f.write(report)