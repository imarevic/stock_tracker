import scraping as sc
import consts as c
import email_sending as es
import email_processing as ep
from helpers import rename_cols, write_string_to_file


def run():
    
    # generate base mail html
    m_html = ep.generate_base_html()

    # loop over stock indeces and prepare data
    empty_cnt = 0
    for k, v in c.ext_urls.items():
        # retrieve data
        html = sc.get_html_content(c.base_url, v)
        table = sc.get_table_content(html, 'table-hover')
        df = sc.extract_data(table[0])

        # rename cols
        df = rename_cols(df, c.rename_dict)

        # process data and create html
        if not df.empty:
            m_html = ep.append_stock_html_to_mail(df, m_html, k)
        else:
            empty_cnt+=1

    # append fallback and closing tags
    if empty_cnt == len(c.ext_urls):
        m_html = ep.append_no_info_fallback(m_html)
    
    m_html = ep.append_html_closing_tags(m_html)

    # write html string to disk (for testing)
    #write_string_to_file(m_html)
    
    # send mails
    es.send_mails(m_html)