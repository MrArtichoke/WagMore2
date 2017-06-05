def initP(form, profileMask):
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
