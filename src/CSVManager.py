import pandas as pd

class CSVManager():

    #private vars
    __urlcsv__ = None
    __curr__ = -1
    __usecols__ = [[0, "filename"],
                   [1, "status"],
                   [2, "url"]]


    def __init__(self, filename):
        self.load(filename)
        
    def load(self, filename):
        print(f"Loading csv file \"{filename}\"") 

        self.__urlcsv__ = pd.read_csv(filename)

        #print(self.__urlcsv__.iloc[3]["url"])
        


    def next(self):
        self.__curr__ += 1

    def previous(self):
        self.__curr__ -= 1


    def fetch_url(self, auto_next = False):
        if auto_next:
            self.next()

        return self.__get_curr_r_col__(self.__usecols__[2][0])

    def fetch_filename(self, auto_next = False):
        if auto_next:
            self.next()

        return self.__get_curr_r_col__(self.__usecols__[0][0])


        
    def update_status(self):
        pass

    def __get_row__(self, iter=0):
        return self.__urlcsv__.iloc[iter]

    def __get_curr_row__(self):
        return self.__urlcsv__.iloc[self.__curr__]

    def __get_curr_r_col__(self, column):
        return self.__get_curr_row__().iloc[column]

