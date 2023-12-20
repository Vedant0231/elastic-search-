import json
import uuid
from datetime import datetime
from src.config import Config
from src.elastic_search.elastic_search_connection import es
from src.elastic_search.mapping import mapping


def create_index():
    """
    Create index
    """
    try:
        index_settings = {
            "settings": {
                "index.mapping.total_fields.limit": 10000,
                "index.mapping.nested_fields.limit": 10000
            }
        }

        es.indices.create(index=Config.INDEX_NAME, body=index_settings)  # create index
        es.indices.put_settings(index_settings)  # Create the index with settings
        es.indices.put_mapping(
            index=Config.INDEX_NAME, body=mapping
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
            "city_name": request.get("city_name"),
            "buyer_categories": request.get("buyer_categories"),
            "created_on": time,
            "modified_on": time,
        }

        es.index(index=Config.INDEX_NAME,id=uuid.uuid4(), body=doc)
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
                "sort": [{"created_on": {"order": "desc"}}],
            },
        )

        hits = result["hits"]["hits"]
        data = [{"id": hit["_id"], **hit["_source"]} for hit in hits]

        return data, 200, len(data)

    except Exception as e:
        return str(e), 500, 0


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
        return str(e), 500, 0


def modified_data(request_data):
    """
    Update data in Elasticsearch based on provided values in request_data
    """
    try:
        time = datetime.now()
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
        # update modified on time
        update_body["doc"]["modified_on"] = time

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
