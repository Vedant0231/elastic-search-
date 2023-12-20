mapping = {    # mapping which required while creating index
    "dynamic":"true",
    "properties": {
        "city_name": {"type": "text"},
        "buyer_categories": {
            "type": "nested",
            "dynamic": "true",
            "properties": {
                "High-End Connoisseurs": {
                    "type": "object",
                    "properties": {
                        "buyer_category": {"type": "keyword"},
                        "months": {
                            "type": "nested",
                            "dynamic": "true",
                            "properties": {
                                "month_name": {"type": "keyword"},
                                "data": {"type": "nested", "dynamic": "true"}
                            }
                        }
                    }
                },
                "Value-Conscious Shoppers": {
                    "type": "object",
                    "properties": {
                        "buyer_category": {"type": "keyword"},
                        "months": {
                            "type": "nested",
                            "dynamic": "true",
                            "properties": {
                                "month_name": {"type": "keyword"},
                                "data": {"type": "nested", "dynamic": "true"}
                            }
                        }
                    }
                },
                "Budget Buyers": {
                    "type": "object",
                    "properties": {
                        "buyer_category": {"type": "keyword"},
                        "months": {
                            "type": "nested",
                            "dynamic": "true",
                            "properties": {
                                "month_name": {"type": "keyword"},
                                "data": {"type": "nested", "dynamic": "true"}
                            }  
                        }
                    }
                }
            }
        },
        "created_on": {"type": "date"},
        "modified_on": {"type": "date"},
    }
}