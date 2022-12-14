# Coded by Koala
# Recode by @mrismanaziz

import time
from datetime import datetime
from platform import uname
from time import sleep

from Zelda import ALIVE_NAME, StartTime, bot
from Zelda.events import zelda_cmd

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


async def get_readable_time(seconds: int) -> str:
    count = 0
    up_time = ""
    time_list = []
    time_suffix_list = ["Dtk", "Mnt", "Jam", "Hari"]

    while count < 4:
        count += 1
        remainder, result = divmod(seconds, 60) if count < 3 else divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        up_time += time_list.pop() + ", "

    time_list.reverse()
    up_time += ":".join(time_list)

    return up_time


@bot.on(zelda_cmd(outgoing=True, pattern=r"keping$"))
async def _(pong):
    """For .ping command, ping the userbot from any chat."""
    await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("**γβππππππγ**")
    await pong.edit("**ββπππππππββ**")
    await pong.edit("**ππππππππ ππππ πππ πππ**")
    await pong.edit("**β¬ππππ πππππππ ππππππππ πππβ¬**")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(
        f"**β² πΊπΎπ½ππΎπ» πΌπ΄π»π΄π³ππΆ** "
        f"\n β«Έ α΄·α΅βΏα΅α΅Λ‘ `%sms` \n"
        f"**β² π±πΈπΉπΈ πΏπ΄π»π΄π** "
        f"\n β«Έ α΄·α΅α΅α΅α΅βΏα΅γ`{ALIVE_NAME}`γ \n" % (duration)
    )


@bot.on(zelda_cmd(outgoing=True, pattern=r"kping$"))
async def _(pong):
    """For .ping command, ping the userbot from any chat."""
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("8β===D")
    await pong.edit("8=β==D")
    await pong.edit("8==β=D")
    await pong.edit("8===βD")
    await pong.edit("8==β=D")
    await pong.edit("8=β==D")
    await pong.edit("8β===D")
    await pong.edit("8=β==D")
    await pong.edit("8==β=D")
    await pong.edit("8===βD")
    await pong.edit("8==β=D")
    await pong.edit("8=β==D")
    await pong.edit("8β===D")
    await pong.edit("8=β==D")
    await pong.edit("8==β=D")
    await pong.edit("8===βD")
    await pong.edit("8===βDπ¦")
    await pong.edit("8====Dπ¦π¦")
    await pong.edit("**CROOTTTT PINGGGG!**")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(
        f"**NGENTOT!! π¨**\n**KAMPANG** : %sms\n**Bot Uptime** : {uptime}π" % (duration)
    )


@bot.on(zelda_cmd(outgoing=True, pattern=r"a(?: |$)(.*)"))
async def _(event):
    await event.edit(f"**Haii Salken Saya {DEFAULTUSER}**")
    sleep(2)
    await event.edit("**Assalamualaikum**")


# Owner @Si_Dian


@bot.on(zelda_cmd(outgoing=True, pattern=r"j(?: |$)(.*)"))
async def _(event):
    await event.edit("**JAKA SEMBUNG BAWA GOLOK**")
    sleep(3)
    await event.edit("**NIMBRUNG GOBLOKK!!!π₯**")


# Owner @Si_Dian


@bot.on(zelda_cmd(outgoing=True, pattern=r"k(?: |$)(.*)"))
async def _(event):
    await event.edit(f"**Hallo KIMAAKK SAYA {DEFAULTUSER}**")
    sleep(2)
    await event.edit("**LU SEMUA NGENTOT π₯**")


# Owner @Si_Dian


@bot.on(zelda_cmd(outgoing=True, pattern=r"assal(?: |$)(.*)"))
async def _(event):
    await event.edit("**Salam Dulu Biar Sopan**")
    sleep(2)
    await event.edit("**Ψ§ΩΨ³ΩΩΩΨ§ΩΩΩ ΨΉΩΩΩΩΩΩΩΩΩ ΩΩΨ±ΩΨ­ΩΩΩΨ©Ω Ψ§ΩΩΩΩ ΩΩΨ¨ΩΨ±ΩΩΩΨ§ΨͺΩΩΩ**")
