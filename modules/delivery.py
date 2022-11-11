import requests
import json

def getDelivery(code, invoice):
    code = "04"
    invoice = "566223490280"

    url = 'https://info.sweettracker.co.kr/api/v1/trackingInfo?t_key=7r7oaKc5c22PTh3FgFIB6Q&t_code='+ str(code) + '&t_invoice=' + str(invoice)
    data = json.loads(requests.get(url).text)

    info = {}

    info["complete"] = data['complete']
    info["invoice_no"] = data['invoiceNo']
    info["item_name"] = data['itemName']
    info["receiver_addr"] = data['receiverAddr']
    info["receiver_name"] = data['receiverName']
    info["sender_name"] = data['senderName']
    info["last_detail"] = data['lastDetail']
    trackingDetails_count = len(data['trackingDetails'])

    trackingDetails = []
    for i in range(trackingDetails_count):
        details = {}
        tracking = data['trackingDetails'][i]
        details["trans_kind"] = tracking['kind']
        details["trans_telno"] = tracking['telno']
        details["trans_time"] = tracking['time']
        details["trans_where"] = tracking['where']
        trackingDetails.append(details)

    return info, trackingDetails

    """
    dict_items(
    [('adUrl', ''), ('complete', True), ('invoiceNo', '566223490280'), ('itemImage', ''), ('itemName', '[UB152-B-1] 보이로 전기요 (블루-UB152 1인)_ 1개'), ('level', 6), ('receiverAddr', ''), ('receiverName', ''), ('recipient', ''), ('result', 'Y'), ('senderName', ''), ('trackingDetails', [{'kind': '집화처리', 'level': 2, 'manName': '', 'manPic': '', 'telno': '02-2066-8777', 'telno2': '', 'time': 1663667438000, 'timeString': '2022-09-20 18:50:38', 'where': '서울구로온수', 'code': None, 'remark': None}, {'kind': '간선상차', 'level': 3, 'manName': '', 'manPic': '', 'telno': '02-2657-7806', 'telno2': '', 'time': 1663680525000, 'timeString': '2022-09-20 22:28:45', 'where': '가산콘솔Hub', 'code': None, 'remark': None}, {'kind': '간선하차', 'level': 3, 'manName': '', 'manPic': '', 'telno': '', 'telno2': '', 'time': 1663695247000, 'timeString': '2022-09-21 02:34:07', 'where': '곤지암Hub', 'code': None, 'remark': None}, {'kind': '간선하차', 'level': 3, 'manName': '', 'manPic': '', 'telno': '', 'telno2': '', 'time': 1663695456000, 'timeString': '2022-09-21 02:37:36', 'where': '곤지암Hub', 'code': None, 'remark': None}, {'kind': '간선상차', 'level': 3, 'manName': '', 'manPic': '', 'telno': '', 'telno2': '', 'time': 1663695523000, 'timeString': '2022-09-21 02:38:43', 'where': '곤지암Hub', 'code': None, 'remark': None}, {'kind': '간선하차', 'level': 3, 'manName': '', 'manPic': '', 'telno': '02-707-1255', 'telno2': '', 'time': 1663718533000, 'timeString': '2022-09-21 09:02:13', 'where': '종로A', 'code': None, 'remark': None}, {'kind': '간선하차', 'level': 3, 'manName': '', 'manPic': '', 'telno': '02-707-1255', 'telno2': '', 'time': 1663718612000, 'timeString': '2022-09-21 09:03:32', 'where': '종로A', 'code': None, 'remark': None}, {'kind': '배달출발\n(배달예정시간\n:16∼18시)', 'level': 5, 'manName': '김원규', 'manPic': '', 'telno': '010-8489-2076', 'telno2': '01076099575', 'time': 1663728376000, 'timeString': '2022-09-21 11:46:16', 'where': '명륜3가', 'code': None, 'remark': None}, {'kind': '배달완료', 'level': 6, 'manName': '김원규', 'manPic': '', 'telno': '010-8489-2076', 'telno2': '01076099575', 'time': 1663743517000, 'timeString': '2022-09-21 15:58:37', 'where': '명륜3가', 'code': None, 'remark': None}]), ('orderNumber', None), ('estimate', '16∼18시'), ('productInfo', None), ('zipCode', None), ('lastDetail', {'kind': '배달완료', 'level': 6, 'manName': '김원규', 'manPic': '', 'telno': '010-8489-2076', 'telno2': '01076099575', 'time': 1663743517000, 'timeString': '2022-09-21 15:58:37', 'where': '명륜3가', 'code': None, 'remark': None}), ('lastStateDetail', {'kind': '배달완료', 'level': 6, 'manName': '김원규', 'manPic': '', 'telno': '010-8489-2076', 'telno2': '01076099575', 'time': 1663743517000, 'timeString': '2022-09-21 15:58:37', 'where': '명륜3가', 'code': None, 'remark': None}), ('firstDetail', {'kind': '집화처리', 'level': 2, 'manName': '', 'manPic': '', 'telno': '02-2066-8777', 'telno2': '', 'time': 1663667438000, 'timeString': '2022-09-20 18:50:38', 'where': '서울구로온수', 'code': None, 'remark': None}), ('completeYN', 'Y')]
    )
    """