# Pixelle-Video

A fork of [AIDC-AI/Ovis](https://github.com/AIDC-AI/Pixelle-Video) focused on video understanding and generation with multimodal capabilities.

## Features

- Video understanding with multimodal LLMs
- Frame-level visual tokenization
- Support for long-context video processing
- Efficient inference with quantization support

## Installation

### From PyPI

```bash
pip install pixelle-video
```

### From Source

```bash
git clone https://github.com/your-org/Pixelle-Video.git
cd Pixelle-Video
pip install -e .
```

### Dev Container

This project includes a Dev Container configuration for a consistent development environment.

1. Install [Docker](https://www.docker.com/) and the [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) for VS Code.
2. Open the project in VS Code and click **Reopen in Container**.

## Quick Start

```python
from pixelle_video import VideoProcessor, load_model

# Load model
model, tokenizer = load_model("pixelle-video-7b")

# Process a video
processor = VideoProcessor(model, tokenizer)
response = processor.chat(
    video_path="path/to/video.mp4",
    query="Describe what is happening in this video."
)
print(response)
```

## Docker

```bash
docker build -t pixelle-video .
docker run --gpus all -it pixelle-video
```

## Requirements

- Python >= 3.10
- PyTorch >= 2.1
- CUDA 11.8+ (for GPU inference)

See `pyproject.toml` for full dependency list.

## License

This project is licensed under the Apache 2.0 License — see [LICENSE](LICENSE) for details.
