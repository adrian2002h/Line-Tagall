from linepy import *
#Says to import everything from the package Linepy
import json

#line = Lineline(authToken='AUTH TOKEN')

line = LineClient(id = 'Enter your email', passwd = 'Password')
#If you want to login into different accounts, uncomment the next line, and recomment the first, or vise versa to save one accounts login info.
#line = LineClient(id = 'ENTER YOUR SECOND EMAIL', passwd = 'Password') # IF APPLIES, otheriwise, leave as a comment or delete this line', 


line.log("Auth Token : " + str(line.authToken))
#logs the authentication Token

channel = LineChannel(line)
line.log("Channel Access Token : " + str(channel.channelAccessToken))
#logs the channels access token

poll = LinePoll(line)
#creates a new instance for the selfbot
#while true runs forever since it says while this is true, do this, so having true there, it will constantly run.
while True:
    try:
        ops = poll.singleTrace(count=50)
        for op in ops:
            if op.type == 26:
                msg = op.message
            elif op.type == 25:
                msg = op.message
                text = msg.text
                msg_id = msg.id
                receiver = msg.to
                sender = msg._from
                try:
                        if text.lower() == '.tagall':
                                group = line.getGroup(msg.to)
                                line_Ids1 = [contact.mid for contact in group.members]
                                if len(line_Ids1) >= 1:
                                        line.mention(msg.to, line_Ids1[0:10])
                                        print("List 1 printed")
                                if len(line_Ids1) > 10: 
                                        line.mention(msg.to, line_Ids1[10:19])
                                        print("List 2 printed")
                                if len(line_Ids1) > 19:
                                        line.mention(msg.to, line_Ids1[19: 28])
                                        print("List 3 printed")
                                if len(line_Ids1) > 28:
                                        line.mention(msg.to, line_Ids1[28:38])
                                        print("List 4 printed")
                                if len(line_Ids1) > 38:
                                        line.mention(msg.to, line_Ids1[38:48])
                                        print("List 5 printed")
                                if len(line_Ids1) > 48:
                                        line.mention(msg.to, line_Ids1[48:58])
                                        print("List 6 printed")
                                if len(line_Ids1) > 58:
                                        line.mention(msg.to, line_Ids1[58:68])
                                        print("List 7 printed")
                                if len(line_Ids1) > 68:
                                        line.mention(msg.to, line_Ids1[68:78])
                                        print("List 8 printed")
                                if len(line_Ids1) > 78:
                                        line.mention(msg.to, line_Ids1[78:88])
                                        print("List 9 printed")
                                if len(line_Ids1) > 88:
                                        line.mention(msg.to, line_Ids1[88:98])
                                        print("List 10 printed")
                except Exception as e:
                    line.log("[SEND_MESSAGE] ERROR : " + str(e))
                    #This sends an error message

            

            # Don't remove this line, if you wan't get error soon!
            poll.setRevision(op.revision)
            
    except Exception as e:
        line.log("[SINGLE_TRACE] ERROR : " + str(e))
