from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional

from dataclasses_json import DataClassJsonMixin
from marshmallow import fields

from videoarchiver.windows import Windows


@dataclass
class Episode(DataClassJsonMixin):
    article_id: int
    caption: str
    delivery_start_date: datetime = field(
        metadata={
            "dataclasses_json": {
                "encoder": datetime.isoformat,
                "decoder": datetime.fromisoformat,
                "mm_field": fields.DateTime(format="iso"),
            }
        }
    )
    directory: str
    episode_code: int
    episode_id: int
    episode_name: str
    episode_num: int
    extra_large_image_url: str
    image_url: str
    image_url_mb: str
    image_url_pc: str
    large_image_url: str
    medium_image_url: str
    play_time: int
    program_code: int
    program_name: str
    small_image_url: str
    small_medium_image_url: str
    sort: int
    sub_sort: Optional[int]

    @property
    def episode_name_for_windows_path(self):
        return Windows.replace_disallow_character(self.episode_name)
