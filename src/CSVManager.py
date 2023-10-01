import pandas as pd

class CSVManager():

    #private vars
    __urlcsv__ = None
    __curr__ = 0
    __curr_max__ = -1
    __end_data__ = False 
    __usecols__ = [[0, "filename"],
                   [1, "status"],
                   [2, "url"],
                   [3, "nostat"]]


    def __init__(self, filename):
        self.load(filename)
        
    def load(self, filename):
        print(f"Loading csv file \"{filename}\"") 

        self.__urlcsv__ = pd.read_csv(filename)
        self.__curr_max__ = self.__urlcsv__.__len__()
        self.__end_data__ = False
        #print(self.__urlcsv__.iloc[3]["url"])
        

    def is_end_data(self):
        return not self.__curr__ < self.__curr_max__
 
    def size(self):
        return self.__curr_max__


    def next(self):
        self.__curr__ += 1

    def previous(self):
        self.__curr__ -= 1


    def fetch_url(self, auto_next = False):
        tmp = self.__get_curr_r_col__(self.__usecols__[2][0])
        if auto_next:
            self.next()
        return tmp


    def fetch_filename(self, auto_next = False):
        if auto_next:
            self.next()

        return self.__get_curr_r_col__(self.__usecols__[0][0])


    def fetch_nostat(self, auto_next = False):
        if auto_next:
            self.next()

        return self.__get_curr_r_col__(self.__usecols__[3][0])
        
    def update_status(self, nostat):
        pass     

    def __get_name_of_nostat(self, nostat):
        rval = ""
        match nostat:
            case 0:
                rval = "Saved"
            case -1:
                rval = "ERROR"
        return rval


    def __get_row__(self, iter=0):
        return self.__urlcsv__.iloc[iter]

    def __get_curr_row__(self):
        return self.__urlcsv__.iloc[self.__get_curr__()]

    def __get_curr_r_col__(self, column):
        return self.__get_curr_row__().iloc[column]

    def __get_curr__(self):
        if self.__curr__ < self.__curr_max__:
            self.__end_data__ = False
            return self.__curr__
            
        self.__end_data__ = True
        return self.__curr_max__ - 1