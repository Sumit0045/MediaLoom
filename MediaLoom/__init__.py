import asyncio, os, uvicorn
from fastapi import FastAPI
from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN


# ---------------------------------------------------------------- #

loop = asyncio.get_event_loop()

# ----------------------------- App-Client ----------------------------- #

api = FastAPI()
app = Client(":MediaLoom:", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)



# ----------------------------Bot-Info---------------------------- #

async def run_app():
    port = int(os.getenv("PORT", 8000))
    config = uvicorn.Config("MediaLoom:api", host="0.0.0.0", port=port, workers=1)
    server = uvicorn.Server(config)
    await server.serve()

async def start_app():
    global BOT_ID, BOT_NAME, BOT_USERNAME
    await app.start()
    getme = await app.get_me()
    BOT_ID = getme.id
    BOT_USERNAME = getme.username
    if getme.last_name:
        BOT_NAME = getme.first_name + " " + getme.last_name
    else:
        BOT_NAME = getme.first_name

loop.create_task(run_app())
loop.run_until_complete(start_app())

# ---------------------------------------------------------------- #
