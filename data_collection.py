# -*- coding: utf-8 -*-


import glassdoor_scraper as gs 
import pandas as pd 

path = "C:/Users/Akshay/Documents/ds_salary_proj/chromedriver"

df = gs.get_jobs('data scientist',1000, False, path, 15)

df.to_csv('glassdoor_jobs.csv', index = False)