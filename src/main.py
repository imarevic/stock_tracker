import scraping as sc
import consts as c


def main():
    
    html = sc.get_html_content(c.base_url, c.ext_urls[0])
    table = sc.get_table_content(html, 'table-hover')
    df = sc.extract_data(table[0])
    print(df.head(40))



if __name__ == "__main__":
    main()