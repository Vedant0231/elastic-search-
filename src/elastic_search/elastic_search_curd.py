import uuid
from datetime import datetime
from src.config import Config
from src.elastic_search.elastic_search_connection import es
from src.elastic_search.mapping import country_mapping


def create_index():
    """
    Create index
    """
    try:
        es.indices.create(Config.INDEX_NAME)  # create index
        es.indices.put_mapping(
            index=Config.INDEX_NAME, body=country_mapping
        )  # update index with mapping
        return "data added", 201
    except Exception as e:
        return str(e), 500


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

        es.index(index=Config.INDEX_NAME, body=doc)
        es.indices.refresh(index=Config.INDEX_NAME)

        return "data added", 201
    except Exception as e:
        return str(e), 500


def get_all_data():
    """
    get all data
    """
    try:
        result = es.search(
            index=Config.INDEX_NAME,
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

        result = es.search(index=Config.INDEX_NAME, body=query)

        hits = result["hits"]["hits"]
        data = [{"id": hit["_id"], **hit["_source"]} for hit in hits]

        return data, 200, len(data)

    except Exception as e:
        return str(e), 500


def modified_data(request_data):
    """
    Update data in Elasticsearch based on provided values in request_data
    """
    try:
        result = es.search(
            index=Config.INDEX_NAME, body={"query": {"match": {"id": request_data.id}}}
        )
        doc_id = result["hits"]["hits"][0]["_id"]
        
        # Prepare update body based on provided values
        update_body = {"doc": {}}
        if request_data.name is not None:
            update_body["doc"]["country_name"] = request_data.name
        if request_data.bio is not None:
            update_body["doc"]["country_bio"] = request_data.bio
        
        if update_body["doc"]:
            es.update(index=Config.INDEX_NAME, id=doc_id, body=update_body)
            return "Data updated successfully", 200
        else:
            return "No changes to update", 200

    except Exception as e:
        return str(e), 500


def delete_data(id):
    """
    delete data elastic search
    """
    try:
        result = es.search(
            index=Config.INDEX_NAME, body={"query": {"match": {"id": id}}}
        )
        doc_id = result["hits"]["hits"][0]["_id"]
        es.update(
            index=Config.INDEX_NAME,
            id=doc_id,
            body={"doc": {"is_delete": True, "is_active": False}},
        )

        return "Data marked as deleted successfully", 200
    except Exception as e:
        return str(e), 500
