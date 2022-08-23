import requests


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        """Метод загружает файлы по списку file_list на Яндекс диск"""
        headers = {'Authorization': f'OAuth {token}'}
        params = {'path': f'Netology test/{file_path}', 'overwrite': 'true'}
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        upload_link = requests.get(upload_url, headers=headers, params=params).json()['href']
        resp = requests.put(upload_link, data=open(file_path, encoding='utf-8'))
        resp.raise_for_status()
        if resp.status_code == 201:
            return print("Файл загружен")
        else:
            return print("Ошибка")


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = 'Test_save.txt'
    token = ...  # Вставить свой token полученный из Yandex disk api
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)
