import traceback
from .intent import what_intent
from .utils.global_pak import update_msg_with_type
from .rules import get_rules_mapping
from .rules.kg import kg_with_domains

from .rules.blockchain import blockchain_chat_slice 
@update_msg_with_type('services')
def _wrap_service(data):
    return data
def _get_bc_answer(intent: str = '', what_robot_say: list = [], what_people_say: list = [''], people_intents: list = [''], inloop: int = 0, *args, **kwargs) -> dict:
    sentence = what_people_say[-1]
    open_id = kwargs.get('open_id', 'null')
    ret = blockchain_chat_slice(sentence=sentence, openId=open_id, *args, **kwargs)
    if not ret:
        return {}
    else:
        tp = ret.get('type', '')
        if tp == 'recommand':
            ret['items1'] = ret['message1']
            ret['items2'] = ret['message2']
            ret.pop('message1')
            ret.pop('message2')
            ret['message'] = 'see data items..'
            ret['inloop'] = 0            
        elif tp == 'queryCoin' or tp == 'sendNews':
            ret['items'] = ret['message']
            ret['message'] = 'see data items..'
            ret['inloop'] = 0
        elif tp == 'knowledge':
            ret['inloop'] = 0
        elif tp == 'chat':
            ret['message'] = ret['message']['reply']
            ret['inloop'] = 0
        #data = _wrap_service(ret)
        return ret





## main entrance of answer
@update_msg_with_type()
def get_answer(project: str = 'qiantai', intent: str = '', what_robot_say: list = [], what_people_say: list = [''], people_intents: list = [''], inloop: int = 0, *args, **kwargs) -> dict:
    ''' 
    Examples of the dict objects being extracted and returned:
    {
        "type":"music",
        "message": 'Okay，now playing song AAA by BBB'
        "slots":
        {
            "album":"album name",
            "singer":"BBB",
            "song":"AAA”
        }
        "inloop": 0/1/2
    },
    {
        "type":"weather",
        "slots":
        {
            "year":"2018"
            "month":"10",
            "day":"17",
            "time":"15",  
            "format":"24h",   #24h/12h
        },
        "inloop": 0/1/2   
    },
    {
        "type":"alarm",
        "slots":
        {
            "year":"2018"
            "month":"10",
            "day":"17",
            "time":"15",      
            "format":"24h",   #24h/12h
        },
        "inloop": 0/1/2   
    }
    '''
    if project == 'chainmaster' or project == 'chainmaster_qun':
        if project == 'chainmaster_qun': kwargs['query_coin_trend_pic'] = False
        bc_ret_data = _get_bc_answer(what_people_say=what_people_say, *args, **kwargs)
        if bc_ret_data:
            if project != 'chainmaster_qun' and bc_ret_data['type'] == 'knowledge': bc_ret_data['type'] = 'chat'
            return bc_ret_data
        kg_answer = kg_with_domains(what_people_say[-1], domains=['blockchain'])
        if kg_answer:
            if project != 'chainmaster_qun': return {'type': 'chat', 'message': kg_answer}
            return {'type': 'knowledge', 'message': kg_answer}

    if project == 'qiantai' or project == 'lucy':
        kg_answer = kg_with_domains(what_people_say[-1], domains=['commic', 'food'])
        if kg_answer:
            return {'type': 'chat', 'message': kg_answer}

    ####
    ## mapping intents with correlated answer fucntions
    rules_mapping = get_rules_mapping()
    try:
        inloop = inloop
        intent, people_intents = what_intent(what_people_say, inloop)
        print(">1>", intent, what_robot_say, what_people_say, people_intents, inloop,)
        if intent in rules_mapping:
            handler = rules_mapping[intent]
            try:
                ret_data = handler(what_robot_say, what_people_say, people_intents, inloop, *args, **kwargs)
            except TypeError:
                ret_data = handler(what_robot_say, what_people_say, people_intents, inloop)
            if ret_data['type'] != "can't get slot":
                return ret_data
            else:
                ## inloop
                inloop = 1
                intent, people_intents = what_intent(what_people_say, inloop)
                print(">2>", intent, what_robot_say, what_people_say, people_intents, inloop,)
                if intent in rules_mapping:
                    handler = rules_mapping[intent]
                    try:
                        ret_data = handler(what_robot_say, what_people_say, people_intents, inloop, *args, **kwargs)
                    except TypeError:
                        ret_data = handler(what_robot_say, what_people_say, people_intents, inloop)
                    if ret_data['type'] != "can't get slot":
                        return ret_data
                    else:
                        raise Exception('Cannot get slots even inloop is equal to 1 .')
                ###
        raise Exception('no intent: ' + intent )
    except:
        traceback.print_exc()

    try:
        ret_data = rules_mapping['chat'](what_robot_say, what_people_say, people_intents, 1, *args, **kwargs)
    except:
        traceback.print_exc()
        ret_data = {'success': -1, 'error_message': 'inner error'}
    return ret_data

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  