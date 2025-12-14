from pydantic import BaseModel, Field

class RunCreateRequest(BaseModel):
    input: str = Field(min_length=1)
    mode: str = Field(default="Summarise")

    # Privacy controls
    no_store: bool = False
    redact_before_store: bool = True
    require_confirm_if_pii: bool = True
    confirmed_pii: bool = False
