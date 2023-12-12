from src.elastic_search.elastic_search_connection import es
import uuid
from datetime import datetime

index_name = "test"


def post_data(request):
    """
    post data in elastic search
    """
    try:
        time = datetime.now()
        doc = {
            "id": uuid.uuid4(),
            "country_name": request.name,
            "is_active": True,
            "is_delete": False,
            "created_on": time,
            "modified_on": time,
            "country_bio": request.bio,
        }

        es.index(index=index_name, body=doc)
        es.indices.refresh(index=index_name)

        return "data added", 201
    except Exception as e:
        return str(e), 500


def get_all_data():
    """
    get all data
    """
    try:
        result = es.search(
            index=index_name,
            body={
                "query": {"bool": {"must_not": {"term": {"is_delete": True}}}},
                "sort": [{"created_on": {"order": "desc"}}],
            },
        )

        hits = result["hits"]["hits"]
        data = [{"id": hit["_id"], **hit["_source"]} for hit in hits]

        return data, 200, len(data)

    except Exception as e:
        return str(e), 500


def get_by_name(city_name):
    """
    get data by name
    """
    try:
        query = {
            "query": {
                "bool": {
                    "must_not": {"term": {"is_delete": True}},
                    "must": {"match_phrase_prefix": {"country_name": city_name}},
                }
            }
        }

        result = es.search(index=index_name, body=query)

        hits = result["hits"]["hits"]
        data = [{"id": hit["_id"], **hit["_source"]} for hit in hits]

        return data, 200, len(data)

    except Exception as e:
        return str(e), 500


def delete_data(id):
    """
    delete data elastic search
    """
    try:
        result = es.search(index=index_name, body={"query": {"match": {"id": id}}})
        doc_id = result["hits"]["hits"][0]["_id"]
        es.update(
            index=index_name,
            id=doc_id,
            body={"doc": {"is_delete": True, "is_active": False}},
        )

        return "Data marked as deleted successfully", 200
    except Exception as e:
        return str(e), 500
