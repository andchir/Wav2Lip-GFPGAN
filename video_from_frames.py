import os
import cv2
import numpy as np

current_dir = os.path.dirname(__file__)
output_path = os.path.join(current_dir, 'outputs')
restored_frames_path = os.path.join(output_path, 'restored_imgs/')
processed_video_output_path = output_path

dir_list = os.listdir(restored_frames_path)
dir_list.sort()

batch = 0
batch_size = 300
frame_size = None
from tqdm import tqdm

for i in tqdm(range(0, len(dir_list), batch_size)):
    img_array = []
    start, end = i, i + batch_size
    print("processing ", start, end)
    for filename in tqdm(dir_list[start:end]):
        filename = restored_frames_path + filename
        img = cv2.imread(filename)
        if img is None:
            continue
        height, width, layers = img.shape
        size = (width, height)
        if frame_size is None:
            frame_size = size
        img_array.append(img)

    out = cv2.VideoWriter(processed_video_output_path + '/batch_' + str(batch).zfill(4) + '.avi',
                          cv2.VideoWriter_fourcc(*'DIVX'), 30, frame_size)
    batch = batch + 1

    for i in range(len(img_array)):
        out.write(img_array[i])
    out.release()


concat_text_file_path = os.path.join(output_path, 'concat.txt')
concat_text_file = open(concat_text_file_path, 'w')
for ips in range(batch):
  concat_text_file.write('file batch_' + str(ips).zfill(4) + ".avi\n")
concat_text_file.close()
