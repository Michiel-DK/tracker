from pytickersymbols import PyTickerSymbols
import itertools

def get_tickers():
    stock_data = PyTickerSymbols()
    omx_helsinki_25 = stock_data.get_omx_helsinki_25_nyc_yahoo_tickers()
    ftse_100 = stock_data.get_ftse_100_nyc_yahoo_tickers()
    cac_40 = stock_data.get_cac_40_nyc_yahoo_tickers()
    omx_stockholm_30 = stock_data.get_omx_stockholm_30_nyc_yahoo_tickers()
    dow_jones = stock_data.get_dow_jones_nyc_yahoo_tickers()
    sp_500 = stock_data.get_sp_500_nyc_yahoo_tickers()
    ibex_35 = stock_data.get_ibex_35_nyc_yahoo_tickers()
    sdax = stock_data.get_sdax_nyc_yahoo_tickers()
    cac_mid_60 = stock_data.get_cac_mid_60_nyc_yahoo_tickers()
    dax = stock_data.get_dax_nyc_yahoo_tickers()
    nasdaq_100 = stock_data.get_nasdaq_100_nyc_yahoo_tickers()
    aex = stock_data.get_aex_nyc_yahoo_tickers()
    euro_stoxx_50 = stock_data.get_euro_stoxx_50_nyc_yahoo_tickers()
    bel_20 = stock_data.get_bel_20_nyc_yahoo_tickers()
    switzerland_20 = stock_data.get_switzerland_20_nyc_yahoo_tickers()
    sp_100 = stock_data.get_sp_100_nyc_yahoo_tickers()
    moex = stock_data.get_moex_nyc_yahoo_tickers()
    tecdax = stock_data.get_tecdax_nyc_yahoo_tickers()
    cdax = stock_data.get_cdax_nyc_yahoo_tickers()
    mdax = stock_data.get_mdax_nyc_yahoo_tickers()
    
    big_ls = [nasdaq_100, tecdax, aex, euro_stoxx_50, bel_20, omx_helsinki_25, ftse_100, cac_40, \
        omx_stockholm_30, dow_jones, sp_500, ibex_35, sdax, dax, cac_mid_60,sp_100, switzerland_20, moex, cdax, mdax]
    
    merged = list(set(list(itertools.chain(*big_ls))))
    
    y_list = []
    f_list = []
    for i in merged:
        if (len(i) > 4) and i.endswith('Y'):
            y_list.append(i[:-1])
        elif (len(i) > 4) and i.endswith('F'):
            f_list.append(i[:-1])
        else:
            pass
        
    doubles = list(set(y_list) & set(f_list))
    doubles_y = [x+'Y' for x in doubles]
    
    undoubled_merged = [x for x in merged if x not in doubles_y]
    
    return sorted(undoubled_merged)