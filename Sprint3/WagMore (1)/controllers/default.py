from datetime import datetime
import datetime
import maskingpersonality
import matchTest
import urllib2
import requests
import json
from random import randint

def noMoney():
    return dict()

def buyDogBone():
    if db(db.profile.id==auth.user.id).select(db.profile.commonPawCoin).first().commonPawCoin >= 5:
        db(db.profile.id==auth.user.id).update(commonPawCoin = db.profile.commonPawCoin-5)
        db(db.profile.id==auth.user.id).update(dogBone = db.profile.dogBone+1)
        redirect(URL("shop"))
    else:
        redirect(URL("noMoney"))
    return dict()
def buyTeddyBear():
    if db(db.profile.id==auth.user.id).select(db.profile.commonPawCoin).first().commonPawCoin >= 10 and db(db.profile.id==auth.user.id).select(db.profile.uncommonPawCoin).first().uncommonPawCoin >= 5 and db(db.profile.id==auth.user.id).select(db.profile.rarePawCoin).first().rarePawCoin >= 3:
        db(db.profile.id==auth.user.id).update(commonPawCoin = db.profile.commonPawCoin-10)
        db(db.profile.id==auth.user.id).update(uncommonPawCoin = db.profile.uncommonPawCoin-5)
        db(db.profile.id==auth.user.id).update(rarePawCoin = db.profile.rarePawCoin-3)
        db(db.profile.id==auth.user.id).update(teddyBear = db.profile.teddyBear+1)
        redirect(URL("shop"))
    else:
        redirect(URL("noMoney"))
    return dict()
def buyBaconBone():
    if db(db.profile.id==auth.user.id).select(db.profile.commonPawCoin).first().commonPawCoin >= 5 and db(db.profile.id==auth.user.id).select(db.profile.uncommonPawCoin).first().uncommonPawCoin >= 1:
        db(db.profile.id==auth.user.id).update(commonPawCoin = db.profile.commonPawCoin-5)
        db(db.profile.id==auth.user.id).update(uncommonPawCoin = db.profile.uncommonPawCoin-1)
        db(db.profile.id==auth.user.id).update(rarePawCoin = db.profile.rarePawCoin-0)
        db(db.profile.id==auth.user.id).update(dogBoneBacon = db.profile.dogBoneBacon+1)
        redirect(URL("shop"))
    else:
        redirect(URL("noMoney"))
    return dict()
def buyCheeseBone():
    if db(db.profile.id==auth.user.id).select(db.profile.commonPawCoin).first().commonPawCoin >= 5 and db(db.profile.id==auth.user.id).select(db.profile.uncommonPawCoin).first().uncommonPawCoin >= 1:
        db(db.profile.id==auth.user.id).update(commonPawCoin = db.profile.commonPawCoin-5)
        db(db.profile.id==auth.user.id).update(uncommonPawCoin = db.profile.uncommonPawCoin-1)
        db(db.profile.id==auth.user.id).update(rarePawCoin = db.profile.rarePawCoin-0)
        db(db.profile.id==auth.user.id).update(dogBoneCheese = db.profile.dogBoneCheese+1)
        redirect(URL("shop"))
    else:
        redirect(URL("noMoney"))
    return dict()
def buydogHat1():
    if db(db.profile.id==auth.user.id).select(db.profile.commonPawCoin).first().commonPawCoin >= 5 and db(db.profile.id==auth.user.id).select(db.profile.uncommonPawCoin).first().uncommonPawCoin >= 1 and db(db.profile.id==auth.user.id).select(db.profile.rarePawCoin).first().rarePawCoin >= 1:
        db(db.profile.id==auth.user.id).update(commonPawCoin = db.profile.commonPawCoin-5)
        db(db.profile.id==auth.user.id).update(uncommonPawCoin = db.profile.uncommonPawCoin-1)
        db(db.profile.id==auth.user.id).update(rarePawCoin = db.profile.rarePawCoin-1)
        db(db.profile.id==auth.user.id).update(dogHat = db.profile.dogHat+1)
        redirect(URL("shop"))
    else:
        redirect(URL("noMoney"))
    return dict()
def buydogHat2():
    if db(db.profile.id==auth.user.id).select(db.profile.commonPawCoin).first().commonPawCoin >= 5 and db(db.profile.id==auth.user.id).select(db.profile.uncommonPawCoin).first().uncommonPawCoin >= 1 and db(db.profile.id==auth.user.id).select(db.profile.rarePawCoin).first().rarePawCoin >= 1:
        db(db.profile.id==auth.user.id).update(commonPawCoin = db.profile.commonPawCoin-5)
        db(db.profile.id==auth.user.id).update(uncommonPawCoin = db.profile.uncommonPawCoin-1)
        db(db.profile.id==auth.user.id).update(rarePawCoin = db.profile.rarePawCoin-1)
        db(db.profile.id==auth.user.id).update(dogHat2 = db.profile.dogHat2+1)
        redirect(URL("shop"))
    else:
        redirect(URL("noMoney"))
    return dict()
def buydogHouse():
    if db(db.profile.id==auth.user.id).select(db.profile.commonPawCoin).first().commonPawCoin >= 100 and db(db.profile.id==auth.user.id).select(db.profile.uncommonPawCoin).first().uncommonPawCoin >= 50 and db(db.profile.id==auth.user.id).select(db.profile.rarePawCoin).first().rarePawCoin >= 30:
        db(db.profile.id==auth.user.id).update(commonPawCoin = db.profile.commonPawCoin-100)
        db(db.profile.id==auth.user.id).update(uncommonPawCoin = db.profile.uncommonPawCoin-50)
        db(db.profile.id==auth.user.id).update(rarePawCoin = db.profile.rarePawCoin-30)
        db(db.profile.id==auth.user.id).update(dogHouseUltimate = db.profile.dogHouseUltimate+1)
        redirect(URL("shop"))
    else:
        redirect(URL("noMoney"))
    return dict()
def buyDuck():
    if db(db.profile.id==auth.user.id).select(db.profile.uncommonPawCoin).first().uncommonPawCoin >= 6 and db(db.profile.id==auth.user.id).select(db.profile.rarePawCoin).first().rarePawCoin >= 2:
        db(db.profile.id==auth.user.id).update(commonPawCoin = db.profile.commonPawCoin-0)
        db(db.profile.id==auth.user.id).update(uncommonPawCoin = db.profile.uncommonPawCoin-6)
        db(db.profile.id==auth.user.id).update(rarePawCoin = db.profile.rarePawCoin-2)
        db(db.profile.id==auth.user.id).update(rubberDuck = db.profile.rubberDuck+1)
        redirect(URL("shop"))
    else:
        redirect(URL("noMoney"))
    return dict()
def buyBall():
    if db(db.profile.id==auth.user.id).select(db.profile.uncommonPawCoin).first().uncommonPawCoin >= 7 and db(db.profile.id==auth.user.id).select(db.profile.rarePawCoin).first().rarePawCoin >= 3:
        db(db.profile.id==auth.user.id).update(commonPawCoin = db.profile.commonPawCoin-0)
        db(db.profile.id==auth.user.id).update(uncommonPawCoin = db.profile.uncommonPawCoin-7)
        db(db.profile.id==auth.user.id).update(rarePawCoin = db.profile.rarePawCoin-3)
        db(db.profile.id==auth.user.id).update(squeakyBall = db.profile.squeakyBall+1)
        redirect(URL("shop"))
    else:
        redirect(URL("noMoney"))
    return dict()

def bitMask(form, profileMask):
    if len(profileMask.select()[0].interestMask)>30:
        return
    for value in form:
        previousMask=profileMask.select()[0].interestMask
        if value==False:
            profileMask.update(interestMask=previousMask+'0')
        if value==True:
            profileMask.update(interestMask=previousMask+'1')
    return


def checkProfileCompletion(profile):
    if(db(db.images.id==profile.id).count()==0):
        print("User with id number %d hasn't completed their profile pictures"%(profile.id))
        redirect(URL('createProfile2'))
    if(db(db.interestFood.id==profile.id).count()==0):
        redirect(URL('createProfile_interests',args="Remake"))
    if(db(db.interestActivities.id==profile.id).count()==0):
        redirect(URL('createProfile_interests',args="Remake"))
    if(db(db.interestSports.id==profile.id).count()==0):
        redirect(URL('createProfile_interests',args="Remake"))
    if(db(db.interestHobbies.id==profile.id).count()==0):
        redirect(URL('createProfile_interests',args="Remake"))
    if(db(db.interestPlaces.id==profile.id).count()==0):
        redirect(URL('createProfile_interests',args="Remake"))
    if(db(db.question1.id==profile.id).count()==0):
        redirect(URL('questions1',args="Remake"))
    if(db(db.question2.id==profile.id).count()==0):
        redirect(URL('questions2',args="Remake"))
    if(db(db.question3.id==profile.id).count()==0):
        redirect(URL('questions3',args="Remake"))
    if(db(db.question4.id==profile.id).count()==0):
        redirect(URL('questions4',args="Remake"))
    return

@auth.requires_login()
def changeBio():
    profileID=request.args(0, cast=int)
    if(profileID!=auth.user.id):
        redirect(URL('profiles'))
    profile = db.profile(profileID) or redirect(URL('index'))
    return dict(profile=profile)

@auth.requires_login()
def updateBio():
    print(request.args(0))
    profile=db(db.profile.id==request.args(0))
    newBio=request.vars.newBio
    newDogsBio=request.vars.newDogsBio
    if len(newBio)!=0:
        profile.update(bio=newBio)
    if len(newDogsBio)!=0:
        profile.update(dogBio=newDogsBio)
    redirect(URL('default', 'show', args=[auth.user.id,-1]))

def cart():
    return dict()

@auth.requires_login()
def changeDog():
    if(request.args(0,cast=int)!=auth.user.id):
        redirect(URL('profiles'))
    images = db().select(db.images.ALL)
    images = db.images[request.args(0,cast=int)]
    if not (images and images.id == auth.user_id):
        redirect(URL('index'))
    form = SQLFORM(db.images, images,
                   deletable=True,
                   )
    if form.process(keepvalues=True).accepted:
        response.flash = 'post accepted'
        redirect(URL('default', 'show', args=[auth.user.id,-1]))

    return dict(form=form, images=images)

def updateLocation():
    nurl = 'https://freegeoip.net/json'
    r = requests.get(nurl)
    j = json.loads(r.text)
    location_city = j['city']
    db(db.profile.id==auth.user.id).update(locationLong=j['longitude'],locationLat=j['latitude'], city=j['city'])

@auth.requires_login()
def matchReload():
    print("Calculating your matches! Please wait...")
    db.profile.id.default = auth.user.id
    profile1 = db(db.profile.id == auth.user.id)
    profiles = db(db.profile.id != auth.user.id)
    ##db(db.matchTable.idFromMatch==auth.user.id).delete()
    if (len(profile1.select()[0].locationLat)==0 or len(profile1.select()[0].locationLong)==0):
        response.flash="We need your location to find matches!"
        updateLocation()
        return;
    for profile in profiles.select():
        profile2 = db(db.profile.id == profile.id)
        # if matchLocat > 25.0:
        #    print("Too far away! Person won't show up in matches!")
        if matchTest.lookingforConstraint(profile1, profile2) == True:
            print("Match with same interest")
        else:
            print("Not a match")
        matchPercen = matchTest.testAdven(profile1, profile2)
        distance=matchTest.calcDistance(profile1, profile2)
        if (matchPercen > 39 and db((db.matchTable.idFromMatch == auth.user.id) & (db.matchTable.idToMatch ==
            profile2.select()[0].id)).count() == 0):
            db.matchTable.insert(idToMatch=profile2.select()[0].id, percentage=matchPercen, idFromMatch=auth.user.id,
                                 images_id=profile2.select()[0].id,distance=distance)


@auth.requires_login()
def profiles():
    dailyReward=""
    #forRewards = db(db.profile.id==auth.user.id)
    #forRewards2 = db.profile
    form = SQLFORM(db.profile)
    #profiles = db(db.profile.id>0 and matches(db.matchTable.idToMatch ==db.profile.id).count()>0).select()
    if(db(db.profile.id==auth.user.id).count()==0):
        redirect(URL('mainPage'))
    checkProfileCompletion(db(db.profile.id == auth.user.id).select()[0])
    if (request.args(0)=="ReloadMatches"):
        updateLocation()
        matchReload()
        showBlocked=False
    elif request.args(0)=="blocked":
        showBlocked=True
    else:
        showBlocked=False
    todayDate = datetime.datetime.now()
    logindate = db(db.profile.id == auth.user.id).select(db.profile.dateLoggedin)
    lastlogindate = db(db.profile.id == auth.user.id).select(db.profile.dateLastLoggedIn)
    db(db.profile.id == auth.user.id).update(dateLastLoggedIn = db.profile.dateLoggedin)
    db(db.profile.id == auth.user.id).update(dateLoggedin = todayDate)
    if logindate > lastlogindate:
        randNum = randint(1,100)
        if (randNum >= 1 and randNum <= 5):
            db(db.profile.id==auth.user.id).update(commonPawCoin = db.profile.commonPawCoin+1)
            dailyReward = dailyReward + "Thank you for logging in! Your daily reward is 1x Common Paw Coin!"
        elif (randNum >= 6 and randNum <= 10):
            db(db.profile.id==auth.user.id).update(commonPawCoin = db.profile.commonPawCoin+2)
            dailyReward = dailyReward +"Thank you for logging in! Your daily reward is 2x Common Paw Coin!"
        elif (randNum >= 11 and randNum <= 15):
            db(db.profile.id==auth.user.id).update(commonPawCoin = db.profile.commonPawCoin+3)
            dailyReward = dailyReward +"Thank you for logging in! Your daily reward is 3x Common Paw Coin!"
        elif (randNum >= 16 and randNum <= 20):
            db(db.profile.id==auth.user.id).update(commonPawCoin = db.profile.commonPawCoin+4)
            dailyReward = dailyReward +"Thank you for logging in! Your daily reward is 4x Common Paw Coin!"
        elif (randNum >= 21 and randNum <= 25):
            db(db.profile.id==auth.user.id).update(uncommonPawCoin = db.profile.uncommonPawCoin+1)
            dailyReward = dailyReward +"Thank you for logging in! Your daily reward is 1x Uncommon Paw Coin!"
        elif (randNum >= 26 and randNum <= 30):
            db(db.profile.id==auth.user.id).update(commonPawCoin = db.profile.commonPawCoin+1)
            db(db.profile.id==auth.user.id).update(uncommonPawCoin = db.profile.uncommonPawCoin+1)
            dailyReward = dailyReward +"Thank you for logging in! Your daily reward is 1x Common Paw Coin & 1x Uncommon Paw Coin!"
        elif (randNum >= 31 and randNum <= 35):
            db(db.profile.id==auth.user.id).update(commonPawCoin = db.profile.commonPawCoin+2)
            db(db.profile.id==auth.user.id).update(uncommonPawCoin = db.profile.uncommonPawCoin+1)
            dailyReward = dailyReward +"Thank you for logging in! Your daily reward is 2x Common Paw Coin & 1x Uncommon Paw Coin!"
        elif (randNum >= 36 and randNum <= 40):
            db(db.profile.id==auth.user.id).update(commonPawCoin = db.profile.commonPawCoin+2)
            db(db.profile.id==auth.user.id).update(uncommonPawCoin = db.profile.uncommonPawCoin+2)
            dailyReward = dailyReward +"Thank you for logging in! Your daily reward is 2x Common Paw Coin & 2x Uncommon Paw Coin!"
        elif (randNum >= 41 and randNum <= 45):
            db(db.profile.id==auth.user.id).update(commonPawCoin = db.profile.commonPawCoin+3)
            db(db.profile.id==auth.user.id).update(uncommonPawCoin = db.profile.uncommonPawCoin+3)
            dailyReward = dailyReward +"Thank you for logging in! Your daily reward is 3x Common Paw Coin & 3x Uncommon Paw Coin!"
        elif (randNum >= 46 and randNum <= 50):
            db(db.profile.id==auth.user.id).update(rarePawCoin = db.profile.rarePawCoin+3)
            dailyReward = dailyReward +"Thank you for logging in! Your daily reward is 1x Rare Paw Coin!"
        elif (randNum >= 51 and randNum <= 55):
            db(db.profile.id==auth.user.id).update(uncommonPawCoin = db.profile.uncommonPawCoin+3)
            db(db.profile.id==auth.user.id).update(rarePawCoin = db.profile.rarePawCoin+1)
            dailyReward = dailyReward +"Thank you for logging in! Your daily reward is 3x Uncommon Paw Coin & 1x Rare Paw Coin!"
        elif (randNum >= 56 and randNum <= 60):
            db(db.profile.id==auth.user.id).update(commonPawCoin = db.profile.commonPawCoin+5)
            dailyReward = dailyReward +"Thank you for logging in! Your daily reward is 5x Common Paw Coin!"
        elif (randNum >= 61 and randNum <= 65):
            db(db.profile.id==auth.user.id).update(uncommonPawCoin = db.profile.uncommonPawCoin+5)
            dailyReward = dailyReward +"Thank you for logging in! Your daily reward is 5x Uncommon Paw Coin!"
        elif (randNum >= 66 and randNum <= 70):
            db(db.profile.id==auth.user.id).update(commonPawCoin = db.profile.commonPawCoin+6)
            dailyReward = dailyReward +"Thank you for logging in! Your daily reward is 6x Common Paw Coin!"
        elif (randNum >= 71 and randNum <= 75):
            db(db.profile.id==auth.user.id).update(uncommonPawCoin = db.profile.uncommonPawCoin+6)
            dailyReward = dailyReward +"Thank you for logging in! Your daily reward is 6x Uncommon Paw Coin!"
        elif (randNum >= 76 and randNum <= 80):
            db(db.profile.id==auth.user.id).update(uncommonPawCoin = db.profile.uncommonPawCoin+4)
            db(db.profile.id==auth.user.id).update(rarePawCoin = db.profile.rarePawCoin+4)
            dailyReward = dailyReward +"Thank you for logging in! Your daily reward is 4x Uncommon Paw Coin & 4x Rare Paw Coin!"
        elif (randNum >= 81 and randNum <= 85):
            db(db.profile.id==auth.user.id).update(rarePawCoin = db.profile.rarePawCoin+7)
            dailyReward = dailyReward +"Thank you for logging in! Your daily reward is 7x Rare Paw Coin!"
        elif (randNum >= 86 and randNum <= 90):
            db(db.profile.id==auth.user.id).update(commonPawCoin = db.profile.commonPawCoin+9)
            db(db.profile.id==auth.user.id).update(uncommonPawCoin = db.profile.uncommonPawCoin+9)
            dailyReward = dailyReward +"Thank you for logging in! Your daily reward is 9x Common Paw Coin & 9x Uncommon Paw Coin!"
        elif (randNum >= 91 and randNum <= 95):
            db(db.profile.id==auth.user.id).update(commonPawCoin = db.profile.commonPawCoin+11)
            db(db.profile.id==auth.user.id).update(uncommonPawCoin = db.profile.uncommonPawCoin+11)
            dailyReward = dailyReward +"Thank you for logging in! Your daily reward is 11x Common Paw Coin & 11x Uncommon Paw Coin!"
        elif (randNum >= 96 and randNum <= 99):
            db(db.profile.id==auth.user.id).update(rarePawCoin = db.profile.rarePawCoin+7)
            dailyReward = dailyReward +"Thank you for logging in! Your daily reward is 8x Rare Paw Coin!"
        elif (randNum == 100):
            db(db.profile.id==auth.user.id).update(rarePawCoin = db.profile.rarePawCoin+10)
            dailyReward = dailyReward +"Thank you for logging in! Your daily reward is 10x Rare Paw Coin!"
    matches = db(db.matchTable.idFromMatch == auth.user.id)
    commonCoin = db(db.profile.id==auth.user.id).select(db.profile.commonPawCoin).first().commonPawCoin
    uncommonCoin = db(db.profile.id==auth.user.id).select(db.profile.uncommonPawCoin).first().uncommonPawCoin
    rareCoin = db(db.profile.id==auth.user.id).select(db.profile.rarePawCoin).first().rarePawCoin
    numberOfMatches=matches.count()
    numberOfBlocked=matches(db.matchTable.blocked==True).count()
    matches=matches.select(db.matchTable.ALL, orderby=~db.matchTable.percentage)
    response.flash=''
    return dict(form=form, commonCoin=commonCoin, uncommonCoin=uncommonCoin, rareCoin=rareCoin, matches=matches, numberOfMatches=numberOfMatches, numberOfBlocked=numberOfBlocked, showBlocked=showBlocked, dailyReward=dailyReward)

def getMessages():
    matches = db(db.matchTable.idFromMatch == auth.user.id)  # all the user's matches
    matches = matches.select(db.matchTable.ALL, orderby=~db.matchTable.percentage)
    match_id = [] # holds match id (matchTable.id)
    messages_count = [] # holds # of messages from user's match
    type = request.args[0] # to determine if return unread msgs or read msgs; args is either "read" or "unread"
    match_profile = db(db.profile.id == -1).select() # initializing the variable; will hold user's matches who sent the user msgs

    for match in matches:
        otherMatch = db((db.matchTable.idFromMatch == match.idToMatch) & (db.matchTable.idToMatch == auth.user.id)) # finds the reverse matches eg, 34, 33; finds 33,34
        if (otherMatch.count() > 0): # if reverse match exists, get that id
            otherMatchID = db((db.matchTable.idFromMatch == match.idToMatch) & (db.matchTable.idToMatch == auth.user.id)).select()[0].id
        else:
            otherMatchID = -1
        if(type == "unread"): # get unread messages
            print("++++++++++++++++++\nlisting all unread msgs with user's match " + str(db(db.profile.id == match.idToMatch).select()[0].name) + "...")
            unread_messages = db(((db.post.item_id == match.id) | (db.post.item_id == otherMatchID)) & (
                db.post.fromid != auth.user.id) & (db.post.opened == False)).count() #holds # of messages that was recieved by user's match? and has not opened it
            print("there is/are: " + str(unread_messages) + " unread messages from " + str(db(db.profile.id == match.idToMatch).select()[0].name))
            if unread_messages > 0:
                print("adding to list...")
                match_profile = match_profile & db(db.profile.id == match.idToMatch).select()
                match_id.append(match.id)
                messages_count.append(unread_messages)
        elif (type == "read"): # or get read messages
            print("===================\nlisting all read msgs with user's match " + str(db(db.profile.id == match.idToMatch).select()[0].name) + "...")
            read_messages = db(((db.post.item_id == match.id) | (db.post.item_id == otherMatchID)) & (
            db.post.fromid != auth.user.id) & (db.post.opened == True)).count()
            print("there is/are: " + str(read_messages) + " read messages from " + str(db(db.profile.id == match.idToMatch).select()[0].name))
            if read_messages >= 1:
                print("adding to list...")
                match_profile = match_profile & db(db.profile.id == match.idToMatch).select()
                match_id.append(match.id)
                messages_count.append(read_messages)
    return ''.join([DIV(k.name," (" + str(messages_count[i]) + ") ",
                        _onclick="window.location = '%s'" % URL('show', args=[k.id, match_id[i]]),
                        _onmouseover="this.style.backgroundColor='yellow',this.style.cursor='pointer'",
                        _onmouseout="this.style.backgroundColor='white'"
                        ).xml() for i,k in enumerate(match_profile)])  # i will be the arr index, k will be the row of data

def unMessages():
    return ""

def blockPerson():
    prevValue=db((db.matchTable.idFromMatch==auth.user.id) & (db.matchTable.idToMatch==request.args(0, cast=int))).select()[0].blocked
    db((db.matchTable.idFromMatch==auth.user.id) & (db.matchTable.idToMatch==request.args(0, cast=int))).update(blocked=not prevValue)
    redirect(URL('profiles'))

def index():
    if auth.is_logged_in():
        redirect(URL('profiles'))
    return dict()

def first():
    return dict()


def second():
    return dict()


def loginpage():
    return dict()


def signuppage():
    return dict()


def signuppage2():
    return dict()


@auth.requires_login()
def createProfile2():
    updateLocation()
    db(db.images.id==auth.user.id).delete()
    db.images.id.default = auth.user.id
    form = SQLFORM(db.images)
    if form.process().accepted:
        response.flash = 'form accepted'
        redirect(URL("createProfile_interests"))
    elif form.errors:
        response.flash = 'form has errors'
    else:
        response.flash = 'please fill out the form'
    return dict(form=form)


@auth.requires_login()
def createProfile_interests():
    db(db.interestFood.id==auth.user.id).delete()
    db.interestFood.id.default = auth.user.id
    form = SQLFORM(db.interestFood)
    if form.process().accepted:
        response.flash = 'form accepted'
        # Modifiying the profile mask
        profileMask = db(db.profile.id == auth.user.id)
        profileMask.update(interestMask='')
        # function in maskModule.py (in the module folder of the application)
        bitMask(form.vars.values(), profileMask)
        if (request.args(0)=="Remake"):
            redirect(URL("createProfile_interest_2",args="Remake"))
        redirect(URL("createProfile_interest_2"))
    return dict(form=form)

@auth.requires_login()
def video():

    if(request.args(0,cast=int)!=auth.user.id):
        redirect(URL('profiles'))
    images = db().select(db.images.ALL)
    images = db.images[request.args(0,cast=int)]
    if not (images and images.id == auth.user_id):
        redirect(URL('index'))
    form = SQLFORM(db.images, images,
                   deletable=True,
                   )

    if form.process(keepvalues=True).accepted:
        response.flash = 'post accepted'
        redirect(URL('default', 'show', args=[auth.user.id,-1]))

    return dict(form=form,images=images)

@auth.requires_login()
def morepictures():
    if(request.args(0,cast=int)!=auth.user.id):
        redirect(URL('profiles'))
    images = db().select(db.images.ALL)
    images = db.images[request.args(0)]
    if not (images and images.id == auth.user_id):
        redirect(URL('index'))
    form = SQLFORM(db.images, images,
                   deletable=True,
                   )
    if form.process(keepvalues=True).accepted:
        response.flash = 'post accepted'
        redirect(URL('default', 'show', args=[auth.user.id,-1]))

    return dict(form=form, images=images)


@auth.requires_login()
def createProfile_interest_2():
    db(db.interestActivities.id==auth.user.id).delete()
    db.interestActivities.id.default = auth.user.id
    form = SQLFORM(db.interestActivities)
    if form.process().accepted:
        response.flash = 'form accepted'
        profileMask = db(db.profile.id == auth.user.id)
        bitMask(form.vars.values(), profileMask)
        if (request.args(0)=="Remake"):
            redirect(URL("createProfile_interest_3",args="Remake"))
        redirect(URL("createProfile_interest_3"))
    return dict(form=form)

@auth.requires_login()
def createProfile_interest_3():
    db(db.interestSports.id==auth.user.id).delete()
    db.interestSports.id.default = auth.user.id
    form = SQLFORM(db.interestSports)
    if form.process().accepted:
        response.flash = 'form accepted'
        profileMask = db(db.profile.id == auth.user.id)
        bitMask(form.vars.values(), profileMask)
        if (request.args(0)=="Remake"):
            redirect(URL("createProfile_interest_4",args="Remake"))
        redirect(URL("createProfile_interest_4"))
    return dict(form=form)

@auth.requires_login()
def createProfile_interest_4():
    db(db.interestHobbies.id==auth.user.id).delete()
    db.interestHobbies.id.default = auth.user.id
    form = SQLFORM(db.interestHobbies)
    if form.process().accepted:
        response.flash = 'form accepted'
        profileMask = db(db.profile.id == auth.user.id)
        bitMask(form.vars.values(), profileMask)
        if (request.args(0)=="Remake"):
            redirect(URL("createProfile_interest_5",args="Remake"))
        redirect(URL("createProfile_interest_5"))
    return dict(form=form)

@auth.requires_login()
def createProfile_interest_5():
    db(db.interestPlaces.id==auth.user.id).delete()
    db.interestPlaces.id.default = auth.user.id
    form = SQLFORM(db.interestPlaces)
    if form.process().accepted:
        response.flash = 'form accepted'
        profileMask = db(db.profile.id == auth.user.id)
        bitMask(form.vars.values(), profileMask)
        if request.args(0)=="Remake":
            redirect(URL("profiles"))
        redirect(URL("questions1"))
    return dict(form=form)



def createProfile_aboutYourself():
    return dict()


def createProfile_confirmation():
    return dict()

@auth.requires_login()
def show():
    profileID=request.args(0, cast=int)
    matchID=request.args(1,cast=int)
    profile = db.profile(profileID) or redirect(URL('index'))
    image = db.images(profileID) or redirect(URL('index'))
    #If match id the user is trying to view its profile

    if(matchID!=-1):

        # If the other person matched already sent youa message, there will be an ID for your message chat already
        testAlready=db((db.matchTable.idFromMatch==profileID) & (db.matchTable.idToMatch==auth.user.id))
        if(testAlready.count()!=0 and db(db.post.item_id==testAlready.select()[0].id).count()!=0):
            matchID=testAlready.select()[0].id
        db.post.item_id.default = matchID
        db.post.author.default = auth.user.first_name
        db.post.fromid.default = auth.user.id
        db.post.toid.default = profileID
        form = SQLFORM(db.post, labels = {'photo':'Send a photo!', 'video':'Send a video!'}, submit_button='Send!')
        if form.process().accepted:
            response.flash = 'Your comment is posted!'
        comments = db(db.post.item_id == matchID).select().sort(lambda p: p.timesent, reverse=True)
        db((db.post.item_id == matchID) & (db.post.fromid!=auth.user.id)).update(opened=True)
        match=db(db.matchTable.id==request.args(1,cast=int)).select()[0]

    else:
        form=None
        comments=[]
        match=None


    mapSource="https://www.google.com/maps/embed/v1/place?key=AIzaSyBuvFgnD0flhVwNGCHXgyjXR5JBN16pSTI&q="+ str(profile.locationLat) + ',' + str(profile.locationLong)

    return dict(profile=profile, images=image, comments=comments, form=form, match=match, mapSource=mapSource,)


@auth.requires_login()
def mainPage():
    if (db(db.profile.id == auth.user.id).count() == 1):
        redirect(URL("index"))
    db.profile.id.default = auth.user.id
    db.profile.name.default = auth.user.first_name + ' ' + auth.user.last_name
    db.profile.locationLong.default = 0
    db.profile.locationLat.default = 0
    form = SQLFORM(db.profile)
    if form.process().accepted:
        response.flash = 'form accepted'
        redirect(URL("createProfile2"))
    elif form.errors:
        response.flash = 'form has errors'
    else:
        response.flash = 'please fill out the form'
    return dict(form=form)


# Page for managing item posts as well as the comments inside of them
@auth.requires_membership('manager')
def manage_users():
    grid = SQLFORM.smartgrid(db.auth_user)
    return dict(grid=grid)


# Page for managing item posts as well as the comments inside of them
@auth.requires_membership('manager')
def manage_profiles():
    grid = SQLFORM.smartgrid(db.profile)
    return dict(grid=grid)


@auth.requires_login()
def questions1():
    db(db.question1.id==auth.user.id).delete()
    db.question1.id.default = auth.user.id
    form = SQLFORM(db.question1)
    if form.process().accepted:
        response.flash = 'form accepted'
        profileMask = db(db.profile.id == auth.user.id)
        maskingpersonality.q1Mask(form.vars.values(), profileMask)
        if (request.args(0)=="Remake"):
            redirect(URL("profiles"))
        redirect(URL("questions2"))
    return dict(form=form)

@auth.requires_login()
def questions2():
    db(db.question2.id==auth.user.id).delete()
    db.question2.id.default = auth.user.id
    form = SQLFORM(db.question2)
    if form.process().accepted:
        response.flash = 'form accepted'
        profileMask = db(db.profile.id == auth.user.id)
        maskingpersonality.q2Mask(form.vars.values(), profileMask)
        if (request.args(0)=="Remake"):
            redirect(URL("profiles"))
        redirect(URL("questions3"))
    return dict(form=form)

@auth.requires_login()
def questions3():
    db(db.question3.id==auth.user.id).delete()
    db.question3.id.default = auth.user.id
    form = SQLFORM(db.question3)
    if form.process().accepted:
        response.flash = 'form accepted'
        profileMask = db(db.profile.id == auth.user.id)
        maskingpersonality.q3Mask(form.vars.values(), profileMask)
        if (request.args(0)=="Remake"):
            redirect(URL("profiles"))
        redirect(URL("questions4"))
    return dict(form=form)

@auth.requires_login()
def questions4():
    db(db.question4.id==auth.user.id).delete()
    db.question4.id.default = auth.user.id
    form = SQLFORM(db.question4)
    if form.process().accepted:
        response.flash = 'form accepted'
        profileMask = db(db.profile.id == auth.user.id)
        maskingpersonality.q4Mask(form.vars.values(), profileMask)
        if (request.args(0)=="Remake"):
            redirect(URL("profiles"))
        redirect(URL("createProfile_confirmation"))
    return dict(form=form)



def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    also notice there is http://..../[app]/appadmin/manage/auth to allow administrator to manage users
    """
    auth.settings.register_next = URL("mainPage")
    auth.settings.login_next = URL("profiles", args="ReloadMatches")

    return dict(form=auth())

@auth.requires_login()
def shop():
    isClicked1 = 0
    commonCoin = db(db.profile.id==auth.user.id).select(db.profile.commonPawCoin).first().commonPawCoin
    commonCoin2 = db(db.profile.id==auth.user.id).select(db.profile.commonPawCoin).first().commonPawCoin
    uncommonCoin = db(db.profile.id==auth.user.id).select(db.profile.uncommonPawCoin).first().uncommonPawCoin
    rareCoin = db(db.profile.id==auth.user.id).select(db.profile.rarePawCoin).first().rarePawCoin

    #totalCosts

    #dogBone
    totalCost1 = 5
    # print(request.vars.count)
    return dict(isClicked1=isClicked1, commonCoin=commonCoin, commonCoin2=commonCoin2, uncommonCoin=uncommonCoin, rareCoin=rareCoin, totalCost1=totalCost1)

@auth.requires_login()
def inventory():
    teddyBear = db(db.profile.id==auth.user.id).select(db.profile.teddyBear).first().teddyBear
    dogHat = db(db.profile.id==auth.user.id).select(db.profile.dogHat).first().dogHat
    dogHat2 = db(db.profile.id==auth.user.id).select(db.profile.dogHat2).first().dogHat2
    dogHouseUltimate = db(db.profile.id==auth.user.id).select(db.profile.dogHouseUltimate).first().dogHouseUltimate
    dogBone = db(db.profile.id==auth.user.id).select(db.profile.dogBone).first().dogBone
    dogBoneBacon = db(db.profile.id==auth.user.id).select(db.profile.dogBoneBacon).first().dogBoneBacon
    dogBoneCheese = db(db.profile.id==auth.user.id).select(db.profile.dogBoneCheese).first().dogBoneCheese
    rubberDuck = db(db.profile.id==auth.user.id).select(db.profile.rubberDuck).first().rubberDuck
    squeakyBall = db(db.profile.id==auth.user.id).select(db.profile.squeakyBall).first().squeakyBall
    commonCoin = db(db.profile.id==auth.user.id).select(db.profile.commonPawCoin).first().commonPawCoin
    rareCoin = db(db.profile.id==auth.user.id).select(db.profile.rarePawCoin).first().rarePawCoin
    uncommonCoin = db(db.profile.id==auth.user.id).select(db.profile.uncommonPawCoin).first().uncommonPawCoin
    return dict(teddyBear = teddyBear, dogHat = dogHat, dogHat2 = dogHat2, dogHouseUltimate = dogHouseUltimate, dogBone = dogBone, dogBoneBacon = dogBoneBacon, dogBoneCheese = dogBoneCheese,
               rubberDuck = rubberDuck, squeakyBall = squeakyBall, commonCoin = commonCoin, rareCoin = rareCoin, uncommonCoin = uncommonCoin)

@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()

#forum
@auth.requires_login()
def forum():
    matches = db(db.matchTable.idFromMatch == auth.user.id) # rows
    idToMatch = []
    for match in matches.select(db.matchTable.idToMatch):
        idToMatch.append(match.idToMatch)
    posts = db().select(db.forum_post.ALL, orderby=~db.forum_post.created_on)
    if(request.args):
        if(request.args[0] == 'top'):
            posts = db().select(db.forum_post.ALL, orderby=~db.forum_post.votes)
    return dict(posts=posts,matches=matches,idToMatch=idToMatch)

def edit_post():
    print(str(request.args(0)))
    if request.args(0) is None:
        form = SQLFORM(db.forum_post,
                 submit_button = 'Add post',
                  )
        if form.process(keepvalues=True).accepted:
         response.flash = 'post accepted'
         redirect(URL('default', 'forum'))
        elif form.errors:
             response.flash = 'please complete your post'
    else:
        forum_post = db.forum_post[request.args(0)]
        if not (forum_post and forum_post.user_id == auth.user_id):
            redirect(URL('forum'))
        form = SQLFORM(db.forum_post, forum_post,
                   showid=False,
                   deletable=True,
                   submit_button='Update your post',
                   )
    if form.process(keepvalues=True).accepted:
        response.flash = 'post accepted'
        redirect(URL('default', 'forum'))
    return dict(form=form)

def post_show():
    post = db.forum_post(request.args(0, cast=int)) or redirect(URL('forum'))
    db.comm.belongs_to.default = post.id
    db.comm.author.default = auth.user.first_name + ' ' + auth.user.last_name
    matches = db(db.matchTable.idFromMatch == auth.user.id) # rows
    idToMatch = []
    for match in matches.select(db.matchTable.idToMatch):
        idToMatch.append(match.idToMatch)
    form = SQLFORM(db.comm)
    if form.process().accepted:
        response.flash = 'your comment is posted'
    comments = db(db.comm.belongs_to == post.id).select()
    return dict(post=post, comments=comments, form=form,idToMatch=idToMatch)

def forum_profile():
    posts = db(db.forum_post.user_id == auth.user.id).select(orderby=db.forum_post.created_on, limitby=(0, 10))
    return dict(posts=posts)

def upvote():
    post = db.forum_post(request.args(0, cast=int))
    user_vote = db((db.votes.voter == auth.user_id) & (db.votes.forum_post == post.id)).select()
    print(user_vote)
    if(user_vote):
        downvoted = user_vote[0].downvote
        upvoted = user_vote[0].upvote
        if (downvoted and upvoted):
            print("")
        else:
            if (upvoted and (not downvoted)):
                updated_votes = post.votes - 1
                post.update_record(votes=updated_votes)
                user_vote[0].update_record(downvote=False)
                user_vote[0].update_record(upvote=False)
            else:
                if ((not upvoted) and (not downvoted)):
                    updated_votes = post.votes + 1
                    post.update_record(votes=updated_votes)
                    user_vote[0].update_record(downvote=False)
                    user_vote[0].update_record(upvote=True)
                else:
                    updated_votes = post.votes + 2
                    post.update_record(votes=updated_votes)
                    user_vote[0].update_record(downvote=False)
                    user_vote[0].update_record(upvote=True)
    else:
        updated_votes = post.votes + 1
        post.update_record(votes=updated_votes)
        db.votes.insert(forum_post=post.id, voter=auth.user_id,upvote=True,downvote=False)
        redirect(URL("forum"))

def downvote():
    post = db.forum_post(request.args(0, cast=int))
    user_vote = db((db.votes.voter == auth.user_id) & (db.votes.forum_post == post.id)).select()
    if (user_vote):
        downvoted = user_vote[0].downvote
        upvoted = user_vote[0].upvote
        if (downvoted and upvoted):
            print("")
        else:
            if (downvoted and (not upvoted)):
                updated_votes = post.votes + 1
                post.update_record(votes=updated_votes)
                user_vote[0].update_record(downvote=False)
                user_vote[0].update_record(upvote=False)
            else:
                if ((not upvoted) and (not downvoted)):
                    updated_votes = post.votes - 1
                    if(updated_votes <= -2):
                        db((db.forum_post.votes <= -2) & (db.forum_post.id == post.id)).delete()
                        db(db.votes.forum_post == post.id).delete()
                        db(db.comm.belongs_to == post.id).delete()
                    else:
                        post.update_record(votes=updated_votes)
                        db.votes.insert(forum_post=post.id, voter=auth.user_id, upvote=False, downvote=True)
                        post.update_record(votes=updated_votes)
                        user_vote[0].update_record(downvote=True)
                        user_vote[0].update_record(upvote=False)
                else:
                    updated_votes = post.votes - 2
                    if(updated_votes <= -2):
                        db((db.forum_post.votes <= -2) & (db.forum_post.id == post.id)).delete()
                        db(db.votes.forum_post == post.id).delete()
                        db(db.comm.belongs_to == post.id).delete()
                    else:
                        post.update_record(votes=updated_votes)
                        db.votes.insert(forum_post=post.id, voter=auth.user_id, upvote=False, downvote=True)
                        post.update_record(votes=updated_votes)
                        user_vote[0].update_record(downvote=True)
                        user_vote[0].update_record(upvote=False)
    else:
        updated_votes = post.votes - 1
        post.update_record(votes=updated_votes)
        if(updated_votes <= -2):
            db((db.forum_post.votes <= -2) & (db.forum_post.id == post.id)).delete()
            db(db.votes.forum_post == post.id).delete()
            db(db.comm.belongs_to == post.id).delete()
        else:
            post.update_record(votes=updated_votes)
            db.votes.insert(forum_post=post.id, voter=auth.user_id, upvote=False, downvote=True)
    redirect(URL("forum"))
