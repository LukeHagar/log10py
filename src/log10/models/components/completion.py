"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .createchatcompletionrequest import CreateChatCompletionRequest
from .createchatcompletionresponse import CreateChatCompletionResponse
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from log10 import utils
from typing import List, Optional


class Kind(str, Enum):
    r"""The kind of completion i.e. chat messages or prompt"""
    CHAT = 'chat'
    PROMPT = 'prompt'


class Status(str, Enum):
    r"""The status of this completion."""
    STARTED = 'started'
    FINISHED = 'finished'
    FAILED = 'failed'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Stacktrace:
    file: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('file') }})
    r"""The file associated with this stacktrace."""
    line: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('line') }})
    r"""The line associated with this stacktrace."""
    lineno: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('lineno') }})
    r"""The line number associated with this stacktrace."""
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    r"""The function or module associated with this stacktrace."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Completion:
    organization_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('organization_id') }})
    r"""The unique identifier for the organization."""
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    r"""The unique identifier for this task."""
    kind: Optional[Kind] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('kind'), 'exclude': lambda f: f is None }})
    r"""The kind of completion i.e. chat messages or prompt"""
    status: Optional[Status] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status'), 'exclude': lambda f: f is None }})
    r"""The status of this completion."""
    tags: Optional[List[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tags'), 'exclude': lambda f: f is None }})
    r"""The tags for this completion."""
    request: Optional[CreateChatCompletionRequest] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('request'), 'exclude': lambda f: f is None }})
    response: Optional[CreateChatCompletionResponse] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('response'), 'exclude': lambda f: f is None }})
    r"""Represents a chat completion response returned by model, based on the provided input."""
    stacktrace: Optional[List[Stacktrace]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('stacktrace'), 'exclude': lambda f: f is None }})
    r"""The stacktrace for this completion."""
    session_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('session_id'), 'exclude': lambda f: f is None }})
    r"""The session id for this completion."""
    duration: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('duration'), 'exclude': lambda f: f is None }})
    r"""The duration of this completion in seconds."""
    failure_kind: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('failure_kind'), 'exclude': lambda f: f is None }})
    r"""The failure kind of this completion."""
    failure_reason: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('failure_reason'), 'exclude': lambda f: f is None }})
    r"""The failure reason of this completion."""
    

