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

import unittest
from dataclasses import dataclass
from typing import List

from dataclasses_json import LetterCase, dataclass_json

from card_framework.v2.enums import HorizontalAlignment

from .widget import Widget


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class InvalidWidget(Widget):
  """Bad Widget, no override"""


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ValidWidget(Widget):
  """Good Widget"""
  camel_case_property: str = 'Inigo Montoya'

  @property
  def _widget_tag(self) -> str:
    return 'widget'


class WidgetTest(unittest.TestCase):
  def test_invalid_widget(self) -> None:
    widget = InvalidWidget()
    with self.assertRaises(NotImplementedError):
      widget._widget_tag

  def test_valid_widget(self) -> None:
    widget = ValidWidget()
    self.assertEqual(widget._widget_tag, 'widget')

  def test_valid_widget_render(self) -> None:
    widget = ValidWidget()
    self.assertDictEqual(
        widget.render(),
        {'widget': {'camelCaseProperty': 'Inigo Montoya'}})
