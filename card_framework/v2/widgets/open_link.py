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
from dataclasses import dataclass

from card_framework import AutoNumber, enum_field, standard_field
from dataclasses_json import LetterCase, dataclass_json


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class OpenLink(object):
  class OnClose(AutoNumber):
    """OnClose
    """
    NOTHING = 'NOTHING'
    RELOAD = 'RELOAD'

  class OpenAs(AutoNumber):
    """OpenAs
    """
    FULL_SIZE = 'FULL_SIZE'
    OVERLAY = 'OVERLAY'

  url: str = standard_field()
  open_as: str = enum_field()       # Not supported by chat apps
  on_close: str = enum_field()      # Not supported by chat apps
