from environs import Env

#  Использование environs
env = Env()
env.read_env()

# С файла .env прочитываем эти данные:

BOT_TOKEN = env.str("BOT_TOKEN")  # Bot token
ADMINS = env.list("ADMINS")  # adminlar ro'yxati
GROUP=env.str("GROUP")

