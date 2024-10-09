# Load the training history
with open('/content/drive/MyDrive/training_history_16_50.pkl', 'rb') as file:
    loaded_history = pickle.load(file)

# Extract accuracy and validation accuracy
train_accuracy = loaded_history['accuracy']
val_accuracy = loaded_history['val_accuracy']

# Print training and validation accuracy
print("Training Accuracy:")
print(train_accuracy)

print("Validation Accuracy:")
print(val_accuracy)

# Optionally, print the last epoch's accuracies
print(f"Final Training Accuracy: {train_accuracy[-1]}")
print(f"Final Validation Accuracy: {val_accuracy[-1]}")
