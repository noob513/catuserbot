#made by LEGENDX22
#maked by LEGENDX22
#credits TEAMLEGEND

from telethon.errors.rpcerrorlist import YouBlockedUserError

from userbot.utils import admin_cmd



bot = Config.PM_LOGGR_BOT_API_ID


@borg.on(admin_cmd("fban ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    sysarg = event.pattern_match.group(1)
    if sysarg == "":
        async with borg.conversation(bot) as conv:
            try:
                await conv.send_message("/fban ")
                audio = await conv.get_response()
                await borg.send_message(event.chat_id, audio.text)
                await event.delete()
            except YouBlockedUserError:
                await event.edit("Error: GO TO LEGEND X FAST")
    elif "@" in sysarg:
        async with borg.conversation(bot) as conv:
            try:
                await conv.send_message("/fban " + sysarg)
                audio = await conv.get_response()
                await borg.send_message(event.chat_id, audio.text)
                await event.delete()
            except YouBlockedUserError:
                await event.edit("Error: GO TO LEGEND X FAST!")
    elif "" in sysarg:
        async with borg.conversation(bot) as conv:
            try:
                await conv.send_message("/fban " + sysarg)
                audio = await conv.get_response()
                await borg.send_message(event.chat_id, audio.text)
                await event.delete()
            except YouBlockedUserError:
                await event.edit("Error: GO TO LEGEND X FAST")


@borg.on(admin_cmd("unfban ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    sysarg = event.pattern_match.group(1)
    if sysarg == "":
        async with borg.conversation(bot) as conv:
            try:
                await conv.send_message("/unfban ")
                audio = await conv.get_response()
                await borg.send_message(event.chat_id, audio.text)
                await event.delete()
            except YouBlockedUserError:
                await event.edit("Error: go to LEGEND X FAST")
    elif "@" in sysarg:
        async with borg.conversation(bot) as conv:
            try:
                await conv.send_message("/unfban " + sysarg)
                audio = await conv.get_response()
                await borg.send_message(event.chat_id, audio.text)
                await event.delete()
            except YouBlockedUserError:
                await event.edit("Error: GO TO LEGEND X FAST")
    elif "" in sysarg:
        async with borg.conversation(bot) as conv:
            try:
                await conv.send_message("/unfban " + sysarg)
                audio = await conv.get_response()
                await borg.send_message(event.chat_id, audio.text)
                await event.delete()
            except YouBlockedUserError:
                await event.edit("Error : GO TO LEGEND X FAST")