import os
import random
import requests
from moviepy.editor import ImageSequenceClip, AudioFileClip, CompositeAudioClip
from PIL import Image
import colorama
from colorama import *
import time

# Read the search term from the stocktopic.txt file
with open('stocktopic.txt', 'r') as file:
    search_term = file.read().strip()

print(Fore.CYAN + 'Connecting to pixabay API...')
# Make the API request using the search term
url = f'https://pixabay.com/api/?key=(YOUR API KEY GOES HERE)&q={search_term}&image_type=photo&pretty=true&per_page=20'
r = requests.get(url)
json_data = r.json()
time.sleep(1)
print(Fore.CYAN + 'Connection Established...')
time.sleep(0.5)
print(Fore.BLUE + 'Starting AYT automater videomaker service...')
time.sleep(2)
print('')
print('')
print(Fore.BLUE + 'AYT automater : VideoMaker service | Made by flip')
print('')

# Download images
image_paths = []
for image in json_data['hits']:
    name = str(image['id'])  # Convert to string
    img_url = image['largeImageURL']
    r = requests.get(img_url, stream=True)
    # Save the image in the "images" folder
    image_path = os.path.join('images', name + '.jpg')
    with open(image_path, 'wb') as f:
        f.write(r.content)
    image_paths.append(image_path)
    print(Fore.RED + f"Downloaded image: {image_path}")

# Resize images to have even dimensions
min_width = min_height = float('inf')
for image_path in image_paths:
    with Image.open(image_path) as img:
        width, height = img.size
        min_width = min(min_width, width)
        min_height = min(min_height, height)

# Ensure the dimensions are even
if min_width % 2 != 0:
    min_width -= 1
if min_height % 2 != 0:
    min_height -= 1

# Resize all images to the smallest dimensions found
for image_path in image_paths:
    with Image.open(image_path) as img:
        img_resized = img.resize((min_width, min_height), Image.BICUBIC)
        img_resized.save(image_path)

# Determine the duration of the voiceover
voiceover_path = os.path.join('output', 'output.mp3')
voiceover_clip = AudioFileClip(voiceover_path)
voiceover_duration = voiceover_clip.duration

# Calculate the total duration for which images should be shown (same as voiceover duration)
total_image_duration = voiceover_duration

# Calculate the number of images needed to fill this duration
image_duration = 0.8  # Duration per image
num_images = int(total_image_duration / image_duration)

# Trim image paths to match the required number of images
image_sequence = image_paths[:num_images]

# Create video from downloaded images until the voiceover ends
clip = ImageSequenceClip(image_sequence, durations=[image_duration] * num_images)

# Load voiceover audio file
voiceover_clip = voiceover_clip.set_duration(clip.duration)

# Load background music
music_folder = 'music'
music_files = [f for f in os.listdir(music_folder) if f.endswith('.mp3')]
random_music_file = random.choice(music_files)
music_path = os.path.join(music_folder, random_music_file)
music_clip = AudioFileClip(music_path)

# Set the duration of the music clip to match the voiceover
music_clip = music_clip.set_duration(voiceover_clip.duration)

# Adjust the volume of the music clip
music_clip = music_clip.volumex(0.2)

# Combine voiceover and background music
final_audio = CompositeAudioClip([voiceover_clip, music_clip])

# Set audio to the video
final_clip = clip.set_audio(final_audio)

# Save the final video
output_folder = 'output'
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
final_clip.write_videofile(os.path.join(output_folder, 'finaloutput.mp4'), codec='libx264', fps=24, ffmpeg_params=['-pix_fmt', 'yuv420p'])
