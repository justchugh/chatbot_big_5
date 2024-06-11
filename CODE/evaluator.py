import pandas as pd

def get_list(csvname):
    df = pd.read_csv(csvname)
    questions = list(df['questions'])
    factors = list(df['factors'])
    direction = list(df['direction'])
    return questions,factors,direction

def evaluate(scores):
    questions,factors,direction = get_list("big-five.csv")
    l = len(scores)
    questions,factors,direction = questions[:l],factors[:l],direction[:l]
    uni_fac = set(factors)
    fac={}
    for i in uni_fac:
        fac[i]=[]
    for i in range(l):
        if(direction[i]=='-'):
            scores[i]=-scores[i]
        fac[factors[i]].append(scores[i])
    for i in fac.keys():
        fac[i]=sum(fac[i])
    return fac

def get_personality(scores,length):
    df = pd.read_csv("personality.csv")
    mins,maxs=length/len(scores.keys()),length
    mid = (mins+maxs)//2
    response=[]
    for i in scores.keys():
        if(scores[i]<mid):
            res=list(df[(df['factor']==i) & (df['score']=='L')]['response'])
            response.append(res[0])
        else:
            res=list(df[(df['factor']==i) & (df['score']=='H')]['response'])
            response.append(res[0])
    return response

# scores=[5,1,2,5,2,1,5,4,2,3,4,3,1,5,2]
# fac = evaluate(scores)
# print("Check your evaluation below\n")
# response = get_personality(fac,len(scores))
# print(''.join(response))
# print("I hope you agree")
