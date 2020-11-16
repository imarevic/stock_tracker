import consts as c
from datetime import datetime


def generate_base_html():
    
    now = datetime.now()

    base_html = """<html>
    <head>
    <style>
    table, td, th {{
        border: 1px solid black;
        text-align: center;
    }}
    table {{
        border-collapse: collapse;
        width: 100%;
        }}
    </style>
    </head>
    <body>
    <h3><em>Stock Tracker Information</em></h1>
    <br><br>
    Stocks, if any, that dropped more than {}% relative to previous closing: <br><br>
    
    <em>Note</em>: 
    <ul>
        <li>DAX, TECDAX, MDAX, SDAX and EUROSTOXX prices in Euro, DOW JONES, S&P500 und NASDAQ100 in dollar</li>
        <li>results may not be complete due to JavaScript being loaded with delay on the source site and possibly not being picked up by the request</li>
    </ul>
    <em>Data as of {}</em>
    <hr>
    """.format(c.per_threshold,  now.strftime("%m/%d/%Y, %H:%M:%S"))
             
    return base_html


def append_stock_html_to_mail(df, m_html, heading):

    df_html = df.to_html(index=False)
    m_html = """{}
    <h4>{}</h4>
    {}
    <hr>
    """.format(m_html, heading, df_html)
    
    return m_html


def append_no_info_fallback(m_html):

    m_html = """{}
    <br><br>
    No information to display as no major stock drops occured.
    <br><br>
    <hr>
    """.format(m_html)

    return m_html


def append_html_closing_tags(m_html):

    m_html = """{}
    </body>
    </html>""".format(m_html) 
    return m_html
