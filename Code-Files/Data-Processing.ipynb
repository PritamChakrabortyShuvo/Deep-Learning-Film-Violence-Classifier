{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def load_sequences_from_directory(directory_path, img_size=(240, 240)):\n",
    "    data = {'train': {'sequences': [], 'labels': []},\n",
    "            'val': {'sequences': [], 'labels': []},\n",
    "            'test': {'sequences': [], 'labels': []}}\n",
    "\n",
    "    for set_type in ['train', 'val', 'test']:\n",
    "        set_type_dir = os.path.join(directory_path, set_type)\n",
    "        if os.path.isdir(set_type_dir):\n",
    "            for label in ['violence', 'nonviolence']:\n",
    "                label_dir = os.path.join(set_type_dir, label)\n",
    "                if os.path.isdir(label_dir):\n",
    "                    for seq in sorted(os.listdir(label_dir)):\n",
    "                        seq_dir = os.path.join(label_dir, seq)\n",
    "                        if os.path.isdir(seq_dir):\n",
    "                            frames = []\n",
    "                            for frame_file in sorted(os.listdir(seq_dir)):\n",
    "                                frame_path = os.path.join(seq_dir, frame_file)\n",
    "                                frame = cv2.imread(frame_path)\n",
    "                                if frame is not None:\n",
    "                                    frame = cv2.resize(frame, img_size)\n",
    "                                    frames.append(frame)\n",
    "                            if frames:\n",
    "                                data[set_type]['sequences'].append(np.array(frames))\n",
    "                                data[set_type]['labels'].append(label)\n",
    "                                print(f\"Loaded sequence from {seq_dir} with {len(frames)} frames for label '{label}'\")\n",
    "                        else:\n",
    "                            print(f\"Skipping non-directory {seq_dir}\")\n",
    "                else:\n",
    "                    print(f\"Label directory not found: {label_dir}\")\n",
    "        else:\n",
    "            print(f\"Set type directory not found: {set_type_dir}\")\n",
    "\n",
    "    for set_type in data:\n",
    "        print(f'Total {set_type} sequences loaded: {len(data[set_type][\"sequences\"])}')\n",
    "        print(f'Total {set_type} labels loaded: {len(data[set_type][\"labels\"])}')\n",
    "\n",
    "    return data"
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
