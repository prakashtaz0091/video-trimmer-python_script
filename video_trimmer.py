from moviepy.video.io.VideoFileClip import VideoFileClip

def trim_video(input_video, output_video, start_time, **kwargs):
    # Load the video clip
    clip = VideoFileClip(input_video)
    
    if kwargs.get("end_time") is None:
        end_time = clip.duration

    # print(end_time)
    # # Trim the video from start_time to end_time
    trimmed_clip = clip.subclip(start_time, end_time)
    
    # # Write the trimmed video to a new file
    trimmed_clip.write_videofile(output_video)






def time_to_seconds(time_str):
    # Split the time string into hours, minutes, and seconds
    hours, minutes, seconds = map(int, time_str.split(':'))
    
    # Convert hours and minutes to seconds
    total_seconds = (hours * 3600) + (minutes * 60) + seconds
    
    return total_seconds


input_video = "video.mp4"
output_video = "trimmed_video.mp4"  # Replace with the desired output file path
time_str = input("Enter the start time in the format hour:min:second: ")
start_time = time_to_seconds(time_str)  # Start time in seconds
trim_video(input_video, output_video, start_time)


