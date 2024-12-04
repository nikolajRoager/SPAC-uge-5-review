import unittest
from downloader import Downloader

from unittest import IsolatedAsyncioTestCase


#Get status from URL, used for  testing if download_file from the downloader is working
async def getFromUrl(url : str):
    downloader = Downloader()
    status, data = await downloader.download_file(url)
    return status

class TestAddFunction(unittest.IsolatedAsyncioTestCase):
    async def test_working(self):
        #arch wiki is highly unlikely to ever be down
        self.assertEqual(await getFromUrl("https://wiki.archlinux.org/title/Main_page"), 200)

    async def test_badURL(self):
        #This is not a website
        self.assertNotEqual(await getFromUrl("nono://notAWebsiteURL.nope"), 200)

if __name__ == '__main__':
    print("Start test")
    unittest.main()
    