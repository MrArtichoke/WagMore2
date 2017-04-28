def q1Mask(form, profileMask):
    for value in form:
        adveMask=profileMask.select()[0].adventurous
        bubbMask=profileMask.select()[0].bubbly
        confMask=profileMask.select()[0].confident
        consMask=profileMask.select()[0].conservative
        creaMask=profileMask.select()[0].creative
        fierMask=profileMask.select()[0].fiery
        goofMask=profileMask.select()[0].goofy
        inteMask=profileMask.select()[0].intellectual
        intrMask=profileMask.select()[0].introverted
        openMask=profileMask.select()[0].openness
        sponMask=profileMask.select()[0].spontaneity
        
        if adveMask==None:
            adveMask=0
        if bubbMask==None:
            bubbMask=0
        if confMask==None:
            confMask=0
        if consMask==None:
            consMask=0
        if creaMask==None:
            creaMask=0
        if fierMask==None:
            fierMask=0
        if goofMask==None:
            goofMask=0
        if inteMask==None:
            inteMask=0
        if intrMask==None:
            intrMask=0
        if openMask==None:
            openMask=0
        if sponMask==None:
            sponMask=0
        profileMask.update(adventurous=adveMask)
        profileMask.update(bubbly=bubbMask)
        profileMask.update(confident=confMask)
        profileMask.update(conservative=consMask)
        profileMask.update(creative=creaMask)
        profileMask.update(fiery=fierMask)
        profileMask.update(goofy=goofMask)
        profileMask.update(intellectual=inteMask)
        profileMask.update(introverted=intrMask)
        profileMask.update(openness=openMask)
        profileMask.update(spontaneity=sponMask)

        print(value)
        
#       On a Friday night, I am most likely to...:
        if value=='Get ready for a weekend of travel':
            profileMask.update(adventurous=adveMask+2)
            profileMask.update(confident=confMask+1)
            profileMask.update(spontaneity=sponMask+2)
        if value=='Go dancing':
            profileMask.update(bubbly=bubbMask+2)
            profileMask.update(confident=confMask+2)
            profileMask.update(openness=openMask+1)
        if value=='Read a book and stay in (with my pup!)':
            profileMask.update(introverted=intrMask+2)
            profileMask.update(conservative=consMask+2)
            profileMask.update(intellectual=inteMask+1)
        if value=='Something creative (painting, drawing, writing)':
            profileMask.update(creative=creaMask+2)
            profileMask.update(introverted=intrMask+2)
            profileMask.update(intellectual=inteMask+1)
#       My favorite movie genre:
        if value=='Comedy':
            profileMask.update(goofy=goofMask+2)
            profileMask.update(bubbly=bubbMask+2)
            profileMask.update(creative=creaMask+1)
        if value=='Drama':
            profileMask.update(conservative=consMask+2)
            profileMask.update(intellectual=inteMask+2)
            profileMask.update(introverted=intrMask+1)
        if value=='Science fiction/fantasy':
            profileMask.update(adventurous=adveMask+2)
            profileMask.update(creative=creaMask+2)
            profileMask.update(goofy=goofMask+1)
        if value=='Animated':
            profileMask.update(creative=creaMask+2)
            profileMask.update(goofy=goofMask+2)
            profileMask.update(bubbly=bubbMask+1)
#       I enjoy discussions involving philosophy, politics, and/or sciences:
        if value=='Definitely!':
            profileMask.update(intellectual=inteMask+2)
            profileMask.update(fiery=fierMask+2)
            profileMask.update(confident=confMask+1)
        if value=='Mostly':
            profileMask.update(intellectual=inteMask+2)
            profileMask.update(confident=confMask+2)
            profileMask.update(openness=openMask+1)
        if value=='Sometimes':
            profileMask.update(introverted=intrMask+2)
            profileMask.update(conservative=consMask+2)
            profileMask.update(intellectual=inteMask+1)
        if value=='Not really':
            profileMask.update(introverted=intrMask+2)
            profileMask.update(conservative=consMask+2)
            profileMask.update(conservative=consMask+1)
#       If money were no object, out of the following professions, I would be...:
        if value=='A professional clown':
            profileMask.update(goofy=goofMask+2)
            profileMask.update(bubbly=bubbMask+2)
            profileMask.update(openness=openMask+1)
        if value=='A lion tamer':
            profileMask.update(confident=confMask+2)
            profileMask.update(fiery=fierMask+2)
            profileMask.update(adventurous=adveMask+1)
        if value=='A hot-air balloon operator':
            profileMask.update(adventurous=adveMask+2)
            profileMask.update(confident=confMask+2)
            profileMask.update(spontaneity=sponMask+1)
        if value=='An artist':
            profileMask.update(creative=creaMask+2)
            profileMask.update(introverted=intrMask+2)
            profileMask.update(intellectual=inteMask+1)
#       In school, I was mostly interested in...:
        if value=='Art':
            profileMask.update(creative=creaMask+2)
            profileMask.update(introverted=intrMask+2)
            profileMask.update(bubbly=bubbMask+1)
        if value=='Science':
            profileMask.update(intellectual=inteMask+2)
            profileMask.update(confident=confMask+2)
            profileMask.update(conservative=consMask+1)
        if value=='Computer science/math':
            profileMask.update(intellectual=inteMask+2)
            profileMask.update(confident=confMask+2)
            profileMask.update(conservative=consMask+1)
        if value=='Humanities':
            profileMask.update(creative=creaMask+2)
            profileMask.update(openness=openMask+2)
            profileMask.update(introverted=intrMask+1)
    return

def q2Mask(form, profileMask):
    for value in form:
        adveMask=profileMask.select()[0].adventurous
        bubbMask=profileMask.select()[0].bubbly
        confMask=profileMask.select()[0].confident
        consMask=profileMask.select()[0].conservative
        creaMask=profileMask.select()[0].creative
        fierMask=profileMask.select()[0].fiery
        goofMask=profileMask.select()[0].goofy
        inteMask=profileMask.select()[0].intellectual
        intrMask=profileMask.select()[0].introverted
        openMask=profileMask.select()[0].openness
        sponMask=profileMask.select()[0].spontaneity
        
        if adveMask==None:
            adveMask=0
        if bubbMask==None:
            bubbMask=0
        if confMask==None:
            confMask=0
        if consMask==None:
            consMask=0
        if creaMask==None:
            creaMask=0
        if fierMask==None:
            fierMask=0
        if goofMask==None:
            goofMask=0
        if inteMask==None:
            inteMask=0
        if intrMask==None:
            intrMask=0
        if openMask==None:
            openMask=0
        if sponMask==None:
            sponMask=0
        profileMask.update(adventurous=adveMask)
        profileMask.update(bubbly=bubbMask)
        profileMask.update(confident=confMask)
        profileMask.update(conservative=consMask)
        profileMask.update(creative=creaMask)
        profileMask.update(fiery=fierMask)
        profileMask.update(goofy=goofMask)
        profileMask.update(intellectual=inteMask)
        profileMask.update(introverted=intrMask)
        profileMask.update(openness=openMask)
        profileMask.update(spontaneity=sponMask)

        print(value)
        
#       If I could have one superpower, it would be...:
        if value=='To fly':
            profileMask.update(adventurous=adveMask+2)
            profileMask.update(spontaneity=sponMask+2)
            profileMask.update(fiery=fierMask+1)
        if value=='To turn invisible':
            profileMask.update(introverted=intrMask+2)
            profileMask.update(conservative=consMask+2)
            profileMask.update(intellectual=inteMask+1)
        if value=='To read minds':
            profileMask.update(intellectual=inteMask+2)
            profileMask.update(fiery=fierMask+2)
            profileMask.update(introverted=intrMask+1)
        if value=='To talk to animals':
            profileMask.update(bubbly=bubbMask+2)
            profileMask.update(openness=openMask+2)
            profileMask.update(goofy=goofMask+1)
#       When I travel to a foreign country, the first thing I want to do is:
        if value=='Meet locals and practice the languages':
            profileMask.update(openness=openMask+2)
            profileMask.update(confident=confMask+2)
            profileMask.update(spontaneity=sponMask+1)
        if value=='Go to a museum':
            profileMask.update(introverted=intrMask+2)
            profileMask.update(intellectual=inteMask+2)
            profileMask.update(creative=creaMask+1)
        if value=='Try the food and cuisine':
            profileMask.update(adventurous=adveMask+2)
            profileMask.update(openness=openMask+2)
            profileMask.update(conservative=consMask+1)
        if value=='I have not traveled to a foreign country':
            profileMask.update(conservative=consMask+2)
            profileMask.update(introverted=intrMask+2)
            profileMask.update(intellectual=inteMask+1)
#       If my dog could talk, he/she would say I am:
        if value=='Playful':
            profileMask.update(bubbly=bubbMask+2)
            profileMask.update(spontaneity=sponMask+2)
            profileMask.update(openness=openMask+1)
        if value=='Strict':
            profileMask.update(conservative=consMask+2)
            profileMask.update(confident=confMask+2)
            profileMask.update(fiery=fierMask+1)
        if value=='Reserved':
            profileMask.update(introverted=intrMask+2)
            profileMask.update(conservative=consMask+2)
            profileMask.update(intellectual=inteMask+1)
        if value=='Energetic':
            profileMask.update(fiery=fierMask+2)
            profileMask.update(confident=confMask+2)
            profileMask.update(spontaneity=sponMask+1)
#       The fictional character I most identify with from the following is:
        if value=='Charlie Brown':
            profileMask.update(introverted=intrMask+2)
            profileMask.update(conservative=consMask+2)
            profileMask.update(creative=creaMask+1)
        if value=='Buzz Lightyear':
            profileMask.update(confident=confMask+2)
            profileMask.update(fiery=fierMask+2)
            profileMask.update(adventurous=adveMask+1)
        if value=='Mulan':
            profileMask.update(adventurous=adveMask+2)
            profileMask.update(confident=confMask+2)
            profileMask.update(fiery=fierMask+1)
        if value=='Dory':
            profileMask.update(bubbly=bubbMask+2)
            profileMask.update(goofy=goofMask+2)
            profileMask.update(openness=openMask+1)
#       If I were a dog, I would be a:
        if value=='German Shepherd':
            profileMask.update(confident=confMask+2)
            profileMask.update(conservative=consMask+2)
            profileMask.update(intellectual=inteMask+1)
        if value=='Pug':
            profileMask.update(goofy=goofMask+2)
            profileMask.update(bubbly=bubbMask+2)
            profileMask.update(fiery=fierMask+1)
        if value=='Labrador Retriever':
            profileMask.update(intellectual=inteMask+2)
            profileMask.update(conservative=consMask+2)
            profileMask.update(spontaneity=sponMask+1)
        if value=='Poodle':
            profileMask.update(creative=creaMask+2)
            profileMask.update(introverted=intrMask+2)
            profileMask.update(bubbly=bubbMask+1)
    return

def q3Mask(form, profileMask):
    for value in form:
        adveMask=profileMask.select()[0].adventurous
        bubbMask=profileMask.select()[0].bubbly
        confMask=profileMask.select()[0].confident
        consMask=profileMask.select()[0].conservative
        creaMask=profileMask.select()[0].creative
        fierMask=profileMask.select()[0].fiery
        goofMask=profileMask.select()[0].goofy
        inteMask=profileMask.select()[0].intellectual
        intrMask=profileMask.select()[0].introverted
        openMask=profileMask.select()[0].openness
        sponMask=profileMask.select()[0].spontaneity
        
        if adveMask==None:
            adveMask=0
        if bubbMask==None:
            bubbMask=0
        if confMask==None:
            confMask=0
        if consMask==None:
            consMask=0
        if creaMask==None:
            creaMask=0
        if fierMask==None:
            fierMask=0
        if goofMask==None:
            goofMask=0
        if inteMask==None:
            inteMask=0
        if intrMask==None:
            intrMask=0
        if openMask==None:
            openMask=0
        if sponMask==None:
            sponMask=0
        profileMask.update(adventurous=adveMask)
        profileMask.update(bubbly=bubbMask)
        profileMask.update(confident=confMask)
        profileMask.update(conservative=consMask)
        profileMask.update(creative=creaMask)
        profileMask.update(fiery=fierMask)
        profileMask.update(goofy=goofMask)
        profileMask.update(intellectual=inteMask)
        profileMask.update(introverted=intrMask)
        profileMask.update(openness=openMask)
        profileMask.update(spontaneity=sponMask)

        print(value)
        
#       A spontaneous road trip (with my pup!) sounds fun:
        if value=='For sure!':
            profileMask.update(adventurous=adveMask+2)
#       I am the life of the party:
        if value=='Totally!':
            profileMask.update(bubbly=bubbMask+2)
#       I am not shy meeting new people:
        if value=='Yes':
            profileMask.update(confident=confMask+2)
#       I do not drink or do drugs:
        if value=='True':
            profileMask.update(conservative=consMask+2)
#       I prefer to create a piece of art rather than to analyze a piece of art:
        if value=='Yep!':
            profileMask.update(creative=creaMask+2)
    return

def q4Mask(form, profileMask):
    for value in form:
        adveMask=profileMask.select()[0].adventurous
        bubbMask=profileMask.select()[0].bubbly
        confMask=profileMask.select()[0].confident
        consMask=profileMask.select()[0].conservative
        creaMask=profileMask.select()[0].creative
        fierMask=profileMask.select()[0].fiery
        goofMask=profileMask.select()[0].goofy
        inteMask=profileMask.select()[0].intellectual
        intrMask=profileMask.select()[0].introverted
        openMask=profileMask.select()[0].openness
        sponMask=profileMask.select()[0].spontaneity
        
        if adveMask==None:
            adveMask=0
        if bubbMask==None:
            bubbMask=0
        if confMask==None:
            confMask=0
        if consMask==None:
            consMask=0
        if creaMask==None:
            creaMask=0
        if fierMask==None:
            fierMask=0
        if goofMask==None:
            goofMask=0
        if inteMask==None:
            inteMask=0
        if intrMask==None:
            intrMask=0
        if openMask==None:
            openMask=0
        if sponMask==None:
            sponMask=0
        profileMask.update(adventurous=adveMask)
        profileMask.update(bubbly=bubbMask)
        profileMask.update(confident=confMask)
        profileMask.update(conservative=consMask)
        profileMask.update(creative=creaMask)
        profileMask.update(fiery=fierMask)
        profileMask.update(goofy=goofMask)
        profileMask.update(intellectual=inteMask)
        profileMask.update(introverted=intrMask)
        profileMask.update(openness=openMask)
        profileMask.update(spontaneity=sponMask)

        print(value)
        
#       I have a short temper:
        if value=='For sure!':
            profileMask.update(fiery=fierMask+2)
#       Pillow fights are fun! I would love to/have participated in a mass pillow fight:
        if value=='Totally!':
            profileMask.update(goofy=goofMask+2)
#       I read more than two books a month:
        if value=='Yes':
            profileMask.update(intellectual=inteMask+2)
#       I can be quiet or reserved when I first meet someone:
        if value=='True':
            profileMask.update(introverted=intrMask+2)
#       My life is an open book:
        if value=='Yep!':
            profileMask.update(openness=openMask+2)
#       Last minute plans never stress me out:
        if value=='Agree!':
            profileMask.update(spontaneity=sponMask+2)
    return






"""def q1Mask(form, personalityMask):
    for value in form:
        if value == 'Get ready for a weekend of travel':
            previousAdventurous=personalityMask.select().adventurous
            previousSpontaneity=personalityMask.select().spontaneity
            previousConfident=personalityMask.select().confident
            personalityMask.update(adventurous=previousAdventurous+2)
            personalityMask.update(spontaneity=previousSpontaneity+2)
            personalityMask.update(confident=previousConfident+1)
            print(value)
        elif value == 'Go dancing':
            previousBubbly=personalityMask.select().bubbly
            personalityMask.update(bubbly=previousBubbly+2)
        elif value == 'Read a book and stay in (with my pup!)':
            previousIntroverted=personalityMask.select().introverted
            personalityMask.update(introverted=previousIntroverted+2)
        elif value == 'Something creative (painting, drawing, writing)':
            previousCreative=personalityMask.select().creative
            personalityMask.update(creative=previousCreative+2)
    return"""
