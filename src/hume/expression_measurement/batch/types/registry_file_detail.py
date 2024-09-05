# This file was auto-generated by Fern from our API Definition.

from ....core.pydantic_utilities import UniversalBaseModel
import pydantic
from ....core.pydantic_utilities import IS_PYDANTIC_V2
import typing


class RegistryFileDetail(UniversalBaseModel):
    file_id: str = pydantic.Field()
    """
    File ID in the Asset Registry
    """

    file_url: str = pydantic.Field()
    """
    URL to the file in the Asset Registry
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow