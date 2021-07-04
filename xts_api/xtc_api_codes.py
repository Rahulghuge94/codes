'''function for xts api to get data historical data
   create xtsconnect object with desired var name.. here i have named it xt1
   replace xt1 with your market data xtsconnect objct.
'''
def get_data(instrumentid,starttime,endtime,compressionValue,exchangesegment):
    res=xt1.get_ohlc(exchangesegment,instrumentid,starttime,endtime,compressionValue)
    #print(res)
    data=res['result']['dataReponse']
    data=data.split(',')
    data=[i.split('|') for i in data]
    data=[[data[i][0],float(data[i][1]),float(data[i][2]),float(data[i][3]),float(data[i][4]),float(data[i][5]),float(data[i][6])] for i in range(len(data))]
    df=pd.DataFrame(data,columns=['Datetime','Open','High','Low',"Close",'Volume','OI'])
    return df
def get_future(symbol,expiry):
    month={"01":'Jan',"02":'Feb',"03":'Mar',"04":'Apr',"05":'May',"06":'Jun',"07":'Jul',"08":'Aug',"09":'Sep',"10":'Oct',"11":'Nov',"12":'Dec'}
    date=expiry[6:]
    mon=month[expiry[4:6]]
    year=expiry[:4]
    symbol=symbol.upper()
    return xt1.get_future_symbol(2,'FUTIDX',symbol,f'{date}{mon}{year}')['result'][0]['ExchangeInstrumentID']
