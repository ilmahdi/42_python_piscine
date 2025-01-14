def NULL_not_found(object: any) -> int:
    obj_type = type(object)
    if object is None:
        print(f"Nothing: None {obj_type}")
    elif isinstance(object, float) and object != object:
        print(f"Cheese: nan {obj_type}")
    elif object is False:
        print(f"Fake: {object} {obj_type}")
    elif object == 0:
        print(f"Zero: {object} {obj_type}")
    elif object == "":
        print(f"Empty: {obj_type}")
    else:
        print("Type not Found")
        return 1
    return 0
