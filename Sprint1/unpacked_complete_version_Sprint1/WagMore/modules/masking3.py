def bitMask(form, profileMask):
    for value in form:
        previousMask=profileMask.select()[0].interestMask
        if value==False:
            profileMask.update(interestMask=previousMask+'0')
        if value==True:
            profileMask.update(interestMask=previousMask+'1')
    return
