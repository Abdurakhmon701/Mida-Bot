from aiogram.dispatcher.filters.state import StatesGroup, State
# Машинное состояние, первый  и второе состояние при отправке сообщения пользоваетлям.
class MessageState(StatesGroup):
	first = State()
	second = State()

