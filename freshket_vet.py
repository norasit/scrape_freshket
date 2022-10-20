import bs4
import pandas as pd
import requests
from selenium import webdriver


def scrape(start=1,end = 79): # Oct 2022, there are 79 pages in vetgetable category from freshket.com
    page_list = [ i for i in range(start,end+1)] # create list of page in product category

    # create blank pandas dataframe
    df = pd.DataFrame(columns = ['products','packages','prices', 'Date&Time'] )

    for num in page_list: # scraping product information in each page 
        
        url = f'https://freshket.co/market/vegetable?page={str(num)}'
        driver = webdriver.Chrome()
        driver.get(url)
        data = driver.page_source
        driver.close()
        soup = bs4.BeautifulSoup(data)
        # products => names, brands , details
        products = soup.find_all('h3',{'class':'MuiTypography-root jss200 MuiTypography-h5 MuiTypography-colorTextPrimary'})
        
        # packages => type, size, weight of packages
        packages = soup.find_all('p',{'class':'MuiTypography-root jss201 MuiTypography-body2 MuiTypography-colorTextSecondary'})
        
        # prices in Thai Baht
        prices = soup.find_all('h5')
    
        all_products_list=[]
        for i in products:
            all_products_list.append(i.text)

        all_packages_list=[]
        for j in packages:
            all_packages_list.append(j.text)
    
        all_prices_list= []
        for k in prices:
            all_prices_list.append(float(k.text.replace(',','')[1:]))
        
        # create pandas dataframe for each page
        df_num = pd.DataFrame(list(zip(all_products_list,all_packages_list,all_prices_list)), columns = ['products','packages','prices'])

        # create column timestamp in each page
        df_num['Date&Time'] = pd.Timestamp.today()
        
        # append data frame from each page
        df = df.append(df_num, ignore_index = True)

    return df
