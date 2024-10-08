data = load_sequences_from_directory('/content/drive/MyDrive/Version001')

for set_type in data:
    print(f"Checking frame shapes for {set_type} set...")
    for sequence in data[set_type]['sequences']:
        for frame in sequence:
            if frame.shape != (240, 240, 3):
                print(f"Found a frame in {set_type} set with shape {frame.shape}")
all_labels = [label for set_type in data for label in data[set_type]['labels']]
label_encoder = LabelEncoder()
label_encoder.fit(all_labels)
for set_type in data:
    labels_encoded = label_encoder.transform(data[set_type]['labels'])
    data[set_type]['labels_categorical'] = to_categorical(labels_encoded, num_classes=2)
for set_type in data:
    data[set_type]['sequences'] = np.array(data[set_type]['sequences'])
    data[set_type]['labels_categorical'] = np.array(data[set_type]['labels_categorical'])

X_train, y_train = data['train']['sequences'], data['train']['labels_categorical']
X_val, y_val = data['val']['sequences'], data['val']['labels_categorical']
X_test, y_test = data['test']['sequences'], data['test']['labels_categorical']

print("All frames are now 240x240 RGB images and labels are encoded.")

print(f"X_train shape: {X_train.shape}")
print(f"y_train shape: {y_train.shape}")
print(f"X_val shape: {X_val.shape}")
print(f"y_val shape: {y_val.shape}")
print(f"X_test shape: {X_test.shape}")
print(f"y_test shape: {y_test.shape}")