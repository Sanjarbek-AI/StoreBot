from aiogram import Dispatcher

from loader import dp
from .admin_filter import IsAdmin

if __name__ == "filters":
    dp.filters_factory.bind(IsAdmin)