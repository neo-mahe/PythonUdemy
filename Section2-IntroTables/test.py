import os
import shutil
from datetime import datetime
import logging
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# Setting the time string to be appended to the files
timeString = datetime.now().strftime("%Y%m%d-%H%M%S")

# This is the logs directory path

zipped_file = "D:\\Export_Users\\zipped_file\\" + timeString
unzipped_file = "D:\\Export_Users\\unzipped_file\\" + timeString
logger = logging.getLogger()
dirPath = "D:\\Export_Users\\"


# create log_dir
def create_log_dir():
    log_dir = "D:\\Export_Users\\Logs\\"
    if not os.path.exists(log_dir):
        os.makedirs(log_dir, exist_ok=True)

    log_file = log_dir + timeString + ".txt"
    logFormat = "%(levelname)s %(asctime)s - %(message)s"
    logging.basicConfig(filename=log_file, level=logging.DEBUG, format=logFormat, filemode='w')


# Removing the old folders & files as these are not required

def remove_old_files():
    if os.path.exists(dirPath):
        shutil.rmtree(dirPath)
        print("Removing the old folders & files structure")
    else:
        print("Skipping this step as the old folder & file structure doesn't exists")


def launchWebsite():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("url")


create_log_dir()