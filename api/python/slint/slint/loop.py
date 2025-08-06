# Copyright © SixtyFPS GmbH <info@slint.dev>
# SPDX-License-Identifier: GPL-3.0-only OR LicenseRef-Slint-Royalty-free-2.0 OR LicenseRef-Slint-Software-3.0

from . import slint as native
import asyncio.selector_events
import selectors
import typing
from collections.abc import Mapping


class _SlintSelector(selectors._BaseSelectorImpl):
    def __init__(self) -> None:
        super().__init__()
        self.next_timeout = None

    def register(self, fileobj: typing.Any, events: typing.Any, data: typing.Any=None) -> selectors.SelectorKey:
        return super().register(fileobj, events, data)

    def unregister(self, fileobj) -> selectors.SelectorKey:
        return super().unregister(fileobj)

    def modify(self, fileobj, events, data=None) -> selectors.SelectorKey:
        return super().modify(fileobj, events, data)

    def select(self, timeout=None) -> typing.List[typing.Tuple[selectors.SelectorKey, typing.IO]]:
        # raise NotImplementedError
        self.next_timeout = timeout
        return []

    def close(self) -> None:
        super().close()

    def get_key(self, fileobj) -> selectors.SelectorKey:
        return super().get_key(fileobj)

    def get_map(self) -> Mapping[typing.IO, selectors.SelectorKey]:
        return super().get_map()

class SlintEventLoop(asyncio.selector_events.BaseSelectorEventLoop):
    def __init__(self) -> None:
        super().__init__(_SlintSelector())

    def run_forever(self) -> None:
        raise NotImplementedError

    def run_until_complete(self, future: asyncio.Future) -> None:
        raise NotImplementedError

    def stop(self) -> None:
        raise NotImplementedError

    def close(self) -> None:
        raise NotImplementedError

    def is_closed(self) -> bool:
        raise NotImplementedError
