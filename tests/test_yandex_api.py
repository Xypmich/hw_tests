import unittest
import requests
from parameterized import parameterized
from pprint import pprint


class TestApi(unittest.TestCase):
    ya_token = 'AQAAAABe-VUjAADLW7Gmt64TDEzInySP6-ik8pc' #input('Введите токен Яндекс Диска: ')
    URL = 'https://cloud-api.yandex.net/v1/disk/resources'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'OAuth {ya_token}'
    }

    @parameterized.expand(
        [
            ('test', '<Response [201]>', True),
            ('test', '<Response [409]>', True),
            ('book/test', '<Response [409]>', False),
            ('book', '<Response [201]>', True),
            ('book/test', '<Response [201]>', False)
        ]
    )
    def test_dir_create(self, path, result, bool_):
        response = requests.put(TestApi.URL, headers=TestApi.headers, params={'path': path})
        self.assertEqual(str(response), result)
        file_list = requests.get(TestApi.URL, headers=TestApi.headers, params={'path': '/',
                                                                               'fields': '_embedded.items.name'})
        self.assertEqual(path in [files['name'] for files in file_list.json()['_embedded']['items']], bool_)

    @classmethod
    def tearDownClass(cls) -> None:
        requests.delete(TestApi.URL, headers=TestApi.headers, params={'path': 'test', 'permanently': True})
        requests.delete(TestApi.URL, headers=TestApi.headers, params={'path': 'book', 'permanently': True})
