import cv2
import moviepy.editor as mp
import os
# Path to the input video
input_video_path = "Small Talk.mp4"

# Path to the replacement picture
replacement_image_path = 'image.png'

# Output video path
output_video_path = 'output_video.mp4'

# Time in seconds to start replacing the frame
start_time = 5

# Duration in seconds for which to replace the frame
duration = 3

# Load the input video
video = cv2.VideoCapture(input_video_path)

# Read the first frame to get frame properties
ret, frame = video.read()
frame_height, frame_width, _ = frame.shape

# Calculate frame numbers to start and stop replacing frames
frame_rate = video.get(cv2.CAP_PROP_FPS)
start_frame = int(start_time * frame_rate)
end_frame = int((start_time + duration) * frame_rate)

# Load the replacement image
replacement_image = cv2.imread(replacement_image_path)

# Create a new video writer object for the output video
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
output_video = cv2.VideoWriter(output_video_path, fourcc, frame_rate, (frame_width, frame_height))

# Iterate through the frames and replace the desired frames
frame_count = 0
while True:
    ret, frame = video.read()
    if not ret:
        break

    if frame_count >= start_frame and frame_count <= end_frame:
        # Resize the replacement image to match the frame size
        resized_image = cv2.resize(replacement_image, (frame_width, frame_height))

        # Replace the frame with the resized replacement image
        frame = resized_image

    # Save the modified frame to the output video
    output_video.write(frame)

    frame_count += 1

# Release resources
video.release()
output_video.release()

# Path to the source video
source_video_path = "Small Talk.mp4"

# Path to save the extracted audio
audio_output_path = 'extracted_audio.mp3'

# Path to the target video
target_video_path = 'output_video.mp4'

# Path to save the final video with added audio
final_output_path = 'final_video.mp4'

# Extract audio from the source video
video_clip = mp.VideoFileClip(source_video_path)
audio_clip = video_clip.audio
audio_clip.write_audiofile(audio_output_path)

# Load the target video
target_video_clip = mp.VideoFileClip(target_video_path)

# Load the extracted audio
extracted_audio_clip = mp.AudioFileClip(audio_output_path)

# Set the extracted audio to the target video
final_video = target_video_clip.set_audio(extracted_audio_clip)

# Write the final video with added audio
final_video.write_videofile(final_output_path, codec='libx264')

# delete the extracted_audio.mp3 file from disk
file_path ="extracted_audio.mp3"
if os.path.exists(file_path):
    os.remove(file_path)
else:
    pass

print("Modified video saved successfully!")
