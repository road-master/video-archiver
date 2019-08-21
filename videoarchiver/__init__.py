from enum import Enum
from pathlib import Path

from videoarchiver.config import Config

CONFIG: Config = Config()


class Directory(Enum):
    """
    This class implements constant of path to directory of CSV.
    """
    DOWNLOAD = Path(__file__).parent.parent / 'videooutput'
    CACHE = Path(__file__).parent.parent / 'yamloutput'

    @property
    def value(self) -> Path:
        """This method overwrite super method for type hint."""
        return super().value
