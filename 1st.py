import requests
import csv
if __name__ == '__main__':
    f = open('./1st.csv', mode='w', encoding='utf-8', newline='')
    csv_writer = csv.DictWriter(f, fieldnames=[
        'ISIN',
        'Bond Code',
        'Issuer',
        'Bond Type',
        'Issue Date',
        'Latest Rating'

    ] )  # 字典写入
    csv_writer.writeheader()
    url = 'https://iftp.chinamoney.com.cn/ags/ms/cm-u-bond-md/BondMarketInfoListEN'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        'Cookie': 'apache=bbfde8c184f3e1c6074ffab28a313c87; _ulta_id.ECM-Prod.ccc4=f3bd9a6c83968b3f; _ulta_ses.ECM-Prod.ccc4=8f93fd587f528f39; AlteonP10=Ann5ACw/F6xL9EB+91vYGQ$$',
        'Referer': 'https://iftp.chinamoney.com.cn/english/bdInfo//'
    }
    data = {
        'pageNo': '1',
        'pageSize': '15',
        'isin': '',
        'bondCode': '',
        'issueEnty': '',
        'bondType': '100001',
        'couponType': '',
        'issueYear': '2023',
        'rtngShrt': '',
        'bondSpclPrjctVrty': ''
    }
    res = requests.post( url=url, headers=headers, data=data )
    li_list = res.json()['data']['resultList']
    for li in li_list:
        isin = li['isin']
        bondCode = li['bondCode']
        entyFullName = li['entyFullName']
        bondType = li['bondType']
        issueStartDate = li['issueStartDate']
        debtRtng = li['debtRtng']
        dic = {
            'ISIN':li['isin'],
            'Bond Code':li['bondCode'],
            'Issuer':li['entyFullName'],
            'Bond Type':li['bondType'],
            'Issue Date':li['issueStartDate'],
            'Latest Rating':li['debtRtng'],
        }
        csv_writer.writerow( dic )
        print( dic )