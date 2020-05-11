# -*- coding: utf-8 -*-
from linepy import *
import json, time, random

#line = Lineline(authToken='AUTH TOKEN')

line = LineClient(id = 'ENTER YOUR LINE EMAIL ADRESS HERE', passwd = 'Password')


line.log("Auth Token : " + str(line.authToken))

channel = LineChannel(line)
line.log("Channel Access Token : " + str(channel.channelAccessToken))

poll = LinePoll(line)

cctv={
    "cyduk":{},
    "point":{},
    "sidermem":{}
}

while True:
    try:
        ops=poll.singleTrace(count=50)
        for op in ops:
            if op.type == 26:
                msg = op.message
                if msg.text != None:
                    if msg.toType == 2:
                        may = line.getProfile().mid
                        if may in str(msg.contentMetadata) and 'MENTION' in str(msg.contentMetadata):
                            pilih = ['yang tag sy semoga jomblo seumur hidup','ngapain tag tag woe, kangen?','ada apa ini? ko di tag?','duhh kena tag, dianya kesepian kali yah','gk usah tag, gift tikel aja']
                            rslt = random.choice(pilih)
                            line.sendText(msg.to, str(rslt))
                        else:
                            pass
                    else:
                        pass
                else:
                    pass
            elif op.type == 25:
                msg = op.message
                text = msg.text
                msg_id = msg.id
                receiver = msg.to
                sender = msg._from
                try:
                    if msg.contentType == 0:
                        if msg.toType == 2:
                            line.sendChatChecked(receiver, msg_id)
                            contact = line.getContact(sender)
                            if text.lower() == 'me':
                                line.sendMessage(receiver, None, contentMetadata={'mid': sender}, contentType=13)
                            elif text.lower() == 'speed':
                                start = time.time()
                                line.sendText(receiver, "TestSpeed")
                                elapsed_time = time.time() - start
                                line.sendText(receiver, "%sdetik" % (elapsed_time))
                            elif 'spic' in text.lower():
                                try:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    u = key["MENTIONEES"][0]["M"]
                                    a = line.getContact(u).pictureStatus
                                    line.sendImageWithURL(receiver, 'http://dl.profile.line.naver.jp/'+a)
                                except Exception as e:
                                    line.sendText(receiver, str(e))
                            elif 'scover' in text.lower():
                                try:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    u = key["MENTIONEES"][0]["M"]
                                    a = channel.getProfileCoverURL(mid=u)
                                    line.sendImageWithURL(receiver, a)
                                except Exception as e:
                                    line.sendText(receiver, str(e))
                            elif text.lower() == 'tagall':
                                group = line.getGroup(msg.to)
                                nama = [contact.mid for contact in group.members]
                                nm1, nm2, nm3, nm4, nm5, jml = [], [], [], [], [], len(nama)
                                if jml <= 100:
                                    line.mention(msg.to, nama)
                                if jml > 100 and jml < 200:
                                    for i in range(0, 100):
                                        nm1 += [nama[i]]
                                    line.mention(msg.to, nm1)
                                    for j in range(101, len(nama)):
                                        nm2 += [nama[j]]
                                    line.mention(msg.to, nm2)
                                if jml > 200 and jml < 300:
                                    for i in range(0, 100):
                                        nm1 += [nama[i]]
                                    line.mention(msg.to, nm1)
                                    for j in range(101, 200):
                                        nm2 += [nama[j]]
                                    line.mention(msg.to, nm2)
                                    for k in range(201, len(nama)):
                                        nm3 += [nama[k]]
                                    line.mention(msg.to, nm3)
                                if jml > 300 and jml < 400:
                                    for i in range(0, 100):
                                        nm1 += [nama[i]]
                                    line.mention(msg.to, nm1)
                                    for j in range(101, 200):
                                        nm2 += [nama[j]]
                                    line.mention(msg.to, nm2)
                                    for k in range(201, len(nama)):
                                        nm3 += [nama[k]]
                                    line.mention(msg.to, nm3)
                                    for l in range(301, len(nama)):
                                        nm4 += [nama[l]]
                                    line.mention(msg.to, nm4)
                                if jml > 400 and jml < 501:
                                    for i in range(0, 100):
                                        nm1 += [nama[i]]
                                    line.mention(msg.to, nm1)
                                    for j in range(101, 200):
                                        nm2 += [nama[j]]
                                    line.mention(msg.to, nm2)
                                    for k in range(201, len(nama)):
                                        nm3 += [nama[k]]
                                    line.mention(msg.to, nm3)
                                    for l in range(301, len(nama)):
                                        nm4 += [nama[l]]
                                    line.mention(msg.to, nm4)
                                    for m in range(401, len(nama)):
                                        nm5 += [nama[m]]
                                    line.mention(msg.to, nm5)             
                                line.sendText(receiver, "Members :"+str(jml))
                            elif text.lower() == 'ceksider':
                                try:
                                    del cctv['point'][msg.to]
                                    del cctv['sidermem'][msg.to]
                                    del cctv['cyduk'][msg.to]
                                except:
                                    pass
                                cctv['point'][msg.to] = msg.id
                                cctv['sidermem'][msg.to] = ""
                                cctv['cyduk'][msg.to]=True
                            elif text.lower() == 'offread':
                                if msg.to in cctv['point']:
                                    cctv['cyduk'][msg.to]=False
                                    line.sendText(msg.to, cctv['sidermem'][msg.to])
                                else:
                                    line.sendText(msg.to, "Heh belom di Set")
                except Exception as e:
                    line.log("[SEND_MESSAGE] ERROR : " + str(e))

            elif op.type == OpType.NOTIFIED_READ_MESSAGE:
                try:
                    if cctv['cyduk'][op.param1]==True:
                        if op.param1 in cctv['point']:
                            Name = line.getContact(op.param2).displayName
                            if Name in cctv['sidermem'][op.param1]:
                                pass
                            else:
                                cctv['sidermem'][op.param1] += "\n~ " + Name
                                pref=['eh ada','hai kak','aloo..','nah','lg ngapain','halo','sini kak']
                                line.sendText(op.param1, str(random.choice(pref))+' '+Name)
                        else:
                            pass
                    else:
                        pass
                except:
                    pass

            else:
                pass

            # Don't remove this line, if you wan't get error soon!
            poll.setRevision(op.revision)
            
    except Exception as e:
        line.log("[SINGLE_TRACE] ERROR : " + str(e))
