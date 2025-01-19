from aiogram.types import Message

# from db import insert_user_record
from loader import dp


# from num2words import num2words
# from .callback import game


# def get_money_text(money_num: float):
# 	calc_operation = '+' if game.type == 'plus' else '-'
# 	result_string = f"Расчетная сумма {calc_operation} налог {int(100 - game.size * 100)}%:\n\n{money_num}\n"
# 	splited_num: list[str] = str(money_num).split('.')
# 	rub = num2words(splited_num[0], lang='ru')
# 	kop = str(splited_num[1])
# 	kop += " коп."
# 	last_word: str = (rub.split())[-1]
# 	if last_word == 'один':
# 		text = rub + ' рубль, ' + kop
# 	elif last_word in {'два', 'три', 'четыре'}:
# 		text = rub + ' рубля, ' + kop
# 	else:
# 		text = rub + ' рублей, ' + kop
# 	result_string += text
# 	return result_string
#
#
@dp.message()
async def text_handler(message: Message) -> None:
    await message.answer("Excusez-moi, je ne vous comprends pas, on ne m'a pas appris cela")
# 	msg = ''.join(message.md_text.split('\\'))
# 	msg = msg.replace(",", ".")
# 	result = None
# 	try:

# 		msg_clean = float(msg)
# 		try:
# 			if game.type == 'plus':
# 				result = round(msg_clean / game.size, 2)
# 			elif game.type == 'minus':
# 				result = round(msg_clean * game.size, 2)
# 			answer_text = f"{get_money_text(result)}"
# 			await message.answer(answer_text)
# 			user_data = dict(
# 				chat_id=message.chat.id,
# 				name=message.chat.username,
# 				date=message.date,
# 				text=' '.join(answer_text.split())
# 				)
# 			await insert_user_record(user_data)
# 		except Exception:
# 			await message.answer("Nice try! Please start this bot...")
# 	except Exception:
# 		if message.poll:
# 			await message.answer(f"Некорректный ввод, используйте только числа и точку! {message}")
# 		await message.answer(f"Некорректный ввод, используйте только числа и точку! {message}")
