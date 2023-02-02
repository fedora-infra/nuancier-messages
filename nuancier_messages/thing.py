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

from .base import SCHEMA_URL, nuancierMessage, THING_SCHEMA


class NewThingV1(nuancierMessage):
    """
    A sub-class of a Fedora message that defines a message schema for messages
    published by nuancier when a new thing is created.
    """

    topic = "nuancier.new"

    body_schema = {
        "id": SCHEMA_URL + topic,
        "$schema": "http://json-schema.org/draft-04/schema#",
        "description": "Schema for messages sent when a new thing is created",
        "type": "object",
        "properties": {"agent_name": {"type": "string"}, "thing": THING_SCHEMA},
        "required": ["agent_name", "thing"],
    }

    def __str__(self):
        """Return a complete human-readable representation of the message."""
        return "New Thing: {thing}\nBy: {agent_name}\n".format(
            thing=self.body["thing"]["name"],
            agent_name=self.body["agent_name"],
        )

    @property
    def summary(self):
        """Return a summary of the message."""
        return '{agent_name} created thing "{name}" ({id})'.format(
            agent_name=self.body["agent_name"],
            name=self.body["thing"]["name"],
            id=self.body["thing"]["id"],
        )
