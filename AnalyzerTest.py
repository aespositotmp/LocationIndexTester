from elasticsearch import Elasticsearch
from MainClass import EsModules
from elasticsearch import client

qa= Elasticsearch(
        ["search1node01q.tmpqa.core.dc"],
        http_auth=('user', 'pass'),
        port=9200, )
staging= Elasticsearch(
        ["search1node01s.tmpstage.core.dc"],
        http_auth=('user', 'pass'),
        port=9200, )


#print(Elasticsearch.analyze(index="jobs-en-4643",analyzer="jobDefaultAnalyzer",text="enginner"))


print("QA Output")
print(client.IndicesClient(qa).analyze(index="jobs-en-1118",analyzer="jobDefaultWithDelimiterAnalyzer",text="enginneer"))
print("Staging Output")
print(client.IndicesClient(staging).analyze(index="jobs-en-1118",text="enginneer",analyzer="jobDefaultWithDelimiterAnalyzer"))