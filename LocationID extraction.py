import configparser
import time
from MainClass import EsModules
from datetime import datetime
import json
import os

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

if ES_environment == 'search1node01q.tmpqa.core.dc':
    env_val = 'QA'
elif ES_environment == 'search1node01s.tmpstage.core.dc':
    env_val = 'Staging'
elif ES_environment == 'search1node01p.tmpprod.core.dc':
    env_val = "Prod"
resultsdir='./Test Results/'+env_val+"/"+alias_lan_code+"/"+runtime
os.makedirs(resultsdir)
x=0
for line in search_term:
    ssearch_term = search_term[x].strip('\n')
    result = EsModules.es_location_suggest(ES_environment, alias_lan_code, test_index, ssearch_term, country_ctx)
    filename = runtime+"Output_error.txt"
    #print(type(result))
    #print(result)
    try:
        id = result["suggest99"][0]["options"][0]["payload"]["id"]
        for ids in result["suggest99"][0]["options"]:
            print(ssearch_term+"-"+str(ids["payload"]["id"]))
    except:
        print(ssearch_term+" does not return any locations")
        with open(os.path.join(resultsdir,filename), "a", encoding='utf-8') as out_file:
            out_file.write(ssearch_term+"\n")
    x = x + 1
    time.sleep(0.001)