def create_prompt(city_name, buyer_category, month_name):
    prompt = [
                {
                    "role": "system",
                    "content": "Act as you are a surveyor or data provider for [City]. Your objective is to generate data for a client engaged in B2B import-export business. Your task is to create relevant datasets for their business needs. Please provide the following information:\n\n1. Enter the city name: [City]\n2. Enter the buyer category (e.g., High-End Connoisseurs, Value-Conscious Shoppers, Budget Buyers): [BuyerCategory]\n3. Enter the month for data generation: [Month]\n\nNow, please carefully comprehend my instructions for generating the desired output.\n\nInstructions:\n1. For each buyer category, you need to generate data for the specified month.\n\nFor the given month:\n  a. Generate data for product categories such as Agriculture, Food, Fashion Accessories, etc.\n  b. Create a list of festivals and the products required for the specified month.\n\nNote: The given task is a 'sequential process.' Additionally, provide insights into the prevailing weather conditions, considering factors such as temperature, precipitation, and any seasonal changes.\n\nSpecify product needs related to festivals and weather for the specified buyer category within [City]. For each identified festival and weather condition, outline the specific products within industries such as fashion, electronics, food, and more, that are likely to experience increased demand.\n\nEnsure that the information is relevant and up-to-date, providing businesses with valuable insights into the dynamic relationship between cultural events, seasonal changes, and consumer product preferences in [City].\n\nNote: If certain data is not available, make predictions based on relevant factors.\n\nGive response in json format. Strictly follow the given output format. Make sure that your response is the same as the given output format and do not add data by your own. In output if the value is a string then it should only be one value, not multiple values."
                },
                {
                    "role": "user",
                    "content": f"Input: \nCity : {city_name}, BuyerCategory : {buyer_category}, Month : {month_name}\n\nOutput format:" + "{\"City\": \"[City]\", \"BuyerCategory\": \"[BuyerCategory]\", \"Month\": \"[Month]\", \"Data\": { \"Festival\":[list of festivals], \n\"ProductCategories\": {\n\"Product categories name\": [list of keywords]},\n\"WetherCondition\": {\n\"Temperature\": <value:str>, \"Precipitation\": <value:str>, \"SeasonalChanges\": <value:str>} }}"
            }
            ]
    return prompt

BUYER_CATEGORIES = [
    "High-End Connoisseurs",
    "Value-Conscious Shoppers",
    "Budget Buyers",
]

MONTH_NAMES = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]
