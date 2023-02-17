# Copyright (C) 2020  Red Hat, Inc.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

"""Unit tests for common properties of the message schemas."""

import pytest

from ..thing import NewThingV1
from .utils import DUMMY_THING


def test_properties():
    """Assert some properties are correct."""
    body = {
        "agent_name": "dummy-user",
        "thing": DUMMY_THING,
    }
    message = NewThingV1(body=body)

    assert message.app_name == "nuancier"
    assert message.app_icon == "https://apps.fedoraproject.org/img/icons/nuancier.png"
    assert message.agent_name == "dummy-user"

    with pytest.warns(DeprecationWarning) as w:
        assert message.agent, ["dummy-user"]

    assert len(w) == 1
    assert (
        w[0].message.args[0]
        == "agent property is deprecated, please use agent_name instead"
    )

    assert message.agent_avatar == (
        "https://seccdn.libravatar.org/avatar/"
        "18e8268125372e35f95ef082fd124e9274d46916efe2277417fa5fecfee31af1"
        "?s=64&d=retro"
    )
    assert message.usernames == ["dummy-user"]
