# from flask import Flask,request
import os
from recruit_item import recruit_info

from flask import (
    Flask,
    g,
    request,
    Response,
    render_template,
)

from py2neo import Graph,Node,Relationship

from neo4j import (
    GraphDatabase,
    basic_auth,
)

from elasticsearch_query_class import elasticsearch
import json
import logging



app=Flask(__name__)






@app.route("/")
def index():
    return render_template('index.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      print(result.get('Query'), type(result))
      query = result.get('Query')
      job_list = get_es(query)
      return render_template("result_debug.html",result = job_list, this_query=query)

@app.route("/get_es/<query>")
def get_es(query):
    es=elasticsearch(index_name="job")
    data=es.search(query)
    # print(data)
    address_data=data["hits"]["hits"]
    # address_list=dict()
    address_list = []
    for item in address_data:
        # address_list[item["_source"]['title']] = item["_source"]['url']
        tmp = recruit_info(item["_source"]['title'], item["_source"]['url'], item["_source"]['date'])
        address_list.append(tmp)
    return address_list

@app.route("/get_neo4j/<query>")
def get_neo4j(query):
    test_graph = Graph(
    "neo4j+s://3a95adb0.databases.neo4j.io", 
    auth=("neo4j", "CW1yXtp2CnlFeEqP0W0nvRyWp9IYPCl89gVsxTIXu1w")
    )
    cypher_tmp = "match (p: Company {company_entity:\"" + query + "\"}) return p"
    data1 = test_graph.run(cypher_tmp)
    tmp = data1.data()
    address_list = []
    for item in tmp:
        print(item, type(item),  item.keys())
        print('Shuai',type(item["p"]))
        address_list.append(item["p"]["title"])
        address_list.append(item["p"]["url"])
    new_json=json.dumps(address_list,ensure_ascii=False)
    return app.response_class(new_json,content_type="application/json")


    
    




# def generate_cypher():







if __name__=="__main__":
    # app.run(threaded=True, debug = True)
    app.run(host='0.0.0.0', port=5000)

