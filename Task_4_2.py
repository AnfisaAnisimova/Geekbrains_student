from requests import get, utils

response = get('http://www.cbr.ru/scripts/XML_daily.asp')


def currency_rates(currency):
    encodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)
    cur_list = content.split("<Valute ID=")
    for fragment in cur_list:
        if currency.upper() in fragment:
            start = fragment.find("<Value>") + 7
            end = fragment.find("</Value>")
            result = fragment[start:end]
            rate = float(result.replace(",", "."))
            print(rate)
            break
    if currency not in content:
        print(None)


currency_rates("USD")
currency_rates("EUR")
currency_rates("MYR") # малайзийский ринггит
currency_rates("GHS") # ганский седи

