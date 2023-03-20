from elasticsearch import Elasticsearch
class elasticsearch():
    def __init__(self,index_name):
        ELASTIC_PASSWORD = "OLApNhqvtWv9v7IccgmV4wu1"
        CLOUD_ID = "job_search_es:dXMtY2VudHJhbDEuZ2NwLmNsb3VkLmVzLmlvJGJiZDExZGEzYzlmMzQ5MWZhYTAyMDBmNDMwMWI3ZGU3JDY2MzUyNWM1MmE1ZjQyNGViYTA4ZTFiYjY4NTUxOTE1"
        
        self.es=Elasticsearch(
            cloud_id=CLOUD_ID,
            basic_auth=("elastic", ELASTIC_PASSWORD));
        self.index_name=index_name
        # self.index_type=index_type
    def search(self,query,count:int=30):
        ds1={
            "query":{
                "multi_match":{
                    "query":query,
                    "fields":["title","intro","content"]
                }
            }
        }
        match_data=self.es.search(index=self.index_name,body=ds1,size=count)
        return match_data