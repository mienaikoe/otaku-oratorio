# Requires ffmpeg to be installed and in your PATH
# Usage: ./convert.sh

# ffmpeg -i ssbb_credits.mp4 -c:v libvpx-vp9 -crf 30 -b:v 0 -b:a 320k -c:a libopus ssbb_credits.webm

if [ ! -x "$(command -v ffmpeg)" ]; then
    echo "Error: ffmpeg is not installed or not in your PATH."
    exit 1
fi

if [ ! -f "Sequence 01.mp4" ]; then
    echo "Error: Sequence 01.mp4 not found!"
    exit 1
fi

echo "Converting Sequence 01.mp4 to ../game/video/ssbb_credits.webm..."
ffmpeg -i "Sequence 01.mp4" -lossless 1 ../game/video/ssbb_credits.webm
