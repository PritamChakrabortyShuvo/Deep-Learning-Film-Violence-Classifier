with open('/content/drive/MyDrive/training_history_16_50.pkl', 'rb') as file:
    loaded_history = pickle.load(file)

plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
print("Training_accuracy........................", loaded_history['accuracy'])
print("Validation_accuracy.............................", loaded_history['val_accuracy'])
plt.plot(loaded_history['accuracy'])
plt.plot(loaded_history['val_accuracy'])
plt.title('Training vs Validation Accuracy')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.legend(['Train', 'Validation'], loc='upper left')

plt.subplot(1, 2, 2)
print("Training_loss........................................", loaded_history['loss'])
print("Testing_loss.......................................", loaded_history['val_loss'])
plt.plot(loaded_history['loss'])
plt.plot(loaded_history['val_loss'])
plt.title('Train vs Validation Loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(['Train', 'Validation'], loc='upper left')

plt.show()
