import requests
import re 
import os

inputted_url = input('Enter the Instagram Link: ')
url = inputted_url

head, sep, tail = inputted_url.partition('p')

if inputted_url == 'https://www.instagram.com/p'+ tail:

    print(inputted_url)