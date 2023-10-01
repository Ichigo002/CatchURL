# Attempt 2 in this pice of shit
import csvmanager as csv
import downloader as dwn

def main():
    csvm = csv.CSVManager("data/urls.csv")
    dwnl = dwn.Downloader()
"""
    for i in range(15):
        if not csvm.is_end_data():
            print(csvm.fetch_url())
            print(csvm.fetch_filename())
            csvm.next()
"""



    
if __name__ == "__main__":
    main()