import pandas as pd

from constants import Constants
from downloader import Downloader


downloader = Downloader()
# Read excel-file
gri = pd.read_excel('GRI_2017_2020.xlsx')

print(Constants.PrimaryUrl.value)

# Filter out rows with missing URL
gri = gri.loc[(gri[Constants.PrimaryUrl.value].notnull()) | (gri[Constants.SecondaryUrl.value].notnull())]

print(gri)

for i, row in gri.iterrows():
    if i > 10: break

    downloaded: bool = downloader.download(row)






