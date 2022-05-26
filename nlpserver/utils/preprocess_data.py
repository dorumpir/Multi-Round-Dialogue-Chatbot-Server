### ------------------------------------------------------------------------------
## 数据预处理
def fetch_request_data(data):
    '''
    {
        "type": "text",
        "deviceid":xxxx,
        "userid":xxx,
        "message": "本次用户输入",            # 用户的对话内容,utf-8
        "background_message":"大海边，阳光照在暖暖的沙滩上"    #看图说话的内容
        "inloop":1/2/3                  # 对话时考虑的轮数，和histories一一对应
        "histories":                  # 倒序排列，第一个表示上一句的内容，第二个表示上两个的内容...
        [
                {
                    "time":"utc time",
                    "what_people_say":"人所说，这一轮的对话内容",
                    "what_robot_say":"机器所说，这一轮的对话内容"
                    "background_message":"大海边，阳光照在暖暖的沙滩上" 
                },
                {
                    "time":"utc time",
                    "what_people_say":"人所说，这一轮的对话内容",
                    "what_robot_say":"机器所说，这一轮的对话内容"
                    "background_message":"大海边，阳光照在暖暖的沙滩上"
                }
        ]
        "favorite_domains":
        {
            "blockchain",
            "food"
        }
        "favorite_domains_priority":
        {
            0,
            1
        }
    }
    '''
    histories = data.get('histories', [])
    what_robot_say = list(reversed(list(map(lambda x: str(x), [history.get('what_robot_say', "") for history in histories]))))
    what_people_say = list(reversed(list(map(lambda x: clean_question(x), [data.get('message', '')] + [history.get('what_people_say', "") for history in histories]))))
    inloop = int(data.get('inloop', 0))
    open_id = data.get('userid', 'null')
    preference = {
                    "favorite_domains": data.get("favorite_domains", {}),
                    "favorite_domains_priority": data.get("favorite_domains_priority", {})
                 }
    return what_robot_say, what_people_say, inloop, preference, open_id


def is_sensitive_question():
    pass

def is_valid_question():
    pass

def clean_question(sentence):
    sentence = str(sentence)
    return sentence.strip('。 ')