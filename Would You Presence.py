# Would You Presence #
# Made by Niclas#2307 #
# https://discord.gg/D2h9gFCbuC #
print("Would You Presence")
print("Made by Niclas#2307")

import pypresence
from pypresence import Presence    # pip install pypresence


import time



client_id = '1008861912919978026'

RPC = Presence(client_id)
RPC.connect()

print(f"Connected to Client.")
time.sleep(5)


start_time=int(time.time())

RPC.update(
    details=f"Invite Would You to your server!",
    large_image = f"https://niclas.wants-to.party/g6qW4sjMeK.jpg",
    large_text = "Would You?",
    buttons = [
        {"label": "🔗 Invite", "url": "https://discord.com/oauth2/authorize?client_id=981649513427111957&permissions=274878294080&scope=bot%20applications.commands"},
        {"label": "⏫ Vote for me!", "url": "https://top.gg/bot/981649513427111957/vote"}
        ],
        start = start_time
        )



while True:
    time.sleep(15)
    RPC.update(
        details=f"Increase your servers activity!",
        large_image = f"https://niclas.wants-to.party/g6qW4sjMeK.jpg",
        large_text = "Would You?",
        buttons = [
            {"label": "🔗 Invite", "url": "https://discord.com/oauth2/authorize?client_id=981649513427111957&permissions=274878294080&scope=bot%20applications.commands"},
            {"label": "⏫ Vote for me!", "url": "https://top.gg/bot/981649513427111957/vote"}
            ],
            start = start_time
            )
    time.sleep(15)
    RPC.update(
        details=f"Invite Would You to your server!",
        large_image = f"https://niclas.wants-to.party/g6qW4sjMeK.jpg",
        large_text = "Would You?",
        buttons = [
            {"label": "🔗 Invite", "url": "https://discord.com/oauth2/authorize?client_id=981649513427111957&permissions=274878294080&scope=bot%20applications.commands"},
            {"label": "⏫ Vote for me!", "url": "https://top.gg/bot/981649513427111957/vote"}
            ],
            start = start_time
            )