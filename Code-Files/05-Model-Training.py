early_stopping = EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True)
model_checkpoint = ModelCheckpoint('/content/drive/MyDrive/inception_lstm_16_50.keras', monitor='val_accuracy', save_best_only=True, mode='max')

history = model.fit(X_train, y_train,
                     validation_data=(X_val, y_val),
                     epochs= #add your batch and epoch here
                     batch_size= #add your batch and epoch here
                     callbacks=[early_stopping, model_checkpoint])
with open('/content/drive/MyDrive/training_history_16_50.pkl', 'wb') as file:
    pickle.dump(history.history, file)