from bs4 import BeautifulSoup
import urllib.request
import consts as c
import pandas as pd


def get_html_content(url, extension):

    URL = url + extension
    page= urllib.request.urlopen(URL)

    content = BeautifulSoup(page, 'html.parser')
    return content


def get_table_content(html_content, class_name):
 
    return html_content.find_all('table', class_=class_name)

def extract_data(table_html):

    # extract table rwos into list of lists
    ind_elems = list(table_html.find_all('tr'))
    base_elems = [elem.find_all('td') for elem in ind_elems]
    base_elems = [elem for elem in base_elems if elem != []]

    # define dict that will hold data
    s_data = {
        'name' : [],
        'current' : [],
        'last_day' : [],
        'percent_change' : []
    }
    # populate dict with data
    for stock in base_elems:

        stock_values_lst = stock[1].text.strip() \
            .replace('\r', 'b').replace('\n', '') \
            .split('b')
        
        if len(stock_values_lst) == 2:
        
            s_data['name'].append(stock[0].find('a').string)

            s_data['current'].append(stock[1].text.strip() \
                .replace('\r', 'b').replace('\n', '') \
                .split('b')[0].replace('.', '') \
                .replace(',','.')
                )

            s_data['last_day'].append(stock[1].text.strip() \
                .replace('\r', 'b').replace('\n', '') \
                .split('b')[1].replace('.', '') \
                .replace(',','.')
                ) 

            s_data['percent_change'].append(stock[4].find_all('span')[1].text \
                .replace(',','.')
                )
    
    # convert to df and filter
    s_df = pd.DataFrame.from_dict(s_data)
    s_df["current"] = s_df.current.astype(float)
    s_df["last_day"] = s_df.last_day.astype(float)
    s_df["percent_change"] = s_df.percent_change.astype(float)
    s_df = s_df[s_df['percent_change'] <= c.per_threshold]
    return s_df




