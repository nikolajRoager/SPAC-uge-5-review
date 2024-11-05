import os
from typing import Tuple

import requests
from constants import Constants
from pdf_validater import PdfValidater
from pandas import Series


class Downloader:
    validater = PdfValidater()
    download_path: str = Constants.DownloadDir.value

    def download_file(self, url) -> Tuple[int, bytes]:
        res: requests.Response = requests.get(url)
        return (res.status_code, res.content)

    def download(self, row: Series) -> bool:
        primary_url: str = row[Constants.PrimaryUrl.value]
        secondary_url: str = row[Constants.SecondaryUrl.value]
        file_name: str = row['BRnum'] + '.pdf'

        with open(os.path.join(self.download_path, file_name), 'wb') as pdf_out:
            try:
                status, content = self.download_file(primary_url)

                pdf_out.write(content)
            except:
                pass


        return True