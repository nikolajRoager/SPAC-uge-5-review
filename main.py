import asyncio
import os
from typing import List
import pandas as pd
from config import Config
from downloader import Downloader
from excel import Excel



downloader = Downloader()
meta_data = Excel(os.path.join(Config.BaseDir.value, Config.MetadataFile.value))
gri = Excel(os.path.join(Config.BaseDir.value, Config.GRIFile.value))
new_rows: List[dict] = []

async def download_row(i, row):
    print(f"Downloading {i}")
    new_row: dict = {}
    downloaded: bool = await downloader.download_row(row)
    for col in meta_data.df.columns:
        if col in gri.df.columns:
            new_row[col] = row[col]
        else:
            new_row[col] = None
    
    new_row[Config.DownLoadedCol.value] = Config.Downloaded.value if downloaded else Config.NotDownloaded.value
    new_rows.append(new_row)
    print(f"Downloaded {i}: {downloaded}")


async def main():
    if Config.FileLimit.value > 0:
        rows = list(gri.df.iterrows())[:Config.FileLimit.value]
    else:
        rows = list(gri.df.iterrows())

    tasks = [download_row(i, row) for i, row in rows]
    await asyncio.gather(*tasks)


asyncio.run(main())

new_rows.sort(key=lambda x: x[Config.IdCol.value])
for row in new_rows:
    if row[Config.IdCol.value] in meta_data.df[Config.IdCol.value].values:
        meta_data.df.loc[meta_data.df[Config.IdCol.value] == row[Config.IdCol.value]] = row
    else:
        meta_data.df = pd.concat([meta_data.df, pd.DataFrame([row])], ignore_index=True)

meta_data.write_file(os.path.join(Config.BaseDir.value, Config.OutputFile.value))