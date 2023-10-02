# Attempt 2 in this pice of shit
import csvmanager as csv
import downloader as dwn
import pandas as pd

def main():

    df = pd.read_xml("data/extra-info.xml")

    csvm = csv.CSVManager(df.iloc[0].iloc[0])
    dwnl = dwn.Downloader(df.iloc[1].iloc[1])

    print("###")
    
    for i in range(csvm.size()):
        fname = csvm.fetch_filename() + ".mp4"
        furl = csvm.fetch_url()

        if dwnl.shall_download(fname):
            codec = dwnl.download_from_url(furl, fname)
            csvm.update_status(codec)
            print("###")
        else:
            print(f"File \"{fname}\" already exist. Skipping...")
        csvm.next()

        
    


    
if __name__ == "__main__":
    main()