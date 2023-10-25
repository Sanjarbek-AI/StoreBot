from aiogram import types
from aiogram.dispatcher import FSMContext

from data.config import ADMINS
from keyboards.default.admin import *
from keyboards.inline.admin import admin_product_update_keyboards
from loader import dp
from states.admin import *


@dp.message_handler(text="🍟 Products", chat_id=ADMINS, state="*")
async def admin_product_handler(message: types.Message):
    text = "Welcome to products menu"
    await message.answer(text=text, reply_markup=admin_product_menu)


@dp.message_handler(text="🍕 Products", chat_id=ADMINS, state="*")
async def admin_product_handler(message: types.Message, state: FSMContext):
    await state.set_state('admin-product-inside')
    text = "Welcome to products menu"
    await message.answer(text=text, reply_markup=await admin_product_inside_menu_def())


@dp.message_handler(text="➕ Add Product", chat_id=ADMINS, state="admin-product-inside")
async def admin_product_handler(message: types.Message):
    text = "Enter name to new product."
    await message.answer(text=text)
    await AddProduct.name.set()


@dp.message_handler(chat_id=ADMINS, state=AddProduct.name)
async def admin_product_handler(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    text = "Enter price to new product."
    await message.answer(text=text)
    await AddProduct.price.set()


@dp.message_handler(chat_id=ADMINS, state=AddProduct.price)
async def admin_product_handler(message: types.Message, state: FSMContext):
    await state.update_data(price=message.text)
    text = "Enter description to new product."
    await message.answer(text=text)
    await AddProduct.about.set()


@dp.message_handler(chat_id=ADMINS, state=AddProduct.about)
async def admin_product_handler(message: types.Message, state: FSMContext):
    await state.update_data(about=message.text)
    text = "Enter image to new product."
    await message.answer(text=text)
    await AddProduct.image.set()


@dp.message_handler(chat_id=ADMINS, state=AddProduct.image, content_types=types.ContentType.PHOTO)
async def admin_product_handler(message: types.Message, state: FSMContext):
    await state.update_data(image=message.photo[-1].file_id)
    text = "Select category to new product."
    await message.answer(text=text, reply_markup=await admin_categories_menu_def())
    await AddProduct.category.set()


@dp.message_handler(chat_id=ADMINS, state=AddProduct.category)
async def admin_product_handler(message: types.Message, state: FSMContext):
    await state.update_data(category=message.text, status=1, created_at=message.date)
    data = await state.get_data()
    if db_manager.add_product(data):
        text = "Successfully added ✅"
    else:
        text = "Bot has some problems ❌"
    await message.answer(text=text, reply_markup=await admin_product_inside_menu_def())


@dp.message_handler(state="admin-product-inside", chat_id=ADMINS)
async def admin_category_handler(message: types.Message):
    name = message.text
    product = db_manager.get_product_by_name(name)

    if product:
        text = f"😋 {product[1]} | {product[2]} sum | {product[5]}\n\n{product[4]}"
        await message.answer_photo(photo=product[3], caption=text,
                                   reply_markup=await admin_product_update_keyboards(product))
