from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")
ADMINS = env.list("ADMINS")
IP = env.str("ip")

CHANNELS = (
    {'id': -1002028491479, 'name': "Test 463", 'link': "https://t.me/+6sccjf47L2E0YWQy"},
    {'id': -1001967245677, 'name': "Test", 'link': "https://t.me/+0gUAMSM42kYyNGVi"},
)
