import vk_api
import botT
import fille
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor


def main():
    """ Пример использования longpoll
        https://vk.com/dev/using_longpoll
        https://vk.com/dev/using_longpoll_2
    """
    
#    vk_session = vk_api.VkApi(token = 'aeb7a7e62e220a95cf2c76702cf1b9c50735ab93b688a95a203c98c678e3d60d48ec521967c551a9c7b40')
    vk_session = vk_api.VkApi(token = '973e44f4661ce7e6f56115203bdf7cffe2904eb0e6e29936ded6ee3a5055545e1e3dc2c4f834d19c7a881')
    vk = vk_session.get_api()
    keyboard = VkKeyboard()
    keyboard.add_button('11а', color=VkKeyboardColor.DEFAULT)
    keyboard.add_button('11б', color=VkKeyboardColor.DEFAULT)
    keyboard.add_button('11в', color=VkKeyboardColor.DEFAULT)
    keyboard.add_line()  # Переход на вторую строку
    keyboard.add_button('Инфо, так сказать', color=VkKeyboardColor.NEGATIVE)
    longpoll = VkLongPoll(vk_session)

    for event in longpoll.listen():

        if event.type == VkEventType.MESSAGE_NEW:
            print('Новое сообщение:')
            print('Текст: ', event.text)
            if event.text=='11а':
                botT.get_timetable2()
                alfa = botT.get_book('11а')
                vk.messages.send(user_id=event.user_id,message=alfa,keyboard=keyboard.get_keyboard())
            if event.text=='11б':
                botT.get_timetable2()
                alfa = botT.get_book('11б')
                vk.messages.send(user_id=event.user_id,message=alfa,keyboard=keyboard.get_keyboard())
            if event.text=='11в':
                botT.get_timetable2()
                alfa = botT.get_book('11в')
                vk.messages.send(user_id=event.user_id,message=alfa,keyboard=keyboard.get_keyboard())
            if event.text=='Инфо, так сказать':
                botT.get_timetable2()
                alfa = botT.get_book('11а')
                vk.messages.send(user_id=event.user_id,message='v1.1 VK_REBORN\nВсе права принадлежат тому, кому принадлежат.\nЧто пишет на доске гуманитарий, когда его вызывают на задачу по физике?\nНе дано',keyboard=keyboard.get_keyboard())
            if event.text=='Начать':
                vk.messages.send(user_id=event.user_id,message='Бот был разработан для 11А.Вопросы пишите куда нибудь.',keyboard=keyboard.get_keyboard())
            print()




if __name__ == '__main__':
    main()
