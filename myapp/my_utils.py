import pandas as pd
import openpyxl
import requests
from django.shortcuts import redirect


check_mxik_code_url = "https://api-tasnif.soliq.uz/cl-api/integration-mxik/get/history/"


result_list = []
