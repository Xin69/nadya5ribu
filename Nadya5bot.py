# -*- coding: utf-8 -*-

from linepy import *
from datetime import datetime
from time import sleep
from bs4 import BeautifulSoup
from humanfriendly import format_timespan, format_size, format_number, format_length
import time, random, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, ast, pytz, urllib, urllib.parse
from gtts import gTTS
from googletrans import Translator
#==============================================================================#
botStart = time.time()

#nadya = LINE()
nadya = LINE("Exox8KlJJlPb6FuVDonf.K9hUseF6j4f/WE5DLTHHBW.5OsdwFlf150EbB+BGtikhIw7vYGNn4pjvFEJ86jD7o4=")
#nadya = LINE("Email","Password")
nadya.log("Auth Token : " + str(nadya.authToken))
channelToken = nadya.getChannelResult()
nadya.log("Channel Token : " + str(channelToken))

#ki = LINE()
ki = LINE("Ey2X4bCWpbehCs5Wc7k9.t2D+Q8GQs5QI1aUzyFPrAq.k0YmfZdnzHbRtGBTmgy8hOMr/Q8MRkdiKy5f0xpUsuw=")
#ki = LINE("Email","Password")
ki.log("Auth Token : " + str(ki.authToken))
channelToken = ki.getChannelResult()
ki.log("Channel Token : " + str(channelToken))

#ki2 = LINE()
ki2 = LINE("ExbTWXWNsNaBgCp0Xv35.fj0S/qYKVWGRwpehA8QPbq.+8KLs76Lq91JR/U5WEoCRnWe2mGjLgIk4C0Fyuur4hA=")
#ki2 = LINE("Email","Password")
ki2.log("Auth Token : " + str(ki2.authToken))
channelToken = ki2.getChannelResult()
ki2.log("Channel Token : " + str(channelToken))

#ki3 = LINE()
ki3 = LINE("Eygrpxx1Kj4C966K1q09.hBhkoFGOWq2ca/v2aGDfkq.IvKjCjfN8RHg0K6D10m5FVxnLzPDIZVboel+HDRZmLk=")
#ki3 = LINE("Email","Password")
ki3.log("Auth Token : " + str(ki3.authToken))
channelToken = ki3.getChannelResult()
ki3.log("Channel Token : " + str(channelToken))

#ki4 = LINE()
ki4 = LINE("EyFRJ6bmcx8bS2zhqei8.wb+1x+ATrwACcZUumYsSUa.pITJ4DluM4zyCd6RD4MPz4M2D+ziA9UbcNKYf38yHlc=")
#ki4 = LINE("Email","Password")
ki4.log("Auth Token : " + str(ki4.authToken))
channelToken = ki4.getChannelResult()
ki4.log("Channel Token : " + str(channelToken))


KAC = [nadya,ki,ki2,ki3,ki4]

nadyaMID = nadya.profile.mid
kiMID = ki.profile.mid
ki2MID = ki2.profile.mid
ki3MID = ki3.profile.mid
ki4MID = ki4.profile.mid

Bots = [nadyaMID,kiMID,ki2MID,ki3MID,ki4MID]
creator = ["u93d1ee4847fa27817ec1ee5d96d8616f","u9f09cfcb17d037e2936b751bd9d40ead"]
Owner = ["u93d1ee4847fa27817ec1ee5d96d8616f"]
admin = ["u93d1ee4847fa27817ec1ee5d96d8616f"]

nadyaProfile = nadya.getProfile()
kiProfile = ki.getProfile()
ki2Profile = ki2.getProfile()
ki3Profile = ki3.getProfile()
ki4Profile = ki4.getProfile()

lineSettings = nadya.getSettings()
kiSettings = ki.getSettings()
ki2Settings = ki2.getSettings()
ki3Settings = ki3.getSettings()
ki4Settings = ki4.getSettings()

oepoll = OEPoll(nadya)
oepoll1 = OEPoll(ki)
oepoll2 = OEPoll(ki2)
oepoll3 = OEPoll(ki3)
oepoll4 = OEPoll(ki4)

responsename = nadya.getProfile().displayName
responsename2 = ki.getProfile().displayName
responsename3 = ki2.getProfile().displayName
responsename4 = ki3.getProfile().displayName
responsename5 = ki4.getProfile().displayName
#==============================================================================#

with open('Owner.json', 'r') as fp:
    Owner = json.load(fp)
    
with open('admin.json', 'r') as fp:
    admin = json.load(fp)
    
myProfile = {
	"displayName": "",
	"statusMessage": "",
	"pictureStatus": ""
}

myProfile["displayName"] = nadyaProfile.displayName
myProfile["statusMessage"] = nadyaProfile.statusMessage
myProfile["pictureStatus"] = nadyaProfile.pictureStatus

readOpen = codecs.open("read.json","r","utf-8")
settingsOpen = codecs.open("temp.json","r","utf-8")

#==============================================================================#

read = json.load(readOpen)
settings = json.load(settingsOpen)

#if settings["restartPoint"] != None:
#    nadya.sendMessage(settings["restartPoint"], "Bot kembali aktif")
#    settings["restartBot"] = None

def restartBot():
    print ("[ INFO ] BOT RESETTED")
    backupData()
#    time.sleep(10)
    python = sys.executable
    os.execl(python, python, *sys.argv)
    
def logError(text):
    nadya.log("[ ERROR ] " + str(text))
    time_ = datetime.now()
    with open("errorLog.txt","a") as error:
        error.write("\n[%s] %s" % (str(time), text))
        
def sendMessageWithMention(to, mid):
    try:
        aa = '{"S":"0","E":"3","M":'+json.dumps(mid)+'}'
        text_ = '@x '
        nadya.sendMessage(to, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
    except Exception as error:
        logError(error)
        
def helpmessage():
    helpMessage = "┏━━━━━━━━━━━━━━━" + "\n" + \
                  "┣  F O R C E -1   P R O T E C T I O N" + "\n" + \
                  "┃" + "\n" + \
                  "┣━━━━" + "\n" + \
                  "┃" + "\n" + \
                  "┣━━━━━━━" + "\n" + \
                  "┣➥ Protect 「On/Off」" + "\n" + \
                  "┣➥ QrProtect 「On/Off」" + "\n" + \
                  "┣➥ InviteProtect 「On/Off」" + "\n" + \
                  "┣➥ CancelProtect 「On/Off」" + "\n" + \
                  "┣➥ SetPro 「On/Off」" + "\n" + \
                  "┃" + "\n" + \
                  "┣━━━━━━━" + "\n" + \
                  "┣➥ AutoAdd「On/Off」" + "\n" + \
                  "┣➥ AutoJoin「On/Off」" + "\n" + \
                  "┣➥ AutoLeave「On/Off」" + "\n" + \
                  "┣➥ Me" + "\n" + \
                  "┣➥ MyMid" + "\n" + \
                  "┣➥ KickAllMember"+ "\n" + \
                  "┃" + "\n" + \
                  "┣━━━━━━━━━━━━━━━━━━━" + "\n" + \
                  "┣➥ BanContact" + "\n" + \
                  "┣➥ UnbanContact" + "\n" + \
                  "┣➥ BanList" + "\n" + \
                  "┣➥ ClearBan" + "\n" + \
                  "┣➥ Respon" + "\n" + \
                  "┣➥ JoinAll" + "\n" + \
                  "┣➥ ByeAll" + "\n" + \
                  "┃" + "\n" + \
                  "┗━〘 FORCE -1  〙"
    return helpMessage
    
#==============================================================================#
def backupData():
    try:
        backup = settings
        f = codecs.open('temp.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = read
        f = codecs.open('read.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        return True
    except Exception as error:
        logError(error)
        return False
        
def command(text):
    pesan = text.lower()
    if pesan.startswith(settings["keyCommand"]):
        cmd = pesan.replace(settings["keyCommand"],"")
    else:
        cmd = "Undefined command"
    return cmd        


def lineBot(op):
    try:
        if op.type == 0:
            print ("[ 0 ] END OF OPERATION")
            return
        if op.type == 5:
            print ("[ 5 ] NOTIFIED ADD CONTACT")
            if settings["autoAdd"] == True:
                nadya.sendMessage(op.param1, "Halo {} terimakasih telah menambahkan saya sebagai teman :D".format(str(nadya.getContact(op.param1).displayName)))
        if op.type == 13:
            print ("[ 13 ] NOTIFIED INVITE INTO GROUP")
            group = nadya.getGroup(op.param1)
            contact = nadya.getContact(op.param2)
            if settings["autoJoin"] == True:
                if settings["autoReject"]["status"] == True:
                    if len(group.members) > settings["autoReject"]["members"]:
                        nadya.acceptGroupInvitation(op.param1)
                    else:
                        nadya.rejectGroupInvitation(op.param1)
                else:
                    nadya.acceptGroupInvitation(op.param1)
            gInviMids = []
            for z in group.invitee:
                if z.mid in op.param3:
                    gInviMids.append(z.mid)
            listContact = ""
            if gInviMids != []:
                for j in gInviMids:
                    name_ = nadya.getContact(j).displayName
                    listContact += "\n      + {}".format(str(name_))

            arg = "   Group Name : {}".format(str(group.name))
            arg += "\n   Executor : {}".format(str(contact.displayName))
            arg += "\n   List User Invited : {}".format(str(listContact))
            print (arg)
                
#-------------------------------------------------------------------------------
        if op.type == 26:
            msg = op.message
            if msg.contentType == 13:
                if settings["wblack"] == True:
                    if msg.contentMetadata["mid"] in settings["commentBlack"]:
                        nadya.sendMessage(msg.to,"sudah masuk daftar hitam")
                        settings["wblack"] = False
                    else:
                        settings["commentBlack"][msg.contentMetadata["mid"]] = True
                        settings["wblack"] = False
                        nadya.sendMessage(msg.to,"Itu tidak berkomentar")
                elif settings["dblack"] == True:
                    if msg.contentMetadata["mid"] in settings["commentBlack"]:
                        del settings["commentBlack"][msg.contentMetadata["mid"]]
                        nadya.sendMessage(msg.to,"Done")
                        settings["dblack"] = False
                    else:
                        settings["dblack"] = False
                        nadya.sendMessage(msg.to,"Tidak ada dalam daftar hitam")
#-------------------------------------------------------------------------------
                elif settings["wblacklist"] == True:
                    if msg.contentMetadata["mid"] in settings["blacklist"]:
                        nadya.sendMessage(msg.to,"sudah masuk daftar hitam")
                        settings["wblacklist"] = False
                    else:
                        settings["blacklist"][msg.contentMetadata["mid"]] = True
                        settings["wblacklist"] = False
                        nadya.sendMessage(msg.to,"Done")
                        
                elif settings["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in settings["blacklist"]:
                        del settings["blacklist"][msg.contentMetadata["mid"]]
                        nadya.sendMessage(msg.to,"Done")
                        settings["dblacklist"] = False
                    else:
                        settings["dblacklist"] = False
                        nadya.sendMessage(msg.to,"Done")
                        
                       
#-------------------------------------------------------------------------------
        if op.type == 26:
            print ("[ 26 ] SEND MESSAGE COMMAND")
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != nadya.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
            if msg.contentType == 0:
                if text is None:
                    return
#==============================================================================#
                if text.lower() == 'help':
                    helpMessage = helpmessage()
                    nadya.sendMessage(to, str(helpMessage))
                 #   nadya.sendContact(to, "u9f09cfcb17d037e2936b751bd9d40ead")
#==============================================================================#
                elif text.lower() == 'speed':
                    start = time.time()
                    nadya.sendMessage(to, "Please Wait...")
                    elapsed_time = time.time() - start
                    nadya.sendMessage(to,format(str(elapsed_time)))

#==============================================================================#
                elif text.lower() == 'status':
                    try:
                        ret_ = "┏━━[ Status ]"
                        if settings["protect"] == True: ret_ += "\n┣ Protect (ON)"
                        else: ret_ += "\n┣ Protect (OFF)"
                        if settings["qrprotect"] == True: ret_ += "\n┣ Qr Protect (ON)"
                        else: ret_ += "\n┣ Qr Protect (OFF)"
                        if settings["inviteprotect"] == True: ret_ += "\n┣ Invite Protect (ON)"
                        else: ret_ += "\n┣ Invite Protect (OFF)"
                        if settings["cancelprotect"] == True: ret_ += "\n┣ Cancel Protect (ON)"
                        else: ret_ += "\n┣ Cancel Protect (OFF)"
                        if settings["autoAdd"] == True: ret_ += "\n┣ Auto Add (ON)"
                        else: ret_ += "\n┣ Auto Add (OFF)"
                        if settings["autoJoin"] == True: ret_ += "\n┣ Auto Join (ON)"
                        else: ret_ += "\n┣ Auto Join (OFF)"
                        if settings["autoLeave"] == True: ret_ += "\n┣ Auto Leave (ON)"
                        else: ret_ += "\n┣ Auto Leave (OFF)"
                        if settings["autoRead"] == True: ret_ += "\n┣ Auto Read (ON)"
                        else: ret_ += "\n┣ Auto Read (OFF)"
                        if settings["checkSticker"] == True: ret_ += "\n┣ Check Sticker (ON)"
                        else: ret_ += "\n┣ Check Sticker (OFF)"
                        if settings["detectMention"] == True: ret_ += "\n┣ Respon (ON)"
                        else: ret_ += "\n┣ Respon (OFF)"
                        ret_ += "\n┗━━[ FORCE ONE ]"
                        nadya.sendMessage(to, str(ret_))
                    except Exception as e:
                        nadya.sendMessage(msg.to, str(e))
#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
                elif text.lower() == 'protect on':
                    if msg._from in Owner:
                        if settings["protect"] == True:
                            if settings["lang"] == "JP":
                                nadya.sendMessage(msg.to,"➙ Protection Already On")
                            else:
                                nadya.sendMessage(msg.to,"➙ Protection Set To On")
                        else:
                            settings["protect"] = True
                            if settings["lang"] == "JP":
                                nadya.sendMessage(msg.to,"➙ Protection Set To On")
                            else:
                                nadya.sendMessage(msg.to,"➙ Protection Already On")
                                
                elif text.lower() == 'protect off':
                    if msg._from in Owner:
                        if settings["protect"] == False:
                            if settings["lang"] == "JP":
                                nadya.sendMessage(msg.to,"➙ Protection Already Off")
                            else:
                                nadya.sendMessage(msg.to,"➙ Protection Set To Off")
                        else:
                            settings["protect"] = False
                            if settings["lang"] == "JP":
                                nadya.sendMessage(msg.to,"➙ Protection Set To Off")
                            else:
                                nadya.sendMessage(msg.to,"➙ Protection Already Off")
#----------------------------------------------------------------------------------------                        
                elif text.lower() == 'qrprotect on':
                    if msg._from in Owner:
                        if settings["qrprotect"] == True:
                            if settings["lang"] == "JP":
                                nadya.sendMessage(msg.to,"➙ Protection Qr Already On")
                            else:
                                nadya.sendMessage(msg.to,"➙ Protection Qr Set To On")
                        else:
                            settings["qrprotect"] = True
                            if settings["lang"] == "JP":
                                nadya.sendMessage(msg.to,"➙ Protection Qr Set To On")
                            else:
                                nadya.sendMessage(msg.to,"➙ Protection Qr Already On")
                                
                elif text.lower() == 'qrprotect off':
                    if msg._from in Owner:
                        if settings["qrprotect"] == False:
                            if settings["lang"] == "JP":
                                nadya.sendMessage(msg.to,"➙ Protection Qr Already Off")
                            else:
                                nadya.sendMessage(msg.to,"➙ Protection Qr Set To Off")
                        else:
                            settings["qrprotect"] = False
                            if settings["lang"] == "JP":
                                nadya.sendMessage(msg.to,"➙ Protection Qr Set To Off")
                            else:
                                nadya.sendMessage(msg.to,"➙ Protection Qr Already Off")
#-------------------------------------------------------------------------------
                elif text.lower() == 'inviteprotect on':
                    if msg._from in Owner:
                        if settings["inviteprotect"] == True:
                            if settings["lang"] == "JP":
                                nadya.sendMessage(msg.to,"➙ Protection Invite Already On")
                            else:
                                nadya.sendMessage(msg.to,"➙ Protection Invite Set To On")
                        else:
                            settings["inviteprotect"] = True
                            if settings["lang"] == "JP":
                                nadya.sendMessage(msg.to,"➙ Protection Invite Set To On")
                            else:
                                nadya.sendMessage(msg.to,"➙ Protection Invite Already On")
                                
                elif text.lower() == 'inviteprotect off':
                    if msg._from in Owner:
                        if settings["inviteprotect"] == False:
                            if settings["lang"] == "JP":
                                nadya.sendMessage(msg.to,"➙ Protection Invite Already Off")
                            else:
                                nadya.sendMessage(msg.to,"➙ Protection Invite Set To Off")
                        else:
                            settings["inviteprotect"] = False
                            if settings["lang"] == "JP":
                                nadya.sendMessage(msg.to,"➙ Protection Invite Set To Off")
                            else:
                                nadya.sendMessage(msg.to,"➙ Protection Invite Already Off")
#-------------------------------------------------------------------------------
                elif text.lower() == 'cancelprotect on':
                    if msg._from in Owner:
                        if settings["cancelprotect"] == True:
                            if settings["lang"] == "JP":
                                nadya.sendMessage(msg.to,"➙ Protection Cancel Invite Already On")
                            else:
                                nadya.sendMessage(msg.to,"➙ Protection Cancel Invite Set To On")
                        else:
                            settings["cancelprotect"] = True
                            if settings["lang"] == "JP":
                                nadya.sendMessage(msg.to,"➙ Protection Cancel Invite Set To On")
                            else:
                                nadya.sendMessage(msg.to,"➙ Protection Cancel Invite Already On")
                                
                elif text.lower() == 'cancelprotect off':
                    if msg._from in Owner:
                        if settings["cancelprotect"] == False:
                            if settings["lang"] == "JP":
                                nadya.sendMessage(msg.to,"➙ Protection Cancel Invite Already Off")
                            else:
                                nadya.sendMessage(msg.to,"➙ Protection Cancel Invite Set To Off")
                        else:
                            settings["cancelprotect"] = False
                            if settings["lang"] == "JP":
                                nadya.sendMessage(msg.to,"➙ Protection Cancel Invite Set To Off")
                            else:
                                nadya.sendMessage(msg.to,"➙ Protection Cancel Invite Already Off")
#-------------------------------------------------------------------------------
                elif text.lower() == 'setpro on':
                    if msg._from in Owner:
                        settings["protect"] = True
                        settings["qrprotect"] = True
                        settings["inviteprotect"] = True
                        settings["cancelprotect"] = True
                        nadya.sendMessage(msg.to,"➙ All Protect Set To On")
                    else:
                        nadya.sendMessage(msg.to,"Just for Owner")
                        		            
                elif text.lower() == 'setpro off':
                    if msg._from in Owner:
                        settings["protect"] = False
                        settings["qrprotect"] = False
                        settings["inviteprotect"] = False
                        settings["cancelprotect"] = False
                        nadya.sendMessage(msg.to,"➙ All Protect Set To Off")
                    else:
                        nadya.sendMessage(msg.to,"Just for Owner")
#-------------------------------------------------------------------------------
                elif text.lower() == 'autojoin on':
                  if msg._from in Owner:    
                    settings["autoJoin"] = True
                    nadya.sendMessage(to, "Berhasil mengaktifkan Auto Join")
                elif text.lower() == 'autojoin off':
                  if msg._from in Owner:    
                    settings["autoJoin"] = False
                    nadya.sendMessage(to, "Berhasil menonaktifkan Auto Join")
                elif text.lower() == 'autoleave on':
                  if msg._from in Owner:
                    settings["autoLeave"] = True
                    nadya.sendMessage(to, "Berhasil mengaktifkan Auto Leave")
                elif text.lower() == 'autoleave off':
                  if msg._from in Owner:
                    settings["autoLeave"] = False
                    nadya.sendMessage(to, "Berhasil menonaktifkan Auto Leave")

#==============================================================================#
                elif text.lower() == "respon":
                    nadya.sendMessage(msg.to,responsename)
                    ki.sendMessage(msg.to,responsename2)
                    ki2.sendMessage(msg.to,responsename3)
                    ki3.sendMessage(msg.to,responsename4)
                    ki4.sendMessage(msg.to,responsename5)
                    
                elif text.lower() in ["byeall"]:
                  if msg._from in Owner:    
                    ki.leaveGroup(msg.to)
                    ki2.leaveGroup(msg.to)
                    ki3.leaveGroup(msg.to)
                    ki4.leaveGroup(msg.to)
               
                elif text.lower() in ["joinall"]:
                  if msg._from in Owner:    
                    G = nadya.getGroup(msg.to)
                    ginfo = nadya.getGroup(msg.to)
                    G.preventedJoinByTicket = False
                    nadya.updateGroup(G)
                    invsend = 0
                    Ticket = nadya.reissueGroupTicket(msg.to)
                    ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                    ki2.acceptGroupInvitationByTicket(msg.to,Ticket)
                    ki3.acceptGroupInvitationByTicket(msg.to,Ticket)
                    ki4.acceptGroupInvitationByTicket(msg.to,Ticket)
                    G = nadya.getGroup(msg.to)
                    G.preventedJoinByTicket = True
                    nadya.updateGroup(G)
                    G.preventedJoinByTicket(G)
                    nadya.updateGroup(G)
                
                elif text.lower() == 'me':
                    sendMessageWithMention(to, nadyaMID)
                    nadya.sendContact(to, nadyaMID)
                elif text.lower() == 'mymid':
                    nadya.sendMessage(msg.to,"[MID]\n" +  nadyaMID)

#==============================================================================#

#-------------------------------------------------------------------------------
                elif text.lower() == 'clearban':
                    if msg._from in Owner:
                        settings["blacklist"] = {}
                        nadya.sendMessage(msg.to,"Blacklist Dibersihkan")
                        
                elif text.lower() == 'bancontact':
                    if msg._from in Owner:
                        settings["wblacklist"] = True
                        nadya.sendMessage(msg.to,"Send Contact")
                        
                elif msg.text in ["unbancontact"]:
                    if msg._from in Owner:
                        settings["dblacklist"] = True
                        nadya.sendMessage(msg.to,"Send Contact")
#-------------------------------------------------------------------------------
                elif text.lower() == 'banlist':
                    if msg._from in Owner:
                        if settings["blacklist"] == {}:
                            nadya.sendMessage(msg.to,"Tidak Ada Banlist")
                        else:
                            nadya.sendMessage(msg.to,"Daftar Banlist")
                            num=1
                            msgs="━━━━━━━━━━List Blacklist━━━━━━━━━"
                            for mi_d in settings["blacklist"]:
                                msgs+="\n[%i] %s" % (num, nadya.getContact(mi_d).displayName)
                                num=(num+1)
                            msgs+="\n━━━━━━━━━━List Blacklist━━━━━━━━━\n\nTotal Blacklist :  %i" % len(settings["blacklist"])
                            nadya.sendMessage(msg.to, msgs)
#=======================================================================================
                elif msg.text.lower().startswith("kill "):
                    if msg._from in Owner:
                       targets = []
                       key = eval(msg.contentMetadata["MENTION"])
                       key["MENTIONEES"][0]["M"]
                       for x in key["MENTIONEES"]:
                           targets.append(x["M"])
                       for target in targets:
                           try:
                               random.choice(KAC).kickoutFromGroup(msg.to,[target])
                           except:
                               random.choice(KAC).sendText(msg.to,"Error")
#-------------------------------------------------------------------------------
                elif text.lower() == 'kickallmember':
                    if msg._from in Owner:
                        if msg.toType == 2:
                            print ("[ 19 ] KICK ALL MEMBER")
                            _name = msg.text.replace("kickallmember","")
                            gs = nadya.getGroup(msg.to)
                            gs = ki.getGroup(msg.to)
                            gs = ki2.getGroup(msg.to)
                            gs = ki3.getGroup(msg.to)
                            gs = ki4.getGroup(msg.to)
    #                       nadya.sendMessage(msg.to,"「 Bye All 」")
    #                       nadya.sendMessage(msg.to,"「 Sory guys 」")
                            targets = []
                            for g in gs.members:
                                if _name in g.displayName:
                                    targets.append(g.mid)
                            if targets == []:
                                nadya.sendMessage(msg.to,"Not Found")
                            else:
                                for target in targets:
                                    if not target in Bots:
                                        if not target in Owner:
                                            if not target in admin:
                                                try:
                                                    klist=[line,ki,ki2,ki3,ki4]
                                                    kicker=random.choice(klist)
                                                    kicker.kickoutFromGroup(msg.to,[target])
                                                    print (msg.to,[g.mid])
                                                except:
                                                    nadya.sendMessage(msg.to,"") 
#==============================================================================#          
                elif text.lower() == 'tag':
                    group = nadya.getGroup(msg.to)
                    nama = [contact.mid for contact in group.members]
                    k = len(nama)//20
                    for a in range(k+1):
                        txt = u''
                        s=0
                        b=[]
                        for i in group.members[a*20 : (a+1)*20]:
                            b.append({"S":str(s), "E" :str(s+6), "M":i.mid})
                            s += 7
                            txt += u'@Alin \n'
                        nadya.sendMessage(to, text=txt, contentMetadata={u'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)
                        nadya.sendMessage(to, "Total {} Mention".format(str(len(nama))))          

#==============================================================================#

#==============================================================================# 

#==============================================================================#   

#===============================================================================[nadyaMID - kiMID]
        if op.type == 19:
            print ("[ 19 ] KICKOUT NADYA MESSAGE")
            try:
                if op.param3 in nadyaMID:
                    if op.param2 in kiMID:
                        G = ki.getGroup(op.param1)
#                        ginfo = ki.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ki.updateGroup(G)
                        invsend = 0
                        Ticket = ki.reissueGroupTicket(op.param1)
                        nadya.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki.updateGroup(G)
                    else:
                        G = ki.getGroup(op.param1)
#                        ginfo = ki.getGroup(op.param1)
                        ki.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ki.updateGroup(G)
                        invsend = 0
                        Ticket = ki.reissueGroupTicket(op.param1)
                        nadya.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#-------------------------------------------------------------------------------[nadyaMID - ki2MID]
                elif op.param3 in nadyaMID:
                    if op.param2 in ki2MID:
                        G = ki2.getGroup(op.param1)
#                        ginfo = ki2.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ki2.updateGroup(G)
                        invsend = 0
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        nadya.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki2.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki2.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki2.updateGroup(G)
                    else:
                        G = ki2.getGroup(op.param1)
#                        ginfo = ki2.getGroup(op.param1)
                        ki2.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ki2.updateGroup(G)
                        invsend = 0
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        nadya.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki2.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki2.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki2.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#-------------------------------------------------------------------------------[nadyaMID - ki3MID]
                elif op.param3 in nadyaMID:
                    if op.param2 in ki3MID:
                        G = ki3.getGroup(op.param1)
#                        ginfo = ki3.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ki3.updateGroup(G)
                        invsend = 0
                        Ticket = ki3.reissueGroupTicket(op.param1)
                        nadya.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki3.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki3.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki3.updateGroup(G)
                    else:
                        G = ki3.getGroup(op.param1)
#                        ginfo = ki3.getGroup(op.param1)
                        ki3.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ki3.updateGroup(G)
                        invsend = 0
                        Ticket = ki3.reissueGroupTicket(op.param1)
                        nadya.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki3.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki3.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki3.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#-------------------------------------------------------------------------------[nadyaMID - ki4MID]
                elif op.param3 in nadyaMID:
                    if op.param2 in ki4MID:
                        G = ki4.getGroup(op.param1)
#                        ginfo = ki4.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ki4.updateGroup(G)
                        invsend = 0
                        Ticket = ki4.reissueGroupTicket(op.param1)
                        nadya.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki4.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki4.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki4.updateGroup(G)
                    else:
                        G = ki4.getGroup(op.param1)
#                        ginfo = ki4.getGroup(op.param1)
                        ki4.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ki4.updateGroup(G)
                        invsend = 0
                        Ticket = ki4.reissueGroupTicket(op.param1)
                        nadya.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki4.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki4.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki4.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#===============================================================================[kiMID nadyaMID]
                if op.param3 in kiMID:
                    if op.param2 in nadyaMID:
                        G = nadya.getGroup(op.param1)
#                        ginfo = nadya.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        nadya.updateGroup(G)
                        invsend = 0
                        Ticket = nadya.reissueGroupTicket(op.param1)
                        nadya.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = nadya.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        nadya.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        nadya.updateGroup(G)
                    else:
                        G = nadya.getGroup(op.param1)
#                        ginfo = nadya.getGroup(op.param1)
                        nadya.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        nadya.updateGroup(G)
                        invsend = 0
                        Ticket = nadya.reissueGroupTicket(op.param1)
                        nadya.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = nadya.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        nadya.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        nadya.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#-------------------------------------------------------------------------------[kiMID ki2MID]
                elif op.param3 in kiMID:
                    if op.param2 in ki2MID:
                        G = ki2.getGroup(op.param1)
#                        ginfo = ki2.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ki2.updateGroup(G)
                        invsend = 0
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        nadya.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki2.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki2.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki2.updateGroup(G)
                    else:
                        G = ki2.getGroup(op.param1)
#                        ginfo = ki2.getGroup(op.param1)
                        ki2.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ki2.updateGroup(G)
                        invsend = 0
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        nadya.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki2.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki2.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki2.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#-------------------------------------------------------------------------------[kiMID ki3MID]
                elif op.param3 in kiMID:
                    if op.param2 in ki3MID:
                        G = ki3.getGroup(op.param1)
#                        ginfo = ki3.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ki3.updateGroup(G)
                        invsend = 0
                        Ticket = ki3.reissueGroupTicket(op.param1)
                        nadya.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki3.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki3.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki3.updateGroup(G)
                    else:
                        G = ki3.getGroup(op.param1)
#                        ginfo = ki3.getGroup(op.param1)
                        ki3.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ki3.updateGroup(G)
                        invsend = 0
                        Ticket = ki3.reissueGroupTicket(op.param1)
                        nadya.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki3.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki3.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki3.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#-------------------------------------------------------------------------------[kiMID ki4MID]
                elif op.param3 in kiMID:
                    if op.param2 in ki4MID:
                        G = ki4.getGroup(op.param1)
#                        ginfo = ki4.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ki4.updateGroup(G)
                        invsend = 0
                        Ticket = ki4.reissueGroupTicket(op.param1)
                        nadya.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki4.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki4.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki4.updateGroup(G)
                    else:
                        G = ki4.getGroup(op.param1)
#                        ginfo = ki4.getGroup(op.param1)
                        ki4.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ki4.updateGroup(G)
                        invsend = 0
                        Ticket = ki4.reissueGroupTicket(op.param1)
                        nadya.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki4.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki4.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki4.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#===============================================================================[ki2MID nadyaMID]
                if op.param3 in ki2MID:
                    if op.param2 in nadyaMID:
                        G = nadya.getGroup(op.param1)
#                        ginfo = nadya.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        nadya.updateGroup(G)
                        invsend = 0
                        Ticket = nadya.reissueGroupTicket(op.param1)
                        nadya.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = nadya.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        nadya.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        nadya.updateGroup(G)
                    else:
                        G = nadya.getGroup(op.param1)
#                        ginfo = nadya.getGroup(op.param1)
                        nadya.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        nadya.updateGroup(G)
                        invsend = 0
                        Ticket = nadya.reissueGroupTicket(op.param1)
                        nadya.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = nadya.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        nadya.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        nadya.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#-------------------------------------------------------------------------------[ki2MID kiMID]
                elif op.param3 in ki2MID:
                    if op.param2 in kiMID:
                        G = ki.getGroup(op.param1)
#                        ginfo = ki.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ki.updateGroup(G)
                        invsend = 0
                        Ticket = ki.reissueGroupTicket(op.param1)
                        nadya.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki.updateGroup(G)
                    else:
                        G = ki.getGroup(op.param1)
#                        ginfo = ki.getGroup(op.param1)
                        ki.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ki.updateGroup(G)
                        invsend = 0
                        Ticket = ki.reissueGroupTicket(op.param1)
                        nadya.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#-------------------------------------------------------------------------------[ki2MID ki3MID]
                elif op.param3 in ki2MID:
                    if op.param2 in ki3MID:
                        G = ki3.getGroup(op.param1)
#                        ginfo = ki3.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ki3.updateGroup(G)
                        invsend = 0
                        Ticket = ki3.reissueGroupTicket(op.param1)
                        nadya.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki3.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki3.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki3.updateGroup(G)
                    else:
                        G = ki3.getGroup(op.param1)
#                        ginfo = ki3.getGroup(op.param1)
                        ki3.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ki3.updateGroup(G)
                        invsend = 0
                        Ticket = ki3.reissueGroupTicket(op.param1)
                        nadya.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki3.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki3.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki3.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#-------------------------------------------------------------------------------[ki2MID ki4MID]
                elif op.param3 in ki2MID:
                    if op.param2 in ki4MID:
                        G = ki4.getGroup(op.param1)
#                        ginfo = ki4.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ki4.updateGroup(G)
                        invsend = 0
                        Ticket = ki4.reissueGroupTicket(op.param1)
                        nadya.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki4.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki4.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki4.updateGroup(G)
                    else:
                        G = ki4.getGroup(op.param1)
#                        ginfo = ki4.getGroup(op.param1)
                        ki4.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ki4.updateGroup(G)
                        invsend = 0
                        Ticket = ki4.reissueGroupTicket(op.param1)
                        nadya.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki4.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki4.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki4.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#===============================================================================[ki3MID nadyaMID]
                if op.param3 in ki3MID:
                    if op.param2 in nadyaMID:
                        G = nadya.getGroup(op.param1)
#                        ginfo = nadya.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        nadya.updateGroup(G)
                        invsend = 0
                        Ticket = nadya.reissueGroupTicket(op.param1)
                        nadya.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = nadya.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        nadya.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        nadya.updateGroup(G)
                    else:
                        G = nadya.getGroup(op.param1)
#                        ginfo = nadya.getGroup(op.param1)
                        nadya.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        nadya.updateGroup(G)
                        invsend = 0
                        Ticket = nadya.reissueGroupTicket(op.param1)
                        nadya.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = nadya.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        nadya.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        nadya.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#-------------------------------------------------------------------------------[ki3MID kiMID]
                elif op.param3 in ki3MID:
                    if op.param2 in kiMID:
                        G = ki.getGroup(op.param1)
#                        ginfo = ki.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ki.updateGroup(G)
                        invsend = 0
                        Ticket = ki.reissueGroupTicket(op.param1)
                        nadya.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki.updateGroup(G)
                    else:
                        G = ki.getGroup(op.param1)
#                        ginfo = ki.getGroup(op.param1)
                        ki.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ki.updateGroup(G)
                        invsend = 0
                        Ticket = ki.reissueGroupTicket(op.param1)
                        nadya.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#-------------------------------------------------------------------------------[ki3MID ki2MID]
                elif op.param3 in ki3MID:
                    if op.param2 in ki2MID:
                        G = ki2.getGroup(op.param1)
#                        ginfo = ki2.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ki2.updateGroup(G)
                        invsend = 0
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        nadya.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki2.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki2.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki2.updateGroup(G)
                    else:
                        G = ki2.getGroup(op.param1)
#                        ginfo = ki2.getGroup(op.param1)
                        ki2.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ki2.updateGroup(G)
                        invsend = 0
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        nadya.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki2.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki2.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki2.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#-------------------------------------------------------------------------------[ki3MID ki4MID]
                elif op.param3 in ki3MID:
                    if op.param2 in ki4MID:
                        G = ki4.getGroup(op.param1)
#                        ginfo = ki4.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ki4.updateGroup(G)
                        invsend = 0
                        Ticket = ki4.reissueGroupTicket(op.param1)
                        nadya.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki4.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki4.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki4.updateGroup(G)
                    else:
                        G = ki4.getGroup(op.param1)
#                        ginfo = ki4.getGroup(op.param1)
                        ki4.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ki4.updateGroup(G)
                        invsend = 0
                        Ticket = ki4.reissueGroupTicket(op.param1)
                        nadya.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki4.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki4.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki4.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#===============================================================================[ki4MID nadyaMID]
                if op.param3 in ki4MID:
                    if op.param2 in nadyaMID:
                        G = nadya.getGroup(op.param1)
#                        ginfo = nadya.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        nadya.updateGroup(G)
                        invsend = 0
                        Ticket = nadya.reissueGroupTicket(op.param1)
                        nadya.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = nadya.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        nadya.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        nadya.updateGroup(G)
                    else:
                        G = nadya.getGroup(op.param1)
#                        ginfo = nadya.getGroup(op.param1)
                        nadya.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        nadya.updateGroup(G)
                        invsend = 0
                        Ticket = nadya.reissueGroupTicket(op.param1)
                        nadya.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = nadya.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        nadya.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        nadya.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#-------------------------------------------------------------------------------[ki4MID kiMID]
                elif op.param3 in ki4MID:
                    if op.param2 in kiMID:
                        G = ki.getGroup(op.param1)
#                        ginfo = ki.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ki.updateGroup(G)
                        invsend = 0
                        Ticket = ki.reissueGroupTicket(op.param1)
                        nadya.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki.updateGroup(G)
                    else:
                        G = ki.getGroup(op.param1)
#                        ginfo = ki.getGroup(op.param1)
                        ki.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ki.updateGroup(G)
                        invsend = 0
                        Ticket = ki.reissueGroupTicket(op.param1)
                        nadya.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#-------------------------------------------------------------------------------[ki4MID ki2MID]
                elif op.param3 in ki4MID:
                    if op.param2 in ki2MID:
                        G = ki2.getGroup(op.param1)
#                        ginfo = ki2.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ki2.updateGroup(G)
                        invsend = 0
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        nadya.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki2.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki2.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki2.updateGroup(G)
                    else:
                        G = ki2.getGroup(op.param1)
#                        ginfo = ki2.getGroup(op.param1)
                        ki2.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ki2.updateGroup(G)
                        invsend = 0
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        nadya.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki2.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki2.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki2.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#-------------------------------------------------------------------------------[ki4MID ki3MID]
                elif op.param3 in ki4MID:
                    if op.param2 in ki3MID:
                        G = ki3.getGroup(op.param1)
#                        ginfo = ki3.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ki3.updateGroup(G)
                        invsend = 0
                        Ticket = ki3.reissueGroupTicket(op.param1)
                        nadya.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki3.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki3.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki3.updateGroup(G)
                    else:
                        G = ki3.getGroup(op.param1)
#                        ginfo = ki3.getGroup(op.param1)
                        ki3.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ki3.updateGroup(G)
                        invsend = 0
                        Ticket = ki3.reissueGroupTicket(op.param1)
                        nadya.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki3.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki3.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki3.updateGroup(G)
                        settings["blacklist"][op.param2] = True
                        
                elif op.param2 not in Bots:
                    if op.param2 in admin:
                        pass
                    elif settings["protect"] == True:
                        settings["blacklist"][op.param2] = True
                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                        random.choice(KAC).sendText(op.param1,"Don't Play bro...!")
                        
                else:
                    pass
            except:
                pass
#==============================================================================#
        if op.type == 13:
            if op.param2 not in Bots:
                if op.param2 in admin:
                    pass
                elif settings["inviteprotect"] == True:
                    settings["blacklist"][op.param2] = True
                    random.choice(KAC).cancelGroupInvitation(op.param1,[op.param3])
                    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                    if op.param2 not in Bots:
                        if op.param2 in admin:
                            pass
                        elif settings["cancelprotect"] == True:
                            settings["blacklist"][op.param2] = True
                            random.choice(KAC).cancelGroupInvitation(op.param1,[op.param3])	
#-------------------------------------------------------------------------------
        if op.type == 11:
            if op.param2 not in Bots:
                if op.param2 in admin and Bots and Owner:
                    pass
                elif settings["qrprotect"] == True:
                    settings["blacklist"][op.param2] = True
                    G = ki.getGroup(op.param1)
                    G.preventedJoinByTicket = True
                    ki.updateGroup(G)
                    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                else:
                    nadya.sendMessage(op.param1,"Qr under protect")
            else:
                nadya.sendMessage(op.param1,"")
#==============================================================================#
        if op.type == 55:
            print ("[ 55 ] NOTIFIED READ MESSAGE")
            if op.param1 in read["readPoint"]:
                _name = nadya.getContact(op.param2).displayName
                tz = pytz.timezone("Asia/Jakarta")
                timeNow = datetime.now(tz=tz)
                timeHours = datetime.strftime(timeNow," (%H:%M)")
                read["readMember"][op.param1][op.param2] = str(_name) + str(timeHours)
        backupData()
    except Exception as error:
        logError(error)
#==============================================================================#
        if op.type == 26:
            msg = op.message
            if text.lower() == '/ti/g/':    
                if settings["autoJoinTicket"] == True:
                    link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                    links = link_re.findall(text)
                    n_links = []
                    for l in links:
                        if l not in n_links:
                            n_links.append(l)
                    for ticket_id in n_links:
                        group = nadya.findGroupByTicket(ticket_id)
                        nadya.acceptGroupInvitationByTicket(group.id,ticket_id)
                        nadya.sendMessage(to, "Berhasil masuk ke group %s" % str(group.name)) 
                        
        if op.type == 26:
            print ("[ 26 ] RECEIVE MESSAGE")
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != nadya.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
                if settings["autoRead"] == True:
                    nadya.sendChatChecked(to, msg_id)
                if to in read["readPoint"]:
                    if sender not in read["ROM"][to]:
                        read["ROM"][to][sender] = True
                if sender in settings["mimic"]["target"] and settings["mimic"]["status"] == True and settings["mimic"]["target"][sender] == True:
                    text = msg.text
                    if text is not None:
                        nadya.sendMessage(msg.to,text)
                if msg.contentType == 0 and sender not in nadyaMID and msg.toType == 2:
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if nadyaMID in mention["M"]:
                                if settings["detectMention"] == True:
                                    contact = nadya.getContact(sender)
                                    nadya.sendMessage(to, "sundala nu")
                                    sendMessageWithMention(to, contact.mid)
                                break
                        
    except Exception as error:
        logError(error)
#==============================================================================#
# Auto join if BOT invited to group
def NOTIFIED_INVITE_INTO_GROUP(op):
    try:
        nadya.acceptGroupInvitation(op.param1)
        ki.acceptGroupInvitation(op.param1)
        ki2.acceptGroupInvitation(op.param1)
        ki3.acceptGroupInvitation(op.param1)
        ki4.acceptGroupInvitation(op.param1)
    except Exception as e:
        nadya.log("[NOTIFIED_INVITE_INTO_GROUP] ERROR : " + str(e))
# Auto kick if BOT out to group
def NOTIFIED_KICKOUT_FROM_GROUP(op):
    try:
        if op.param2 not in Bots:
            random.choice(KAC).kickoutFromGroup(op.param1,op.param2)
        else:
            pass
    except Exception as e:
        nadya.log("[NOTIFIED_KICKOUT_FROM_GROUP] ERROR : " + str(e))

while True:
    try:
        ops = oepoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                lineBot(op)
                oepoll.setRevision(op.revision)
    except Exception as e:
        logError(e)       
