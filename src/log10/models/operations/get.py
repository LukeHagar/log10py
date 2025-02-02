"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ...models.components import feedback as components_feedback
from ...models.components import httpmetadata as components_httpmetadata
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclasses.dataclass
class GetGlobals:
    x_log10_organization: str = dataclasses.field(metadata={'header': { 'field_name': 'X-Log10-Organization', 'style': 'simple', 'explode': False }})
    



@dataclasses.dataclass
class GetRequest:
    feedback_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'feedbackId', 'style': 'simple', 'explode': False }})
    r"""The feedback id to fetch."""
    x_log10_organization: Optional[str] = dataclasses.field(default=None, metadata={'header': { 'field_name': 'X-Log10-Organization', 'style': 'simple', 'explode': False }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetResponse:
    http_meta: components_httpmetadata.HTTPMetadata = dataclasses.field(metadata={'dataclasses_json': { 'exclude': lambda f: True }})
    feedback: Optional[components_feedback.Feedback] = dataclasses.field(default=None)
    r"""OK"""
    

