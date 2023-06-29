import requests

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def _get_upload_link(self, file_path):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": file_path, "overwrite": "true"}
        response = requests.get(url=upload_url, headers=headers, params=params)
        return response.json()

    def upload(self, file_path: str):
        data = self._get_upload_link(file_path=file_path)
        url = data.get('href')
        response = requests.put(url=url, data=open(file_path, 'rb'))
        if response.status_code == 201:
            print("Success")

if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = 'square.jpg'
    token = ' '
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)