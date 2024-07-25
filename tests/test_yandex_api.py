import os

import pytest
import requests
from dotenv import load_dotenv

load_dotenv()


class TestYandexApi:

    def setup_method(self):
        self.token = os.getenv('TOKEN')
        self.headers = {
            'Authorization': 'OAuth ' + self.token,
        }
        self.url = 'https://cloud-api.yandex.net/v1/disk/'

    @pytest.mark.parametrize(
        'folder_name',
        [
            'folder1',
            'folder2',
        ]
    )
    def test_create_folder_201(self, folder_name):
        url = self.url + 'resources'
        params = {'path': folder_name}
        response = requests.put(url, headers=self.headers, params=params)
        assert response.status_code == 201

    @pytest.mark.parametrize(
        'folder_name',
        [
            'folder1',
            'folder2',
        ]
    )
    def test_create_duplicate_folder_409(self, folder_name):
        url = self.url + 'resources'
        params = {'path': folder_name}
        response = requests.put(url, headers=self.headers, params=params)
        assert response.status_code == 409

    @pytest.mark.parametrize(
        'folder_name',
        [
            'folder1',
            'folder2',
        ]
    )
    def test_delete_existing_folder_204(self, folder_name):
        url = self.url + 'resources'
        params = {'path': folder_name}
        response = requests.delete(url, headers=self.headers, params=params)
        assert response.status_code == 204

    @pytest.mark.parametrize(
        'folder_name',
        [
            'folder1',
            'folder2',
        ]
    )
    def test_delete_not_existing_folder_404(self, folder_name):
        url = self.url + 'resources'
        params = {'path': folder_name}
        response = requests.delete(url, headers=self.headers, params=params)
        assert response.status_code == 404
