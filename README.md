
# Video Compression Tool

This Python script allows you to compress video files by choosing between soft, medium, or hard compression levels. You can also specify the output format (e.g., mp4, mkv, avi) for the compressed file.

## Features
- **Compression Quality**: Choose between soft, medium, or hard compression levels.
- **Output Formats**: Specify the output video format such as `mp4`, `mkv`, `avi`, `mov`, etc.
- **Efficient Compression**: The script uses `ffmpeg` for high-quality compression.

## Requirements

### System Requirements
This script depends on `FFmpeg` being installed on your system. Please ensure you have FFmpeg installed and available in your system's PATH.

- **FFmpeg**: [Download FFmpeg](https://ffmpeg.org/download.html)

### Python Dependencies
The following Python dependencies are required to run the script:

- `subprocess` (standard Python library)
- `os` (standard Python library)

Since `subprocess` and `os` are standard libraries, no additional installation for Python packages is required.

### Install FFmpeg

1. **Linux**: Run the following command:
    ```bash
    sudo apt install ffmpeg
    ```

2. **macOS** (with Homebrew):
    ```bash
    brew install ffmpeg
    ```

3. **Windows**:
    - Download the FFmpeg static build from [here](https://ffmpeg.org/download.html).
    - Extract the files and add the `bin` folder to your system's PATH variable.

#### Adding FFmpeg to PATH (Windows)
To add FFmpeg to your Windows PATH:

1. Download FFmpeg from the official website.
2. Extract the zip and copy the path to the `bin` folder (e.g., `C:\ffmpeg\bin`).
3. Open **System Properties** -> **Environment Variables**.
4. Under the "System Variables" section, locate and edit the `Path` variable.
5. Add a new entry and paste the path to the FFmpeg `bin` directory.
6. Click **OK** and restart your terminal.

## How to Use the Script

### Step 1: Clone the Repository

First, clone the repository to your local machine:

```bash
git clone <repository-url>
cd <repository-directory>
```

### Step 2: Ensure FFmpeg is Installed

Make sure FFmpeg is properly installed and available in your system's PATH.

To check if FFmpeg is installed correctly, run:

```bash
ffmpeg -version
```

### Step 3: Run the Script

To compress a video, run the script by following these steps:

1. Open a terminal or command prompt.
2. Run the script by using:

    ```bash
    python video_compressor.py
    ```

3. Provide the necessary inputs when prompted:
   - **Video File Path**: Enter the full path to the video file you want to compress.
   - **Compression Quality**: Choose `1` for soft, `2` for medium, or `3` for hard compression.
   - **Output Format**: Specify the output format (e.g., `mp4`, `mkv`, `avi`).
   - **Output File Name**: Provide a name for the output file (without extension).

The script will compress the video based on the selected quality and output format, saving it to the provided file name.

### Example Usage

```
Enter the path of the video file: /path/to/video.mp4
Choose compression quality:
1. Soft Compress
2. Medium Compress
3. Hard Compress
Enter your choice (1/2/3): 2
Choose output format (e.g., mp4, mkv, avi, etc.): mkv
Enter the output file name (without extension): compressed_video
```

The output will be saved as `compressed_video.mkv`.

## Requirements File

There are no additional Python packages required for this project other than the built-in libraries (`os`, `subprocess`). If you want to create a `requirements.txt` file for reference or to include future packages, you can start with the following minimal version:

```txt
# Standard libraries, no additional dependencies required
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```# Video-Compressor-Python