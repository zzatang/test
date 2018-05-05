
import csv
import time
import datetime
import os


def CreateRerunFile(inputLogFile, fileCounter):
    currentDateTime = datetime.datetime.now().strftime("%Y%m%d_%H%M")
    fileObject = open(inputLogFile, "r",encoding='utf-8')
    lines = list(fileObject)
    outputFileName = ''.join(["rerun_",str(fileCounter), "_", currentDateTime,".csv"])
    oFileObject = open(outputFileName, "w", newline='')
    oWriter = csv.writer(oFileObject)
    oWriter.writerow(["category","spage","lpage","domain"])
    counter = 0

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
            if urlString.find("http") != -1:
                oWriter.writerow(rowToWrite)
                counter += 1

    fileObject.close()
    oFileObject.close()
    os.remove(inputLogFile)
    if counter == 0: os.remove(outputFileName)

if __name__ == "__main__":
    
    logFileList = [f for f in os.listdir(os.getcwd()) if f.endswith(".txt")]

    for idx, val in enumerate(logFileList):
        CreateRerunFile(val, idx+1)

