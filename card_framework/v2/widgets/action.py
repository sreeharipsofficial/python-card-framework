# Copyright 2022 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, List, Mapping

from card_framework import list_field, standard_field
from dataclasses_json import LetterCase, config, dataclass_json

from ..enums import LoadIndicator
from ..widget import Widget


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class Action(Widget):
  function: str = ''
  parameters: List[ActionParameter] = list_field()
  load_indicator: LoadIndicator = standard_field()
  persist_values: bool = standard_field()

  @property
  def _widget_tag(self) -> str:
    """The widget tag name.

    Returns:
        str: The key by which the widget will be rendered in the Section.
    """
    return 'action'


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ActionParameter(Widget):
  key: str = standard_field()
  value: str = standard_field()

  @property
  def _widget_tag(self) -> str:
    """The widget tag name.

    Returns:
        str: The key by which the widget will be rendered in the Section.
    """
    return 'actionParameter'

  def render(self) -> Mapping[str, Any]:
    """Renders the response to json.

    Returns:
        Mapping[str, Any]: _description_
    """
    return self.to_dict()