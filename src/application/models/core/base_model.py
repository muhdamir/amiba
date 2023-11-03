from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel


class BasePostModel(BaseModel):
    """
    Any post data should inherit from BasePostModel
    """

    model_config = ConfigDict(
        extra="forbid",
        alias_generator=to_camel,
        populate_by_name=True,
    )


class BasePatchModel(BasePostModel):
    """
    Any patch data should inherit from BasePatchModel
    """

    pass


class BaseResponseModel(BaseModel):
    """
    Any response data should inherit from BasePatchModel
    """

    model_config = ConfigDict(
        alias_generator=to_camel,
        from_attributes=True,
        populate_by_name=True,
    )
