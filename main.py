from typing import Text
import scrape
from random import randint

print("Scraping site")
data = scrape.main(100)
print("Site scraped successfully")
db = open("PracticeDB.sql","w", encoding='utf-8')
def makeTables():
    db.write("CREATE TABLE QUOTES (id INTEGER PRIMARY KEY, author TEXT NOT NULL, cat TEXT NOT NULL, quote TEXT); \n")
    db.write("CREATE TABLE RATING (id FOREIGN KEY references QUOTES, rating INTEGER)")
    print("TABLES HAVE BEEN MADE SUCCESSFULLY")
def makeEntries():
    for key in data.keys():
        for entry in data[key]:
            db.write("INSERT INTO QUOTES VALUES ("+str(entry[0])+" , \""+entry[1]+"\" ,  \""+key+" \" ,  \""+entry[2]+" \" ); \n")
            db.write("INSERT INTO RATING VALUES ("+str(entry[0])+","+ str(randint(0,10))+");\n")
    db.close()
    print("ENTRIES HAVE BEEN ADDED SUCCESSFULLY")
def main():
    makeTables()
    makeEntries()

main()
#                   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                      
#               @@@@@@@%%%%%%%%%%%%%%%%%%@@@@              @@@@                  
#           &&&&@@@&&&&%%%%%%%%%%%%%%%@@@,,,,              ,,,,&&&&              
#           @@@@&&&%&&&&&&&%%%%%%%%%%%@@@                      @@@@              
#               @@@&&&&&&&&&&&&&&&%%%%@@@                      @@@@              
#                  &@@@@@@@@@@@@@@@@@&       @@@@@@@    @@@@@@@    @@@           
#                  &@@@@@@@@@@@@@@@@@&       @@@@@@@    @@@@@@@    @@@           
#                  &@@@,,,,,,,    @@@&       @@@@@@@    @@@@@@@    @@@           
#                  &@@@///////,,,,@@@&       @@@@@@@    @@@@@@@    @@@           
#                  &@@@///////,,,,@@@&       @@@@@@@    @@@@@@@    @@@           
#                  &@@@@@@@@@@@@@@@@@&...                          @@@           
#                  &@@@&&&&%%%%%%%@@@&...                          @@@           
#                  &@@@&&&&%%%%%%%@@@&...                          @@@           
#                  &@@@%%%%%%%&&&&%%%%@@@....                  @@@@              
#                  &@@@%%%%&&&@@@@%%%%@@@.......    @@@@       @@@@              
#                  &@@@%###%%%@@@@%%%%@@@.......    @@@@       @@@@              
#                  &@@@&&&&@@@%%%%%%%%%%%@@@@..............@@@@                  
#                 &@@@@@@@%%%%%%%&&&&&&&&&&&@@@@@@@@@@@@@@@@@@                  
#               &&&%%%%%%%%%%%%%%%%%%%&&&&&&&%%%%%%%&&&&&&&@@@@                  
#               @@@#%%%%%%%%%%%%%%%%%%&&&&&&&&&&&&&&&&&&&&&@@@@                  
#               @@@#%%%&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&@@@@              
#               @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@              
#               @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@              
#               @@@((((,,,,,,,,,,,       @@@@,,,,,,,,,,,       @@@@              
#               @@@(((((((((((((((((((,,,@@@@((((((((((((((,,,,@@@@              
#               @@@(((((((((((((((((((,,,@@@@((((((((((((((,,,,@@@@              
#               @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ 
