"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ...models.components import httpmetadata as components_httpmetadata
from ...models.components import session as components_session
from dataclasses_json import Undefined, dataclass_json
from log10 import utils
from typing import Optional


@dataclasses.dataclass
class CreateSessionGlobals:
    x_log10_organization: str = dataclasses.field(metadata={'header': { 'field_name': 'X-Log10-Organization', 'style': 'simple', 'explode': False }})
    



@dataclasses.dataclass
class CreateSessionRequest:
    x_log10_organization: Optional[str] = dataclasses.field(default=None, metadata={'header': { 'field_name': 'X-Log10-Organization', 'style': 'simple', 'explode': False }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreateSessionResponseBody:
    r"""Created"""
    session: Optional[components_session.Session] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('session'), 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreateSessionResponse:
    http_meta: components_httpmetadata.HTTPMetadata = dataclasses.field(metadata={'dataclasses_json': { 'exclude': lambda f: True }})
    object: Optional[CreateSessionResponseBody] = dataclasses.field(default=None)
    r"""Created"""
    

