#
# Copyright (C) 2022-2023 by DuskyMusic@Github, < https://github.com/DuskyMusic >.
#
# This file is part of < https://github.com/DuskyMusic/DuskyMusicBotV2 > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/DuskyMusic/DuskyMusicBotV2/blob/master/LICENSE >
#
# All rights reserved.

import os

from config import autoclean


async def auto_clean(popped):
    try:
        rem = popped["file"]
        autoclean.remove(rem)
        count = autoclean.count(rem)
        if count == 0:
            if (
                "vid_" not in rem
                or "live_" not in rem
                or "index_" not in rem
            ):
                try:
                    os.remove(rem)
                except:
                    pass
    except:
        pass
