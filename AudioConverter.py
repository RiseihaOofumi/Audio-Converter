from pydub import AudioSegment
import os

# Point pydub to ffmpeg
os.environ["PATH"] += os.pathsep + r"C:\ffmpeg"  # Make sure this points to the folder containing ffmpeg.exe

# Folder where script is located
folder = os.getcwd()

# List of common audio file extensions pydub can handle
audio_extensions = ['mp3', 'm4a', 'wav', 'flac', 'ogg', 'aac', 'wma']

# Loop through all audio files in the folder
for file in os.listdir(folder):
    if any(file.lower().endswith(f".{ext}") for ext in audio_extensions):
        input_ext = os.path.splitext(file)[1][1:].lower()  # detect file extension automatically
        input_path = os.path.join(folder, file)
        
        # Ask user for desired output format for this specific file
        output_ext = input(f"Enter desired output format for {file} (e.g., mp3, wav, ogg, flac): ").lower()
        output_path = os.path.splitext(input_path)[0] + f".{output_ext}"
        
        print(f"🎵 Converting: {file} ({input_ext}) → {os.path.basename(output_path)}")
        
        sound = AudioSegment.from_file(input_path, format=input_ext)
        sound.export(output_path, format=output_ext, bitrate="192k")

print("✅ All conversions complete!")
