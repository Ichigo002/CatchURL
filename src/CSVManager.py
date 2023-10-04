import pandas as pd
import os
import colorcmd as cc

class CSVManager():

    #private vars
    __filename__ = ""
    __urlcsv__ = None
    __curr__ = 0
    __curr_max__ = -1
    __end_data__ = False 
    __usecols__ = [[0, "filename"],
                   [1, "status"],
                   [2, "url"]]


    def __init__(self, filename):
        self.__filename__ = filename
        self.read() 
        pd.set_option("display.max_rows", 2000)
        
    def read(self):
        print(f"[Loading csv file \"{self.__filename__}\"]") 

        if not os.path.exists(self.__filename__):
            cc.setcol_error()
            print(" READ CSV ERROR: No such file: ", self.__filename__, "\n")
            cc.setcol_clear()
            os.system("pause")
            os._exit(-1)
        self.__urlcsv__ = pd.read_csv(self.__filename__)
        self.__curr_max__ = self.__urlcsv__.__len__()
        self.__end_data__ = False
        #self.__urlcsv__ = self.__urlcsv__.drop(columns=['Unnamed: 4'])
        #print(self.__urlcsv__)
        
    def write(self): 
        self.__urlcsv__.to_csv(self.__filename__, index=False )

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
        fname = self.__get_curr_r_col__(self.__usecols__[0][0])
        if not isinstance(fname, str):
            fname = ""

        return fname
        
    def update_status(self, nostat):
        df = self.__urlcsv__.copy()
        
        df.loc[self.__get_curr__(),  self.__usecols__[1][1]] = self.__get_name_of_nostat(nostat)
        self.__urlcsv__ = df
        self.write()

    def __get_name_of_nostat(self, nostat):
        rval = ""
        match nostat:
            case 0:
                rval = "Saved"
            case -1:
                rval = "ERROR"
            case -3:
                rval = "NotDefined"
            case -4:
                rval = "HTTP ERROR: Forbidden 403"
            case -5:
                rval = "HTTP ERROR"
            case -6:
                rval = "DIR ERROR: Cannot create directory"
            case -7:
                rval = "DIR ERROR"
            case -8:
                rval = ""
 
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
