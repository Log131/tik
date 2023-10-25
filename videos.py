from aiogram import Dispatcher,Bot,executor,types

from aiogram.types import ChatMemberStatus, InlineKeyboardButton, InlineKeyboardMarkup

import datetime
import aiosqlite
import asyncio
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext





token = '6937427392:AAF8ZtTp-FBeODozbOUfsGNWo5tzKj2xSF0'


bot = Bot(token=token)
dp = Dispatcher(bot=bot, storage=MemoryStorage())





async def datas_():
    async with aiosqlite.connect('teleg.db') as tc:
        await tc.execute('CREATE TABLE IF NOT EXISTS users(userid,dates TIMESTAMP,sends)')
        await tc.execute('CREATE TABLE IF NOT EXISTS rrrrr(videos)')
        await tc.commit()
    async with aiosqlite.connect('teleg.db') as tc:
        await tc.execute('INSERT OR REPLACE INTO rrrrr(videos) VALUES (?)', ('ссылка',))
        await tc.commit()

@dp.message_handler(commands=['start'])
async def state_(msg: types.Message):
    row = InlineKeyboardMarkup()
    
    rows = InlineKeyboardButton(text='Перейти на канал', url='https://t.me/kaif_works')
    rows_5 = InlineKeyboardButton(text='Я подписался ☑️', callback_data=f'set_{msg.from_user.id}')
    
    
    row.add(rows).add(rows_5)
    dates = (datetime.datetime.now() + datetime.timedelta(minutes=3)).strftime('%Y-%m-%d %H:%M')
    async with aiosqlite.connect('teleg.db') as tc:
        
        await tc.execute('INSERT OR REPLACE INTO users(userid,dates,sends) VALUES (?,?,?)', (msg.from_user.id,dates,0,))
        
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




class sends(StatesGroup):
    state_s = State()



@dp.message_handler(commands=['r'], state=None)
async def state_6(msg: types.Message, state: FSMContext):
    row = InlineKeyboardMarkup()
    rows = InlineKeyboardButton(text='Отмена', callback_data='cansel')
    row.add(rows)
    s = await bot.get_chat_member(chat_id=-1001791109996, user_id=msg.from_user.id)
    if s.status in [ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.CREATOR]:
        await msg.answer('Отправьте ссылку видео', reply_markup=row)
        await sends.state_s.set()





@dp.message_handler(state=sends.state_s)
async def state_555(msg: types.Message, state: FSMContext):
    try:
        async with aiosqlite.connect('teleg.db') as tc:
            await tc.execute('UPDATE rrrrr SET videos = ?', (msg.text,))
            await tc.commit()
        await msg.answer('Обновлено!')
        await state.finish()
    except Exception as e:

        print(e)
        await state.finish()
        await msg.answer('Произошла ошибка')

@dp.callback_query_handler(text='cansel', state=sends.state_s)
async def state_565(css: types.CallbackQuery, state: FSMContext):
    await css.answer()

    await state.finish()
    
    await css.message.answer('Отменено')





if __name__ == '__main__':
    f = asyncio.get_event_loop()
    f.run_until_complete(datas_())
    executor.start_polling(dp, skip_updates=True)