import os


def get_key(keyname: str):
    if keyname == "GPT_API_KET":
        GPT_API_KET = os.environ.get("GPT_API_KET")
        return GPT_API_KET
    elif keyname == "GPT_ORG_KEY":
        GPT_ORG_KEY = os.environ.get("GPT_ORG_KEY")
        return GPT_ORG_KEY
    elif keyname == "FRED_API_KEY":
        FRED_API_KEY = os.environ.get("FRED_API_KEY")
        return FRED_API_KEY
    elif keyname == "MONGO_PWD":
        MONGO_PWD = os.environ.get("MONGO_PWD")
        return MONGO_PWD
    elif keyname == "MONGO_URI":
        MONGO_PWD = get_key("MONGO_PWD")
        MONGO_URI = YOUR MongoDB URI
        return MONGO_URI
    elif keyname == "GOGL_API_KEY":
        GOGL_API_KEY = os.environ.get("GOGL_API_KEY")
        return GOGL_API_KEY
    else:
        return None
