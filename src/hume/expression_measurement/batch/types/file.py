# This file was auto-generated by Fern from our API Definition.

from ....core.pydantic_utilities import UniversalBaseModel
import typing
import pydantic
import typing_extensions
from ....core.serialization import FieldMetadata
from ....core.pydantic_utilities import IS_PYDANTIC_V2


class File(UniversalBaseModel):
    """
    The list of files submitted for analysis.
    """

    filename: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the file.
    """

    content_type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The content type of the file.
    """

    md_5_sum: typing_extensions.Annotated[str, FieldMetadata(alias="md5sum")] = pydantic.Field()
    """
    The MD5 checksum of the file.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow