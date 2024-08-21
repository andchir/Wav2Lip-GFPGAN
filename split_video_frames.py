import cv2
from tqdm import tqdm
import os

current_dir = os.path.dirname(__file__)
output_path = os.path.join(current_dir, 'outputs')

input_video_path = os.path.join(output_path, 'result.mp4')
unprocessed_frames_folder_path = os.path.join(output_path, 'frames')

if not os.path.exists(unprocessed_frames_folder_path):
    os.makedirs(unprocessed_frames_folder_path)

vidcap = cv2.VideoCapture(input_video_path)
number_off_frames = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))
fps = vidcap.get(cv2.CAP_PROP_FPS)
print("FPS: ", fps, "Frames: ", number_off_frames)

for frame_number in tqdm(range(number_off_frames)):
    _, image = vidcap.read()
    cv2.imwrite(os.path.join(unprocessed_frames_folder_path, str(frame_number).zfill(4) + '.jpg'), image)

