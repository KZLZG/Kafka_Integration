data =  {
    1: {
        "post_id": 1,
        "channel_id": 1,
        "channel": "1",
        "text":"1",
        "photo": "aboba",
        "status":"sent",
        "date_sent": "15.05",
    },
    2: {
        "post_id": 2,
        "channel_id":2,
        "channel": "2",
        "text":"2",
        "photo": "notaboba",
        "status":"sent",
        "date_sent": "16.05",
    },
    3: {
        "post_id": 3,
        "channel_id": 3,
        "channel": "3",
        "text":"3",
        "photo": "somephoto",
        "status":"sent",
        "date_sent": "16.06",
    },
}

response = [ data[1]["post_id"],
             data[1]["channel_id"],
data[1]["channel"],
data[1]["text"],
data[1]["photo"],
data[1]["status"],
data[1]["date_sent"]]

print(response)