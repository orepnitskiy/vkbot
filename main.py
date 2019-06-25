import requests
import vk_api
import json
from vk_api.longpoll import VkLongPoll, VkEventType
from random import randint
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
vk_session = vk_api.VkApi(token='YOUR TOKEN')
longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            if event.from_user:
                if not event.text:
                    keyboard = VkKeyboard(one_time=True)
                    keyboard.add_button("Подобрать займ", color=VkKeyboardColor.PRIMARY)
                    keyboard.add_line()
                    keyboard.add_button("Займы под 0%!", color=VkKeyboardColor.NEGATIVE)
                    keyboard.add_line()
                    keyboard.add_button("Акции и бонусы", color=VkKeyboardColor.POSITIVE)
                    vk.messages.send(
                        user_id=event.user_id,
                        message='Извините, ваше сообщение не распознано. Пожалуйста, используйте инструкции от бота или кнопки в меню',
                        random_id=randint(1, 100000000000000000000000000000000),
                        keyboard=keyboard.get_keyboard()
                    )
                else:
                    if event.text == "0" or event.text == "Главное меню" or event.text == "Начать" or event.text == "Start":
                        keyboard = VkKeyboard(one_time=True)
                        keyboard.add_button("Подобрать займ", color=VkKeyboardColor.PRIMARY)
                        keyboard.add_line()
                        keyboard.add_button("Займы под 0%!", color=VkKeyboardColor.NEGATIVE)
                        keyboard.add_line()
                        keyboard.add_button("Акции и бонусы", color=VkKeyboardColor.POSITIVE)
                        with open("message_main.txt", 'r') as f:
                            message_main = f.read()
                        name = vk.users.get(user_ids=event.user_id)[0]["first_name"]
                        vk.messages.send(
                            user_id=event.user_id,
                            message=f"Привет, {name}! {message_main}",
                            random_id=randint(1,100000000000000000000000000000000),
                            keyboard=keyboard.get_keyboard()
                        )
                    elif event.text == "1" or event.text == "Подобрать займ":
                        keyboard = VkKeyboard(one_time=True)
                        keyboard.add_button("Главное меню", color=VkKeyboardColor.NEGATIVE)
                        with open("message_zaim.txt") as f:
                            message_zaim = f.read()
                        vk.messages.send(
                            user_id=event.user_id,
                            message=message_zaim,
                            random_id=randint(1,100000000000000000000000000000000),
                            keyboard=keyboard.get_keyboard()
                        )
                    elif event.text == "3" or event.text == "Акции и бонусы" or event.text == "Другие акции":
                        keyboard = VkKeyboard(one_time=True)
                        keyboard.add_button("Займ без процентов", color=VkKeyboardColor.PRIMARY)
                        keyboard.add_line()
                        keyboard.add_button("100% одобрение", color=VkKeyboardColor.PRIMARY)
                        keyboard.add_line()
                        keyboard.add_button("Промокоды", color=VkKeyboardColor.PRIMARY)
                        vk.messages.send(
                            user_id=event.user_id,
                            message='Пожалуйста, выберите пункт в меню',
                            random_id=randint(1,100000000000000000000000000000000),
                            keyboard=keyboard.get_keyboard()
                        )
                    elif event.text == "Займ без процентов" or event.text == "Займы под 0%!" or event.text == "2":
                        keyboard = VkKeyboard(one_time=True)
                        if event.text == "Займы под 0%!":
                            keyboard.add_button("Другие акции", color=VkKeyboardColor.PRIMARY)
                            keyboard.add_line()
                        keyboard.add_button("Главное меню", color=VkKeyboardColor.NEGATIVE)
                        with open("message_0.txt", 'r') as f:
                            message_0 = f.read()
                        vk.messages.send(
                            user_id=event.user_id,
                            message=message_0,
                            random_id=randint(1,100000000000000000000000000000000),
                            keyboard=keyboard.get_keyboard()
                        )
                    elif event.text == "100% одобрение":
                        keyboard = VkKeyboard(one_time=True)
                        keyboard.add_button("Другие акции", color=VkKeyboardColor.PRIMARY)
                        keyboard.add_line()
                        keyboard.add_button("Главное меню", color=VkKeyboardColor.NEGATIVE)
                        with open("message_100.txt", 'r') as f:
                            message_100 = f.read()
                        vk.messages.send(
                            user_id=event.user_id,
                            message=message_100,
                            random_id=randint(1,100000000000000000000000000000000),
                            keyboard=keyboard.get_keyboard()
                        )
                    elif event.text == "Промокоды":
                        keyboard = VkKeyboard(one_time=True)
                        keyboard.add_button("Другие акции", color=VkKeyboardColor.PRIMARY)
                        keyboard.add_line()
                        keyboard.add_button("Главное меню", color=VkKeyboardColor.NEGATIVE)
                        vk.messages.send(
                            user_id=event.user_id,
                            message='Промокодов пока нет, подписывайтесь на нашу группу и следите за новостями!⬇',
                            random_id=randint(1,100000000000000000000000000000000),
                            keyboard=keyboard.get_keyboard()
                        )
                    else:
                        keyboard = VkKeyboard(one_time=True)
                        keyboard.add_button("Подобрать займ", color=VkKeyboardColor.PRIMARY)
                        keyboard.add_line()
                        keyboard.add_button("Займы под 0%!", color=VkKeyboardColor.NEGATIVE)
                        keyboard.add_line()
                        keyboard.add_button("Акции и бонусы", color=VkKeyboardColor.POSITIVE)
                        vk.messages.send(
                            user_id=event.user_id,
                            message='Извините, ваше сообщение не распознано. Пожалуйста, используйте инструкции от бота или кнопки в меню',
                            random_id=randint(1, 100000000000000000000000000000000),
                            keyboard=keyboard.get_keyboard()
                        )
