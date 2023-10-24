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
        await tc.execute('CREATE TABLE IF NOT EXISTS users(userid,dates,sends)')
        await tc.commit()

@dp.message_handler(commands=['start'])
async def state_(msg: types.Message):
    row = InlineKeyboardMarkup()
    
    rows = InlineKeyboardButton(text='Перейти на канал', url='https://t.me/kaif_works')
    rows_5 = InlineKeyboardButton(text='Я подписался ☑️', callback_data=f'set_{msg.from_user.id}')
    
    
    row.add(rows).add(rows_5)
    dates = (datetime.datetime.now() + datetime.timedelta(minutes=3)).strftime('%Y-%m-%d %H:%M')
    async with aiosqlite.connect('teleg.db') as tc:
        await tc.execute('INSERT OR IGNORE INTO users(userid,dates,sends) VALUES (?,?,?)', (msg.from_user.id,dates,0,))
        
        await tc.commit()

    try:
        await msg.answer('Привет, Для просмотра второй части из ТикТока, нужны быть подписанным на канал по заработку на написании отзывов @kaif_work', reply_markup=row)
    except:
        pass


@dp.callback_query_handler(text_contains='set')
async def state_5(css: types.CallbackQuery):
    s = css.data.split('_')
    s_ = await bot.get_chat_member(chat_id=-1001791109996, user_id=s[1])
    if s_.status in [ChatMemberStatus.MEMBER, ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.CREATOR]:
        await css.message.answer('Спасибо за подписку. \n А теперь ознакомься с лёгким заработком на написании отзывов и через 2 минуты вам придёт ссылка на вторую часть.\n Хорошего дня ❤️')
    else:
        await css.message.answer('Вы не подписались на канал')






if __name__ == '__main__':
    f = asyncio.get_event_loop()
    f.run_until_complete(datas_())
    executor.start_polling(dp, skip_updates=True)