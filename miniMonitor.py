import pandas as pd
import smtplib
import time

#### Mailer Config####
server = smtplib.SMTP('smtp.gmail.com', 587)   #can use 'localhost' without port or authentication
server.starttls()
server.login("YourEmail@gmail.com", "YourPassword") #enter your gmail credentials

##### Monitoring task
def myMonitor (csvLogFile):
    try:
        df = pd.read_csv(csvLogFile, sep='\t', encoding = "ISO-8859-1") #csv to dataframe
    except:
        print("Error reading the file")

    errors = df[df['Status'] == "FinishedFail"]    ###For testing: #FinishedSuccess #FinishedFail #randomMessage
    #print(df[df['Status'] == "FinishedFail"])
    if len(errors.index) > 0:
        print ('these are the # of errors: ' , len(errors.index))
        messageBody = str(errors.TaskName)
        try:
            server.sendmail("FromEmail@gmail.com", "ToEmail@gmail.com", messageBody)
            server.quit()
            print('Message sent!')

        except:
            print('failure to connect to mail server')
    else:
        print('No errors found, no message sent.')

#### Execute the monitor every 60 seconds.
while True:
    myMonitor('NYVM0571_TaskExecution_Scheduler.txt')
    time.sleep(60)
