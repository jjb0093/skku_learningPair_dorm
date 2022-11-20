import requests
import json

def getDelivery(code, invoice):

    url = 'https://info.sweettracker.co.kr/api/v1/trackingInfo?t_key=BBiZ6d7JKFfUKACipNl06g&t_code='+ str(code) + '&t_invoice=' + str(invoice)
    data = json.loads(requests.get(url).text)

    if("status" in data): return "ERROR"
    else:
        info = {}
        info["complete"] = data['complete']
        #info["invoice_no"] = data['invoiceNo']
        info["item_name"] = data['itemName']
        #info["receiver_addr"] = data['receiverAddr']
        #info["receiver_name"] = data['receiverName']
        #info["sender_name"] = data['senderName']
        #info["last_detail"] = data['lastDetail']
        trackingDetails_count = len(data['trackingDetails'])

        trackingDetails = []
        for i in range(trackingDetails_count):
            details = {}
            tracking = data['trackingDetails'][i]
            details["trans_kind"] = tracking['kind']
            #details["trans_telno"] = tracking['telno']
            details["timeString"] = tracking['timeString']
            details["trans_where"] = tracking['where']
            trackingDetails.append(details)

        return info, trackingDetails