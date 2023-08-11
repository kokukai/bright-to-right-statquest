from moviepy.editor import *

def invert_video(video_path, output_path='output_video.mp4'):
    # Read the video
    clip = VideoFileClip(video_path)
    
    # Invert the colors using numpy
    inverted_video = clip.fl_image(lambda x: 255 - x)
    
    # Set the audio of the inverted video as the original audio
    inverted_video.audio = clip.audio
    
    # Write the result to a file using the correct codec
    inverted_video.write_videofile(output_path, codec='libx264')

