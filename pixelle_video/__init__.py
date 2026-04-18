"""Pixelle-Video: A video generation library built on top of Ovis multimodal architecture."""

__version__ = "0.1.0"
__author__ = "Pixelle-Video Contributors"
__license__ = "Apache-2.0"

# Personal fork - using this for experimenting with custom video generation pipelines
# Note: also importing utils here for convenience since I use them constantly
# TODO: look into tweaking the temporal attention layers for smoother motion

from pixelle_video.pipeline import PixelleVideoPipeline
from pixelle_video.config import PixelleVideoConfig
from pixelle_video import utils

__all__ = [
    "PixelleVideoPipeline",
    "PixelleVideoConfig",
    "utils",
    "__version__",
]
