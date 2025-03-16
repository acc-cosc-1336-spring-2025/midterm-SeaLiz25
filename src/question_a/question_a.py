#write functions here, don't add input('') statements here!
def test_config():
    return True

def get_person_category(age):

    if age < 0:
        return "invalid number"
    elif age <= 1:
        return "infant"
    elif age <= 13:
        return "child"
    elif age <20:
        return "teenager"
    elif age <= 125:
        return "adult"
    else:
        return "invalid number"    
    