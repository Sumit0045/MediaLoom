import asyncio
import importlib
from pyrogram import idle
from MediaLoom.modules import ALL_MODULES

 
loop = asyncio.get_event_loop()


async def sumit_boot():
    for all_module in ALL_MODULES:
        importlib.import_module("MediaLoom.modules." + all_module)

    print("🍄 Successfully Hosted Media Loom.")
    await idle()
    print("» Good Bye ! Stopping Bot.")


if __name__ == "__main__":
    loop.run_until_complete(sumit_boot())
