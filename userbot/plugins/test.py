    
#Credit To @HELLBOY_OP . Keep credit if you are going to edit it. Join @Raganrok_Official


import random, re
from uniborg.util import admin_cmd
import asyncio
from telethon import events

@borg.on(admin_cmd(pattern="test ?(.*)"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
       
        await event.edit("`Testing Hêllẞø†....`")
        await asyncio.sleep(2)
        await event.edit("`Testing Hêllẞø†..`")
        await asyncio.sleep(2)
        await event.edit("__Testing Successful__")
        await asyncio.sleep(2)
        await event.edit("`Making Output` \n\nPlease wait")
        await asyncio.sleep(2)
        await event.edit("__Output Successful__")
        await asyncio.sleep(3.5)
        await event.edit("Your[Ɽǟɢǟռօʀӄɮð†](https:/t.me/Raganrok_official) is working Fine...\n       Join @Raganrok_Official For Any Help......")
