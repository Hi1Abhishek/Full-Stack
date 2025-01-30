# def shape_match(shape):
   
#     if shape == "circle":
#         return "Round shape"
#     elif shape in ("square", "rectangle"):
#         return "Four-sided shape"
#     elif shape == "triangle":
#         return "Three-sided shape"
#     else:
#         return "Unknown shape"

# print(shape_match("circle"))    
# print(shape_match("square"))  
# print(shape_match("triangle"))   
# print(shape_match("hexagon"))    

def shape_match(shape):
    if shape == "circle":
        return "Round shape"
    elif shape in ("square", "rectangle"):
        return "Four-sided shape"
    elif shape == "triangle":
        return "Three-sided shape"
    else:
        return "Unknown shape"
    
    print(shape_match("circle"))
    print(shape_match("square"))
    print(shape_match("triaangle"))
    print(shape_match("hexagon"))
    