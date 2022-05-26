'''
{
    "success":0/1,
    "type": "chat/tasks/services",  #chat：闲聊，task：多轮任务slots，services：可接的3rdparty服务
    "uniqueid":'xxxx',              # 某台设备上或者某台设备上的某个用户
    "message":
    {
        "from":"model name",
        "text":"对话内容",
        "tasks": 
        {
            [
                {
                    "type":"music",
                    "slots":
                    {
                        "album":"专辑名称",
                        "singer":"演唱者",
                        "song":"歌曲名"
                    }
                },
                {
                    "type":"weather",
                    "slots":
                    {
                        "year":"2018",
                        "month":"10",
                        "day":"17",
                        "time":"15",  #几点
                        "format":"24h",   #24h制，12h制
                    }	
                },
                {
                    "type":"alarm",
                    "slots":
                    {
                        "year":"2018",
                        "month":"10",
                        "day":"17",
                        "time":"15",  #几点
                        "format":"24h",   #24h制，12h制
                    }	
                }
            ]
            
        },
        
        "services":  #该部分需遵守各种服务的自定义字段
        {
            [
                {
                    "type":"coinprice",
                    "price":"btc的价格是6862.373636062999美金。",
                    "description":"BTC近24小时整体趋势为上涨, 涨幅为7.50%。24小时内报价最大差价为1284.7800美元。",
                    "image":"http://yktcardshop-mweb/common/photo/btc-usdt-2018-10-15-16-24hours-trend.png"
                },
                {
                    "type":"news",
                    "id":"流水号",
                    "title":"韩国官员称韩国政府将在11月宣布对ICO的立场",
                    "description":"10月15日消息，韩国政府。。。",
                    "timestamp":"时间戳",
                    "summary":"总结"
                }
            ]
        }
    },
    "inloop":0/1                  # 是否已取得任务所需要的信息，一旦取得，多轮对话结束。0表示下轮为单轮开始，1表示在多轮中，此时需要发给NLP多轮对话内容
}
'''



msg_type = ['chat', 'tasks', 'services']

tmpl = {
    "success": 0,
    "type": "chat/tasks/services",  #chat：闲聊，task：多轮任务slots，services：可接的3rdparty服务
    "uniqueid": "FFFF-FFFF-FFFF-FFFF-FFFF-FFFF-FFFF-FFFF",              # 某台设备上或者某台设备上的某个用户
    "message": {
        "from":"model name",
        "text":"对话内容",
        "data": [
            {
                "type":"music",
                "slots":
                {
                    "album":"专辑名称",
                    "singer":"演唱者",
                    "song":"歌曲名"
                }
            },
            {
                "type":"weather",
                "slots":
                {
                    "year":"2018",
                    "month":"10",
                    "day":"17",
                    "time":"15",  #几点
                    "format":"24h",   #24h制，12h制
                }	
            },
            {
                "type":"alarm",
                "slots":
                {
                    "year":"2018",
                    "month":"10",
                    "day":"17",
                    "time":"15",  #几点
                    "format":"24h",   #24h制，12h制
                }	
            }
        ]		
    },
    "inloop": 0		
}



from functools import wraps
from copy import deepcopy
from functools import reduce

# def _gen_main_info_by(msg, data)
def _autogen_main_info(msg):
    '''
    inloop取最大的
    from取第一个模型名
    text取第一个text
    #data内部删掉chat类型
    '''
    data = msg['message']['data']
    inloop = reduce(lambda a, b: max(int(a) ,int(b)), [d.get('inloop', 0) for d in data])
    text = list(filter(None, [d.get('message', '') for d in data]))
    model_names = list(filter(None, [d.get('model_name', '') for d in data]))
    # print(data)
    # print([d.get('model_name', '') for d in data])
    # print(model_names)
    msg['inloop'] = inloop
    msg['message']['from'] = model_names[0] if len(model_names) > 0 else ""
    msg['message']['text'] = text[0] if len(text) > 0 else ""
    #msg['message']['data'] = [d for d in data if d['type'] != 'chat']
    return msg


def update_msg_with_type(type="chat", msg=tmpl):
    def wrapper(func):
        @wraps(func)
        def _wrapper(*args, **kwargs):
            if type not in msg_type:
                raise Exception('Invalid message type: {}'.format(type))

            nonlocal msg
            data = func(*args, **kwargs)
            # TODO 这段代码有问题，else永远走不到，因为message是静态全局变量，固定的
            if msg.get('type', '') not in msg_type:
                # from scratch
                ret_msg = deepcopy(tmpl)
                ret_msg['success'] = 0
                ret_msg['type'] = type
                ret_msg['message']['data'] = [data]
                ret_msg = _autogen_main_info(ret_msg)
                return ret_msg
            else:
                msg['message']['data'].append(data)
                msg = _autogen_main_info(msg)
            return msg
        return _wrapper
    return wrapper


'''
def insert_kv_into_dict(k, v):
    def wrapper(func):
        @wraps(func)
        def _wrapper(*args, **kwargs):
            data = func(*args, **kwargs)
            if not isinstance(data, dict):
                raise Exception('Try to insert {}:{} into {} variable'.format(k, v, type(data)))
            try:
                data[k] = v
            except TypeError as e:
                print(e)
            return data
        return _wrapper
    return wrapper

@update_msg_with_type('tasks')
def f():
    return {'type': 'test', 'slots': {'reply':' 你可以', 'other': 'ohaha'}}

print(f())
print(f())
'''