import requests
import uuid

from config.headers import Headers


class TestReport:

    def test_report(self):
        response = requests.get(
            url=f'https://reporting.test={uuid.uuid4()}',
            headers=Headers.cms_token
        )
        with open('file.xls', 'wb') as f:
            f.write(response.content)
