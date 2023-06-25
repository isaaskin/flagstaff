from __future__ import annotations

import typing


class Command:
    def __init__(self, name: str, target: typing.Union[function, CommandList, Command], options: typing.Union[dict[str, dict], None] = None) -> None:
        self.name = name
        self.target = target
        self.options = options


CommandList = list[Command]
Flagstaff = CommandList
