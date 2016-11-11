import configparser
import time
from MainClass import EsModules
from datetime import datetime

runtime = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
config = configparser.ConfigParser()
config.read('es_test_config.ini')
ES_environment = config['DEFAULT']['environment']
location_file= config['DEFAULT']['testlib']
# print(ES_environment)


#parsed_info = json.dumps((connection_es.info()), indent=4)
#print(parsed_info)

# search term entered in autosuggest
#search_term = input("Enter Search Term: ")
f=open(location_file,'r',encoding='utf-8')
search_term = f.readlines()
f.close()

# language code used in location alias
alias_lan_code = config['DEFAULT']['languagecode']

# country context value for query
country_ctx = config['DEFAULT']['country_context']

# designates if the index is new
is_New = config['DEFAULT'].getboolean('is_New')

if is_New:
    test_index = "-new"
else:
    test_index = ""
x=0
for line in search_term:
    ssearch_term = search_term[x].strip('\n')
    res = EsModules.es_location_suggest(ES_environment, alias_lan_code, test_index, ssearch_term, country_ctx)
    print(ssearch_term)
    EsModules.query_output(res, ssearch_term,alias_lan_code,ES_environment, runtime)
    x = x + 1
    time.sleep(0.01)
