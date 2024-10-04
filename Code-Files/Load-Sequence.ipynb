{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "data = load_sequences_from_directory('/content/drive/MyDrive/Version001')\n",
    "\n",
    "for set_type in data:\n",
    "    print(f\"Checking frame shapes for {set_type} set...\")\n",
    "    for sequence in data[set_type]['sequences']:\n",
    "        for frame in sequence:\n",
    "            if frame.shape != (240, 240, 3):\n",
    "                print(f\"Found a frame in {set_type} set with shape {frame.shape}\")\n",
    "all_labels = [label for set_type in data for label in data[set_type]['labels']]\n",
    "label_encoder = LabelEncoder()\n",
    "label_encoder.fit(all_labels)\n",
    "for set_type in data:\n",
    "    labels_encoded = label_encoder.transform(data[set_type]['labels'])\n",
    "    data[set_type]['labels_categorical'] = to_categorical(labels_encoded, num_classes=2)\n",
    "for set_type in data:\n",
    "    data[set_type]['sequences'] = np.array(data[set_type]['sequences'])\n",
    "    data[set_type]['labels_categorical'] = np.array(data[set_type]['labels_categorical'])\n",
    "\n",
    "X_train, y_train = data['train']['sequences'], data['train']['labels_categorical']\n",
    "X_val, y_val = data['val']['sequences'], data['val']['labels_categorical']\n",
    "X_test, y_test = data['test']['sequences'], data['test']['labels_categorical']\n",
    "\n",
    "print(\"All frames are now 240x240 RGB images and labels are encoded.\")\n",
    "\n",
    "print(f\"X_train shape: {X_train.shape}\")\n",
    "print(f\"y_train shape: {y_train.shape}\")\n",
    "print(f\"X_val shape: {X_val.shape}\")\n",
    "print(f\"y_val shape: {y_val.shape}\")\n",
    "print(f\"X_test shape: {X_test.shape}\")\n",
    "print(f\"y_test shape: {y_test.shape}\")"
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
