# Attempt 2 in this pice of shit
import csvmanager as csv
import downloader as dwn
import pandas as pd

def main():

    df = pd.read_xml("data/extra-info.xml")

    csvm = csv.CSVManager(df.iloc[0].iloc[0])
    dwnl = dwn.Downloader(df.iloc[1].iloc[1])

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
            print(f" File \"{fname}\" already exist. Skipping...")
            dn_skipped += 1
        print("###")
        csvm.next()
    
    print("Summary: \n",
          f"*Saved:   {dn_success} file/s\n",
          f"*Failed:  {dn_fails} file/s\n",
          f"*Skipped: {dn_skipped} file/s\n")

        
    


    
if __name__ == "__main__":
    main()