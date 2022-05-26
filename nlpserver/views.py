from flask import jsonify
from flask import request
from flask import Blueprint

from . import app
api_view = Blueprint('api_view', __name__)

from .utils import fetch_request_data
from .intent import intent
from .rules import DSSMHandler
from .rules.kg import kg_with_domains
from .control import get_answer


@api_view.route('/api/v1/nlp', methods=['GET', 'POST'])
def process_nlp():
    data = request.get_json()
    project = app.config.get('PROJECT', 'processnlp')
    what_robot_say, what_people_say, inloop, preference, open_id = fetch_request_data(data)
    # TODO check validation of the upcoming input there
    # TODO check sensitive words there.
    ret_data = get_answer(project=project, what_robot_say=what_robot_say, what_people_say=what_people_say, inloop=inloop, preference=preference, open_id=open_id)
    '''
    # chatbot in a group only broadcasts news
    if ('chainmaster_qun' == app.config.get('PROJECT', 'processnlp') and
        ret_data['message']['data'][0]['type'] not in ["queryCoin", "recommand"]):
        return ('', 204)
    '''
    return jsonify(ret_data)   

@api_view.route('/api/v1/nlp/intent', methods=['GET', 'POST'])
def get_intent():
    data = request.get_json()
    sentence = data.get('query', '')
    if not sentence:
        return jsonify({'success': -1, 'message': 'no query data'})
    itt = intent.judgeIntent(sentence)
    return jsonify({'success': 0, 'data': itt})

@api_view.route('/api/v1/nlp/chat', methods=['GET', 'POST'])
def get_chat():
    data = request.get_json()
    sentence = data.get('query', '')
    if not sentence:
        return jsonify({'success': -1, 'message': 'no query data'})
    reply = DSSMHandler.get_raw_reply(sentence)
    return jsonify({'success': 0, 'data': reply})
    

@api_view.route('/api/v1/nlp/knowledge/<domain>', methods=['GET', 'POST'])
@api_view.route('/api/v1/nlp/knowledge', defaults={'domain': ''}, methods=['GET', 'POST'])
def get_knowledge(domain):
    data = request.get_json()
    sentence = data.get('query', '')
    if not sentence:
        return jsonify({'success': -1, 'message': 'no query data'})
    print(domain)
    answer = kg_with_domains(sentence, domains=[domain])
    if answer:
        return jsonify({'success': 0, 'data': answer})
    return jsonify({'success': -2, 'message': 'no related knowledge'})
