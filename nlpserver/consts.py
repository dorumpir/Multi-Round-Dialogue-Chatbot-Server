DSSM_ES_URL=''

NEO4J_HOST=''
NEO4J_PORT=''
NEO4J_AUTH=('')

MEM_DATA_URL=''



BC_NEWS_URL = ''
BC_NEWS_KEYWORDS_URL = ''
BC_SUMMARY_URL = ''

BC_COIN_PRICE_URL = ''
BC_COIN_TREND_URL = ''
BC_COIN_ALL_URL = ''

BC_KEYWORDS_URL = ''
BC_KNOWLEDGE_URL = ''
HISTORY_URL = ''
BC_QAPAIRS_URL = ''


###
UCANASK_URL = ''
UCANASK_ASK_URL = ''

from pathlib import Path
_APP_DIR = Path(__file__).absolute().expanduser().parent
BC_WORD_DICT_FILE = str(_APP_DIR/'static'/'blockchain_word_dict.txt')
BC_COIN_LIST_FILE = str(_APP_DIR/'static'/'coin_list.txt')