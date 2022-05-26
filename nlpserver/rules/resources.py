### ------------------------------------------------------------------------------
## 规则
# TODO 其他规则的get_reply按照接口{"type", "message", "inloop", "slot"}格式补全，列在这里
# 1. chat
#from dssm import dssm_model
class DSSMHandler:
    #Dssm = dssm_model.DSSM_Model('model_config')
    #Dssm.model_init()
    @classmethod
    def get_reply(cls, what_robot_say, what_people_say, people_intents, inloop,*args, **kwargs):
        #question = kwargs.get('what_people_say', [''])[0]
        question = what_people_say[-1] if what_people_say else ""
        answer = cls.get_reply_online(question) #cls.Dssm.model_predict(question=question)
        return {'type': 'chat', 'message': answer, 'inloop': 0, 'model_name': 'dssm'}
    @classmethod
    def get_raw_reply(cls, question):
        return cls.get_reply_online(question)
    @classmethod 
    def get_reply_online(cls, question):
        import requests
        dssmurl="....../dssmservice/query"
        reply = requests.get(url=dssmurl, params={"question":question})
        if reply.ok:
            reply = reply.json().get('answer','')
        else:
            reply = '我想换个别的话题，好么'
        return reply
# 2. photo
class PhotoHandler:
    @staticmethod
    def get_reply(*args, **kwargs):
        return {'type': 'photo', 'message': '好的，茄子', 'inloop': 0}
# 3. dance
class DanceHandler:
    @staticmethod
    def get_reply(*args, **kwargs):
        return {'type': 'dance', 'message': '准备开跳', 'inloop': 0}
# 4. game
class BeginGameHandler():
    @staticmethod
    def get_reply(*args, **kwargs):
        return {'type': 'start_track','message': '好的'}
class EndGameHandler():
    @staticmethod
    def get_reply(*args, **kwargs):
        return {'type': 'end_track','message': '好的'}

class Single2Mul():
    def __init__(self, handler, attr='get_reply', ret_type='chat'):
        self.handler = handler()
        self.ret_type = ret_type
    def get_pak(self, what_robot_say, what_people_say, people_intents, inloop,*args, **kwargs):
        try:
            print(what_people_say[-1])
            reply = self.handler.get_reply(what_people_say[-1])
        except:
            reply = 'Invoked by false intent\nQ:{}'.format(what_people_say[-1])
        return {'type': self.ret_type, 'message': reply, 'inloop': 0}

# 5. greet
class GreetHandler():
    from .greet import Greetsb
    handler = Single2Mul(Greetsb)
    @classmethod
    def get_reply(cls, what_robot_say, what_people_say, people_intents, inloop,*args, **kwargs):
        return cls.handler.get_pak(what_robot_say, what_people_say, people_intents, inloop,*args, **kwargs)
# 6. lucy-askskill
class LucySkillHandler():
    from .getskill_lucy import GetSkill
    handler = Single2Mul(GetSkill)
    @classmethod
    def get_reply(cls, what_robot_say, what_people_say, people_intents, inloop,*args, **kwargs):
        return cls.handler.get_pak(what_robot_say, what_people_say, people_intents, inloop,*args, **kwargs)
# 6. chainmaster-askskill
class ChainmasterSkillHandler():
    from .getskill_chainmaster import GetSkill
    handler = Single2Mul(GetSkill)
    @classmethod
    def get_reply(cls, what_robot_say, what_people_say, people_intents, inloop,*args, **kwargs):
        return cls.handler.get_pak(what_robot_say, what_people_say, people_intents, inloop,*args, **kwargs)
# 7. askhobby
class HobbyHandler():
    from .hobby import LucyHobby
    handler = Single2Mul(LucyHobby)
    @classmethod
    def get_reply(cls, what_robot_say, what_people_say, people_intents, inloop,*args, **kwargs):
        return cls.handler.get_pak(what_robot_say, what_people_say, people_intents, inloop,*args, **kwargs)
# 8. askage
class AgeHandler():
    from .age import Getage
    handler = Single2Mul(Getage)
    @classmethod
    def get_reply(cls, what_robot_say, what_people_say, people_intents, inloop,*args, **kwargs):
        return cls.handler.get_pak(what_robot_say, what_people_say, people_intents, inloop,*args, **kwargs)
# 9. asksex
class SexHandler():
    from .sexanswer import GetSex
    handler = Single2Mul(GetSex)
    @classmethod
    def get_reply(cls, what_robot_say, what_people_say, people_intents, inloop,*args, **kwargs):
        return cls.handler.get_pak(what_robot_say, what_people_say, people_intents, inloop,*args, **kwargs)
# 10. time
class TimeHandler():
    from .datetim import Getdate
    handler = Single2Mul(Getdate)
    @classmethod
    def get_reply(cls, what_robot_say, what_people_say, people_intents, inloop,*args, **kwargs):
        return cls.handler.get_pak(what_robot_say, what_people_say, people_intents, inloop,*args, **kwargs)



