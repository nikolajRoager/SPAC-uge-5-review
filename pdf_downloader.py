import pandas as pd
from constants import Constants
from downloader import Downloader
from excel import Excel


downloader = Downloader()
# Read excel-file
gri = Excel('GRI_2017_2020.xlsx').df
# print(Constants.PrimaryUrl.value)

# Filter out rows with missing URL
gri = gri.loc[(gri[Constants.PrimaryUrl.value].notnull()) | (gri[Constants.SecondaryUrl.value].notnull())]

# print(gri)

for i, row in list(gri.iterrows())[:50]:

    print(f"Downloading {i}")
    

    downloaded: bool = downloader.download_row(row)

    print(f"Downloaded {i}: {downloaded}")






