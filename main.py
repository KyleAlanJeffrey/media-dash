# Docs Reference
# https://pyatv.dev/development/

import asyncio
import time
from PIL import Image
from pyatv import scan, pair, connect
from pyatv.const import Protocol
import io
from pyatv.interface import PushListener

atv = None


class SongTitleListener(PushListener):
    def playstatus_update(self, _, playstatus):
        print(playstatus)
        if "title" in playstatus:
            print(playstatus)
            print(f"Current Song Title: {playstatus['title']}")

    def playstatus_error(self, updater, exception: Exception) -> None:
        return super().playstatus_error(updater, exception)


async def main():
    global atv

    loop = asyncio.get_event_loop()
    atvs = await scan(loop)
    conf = None
    for i, atv in enumerate(atvs):
        print(atv.name)
        print(atv.device_info.model)
        if atv.device_info.model.name == "HomePod":
            conf = atvs[i]

    atv = await connect(conf, loop)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
listener = SongTitleListener()

atv.push_updater.listener = listener
# Start the push listener
atv.push_updater.start()
try:
    print(atv)
    # Keep the program running
    while True:
        pass
except KeyboardInterrupt:
    # Stop the push listener on keyboard interrupt
    atv.push_updater.stop()