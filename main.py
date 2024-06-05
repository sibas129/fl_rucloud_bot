from aiogram import Bot, Dispatcher

import asyncio
import logging

from config import BOT_TOKEN


from handlers import commands_h, main_h
from handlers.calendar import calendar_main_h
from handlers.settings import setting_main_h, change_password_h
from handlers.personal import personal_main_h
from handlers.organizations import organizations_main_h, create_group_h
from handlers.file import file_download_h, file_upload_h, get_files_from_group_h, file_delete_h
from handlers.registration import register_h


logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


async def main() -> None:
    dp.include_routers(
        commands_h.router,
        main_h.router,
        calendar_main_h.router,
        setting_main_h.router,
        personal_main_h.router,
        organizations_main_h.router,
        file_download_h.router,
        file_upload_h.router,
        register_h.router,
        create_group_h.router,
        get_files_from_group_h.router,
        change_password_h.router,
        file_delete_h.router,
    )
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())


# import requests
# import xml.etree.ElementTree as ET
#
#
# # URL вашего сервера Nextcloud и конечная точка для получения списка пользователей
# url = "https://nextcloud.prosto-web.agency/ocs/v1.php/cloud/users"
# # Добавляем заголовок OCS-APIRequest для идентификации запроса API
# headers = {
#     'OCS-APIRequest': 'true',
# }
#
# # Выполняем GET-запрос к API, используя имя пользователя и пароль администратора
# response = requests.get(url, headers=headers, auth=('admin', 'admin'))
#
# # Проверяем статус ответа
# if response.status_code == 200:
#     try:
#         # Парсим XML-ответ
#         root = ET.fromstring(response.content)
#
#         # Находим всех пользователей в XML-ответе
#         users = root.findall(".//users/element")
#
#         print("List of users:")
#         for user in users:
#             print(user.text)
#     except ET.ParseError as e:
#         print("Error parsing XML response:", e)
# else:
#     print(f"Failed to retrieve users. Status code: {response.status_code}")
#     print("Response text:", response.text)

# import requests
# from requests.auth import HTTPBasicAuth
# import xml.etree.ElementTree as ET
# #from handlers.personal.personal_main_h import get_files_list
#
# base_url = 'https://nextcloud.prosto-web.agency'
# base_username = 'admin'
# base_password = 'admin'
# # Данные для подключения к вашему серверу Nextcloud
# url = base_url + '/remote.php/dav/files/admin/'
#
# # Заголовки, необходимые для запроса WebDAV
# headers = {
#     'Depth': '1',  # Глубина запроса. 1 означает, что мы получим только содержимое корневой директории.
# }
#
# # Выполняем запрос PROPFIND для получения списка файлов
# response = requests.request("PROPFIND", url, headers=headers, auth=HTTPBasicAuth(base_username, base_password))
#
# if response.status_code == 207:
#     root = ET.fromstring(response.content)
#
#     files = []
#
#     for response_elem in root.findall('{DAV:}response'):
#         href = response_elem.find('{DAV:}href').text
#         propstat = response_elem.find('{DAV:}propstat')
#         prop = propstat.find('{DAV:}prop')
#
#         displayname_elem = prop.find('{DAV:}displayname')
#         displayname = displayname_elem.text if displayname_elem is not None else href
#         filename = displayname.rstrip('/').split('/')[-1].replace("%20", " ")
#
#         resourcetype_elem = prop.find('{DAV:}resourcetype')
#         is_collection = resourcetype_elem.find(
#             '{DAV:}collection') is not None if resourcetype_elem is not None else False
#
#         files.append(filename)
#
#     # Выводим список названий файлов и папок
#     print("List of files and directories:")
#     for file in files:
#         print(file)
# else:
#     print(f"Failed to retrieve files. Status code: {response.status_code}")
#     print("Response text:", response.text)
