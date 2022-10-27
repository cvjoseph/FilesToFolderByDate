import email
import getpass
import imaplib
import os
import shutil
import sys
import quopri
import platform

from datetime import datetime


root_folder = input('Enter Root Folder :\n')

if not os.path.isdir(root_folder):
    print("Invalid path [" + root_folder + "] !!!")
else:
    files = []
    #print(os.listdir(root_folder))
    files = [f for f in os.listdir(root_folder) if os.path.isfile(os.path.join(root_folder, f))]
    #print("2.....")
    #print(files)
    for f in files:
        full_file_path_and_name = os.path.join(root_folder, f)
        if platform.system() == 'Windows':
            cTime = os.path.getmtime(full_file_path_and_name)
            file_datetime = datetime.fromtimestamp(cTime).strftime('%Y-%m-%d %H:%M:%S')
            file_date = datetime.fromtimestamp(cTime).strftime('%Y.%m.%d')

            #print(file_datetime)
            
            new_file_folder = os.path.join(root_folder, file_date)
            new_folder_msg = ""
            if not os.path.isdir(new_file_folder):
                new_folder_msg = "" = "Create new folder.........."
                os.makedirs(new_file_folder)
            else:
               new_folder_msg = "..........Folder already exists"

            new_full_file_path_and_name = os.path.join(new_file_folder, f)
            shutil.move(full_file_path_and_name, new_full_file_path_and_name)

            print("File [" + f + "], Created on [" + file_datetime + "] " + new_folder_msg + ", => File moved")


print("Done :-)")
