### ------------------------------------------------------------------------------
## 意图
from .intent import Intent
intent = Intent()
# TODO 意图种类补全，Intent包测试
DEFAULT_INTENT = 'chat'
def is_repeat(sentence1,sentence2):
    if sentence2==sentence1:
        return True
def _get_all_intents(sentences):
    #intentlist=[]
    #intentlist.append(intent.judgeIntent(sentences[0]))
    #for i in range(1,len(sentences)):
    #   if is_repeat(sentences[i],sentences[i-1]):
    #       intentlist.append("repeater")
    #   else:
    #       intentlist.append(intent.judgeIntent(sentences[i])) 
    #return intentlist
    return [intent.judgeIntent(sentence) for sentence in sentences]

def what_intent(sentences, inloop, preference={}):
    #return DEFAULT_INTENT, [DEFAULT_INTENT]
    # ---
    intents_list = _get_all_intents(sentences)
    if len(intents_list) <= 0:
        #print(1, DEFAULT_INTENT, [DEFAULT_INTENT])
        return DEFAULT_INTENT, [DEFAULT_INTENT]
    if inloop <= 0:
        #print(2, intents_list[0], intents_list)
        return intents_list[0], intents_list
    if len(intents_list) < inloop:
        #print(3, DEFAULT_INTENT, intents_list)
        return DEFAULT_INTENT, intents_list
    else:
        intentlist=[]
        intentlist.append(intent.judgeIntent(sentences[0]))
        for i in range(1,len(sentences)):
            if is_repeat(sentences[i],sentences[i-1]):
               intentlist.append("repeater")
            else:
               intentlist.append(intent.judgeIntent(sentences[i])) 
            #print(4, intents_list[-inloop], intents_list)
        if intentlist[-inloop+1]=="repeater" and intents_list[-inloop+1] in ['chat',"name","askskill","asksex","askage","askhobby","guestsname","greetguest"]:
            return intentlist[-inloop+1], intents_list
        return intents_list[-inloop], intents_list


