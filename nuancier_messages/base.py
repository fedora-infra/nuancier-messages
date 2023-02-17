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

import warnings

from fedora_messaging import message
from fedora_messaging.schema_utils import user_avatar_url


SCHEMA_URL = "http://fedoraproject.org/message-schema/"

THING_SCHEMA = {
    "type": "object",
    "properties": {
        "id": {"type": "number"},
        "name": {"type": "string"},
        "foobar": {"type": ["string", "null"]},
        "url": {"type": "string", "format": "uri"},
    },
    "required": ["id", "name"],
}


class nuancierMessage(message.Message):
    """
    A sub-class of a Fedora message that defines a message schema for messages
    published by nuancier.
    """

    @property
    def app_name(self):
        return "nuancier"

    @property
    def app_icon(self):
        return "https://apps.fedoraproject.org/img/icons/nuancier.png"

    @property
    def agent(self):
        warnings.warn(
            "agent property is deprecated, please use agent_name instead",
            DeprecationWarning,
            stacklevel=2,
        )
        return self.body.get("agent_name")

    @property
    def agent_name(self):
        return self.body.get("agent_name")

    @property
    def agent_avatar(self):
        return user_avatar_url(self.agent_name)

    @property
    def usernames(self):
        return [self.agent_name]

    @property
    def url(self):
        try:
            return self.body["thing"]["url"]
        except KeyError:
            return None
