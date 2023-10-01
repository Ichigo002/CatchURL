# Attempt 2 in this pice of shit
import csvmanager as csv
import downloader as dwn

def main():

    #ans = str(input("Type download folder name: "))

    csvm = csv.CSVManager("data/urls.csv")
    dwnl = dwn.Downloader( )

    print("--------------------------")
    
    for i in range(csvm.size()):
        fname = csvm.fetch_filename()
        furl = csvm.fetch_url()

        if dwnl.shall_download(fname):
            codec = dwnl.download_from_url(furl, fname)
            csvm.update_status(codec)
            print("-=-=-")
        csvm.next()

        
    


    
if __name__ == "__main__":
    main()