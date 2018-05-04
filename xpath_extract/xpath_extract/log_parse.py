
import csv
import time
import datetime
currentDateTime = datetime.datetime.now().strftime("%Y%m%d_%H%M")
#open the log file
logFile = "C:\\Users\\Alan\\Downloads\\last_ps_logs (20).txt"
#logFile = "c:\\users\\s63914\\downloads\\bikewagon_1_rerun.csv"
fileObject = open(logFile, "r",encoding='utf-8')
print("Name of log file: ", fileObject.name)
#lines = fileObject.readlines()
lines = list(fileObject)
outputFileName = ''.join(["C:\\Users\\Alan\\Downloads\\rerun",currentDateTime,".csv"])
oFileObject = open(outputFileName, "w", newline='')
oWriter = csv.writer(oFileObject)
oWriter.writerow(["category","spage","lpage","domain"])

rerun = []
for idx, val in enumerate(lines):
    if (val.strip() == "No products found on this page.") and (idx >= 3):
        fullMessage = lines[idx-3]
        firstQuotePos = fullMessage.find('"')
        secondQuotePos = fullMessage.find('"', firstQuotePos + 1)
        urlString = fullMessage[firstQuotePos+1:secondQuotePos]
        wwwPos = fullMessage.find('www.')
        dotComPos = fullMessage.find('.com')
        domainString = fullMessage[wwwPos+4:dotComPos+4]
        rowToWrite = [urlString,"1","1",domainString]
        oWriter.writerow(rowToWrite)
        #rerun.append(domainString)
     
       
#print(rerun)
fileObject.close()
oFileObject.close()
