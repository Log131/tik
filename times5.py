import schedule

import datetime

from videos import bot
import asyncio
import time
import aiosqlite
from aiogram.types import ChatMemberStatus







async def tests():
    async with aiosqlite.connect('teleg.db') as tc:
        async with tc.execute('SELECT * FROM users') as f:
            s_ = await f.fetchall()
    




    dates = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
    for i in s_:
        print(i)
        s = await bot.get_chat_member(chat_id=-1001791109996, user_id=i[0])
        if s.status in [ChatMemberStatus.MEMBER, ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.CREATOR] and dates >= i[1] and i[2] == 0:
            try:



                async with aiosqlite.connect('teleg.db') as tc:
                    await tc.execute('UPDATE users SET sends = 5 WHERE userid = ?', (i[0],))
                    await tc.commit()
                async with aiosqlite.connect('teleg.db') as tc:
                    async with tc.execute('SELECT videos FROM rrrrr') as rsr:
                        r_ = await rsr.fetchone()
                await bot.send_message(chat_id=i[0], text=r_[0])
            except Exception as e:
                print(e)
    




def funcs_():
    f = asyncio.get_event_loop()
    f.run_until_complete(tests())

schedule.every(15).seconds.do(funcs_)




while True:
    schedule.run_pending()
    time.sleep(5)