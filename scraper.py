from bs4 import BeautifulSoup
from datetime import datetime
from dateutil.relativedelta import *
import requests

current_date = datetime.today().strftime('%Y%m%d')[2::]
max_date = datetime.today()+relativedelta(months=+6)                                        #How far in the future the user can search for flights (6 months)
max_date = max_date.strftime('%Y%m%d')[2::]

def getDates():
    valid = False
    while valid == False:
        print(f"Enter the date of the outgoing flight in the format YYMMDD (e.g today is {current_date})")
        dates = input(">")  

        try:
            if len(dates) != 6:
                print("Please enter an input of length 6")
                raise Exception("")
            
            if int(dates) < int(current_date) and int(dates) < int(max_date):
                 print("Cannot fly out in the past or over 6 months into the future")
                 raise Exception("")
            
            valid = True
            
            

        except ValueError:
                print("Input is not in the format YYMMDD")
        except:
                print("")
    return dates

date = getDates()
GlaSearch = f"https://www.skyscanner.net/transport/flights-from/glas/{date}/?adultsv2=1&cabinclass=economy&childrenv2=&ref=home&rtn=0&preferdirects=false&outboundaltsenabled=false&inboundaltsenabled=false"
EdiSearch = f"https://www.skyscanner.net/transport/flights-from/edi/{date}/?adultsv2=1&cabinclass=economy&childrenv2=&ref=home&rtn=0&preferdirects=false&outboundaltsenabled=false&inboundaltsenabled=false"
