# configs
config_path = './config/config.yaml'

# urls
base_url = 'https://www.finanzen.net/index/'
ext_urls = {
            'DAX' : 'dax/30-werte', 
            'TECDAX' : 'tecdax/werte',
            'DOW JONES' : 'dow_jones/werte',
            'MDAX' : 'mdax/werte',
            'SDAX' : 'sdax/werte',
            'S&P500' : 's&p_500/werte',
            'NASDAQ100' : 'nasdaq_100/werte',
            'EUROSTOXX' : 'euro_stoxx_50/werte',
            'SMI' : 'smi/werte',
            'ATX' : 'atx/werte',
            'CAC40' : 'cac_40/werte'
        }

# rename cols mappings
rename_dict = {
    'name' : 'stock',
    'current' : 'current price',
    'last_day' : 'previous day price',
    'percent_change' : '% drop'
}

# lower threshold in percent
per_threshold = -5.0