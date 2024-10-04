{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# InceptionV3 with LSTM"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "def build_model(input_shape, num_classes):\n",
    "    base_model = InceptionV3(weights='imagenet', include_top=False, input_shape=input_shape)\n",
    "    model = Sequential()\n",
    "\n",
    "    model.add(TimeDistributed(base_model, input_shape=(None, *input_shape)))\n",
    "    model.add(TimeDistributed(Flatten()))\n",
    "    model.add(BatchNormalization())\n",
    "    model.add(LSTM(64, return_sequences=False, kernel_regularizer=l2(0.01)))\n",
    "    model.add(Dropout(0.5))\n",
    "    model.add(BatchNormalization())\n",
    "    model.add(Dense(128, activation='relu', kernel_regularizer=l2(0.01)))\n",
    "    model.add(Dropout(0.5))\n",
    "    model.add(BatchNormalization())\n",
    "    model.add(Dense(num_classes, activation='softmax'))\n",
    "\n",
    "    optimizer = Adam(learning_rate=0.0001)\n",
    "    model.compile(optimizer=optimizer, loss='categorical_crossentropy', metrics=['accuracy'])\n",
    "\n",
    "    return model\n",
    "\n",
    "input_shape = (240, 240, 3)\n",
    "num_classes = y_train.shape[1]\n",
    "\n",
    "model = build_model(input_shape, num_classes)\n",
    "model.summary()"
   ]
  }
 ],
 "metadata": {
  "language_info": {
   "name": "python"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
