from typing import TypedDict

class ProductReview(TypedDict):
    product_name:str
    rating:int
    review:str

# new_product=ProductReview(product_name="Headphone",rating=5,review='positive')
new_product:ProductReview={
    "product_name":"Wireless Headphone",
    "rating":5,
    "review":"positive"
}

print(new_product)