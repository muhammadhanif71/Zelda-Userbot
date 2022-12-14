# Credits: @mrismanaziz
# API by @tofik_dn || https://github.com/tofikdn
# FROM ZELDA USERBOT <https://github.com/nmiabdfhmy/Zelda-Userbot>
# t.me/SharingUserbot & t.me/Lunatic0de

import requests

from Zelda import CMD_HANDLER as cmd
from Zelda import CMD_HELP
from Zelda.utils import edit_or_reply, zelda_cmd


@zelda_cmd(pattern="lyrics(?:\s|$)([\s\S]*)")
async def _(event):
    query = event.pattern_match.group(1)
    if not query:
        return await edit_or_reply(event, "**Silahkan Masukan Judul Lagu**")
    try:
        xxnx = await edit_or_reply(event, "`Searching Lyrics...`")
        respond = requests.get(
            f"https://api-tede.herokuapp.com/api/lirik?l={query}"
        ).json()
        result = f"{respond['data']}"
        await xxnx.edit(result)
    except Exception:
        await xxnx.edit("**Lirik lagu tidak ditemukan.**")


CMD_HELP.update(
    {
        "lyrics": f"**Plugin : **`lyrics`\
        \n\n  •  **Syntax :** `{cmd}lyrics` <judul lagu>\
        \n  •  **Function : **Dapatkan lirik lagu yang cocok dengan judul lagu.\
    "
    }
)
