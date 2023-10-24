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
    




    dates = datetime.datetime.now()
    for i in s_:
        s = await bot.get_chat_member(chat_id=-1001791109996, user_id=i[0])
        if s.status in [ChatMemberStatus.MEMBER, ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.CREATOR] and dates >= i[1] and i[2] == 0:
            try:



                async with aiosqlite.connect('teleg.db') as tc:
                    await tc.execute('UPDATE users SET sends = 5 WHERE userid = ?', (i[0],))
                    await tc.commit()
                await bot.send_message(chat_id=i[0], text='https://youtu.be/iNwjdSx1VdY?si=1B0Ebk-vKEp4dyI2')
            except Exception as e:
                print(e)
    




def funcs_():
    f = asyncio.get_event_loop()
    f.run_until_complete(tests())

schedule.every(15).seconds.do(funcs_)




while True:
    schedule.run_pending()
    time.sleep(5)
