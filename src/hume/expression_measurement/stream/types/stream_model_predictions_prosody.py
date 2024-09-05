# This file was auto-generated by Fern from our API Definition.

from ....core.pydantic_utilities import UniversalBaseModel
import typing
from .stream_model_predictions_prosody_predictions_item import StreamModelPredictionsProsodyPredictionsItem
from ....core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class StreamModelPredictionsProsody(UniversalBaseModel):
    """
    Response for the speech prosody emotion model.
    """

    predictions: typing.Optional[typing.List[StreamModelPredictionsProsodyPredictionsItem]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow