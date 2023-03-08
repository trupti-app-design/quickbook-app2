import streamlit as st
import datetime
import fiscalyear
from fiscalyear import *
import time
from selenium.webdriver import ActionChains
import bs4
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pandas as pd
import datefinder
import regex as re
from dateutil.relativedelta import relativedelta
#from datetime import datetime
import timestring
from selenium.webdriver.chrome.options import Options
import random
import os
#-------Custom Report Time---------------------------------------
fiscalyear.setup_fiscal_calendar(start_month=8)
fiscal_year_start=FiscalYear.current().start
fiscal_year_end=FiscalYear.current().end
Today=datetime.date.today()

Today=Today.strftime("%m/%d/%Y")
fiscal_year_start=fiscal_year_start.strftime("%m/%d/%Y")
fiscal_year_end=fiscal_year_end.strftime("%m/%d/%Y")

#st.write(Today,fiscal_year_end,fiscal_year_start)
#----------------------Dates------------------------------------


st.title("Reports")


report_period=st.session_state["report_result"]
report_values=st.session_state["value_result"]
report_lower_date=st.session_state["min_selection"]
report_higher_date=st.session_state["max_selection"]

report_lower_date=datetime.datetime.strftime(report_lower_date,"%m/%d/%Y")
report_higher_date=datetime.datetime.strftime(report_higher_date,"%m/%d/%Y")

st.write(report_lower_date)
#-----------------------------------------------------------------------------------------
if report_period=="Custom":
    date_macro="custom"
    low_date=str(report_lower_date)
    high_date=str(report_higher_date)
    if report_values=="All":
        show_r_c="all"
    if report_values=="Active":
        show_r_c="active"
    if report_values=="Non-Zero":
        show_r_c="nonzero"
    url="https://app.qbo.intuit.com/app/reportv2?token=PANDL&show_logo=false&date_macro={}&low_date={}&high_date={}&column=monthly&showrows={}&showcols={}&subcol_pp=&subcol_pp_chg=&subcol_pp_pct_chg=&subcol_py=&subcol_py_chg=&subcol_py_pct_chg=&subcol_py_ytd=&subcol_ytd=&subcol_pct_ytd=&subcol_pct_row=&subcol_pct_col=&subcol_pct_inc=false&subcol_pct_exp=false&cash_basis=no&customized=yes&collapsed_rows=&edited_sections=false&divideby1000=false&hidecents=false&exceptzeros=true&negativenums=1&negativered=false&show_header_title=true&show_header_range=true&show_footer_custom_message=true&show_footer_date=true&show_footer_time=true&show_footer_basis=true&header_alignment=Center&footer_alignment=Center&show_header_company=true&company_name=PARTS%20AVATAR%20INVESTMENTS%20INC.&collapse_subs=false&title=Profit%20and%20Loss&footer_custom_message=".format(date_macro,low_date,high_date,show_r_c,show_r_c)
elif report_period=="Today":
    date_macro="today"
    low_date=str(Today)
    high_date=str(Today)

    if report_values=="All":
        show_r_c="all"
    if report_values=="Active":
        show_r_c="active"
    if report_values=="Non-Zero":
        show_r_c="nonzero"
    url="https://app.qbo.intuit.com/app/reportv2?token=PANDL&show_logo=false&date_macro={}&low_date={}&high_date={}&column=monthly&showrows={}&showcols={}&subcol_pp=&subcol_pp_chg=&subcol_pp_pct_chg=&subcol_py=&subcol_py_chg=&subcol_py_pct_chg=&subcol_py_ytd=&subcol_ytd=&subcol_pct_ytd=&subcol_pct_row=&subcol_pct_col=&subcol_pct_inc=false&subcol_pct_exp=false&cash_basis=no&customized=yes&collapsed_rows=&edited_sections=false&divideby1000=false&hidecents=false&exceptzeros=true&negativenums=1&negativered=false&show_header_title=true&show_header_range=true&show_footer_custom_message=true&show_footer_date=true&show_footer_time=true&show_footer_basis=true&header_alignment=Center&footer_alignment=Center&show_header_company=true&company_name=PARTS%20AVATAR%20INVESTMENTS%20INC.&collapse_subs=false&title=Profit%20and%20Loss&footer_custom_message=".format(date_macro,low_date,high_date,show_r_c,show_r_c)
elif report_period=="This Fiscal Year":
    date_macro="thisfiscalyear"
    low_date=str(fiscal_year_start)
    high_date=str(fiscal_year_end)

    if report_values=="All":
        show_r_c="all"
    if report_values=="Active":
        show_r_c="active"
    if report_values=="Non-Zero":
        show_r_c="nonzero"
    url="https://app.qbo.intuit.com/app/reportv2?token=PANDL&show_logo=false&date_macro={}&low_date={}&high_date={}&column=monthly&showrows={}&showcols={}&subcol_pp=&subcol_pp_chg=&subcol_pp_pct_chg=&subcol_py=&subcol_py_chg=&subcol_py_pct_chg=&subcol_py_ytd=&subcol_ytd=&subcol_pct_ytd=&subcol_pct_row=&subcol_pct_col=&subcol_pct_inc=false&subcol_pct_exp=false&cash_basis=no&customized=yes&collapsed_rows=&edited_sections=false&divideby1000=false&hidecents=false&exceptzeros=true&negativenums=1&negativered=false&show_header_title=true&show_header_range=true&show_footer_custom_message=true&show_footer_date=true&show_footer_time=true&show_footer_basis=true&header_alignment=Center&footer_alignment=Center&show_header_company=true&company_name=PARTS%20AVATAR%20INVESTMENTS%20INC.&collapse_subs=false&title=Profit%20and%20Loss&footer_custom_message=".format(date_macro,low_date,high_date,show_r_c,show_r_c)
else:
    pass


#url="https://app.qbo.intuit.com/app/reportv2?token=PANDL&show_logo=false&date_macro=custom&low_date=08/01/2022&high_date=02/13/2023&column=monthly&showrows=active&showcols=active&subcol_pp=&subcol_pp_chg=&subcol_pp_pct_chg=&subcol_py=&subcol_py_chg=&subcol_py_pct_chg=&subcol_py_ytd=&subcol_ytd=&subcol_pct_ytd=&subcol_pct_row=&subcol_pct_col=&subcol_pct_inc=false&subcol_pct_exp=false&cash_basis=no&customized=yes&collapsed_rows=&edited_sections=false&divideby1000=false&hidecents=false&exceptzeros=true&negativenums=1&negativered=false&show_header_title=true&show_header_range=true&show_footer_custom_message=true&show_footer_date=true&show_footer_time=true&show_footer_basis=true&header_alignment=Center&footer_alignment=Center&show_header_company=true&company_name=PARTS%20AVATAR%20INVESTMENTS%20INC.&collapse_subs=false&title=Profit%20and%20Loss&footer_custom_message="
#------------------------------------Scraping-----------------------------------------#

from selenium import webdriver as wb
chromeOptions = wb.ChromeOptions()
#chromeOptions.headless=True
prefs = {"download.default_directory" : r"C:\QB Scrape"}
chromeOptions.add_experimental_option("prefs",prefs)
webD=wb.Chrome("C:/Users/trupti.raut/chromedriver_win32 (3)/chromedriver.exe", options=chromeOptions)
webD.maximize_window()

'''
try:
    st.write("first")
    webD.get("https://accounts.intuit.com/app/sign-in?app_group=QBO&asset_alias=Intuit.accounting.core.qbowebapp&iux_tests=47287%3A11%3A113998&redirect_uri=https%3A%2F%2Fapp.qbo.intuit.com%2Fapp%2Fcompanyselection%3FloadCustomerAssistanceAssets%3Dus&loadCustomerAssistanceAssets=us")
    userID="trupti.raut@partsavatar.ca"
    password="Symphony@231298"

    time.sleep(5)
    uname=webD.find_element("xpath",'//*[@id="iux-identifier-first-international-email-user-id-input"]')

    uname.send_keys("trupti.raut@partsavatar.ca")
    time.sleep(5)
    webD.find_element("xpath",'//*[@id="app"]/div[1]/div/div/div[1]/div/div/div/div[3]/div[1]/div/form/button/span[2]').click()

    time.sleep(5)
    upassword=webD.find_element("xpath",'//*[@id="iux-password-confirmation-password"]')
    upassword.send_keys("Symphony@231298")
    time.sleep(5)
    webD.find_element("xpath",'//*[@id="app"]/div[1]/div/div/div[1]/div/div/div/div[3]/div[1]/div/form/button[2]').click()
    time.sleep(20)
    webD.get(url)
except:
    try:
        st.write("Second")
        webD.get("https://accounts.intuit.com/app/sign-in?app_group=QBO&asset_alias=Intuit.accounting.core.qbowebapp&iux_tests=47287%3A11%3A113998&redirect_uri=https%3A%2F%2Fapp.qbo.intuit.com%2Fapp%2Fcompanyselection%3FloadCustomerAssistanceAssets%3Dus&loadCustomerAssistanceAssets=us")
        userID="trupti.raut@partsavatar.ca"
        password="Symphony@231298"

        time.sleep(5)
        uname=webD.find_element("xpath",'//*[@id="iux-identifier-first-international-email-user-id-input"]')

        uname.send_keys("trupti.raut@partsavatar.ca")
        time.sleep(5)
        webD.find_element("xpath",'//*[@id="app"]/div[1]/div/div/div[1]/div/div/div/div[3]/div[1]/div/form/button/span[2]').click()

        time.sleep(5)
        upassword=webD.find_element("xpath",'//*[@id="iux-password-confirmation-password"]')
        upassword.send_keys("Symphony@231298")
        time.sleep(5)
        webD.find_element("xpath",'//*[@id="app"]/div[1]/div/div/div[1]/div/div/div/div[3]/div[1]/div/form/button[2]').click()
        time.sleep(5)
        webD.find_element("xpath",'//*[@id="app"]/div[1]/div/div/div[1]/div/div/div/div[3]/div[1]/div/div[1]/ul/li[3]/button/div/span[2]').click()
        verification=st.number_input("Insert Verification Code")
        insert_code=webD.find_element("xpath",'//*[@id="ius-mfa-confirm-code"]')
        insert_code.send_keys(verification)
        webD.find_element("xpath",'//*[@id="app"]/div[1]/div/div/div[1]/div/div/div/div[3]/div[1]/div/form/button[1]').click()
        time.sleep(20)
        webD.get(url)
    except:
        try:
            st.write("Third")
            webD.get("https://accounts.intuit.com/app/sign-in?app_group=QBO&asset_alias=Intuit.accounting.core.qbowebapp&iux_tests=47287%3A11%3A113998&redirect_uri=https%3A%2F%2Fapp.qbo.intuit.com%2Fapp%2Fcompanyselection%3FloadCustomerAssistanceAssets%3Dus&loadCustomerAssistanceAssets=us")
            webD.find_element("xpath",'//*[@id="recaptcha-anchor"]/div[1]').click()
            webD.find_element("xpath", '//*[@id="ius-recaptcha-continue-btn"]').click()
            webD.get("https://accounts.intuit.com/app/sign-in?app_group=QBO&asset_alias=Intuit.accounting.core.qbowebapp&iux_tests=47287%3A11%3A113998&redirect_uri=https%3A%2F%2Fapp.qbo.intuit.com%2Fapp%2Fcompanyselection%3FloadCustomerAssistanceAssets%3Dus&loadCustomerAssistanceAssets=us")
            userID = "trupti.raut@partsavatar.ca"
            password = "Symphony@231298"

            time.sleep(5)
            uname = webD.find_element("xpath", '//*[@id="iux-identifier-first-international-email-user-id-input"]')

            uname.send_keys("trupti.raut@partsavatar.ca")
            time.sleep(5)
            webD.find_element("xpath",'//*[@id="app"]/div[1]/div/div/div[1]/div/div/div/div[3]/div[1]/div/form/button/span[2]').click()

            time.sleep(5)
            upassword = webD.find_element("xpath", '//*[@id="iux-password-confirmation-password"]')
            upassword.send_keys("Symphony@231298")
            time.sleep(5)
            webD.find_element("xpath",
                              '//*[@id="app"]/div[1]/div/div/div[1]/div/div/div/div[3]/div[1]/div/form/button[2]').click()
            time.sleep(20)
            webD.get(url)
        except:
            st.write("Fourth")
            webD.get("https://accounts.intuit.com/app/sign-in?app_group=QBO&asset_alias=Intuit.accounting.core.qbowebapp&iux_tests=47287%3A11%3A113998&redirect_uri=https%3A%2F%2Fapp.qbo.intuit.com%2Fapp%2Fcompanyselection%3FloadCustomerAssistanceAssets%3Dus&loadCustomerAssistanceAssets=us")
            userID = "trupti.raut@partsavatar.ca"
            password = "Symphony@231298"

            time.sleep(5)
            uname = webD.find_element("xpath", '//*[@id="iux-identifier-first-international-email-user-id-input"]')

            uname.send_keys("trupti.raut@partsavatar.ca")
            time.sleep(20)
            webD.get(url)

            webD.find_element("xpath",'//*[@id="app"]/div[1]/div/div/div[1]/div/div/div/div[3]/div[1]/div/form/button/span[2]').click()
            st.write("Click")
            time.sleep(15)
            webD.find_element("xpath", '///*[@id="recaptcha-anchor"]/div[2]').click()
            time.sleep(5)
            webD.find_element("xpath", '//*[@id="ius-recaptcha-continue-btn"]').click()

            time.sleep(5)
            upassword = webD.find_element("xpath", '//*[@id="iux-password-confirmation-password"]')
            upassword.send_keys("Symphony@231298")
            time.sleep(5)
            webD.find_element("xpath",'//*[@id="app"]/div[1]/div/div/div[1]/div/div/div/div[3]/div[1]/div/form/button[2]').click()
            time.sleep(20)


'''
webD.get("https://accounts.intuit.com/app/sign-in?app_group=QBO&asset_alias=Intuit.accounting.core.qbowebapp&iux_tests=47287%3A11%3A113998&redirect_uri=https%3A%2F%2Fapp.qbo.intuit.com%2Fapp%2Fcompanyselection%3FloadCustomerAssistanceAssets%3Dus&loadCustomerAssistanceAssets=us")
time.sleep(50)
webD.get(url)
#st.write(url)
time.sleep(15)

#slider=webD.find_element("xpath",'//*[@id="uniqName_40_0"]/div[5]/div[1]/div[2]/div[3]')
#ActionChains(webD).click_and_hold(slider).move_by_offset(x,0).release().perform()
'''
time.sleep(10)

element=webD.find_element("xpath",'//*[@id="uniqName_40_0"]/div[5]/div[1]/div[2]/div[3]')
actions=ActionChains(webD)
actions.move_to_element(element).perform()

setting=webD.find_element("xpath",'//*[@id="uniqName_40_0"]/div[5]/div[1]/div[2]/div[3]')
action=ActionChains(webD)
action.move_to_element(setting).click().perform()
'''

html=webD.page_source

soup=BeautifulSoup(html,'html.parser')
html_table=soup.find('div', attrs={'id':'dgrid_0'})

table_row=pd.read_html(str(html_table))

for row in table_row:
    row.columns=table_row[0].columns

df=pd.concat(table_row)
#df.to_excel(r"C:\Stripe\trial dataframe.xlsx")
st.dataframe(df,1000,1000)

st.session_state["dataframe"] = df

st.write(st.session_state["dataframe"])


#-------------------------Open Pandas file-------------------------

