import os
from typing import Tuple

import requests
from constants import Constants
from pdf_validater import PdfValidater
from pandas import Series


class Downloader:
    validater = PdfValidater()
    download_path: str = Constants.DownloadDir.value

    def __init__(self):
        os.makedirs(self.download_path, exist_ok=True)

    def download_file(self, url) -> Tuple[int, bytes]:
        res: requests.Response = requests.get(url)
        return (res.status_code, res.content)

    def download_row(self, row: Series) -> bool:
        primary_url: str = row[Constants.PrimaryUrl.value]
        secondary_url: str = row[Constants.SecondaryUrl.value]
        file_name: str = row['BRnum'] + '.pdf'
        file_path = os.path.join(self.download_path, file_name)

        for i, url in enumerate([primary_url, secondary_url]):
            with open(file_path, 'wb') as pdf_out:
                try:
                    status, content = self.download_file(url)
                    if status == 200:
                        pdf_out.write(content)
                except:
                    pass
            

            if self.validater.is_valid_pdf(file_path):
                print(i)
                return True
            else:
                try:
                    os.remove(file_path)
                except FileNotFoundError:
                    pass
            return False
        return False