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
    




    dates = datetime.datetime.now().strftime('%Y-%m-%d %H-%M')
    for i in s_:
        print(i)
        s = await bot.get_chat_member(chat_id=-1001791109996, user_id=i[0])
        if s.status in [ChatMemberStatus.MEMBER, ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.CREATOR] and dates >= i[1] and i[2] == 0:
            try:



                async with aiosqlite.connect('teleg.db') as tc:
                    await tc.execute('UPDATE users SET sends = 5 WHERE userid = ?', (i[0],))
                    await tc.commit()
                await bot.send_message(chat_id=i[0], text='https://youtu.be/iNwjdSx1VdY?si=1B0Ebk-vKEp4dyI2')
            except Exception as e:
                print(e)
        
async def tests_5():

    async with aiosqlite.connect('teleg.db') as tc:

        async with tc.execute('SELECT userid,sends0 FROM users') as f:
            s = await f.fetchall()
    for i in s:
        s_ = await bot.get_chat_member(chat_id=-1001791109996, user_id=i[0])
        if i[1] == 0 and s_.status in [ChatMemberStatus.MEMBER, ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.CREATOR]:
            async with aiosqlite.connect('teleg.db') as tc:
                await tc.execute('UPDATE users SET sends0 = 5 WHERE userid = ?', (i[0],))
                await tc.commit()
            try:
                await bot.send_message(chat_id=i[0], text='Спасибо за подписку. \n А теперь ознакомься с лёгким заработком на написании отзывов и через 2 минуты вам придёт ссылка на вторую часть.\n Хорошего дня ❤️')
            except Exception as e:
                print(e)

def funcs_5():
    f = asyncio.get_event_loop()

    f.run_until_complete(tests_5())

schedule.every(5).seconds.do(funcs_5)
    




def funcs_():
    f = asyncio.get_event_loop()
    f.run_until_complete(tests())

schedule.every(15).seconds.do(funcs_)




while True:
    schedule.run_pending()
    time.sleep(5)