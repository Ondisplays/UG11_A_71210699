def ambildanbalik(kalimat, mulai, berhenti, benar):
    if(benar):
        kata = kalimat[mulai-1:berhenti]
        return(kata[::-1])
    elif(not benar):
        return(kalimat[mulai-1:berhenti])
    else:
        print("Maaf, salah input")

print(ambildanbalik("abcdefg",2,4,True))
print(ambildanbalik("abcdefg",1,5,False))
print(ambildanbalik("Qwerty",3,4,True))
print(ambildanbalik("Qwerty",2,2,False))