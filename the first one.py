import requests



url = 'https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2024-11-13&leftTicketDTO.from_station=SJP&leftTicketDTO.to_station=SHH&purpose_codes=ADULT'
headers = {
        'Cookie' : '_uab_collina=173133273623786430645871; JSESSIONID=58D33D3A0912FEA5373D92E498CAF187; tk=ricWLwYPebHhScRn1-ZYfVo_bwa7mesrRzJigggaC1C0; route=9036359bb8a8a461c164a04f8f50b252; BIGipServerotn=3956736266.50210.0000; _jc_save_toDate=2024-11-11; _jc_save_wfdc_flag=dc; guidesStatus=off; highContrastMode=defaltMode; cursorStatus=off; BIGipServerpassport=971505930.50215.0000; uKey=04e441d46d85caef49862b1b260b468980de011b22baccfd585230b0fa2a9fba; _jc_save_fromStation=%u77F3%u5BB6%u5E84%2CSJP; _jc_save_toStation=%u4E0A%u6D77%2CSHH; _jc_save_fromDate=2024-11-13',
        'User-Agent' : 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Mobile Safari/537.36 Edg/130.0.0.0'
}

response = (requests.get(url = url , headers = headers))

json = response.json()

result = json[ 'data']['result']

for i in result:

        index = i.split('|')
        page = 0

        train_num = index[3]
        set_time = index[8]
        arrive_time = index[9]
        print("列车号为", train_num)
        print("出发时间为",set_time)
        print("到达时间为",arrive_time)


