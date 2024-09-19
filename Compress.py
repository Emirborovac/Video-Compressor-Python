import os
import subprocess

# Define compression settings
compression_presets = {
    'soft': {'crf': '23', 'preset': 'medium'},
    'medium': {'crf': '28', 'preset': 'medium'},
    'hard': {'crf': '35', 'preset': 'fast'}
}

def get_compression_quality():
    """Prompts the user to select a compression quality"""
    print("Choose compression quality:")
    print("1. Soft Compress")
    print("2. Medium Compress")
    print("3. Hard Compress")

    choice = input("Enter your choice (1/2/3): ").strip()

    if choice == '1':
        return 'soft'
    elif choice == '2':
        return 'medium'
    elif choice == '3':
        return 'hard'
    else:
        print("Invalid choice. Defaulting to Medium Compress.")
        return 'medium'

def get_output_format():
    """Prompts the user to select an output file format"""
    print("Choose output format (e.g., mp4, mkv, avi, etc.):")
    format_choice = input("Enter the output format: ").strip().lower()

    # Simple check for supported formats (add more if needed)
    if format_choice in ['mp4', 'mkv', 'avi', 'mov', 'flv']:
        return format_choice
    else:
        print("Unsupported format. Defaulting to 'mp4'.")
        return 'mp4'

def compress_video(input_file, output_file, compression_quality, output_format):
    """Compresses the video based on selected quality and format"""
    settings = compression_presets[compression_quality]
    
    # Prepare the FFmpeg command
    ffmpeg_command = [
        'ffmpeg',
        '-i', input_file,                    # Input file
        '-vcodec', 'libx264',                # Video codec (H.264)
        '-crf', settings['crf'],             # Compression level
        '-preset', settings['preset'],       # Compression speed/quality preset
        '-acodec', 'aac',                    # Audio codec (AAC)
        f"{output_file}.{output_format}"     # Output file with chosen format
    ]

    # Run the FFmpeg command
    try:
        subprocess.run(ffmpeg_command, check=True)
        print(f"Compression successful! Output saved as {output_file}.{output_format}")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred during compression: {e}")

if __name__ == "__main__":
    # Get user input for the video file
    input_file = input("Enter the path of the video file: ").strip()

    # Check if the file exists
    if not os.path.exists(input_file):
        print("The input file does not exist. Exiting.")
        exit(1)

    # Ask user for compression quality and output format
    compression_quality = get_compression_quality()
    output_format = get_output_format()

    # Define output file name (without extension)
    output_file = input("Enter the output file name (without extension): ").strip()

    # Run the compression
    compress_video(input_file, output_file, compression_quality, output_format)
