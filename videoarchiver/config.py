from dataclasses import dataclass, field
from typing import List

from dataclasses_json import DataClassJsonMixin
from yamldataclassconfig.config import YamlDataClassConfig


@dataclass
class TvAsahiConfig(DataClassJsonMixin):
    """This class implements configuration for TV Asahi."""

    mail_address: str = None  # type: ignore
    password: str = None  # type: ignore
    list_program_id: List[str] = field(default_factory=list)  # type: ignore


@dataclass
class NiconicoConfig(DataClassJsonMixin):
    """This class implements configuration for Niconico."""

    mail_address: str = None  # type: ignore
    password: str = None  # type: ignore
    list_program_id: List[str] = field(default_factory=list)  # type: ignore


@dataclass
class Config(YamlDataClassConfig):
    """This class implements configuration wrapping."""

    tv_asahi: TvAsahiConfig = field(  # type: ignore
        default=None, metadata={"dataclasses_json": {"mm_field": TvAsahiConfig}}
    )
    niconico: NiconicoConfig = field(  # type: ignore
        default=None, metadata={"dataclasses_json": {"mm_field": NiconicoConfig}}
    )
