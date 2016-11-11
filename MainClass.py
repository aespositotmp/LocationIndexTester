from elasticsearch import *
from datetime import datetime
import json
import os.path



class EsModules():

    def es_location_suggest(ES_environment, alias_lan_code, test_index, search_term, country_ctx):

        #connection_es= conn()
        connection_es = Elasticsearch(
        [ES_environment],
        http_auth=('user', 'pass'),
        port=9200, )

        result = connection_es.suggest(index="locations-" + alias_lan_code + test_index,
                              body=dict(suggest99=dict(text=search_term, completion={"field": "suggest", "context":
                                  {"country_ctx": [country_ctx]},
                                                                                     "size": 100
                                                                                     })))
        return result

    def query_output(result, search_term, langcode, environment, runtime):
        today = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
        #rundate = datetime.now().strftime('%Y-%m-%d %H-%M')
        parsed = json.dumps(result, indent=4, ensure_ascii=False).encode('utf-8')
        if environment=='search1node01q.tmpqa.core.dc':
            env_val='QA'
        elif environment=='search1node01s.tmpstage.core.dc':
            env_val='Staging'
        elif environment=='search1node01p.tmpprod.core.dc':
            env_val="Prod"
        #print(parsed)

        output_name = search_term+ " "+langcode+" "+today + '.txt'
        resultsdir='./'+env_val+"/"+langcode+"/"+runtime
        if not os.path.exists(resultsdir):
            os.makedirs(resultsdir)
        with open(os.path.join(resultsdir,output_name), "wb") as out_file:
            out_file.write(parsed)



       #def search_input(self):
       # result = csv.reader(open('Search_test.csv'), delimiter=',')

# class EsConnect():
#     def connect(es_environment):
#
#         es_environment = es_environment
#
#         return Elasticsearch(
#             [es_environment],
#             http_auth=('user', 'pass'),
#             port=9200,)
#
#
#
# es_mod = EsModules()
# conn = EsConnect()
# result = es_mod.es_location_suggest()

