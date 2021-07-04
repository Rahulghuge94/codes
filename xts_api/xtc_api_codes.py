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
