from pydantic import BaseModel
class user(BaseModel):
    name:str
    age:int

user_data={
    "name":"Moth",
    "age":"twenty five"
}

user=user(**user_data)

print(user)
print(type(user))