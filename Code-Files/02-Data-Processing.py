def load_sequences_from_directory(directory_path, img_size=(240, 240)):
    data = {'train': {'sequences': [], 'labels': []},
            'val': {'sequences': [], 'labels': []},
            'test': {'sequences': [], 'labels': []}}

    for set_type in ['train', 'val', 'test']:
        set_type_dir = os.path.join(directory_path, set_type)
        if os.path.isdir(set_type_dir):
            for label in ['violence', 'nonviolence']:
                label_dir = os.path.join(set_type_dir, label)
                if os.path.isdir(label_dir):
                    for seq in sorted(os.listdir(label_dir)):
                        seq_dir = os.path.join(label_dir, seq)
                        if os.path.isdir(seq_dir):
                            frames = []
                            for frame_file in sorted(os.listdir(seq_dir)):
                                frame_path = os.path.join(seq_dir, frame_file)
                                frame = cv2.imread(frame_path)
                                if frame is not None:
                                    frame = cv2.resize(frame, img_size)
                                    frames.append(frame)
                            if frames:
                                data[set_type]['sequences'].append(np.array(frames))
                                data[set_type]['labels'].append(label)
                                print(f"Loaded sequence from {seq_dir} with {len(frames)} frames for label '{label}'")
                        else:
                            print(f"Skipping non-directory {seq_dir}")
                else:
                    print(f"Label directory not found: {label_dir}")
        else:
            print(f"Set type directory not found: {set_type_dir}")

    for set_type in data:
        print(f'Total {set_type} sequences loaded: {len(data[set_type]["sequences"])}')
        print(f'Total {set_type} labels loaded: {len(data[set_type]["labels"])}')

    return data