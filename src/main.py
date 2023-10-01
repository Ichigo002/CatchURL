# Attempt 2 in this pice of shit
import csvmanager as csv

def main():
    csvm = csv.CSVManager("data/urls.csv")
    print(csvm.fetch_url(True))
    print(csvm.fetch_filename(True))
    print(csvm.fetch_url(True))




    
if __name__ == "__main__":
    main()