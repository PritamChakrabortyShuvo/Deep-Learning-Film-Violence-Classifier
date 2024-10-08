def build_model(input_shape, num_classes):
    base_model = InceptionV3(weights='imagenet', include_top=False, input_shape=input_shape)
    model = Sequential()

    model.add(TimeDistributed(base_model, input_shape=(None, *input_shape)))
    model.add(TimeDistributed(Flatten()))
    model.add(BatchNormalization())
    model.add(LSTM(64, return_sequences=False, kernel_regularizer=l2(0.01)))
    model.add(Dropout(0.5))
    model.add(BatchNormalization())
    model.add(Dense(128, activation='relu', kernel_regularizer=l2(0.01)))
    model.add(Dropout(0.5))
    model.add(BatchNormalization())
    model.add(Dense(num_classes, activation='softmax'))

    optimizer = Adam(learning_rate=0.0001)
    model.compile(optimizer=optimizer, loss='categorical_crossentropy', metrics=['accuracy'])

    return model

input_shape = (240, 240, 3)
num_classes = y_train.shape[1]

model = build_model(input_shape, num_classes)
model.summary()