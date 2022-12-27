from moviepy.editor import *
import os
import numpy as np
from pathlib import Path
import shutil
import glob

# Katna
from Katna.video import Video
from Katna.writer import KeyFrameDiskWriter
import os

class VideoConverter:

    def __init__(self,video_path, duration = 30, keyframes = 10):
        self.video_path = video_path
        self.output_dir = os.path.splitext(video_path)[0].replace('tmp','data')
        Path(self.output_dir).mkdir(exist_ok=True,parents=True)
        self.new_video_path = os.path.join(self.output_dir,'video'+os.path.splitext(self.video_path)[-1])
        shutil.move(self.video_path, os.path.join(self.output_dir,'video'+os.path.splitext(self.video_path)[-1]))
        self.video_path = self.new_video_path
        self.video_duration = self._get_video_duration()
        self.keyframes = keyframes
        self.allowed_duration = duration


    def extact_sound_from_video(self):
        if self.video_duration > self.allowed_duration:
            clip = VideoFileClip(self.video_path).subclip(0,self.allowed_duration)
        else:
            clip = VideoFileClip(self.video_path)
        filename = os.path.join(self.output_dir, 'sound.wav')
        clip.audio.write_audiofile(filename)
        return filename


    def _get_video_duration(self):
        video = VideoFileClip(self.video_path)
        video_duration = int(video.duration)
        return video_duration

    def extract_frames(self):
        clip = VideoFileClip(self.video_path)
        times = np.linspace(0,self.video_duration,6)[:5]
        img_list = []
        for index,t in enumerate(times):
            imgpath = os.path.join(self.output_dir, '{}.png'.format(index+1))
            clip.save_frame(imgpath, t)
            img_list.append(imgpath)

        return img_list


    def extract_frames_2(self):

        # initialize video module
        vd = Video()

        # number of images to be returned
        no_of_frames_to_returned = self.keyframes

        # initialize diskwriter to save data at desired location
        diskwriter = KeyFrameDiskWriter(location=self.output_dir)

        # Video file path
        video_file_path = self.video_path

        print(f"Input video file path = {video_file_path}")

        # extract keyframes and process data with diskwriter
        vd.extract_video_keyframes(
            no_of_frames=no_of_frames_to_returned, file_path=video_file_path,
            writer=diskwriter
        )
        return glob.glob(self.output_dir + '/*.jpeg')
        

