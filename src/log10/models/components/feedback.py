"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from log10 import utils
from typing import List, Optional


@dataclasses.dataclass
class JSONValues:
    r"""The values of the feedback. Must be valid JSON according to the task schema."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Feedback:
    task_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('task_id') }})
    r"""The unique identifier for the task associated with this feedback."""
    json_values: JSONValues = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('json_values') }})
    r"""The values of the feedback. Must be valid JSON according to the task schema."""
    matched_completion_ids: List[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('matched_completion_ids') }})
    r"""The matched completion ids associated with this feedback."""
    comment: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('comment') }})
    r"""The comment associated with this feedback."""
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    r"""The unique identifier for this feedback."""
    created_at_ms: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('created_at_ms'), 'exclude': lambda f: f is None }})
    r"""The epoch this schema was created."""
    completions_summary: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('completions_summary'), 'exclude': lambda f: f is None }})
    

