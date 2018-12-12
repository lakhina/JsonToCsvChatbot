import json

import csv
with open('input.json',errors='ignore') as fp:
    data = json.load(fp)

# open a file for writing

users_data = open('output.csv', 'w')

# create the csv writer object
flag=1
csvwriter = csv.writer(users_data)
for k in data['messages']:
    user_data = data['messages'][k]

    count = 0

    for user in user_data:
        if flag:
            if count == 0:
                print(user)
                header = ['Timestamp', 'Reciever Email','Receiver Id', 'Receiver Name', 'Sender Email', 'Sender Id', 'Sender Name',
                           'Text', 'Resource','Feedback']

                csvwriter.writerow(header)

                count += 1
                flag=0
        # print(user_data[user].keys())

        # print(user_data[user]['isText'])
        if 'isText'  in user_data[user].keys():
            if user_data[user]['isText'] == '1':
                # user_data[user]['photoPath'] = ""
                user_data[user]['audio_name']=""
                # user_data[user]['videoPath']=""
            elif user_data[user]['isText'] == '0':
                user_data[user]['text'] = ""
                # user_data[user]['photoPath']=""
                # user_data[user]['videoPath']=""
                tuser=user_data[user]['audio_name']
                user_data[user].pop('audio_name',None)
                user_data[user]['audio_name'] =tuser
            elif user_data[user]['isText'] == '2':
                user_data[user]['text'] = ""
                # user_data[user]['audio_name']=""
                # user_data[user]['videoPath']=""
                tuser=user_data[user]['photoPath']
                user_data[user].pop('photoPath',None)
                user_data[user]['photoPath'] =tuser
            elif user_data[user]['isText'] == '3':
                user_data[user]['text'] = ""
                # user_data[user]['audio_name']=""
                # user_data[user]['photoPath']=""
                tuser=user_data[user]['videoPath']
                user_data[user].pop('videoPath',None)
                user_data[user]['videoPath'] =tuser


        else:

            print(user_data[user])
            user_data[user]['isText'] ='NA'
            user_data[user]['audio_name'] = ""
        import time
        # print(time.ctime(1543670618))
        # print(user_data[user]['timestamp'])
        t=int(user_data[user]['timestamp'])/1000
        readable = time.ctime(int(t))
        user_data[user]['isText'] =readable
        user_data[user].pop('receiverphoto', None)
        user_data[user].pop('senderphoto', None)
        if 'feedback_string' in user_data[user].keys():

            t_feed = user_data[user]['feedback_string']
            user_data[user].pop('feedback_string', None)
        else:
           user_data[user]['feedback_string']=""


        # print(time.ctime())
        if 'timestamp' in user_data[user].keys():
            # time = user_data[user]['timestamp']
            user_data[user].pop('timestamp', None)
            # user_data[user]['timestamp'] = time
        else:
            user_data[user]['timestamp'] = '1111111111111111'
        user_data[user]['feedback_string'] = t_feed
        csvwriter.writerow(user_data[user].values())

        # rid=user_data[user]['receiverid']
        # user_data[user]['receiverid'] = str(rid)
        # sid = user_data[user]['senderid']
        # user_data[user]['senderid'] = str(sid)








users_data.close()

