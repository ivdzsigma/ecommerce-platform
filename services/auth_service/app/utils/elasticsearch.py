# services/product_service/app/utils/elasticsearch.py
from elasticsearch import Elasticsearch

es = Elasticsearch(["http://elasticsearch:9200"])

def search_products(query: str):
    body = {
        "query": {
            "multi_match": {
                "query": query,
                "fields": ["name^3", "description", "category"]
            }
        }
    }
    return es.search(index="products", body=body)