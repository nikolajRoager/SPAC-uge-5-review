import unittest
from downloader import Downloader
from pandas import Series
from config import Config

from unittest import IsolatedAsyncioTestCase


#Get status from URL, used for  testing if download_file from the downloader is working
async def getFromUrl(url : str) -> int: 
    downloader = Downloader()
    status, data = await downloader.download_file(url)
    return status

async def getFromRow() -> bool:
    downloader = Downloader()
    row: Series =[]
    row[Config.PrimaryUrl.value]="http://www.bookergroupee.com/~/media/Files/B/Booker-Group/pdf/annual-report-2017.pdf"
    row[Config.SecondaryUrl.value]="http://database.globalreporting.org/reports/281d1fc3-20f2-e711-8136-e0071b65f141"
    return await downloader.download_row(row)
#        download_row

    #async def download_row(self, row: Series) -> bool:
    #    primary_url: str = row[Config.PrimaryUrl.value]
    #    secondary_url: str = row[Config.SecondaryUrl.value]
    #    file_name: str = row[Config.IdCol.value] + '.pdf'
    #    file_path = os.path.join(self.download_path, file_name)


class TestAddFunction(unittest.IsolatedAsyncioTestCase):
    async def test_working(self):
        #arch wiki is highly unlikely to ever be down
        self.assertEqual(await getFromUrl("https://wiki.archlinux.org/title/Main_page"), 200)

    async def test_badURL(self):
        #This is not a website
        self.assertNotEqual(await getFromUrl("nono://notAWebsiteURL.nope"), 200)

    async def test_download_row(self):
        self.assertTrue(await getFromRow())
        
    #async def download_row(self, row: Series) -> bool:
    #    primary_url: str = row[Config.PrimaryUrl.value]
    #    secondary_url: str = row[Config.SecondaryUrl.value]
    #    file_name: str = row[Config.IdCol.value] + '.pdf'

if __name__ == '__main__':
    print("Start test")
    unittest.main()
    