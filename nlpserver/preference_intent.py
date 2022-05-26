# Intent sets for different applications

base = ['weather', 'time']
character = ['name', 'askskill', 'askhobby', 'asksex', 'greetguest']
cv = ['begingame', 'endgame', 'dance', 'photo', 'askname'] # askname不对
p2p = ['music', 'mem-in', 'mem-out']
commic = ['']
food = ['']
blockchain = ['recommandnews', 'querycoins', 'sendnews', 'bcknowledge', 'bcqapairs']

# ---
## list only
ITR_TYPE = [list]
DEFAULT_INTENT = 'chat' # should imported from intent
def _combined_inorder(*args, **kwargs):
    ret = []
    for mod in args:
        if type(mod) not in ITR_TYPE:
            raise Exception('illegal domain type: {}'.format(type(mod)))
        for intent in mod:
            if intent not in ret:
                ret.append(intent)
    try:
        ret.remove(DEFAULT_INTENT)
    except ValueError: 
        pass
    finally:
        ret.append(DEFAULT_INTENT)
    return ret

intent_qiantai = _combined_inorder(base, character, p2p, cv, commic, food)
intent_lucy = _combined_inorder(base, character, p2p, commic, food)
intent_chainmaster = _combined_inorder(base, character, p2p, blockchain)
intent_chainmaster_qun = _combined_inorder(base, character, blockchain)

if __name__ == '__main__':
    print('intent_qiantai: ', intent_qiantai)
    print('intent_lucy: ', intent_lucy)
    print('intent_chainmaster: ', intent_chainmaster)
    print('intent_chainmaster_qun: ', intent_chainmaster_qun)
