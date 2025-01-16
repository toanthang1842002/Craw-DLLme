import time

from bs4 import BeautifulSoup
import requests,os
import crawl_from_dllFile_com,time, threading
import concurrent.futures
import query_db

#############################################################################
DB_COLLECTION_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'DataBase')
CREDENTIAL_COLLECTION_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'credential')

#############################################################################

def crawl_from_dllME_com():
    # query_db.get_data('file_name')
    with open(os.path.join(CREDENTIAL_COLLECTION_PATH, 'list_file_name.txt'), 'r') as file:
        list_name = file.read().split('\n')


def check_valid_hash():
    print("hehe")
if __name__ == '__main__':
    # list_url_DLLFile_com = ['/0-9/', '/a/', '/b/', '/c/', '/d/', '/e/', '/f/', '/g/', '/h/', '/i/', '/j/', '/k/', '/l/', '/m/',
    #             '/n/', '/o/', '/p/', '/q/', '/r/', '/s/', '/t/', '/u/', '/v/', '/w/', '/x/', '/y/', '/z/']
    # for url in list_url_DLLFile_com:
    #     _url = "https://www.dll-files.com" + url
    #     crawl_from_dllFile_com.Get_list_file_name(_url)
    crawl_from_dllME_com()

