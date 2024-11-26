from aiogram import Dispatcher, Bot, types, executor
import requests
from keyboards import flags_button
token = '7389508313:AAF6y88RoPol4ytLpAbqmWZ-Ktqp0Ny9rek'
bot = Bot(token=token)
dp = Dispatcher(bot)

flags = requests.get("http://127.0.0.1:8000/api/").json()

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    print(flags)
    await message.reply("Assalamu alaykum. Bayroqlarini ko'rin davlat nomi ustiga bosing: ", reply_markup=flags_button)


@dp.message_handler()
async def echo(message: types.Message):
    davlat = message.text
    bayroq_url = ""
    for flag in flags:
        if davlat == flag["country_name"]:
            bayroq_url = flag['image']
            bayroq_url = bayroq_url[21:]
            print(bayroq_url)

    try:
        bayroq = types.InputFile(f"..{bayroq_url}")
        await message.answer_photo(photo=bayroq, caption=davlat)
    except Exception as e:
        await message.reply(f"Rasmni yuborishda xatolik yuz berdi: {e}")



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

