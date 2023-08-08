def individual_serial(finance) -> dict:
    return{
        "id": str(finance["_id"]),
        "stock": finance["stock"],
        "price": finance["price"],
        "news": finance["news"]
    }

def list_serial(finances) -> list:
    return[individual_serial(finance) for finance in finances]