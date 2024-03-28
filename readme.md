### Video Trimmer Script

This Python script allows you to trim a video file from a specified start time to an optional end time using the MoviePy library.

#### Usage:

1. **Installation:**

   - Make sure you have MoviePy installed. You can install it via pip:
     ```
     pip install moviepy
     ```

2. **Usage Example:**

   - Run the script providing the necessary inputs:

     ```bash
     python trim_video.py
     ```

3. **Input Parameters:**
   - `input_video`: Path to the input video file (e.g., `"video.mp4"`).
   - `output_video`: Path for the trimmed output video file (e.g., `"trimmed_video.mp4"`).
   - `start_time`: Start time of the trim in the format `hour:min:second` (e.g., `"0:01:30"` for 1 minute 30 seconds).
   - `end_time`: (Optional) End time of the trim in the same format as `start_time`. If not provided, the video will be trimmed till the end. You can specify an explicit `end_time` by providing it as a keyword argument `end_time="00:00:00"`. Any valid time frame is accepted.

#### Script Functionality:

- The script `trim_video.py` defines a function `trim_video()` which trims the input video file from a specified start time to an optional end time and saves the trimmed video to a new file.
- It also includes a utility function `time_to_seconds()` to convert time strings into seconds for easy manipulation.

#### Example:

Suppose you have a video file named `"video.mp4"` that you want to trim starting from 1 minute 30 seconds. You want the trimmed portion to span until 2 minutes 30 seconds.

```python
from moviepy.video.io.VideoFileClip import VideoFileClip
from trim_video import trim_video, time_to_seconds

input_video = "video.mp4"
output_video = "trimmed_video.mp4"
start_time = "0:01:30"  # Start trimming from 1 minute 30 seconds
end_time = "0:02:30"  # End trimming at 2 minutes 30 seconds

start_seconds = time_to_seconds(start_time)  # Convert start time to seconds
end_seconds = time_to_seconds(end_time)  # Convert end time to seconds
trim_video(input_video, output_video, start_seconds, end_time=end_seconds)
```

This will trim the video `"video.mp4"` starting from 1 minute 30 seconds and ending at 2 minutes 30 seconds, and save the trimmed version as `"trimmed_video.mp4"`.
