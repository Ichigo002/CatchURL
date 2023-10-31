# Attempt 2 in this pice of shit
import pandas as pd
from ..catch_url.csvmanager import *
from ..catch_url.downloader import *
from ..utils import colorcmd as cc
import os


def main():

    config_path = "data/config.xml"
    if os.path.exists(config_path):
        df = pd.read_xml(config_path)
    else:
        cc.setcol_error()
        print("\n READ XML ERROR: No such file: \"", config_path, "\"\n\n")
        cc.setcol_clear()
        return

    cc.setcol_info()
    csvm = CSVManager(df.iloc[0].iloc[0])
    dwnl = Downloader(df.iloc[1].iloc[1])
    cc.setcol_clear()
    print("###")

    dn_success = 0
    dn_fails = 0
    dn_skipped = 0
    
    for i in range(csvm.size()):
        fname = csvm.fetch_filename() + ".mp4"
        furl = csvm.fetch_url()

        if dwnl.shall_download(fname):
            codec = dwnl.download_from_url(furl, fname)
            csvm.update_status(codec)
            if codec == 0:
                dn_success += 1
            else:
                dn_fails += 1
        else:
            cc.setcol_skip()
            print(f" File \"{fname}\" already exist. Skipping...")
            dn_skipped += 1
        cc.setcol_clear()
        print("###")
        csvm.next()
        
    cc.setcol_summary()
    print("Summary: \n",
          f"*Saved:   {dn_success} file/s\n",
          f"*Failed:  {dn_fails} file/s\n",
          f"*Skipped: {dn_skipped} file/s\n")
    cc.setcol_clear()

def more_main():
    os.system("cls")
    main()
    os.system("pause")