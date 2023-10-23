from aiogram import Dispatcher,Bot,executor,types

from aiogram.types import ChatMemberStatus, InlineKeyboardButton, InlineKeyboardMarkup

import datetime
import aiosqlite
import asyncio







token = '6937427392:AAF8ZtTp-FBeODozbOUfsGNWo5tzKj2xSF0'


bot = Bot(token=token)
dp = Dispatcher(bot=bot)





async def datas_():
    async with aiosqlite.connect('teleg.db') as tc:
        await tc.execute('CREATE TABLE IF NOT EXISTS users(userid,dates,sends, sends0)')
        await tc.commit()

@dp.message_handler(commands=['start'])
async def state_(msg: types.Message):
    row = InlineKeyboardMarkup()
    
    rows = InlineKeyboardButton(text='Перейти на канал', url='https://t.me/kaif_works')
    
    
    
    row.add(rows)
    dates = (datetime.datetime.now() + datetime.timedelta(minutes=5)).strftime('%Y-%m-%d %H:%M')
    async with aiosqlite.connect('teleg.db') as tc:
        await tc.execute('INSERT OR IGNORE INTO users(userid,dates,sends,sends0) VALUES (?,?,?,?)', (msg.from_user.id,dates,0,0,))
        
        await tc.commit()

    try:
        await msg.answer('Привет, Для просмотра второй части из ТикТока, нужны быть подписанным на канал по заработку на написании отзывов @kaif_work', reply_markup=row)
    except:
        pass





if __name__ == '__main__':
    f = asyncio.get_event_loop()
    f.run_until_complete(datas_())
    executor.start_polling(dp, skip_updates=True)