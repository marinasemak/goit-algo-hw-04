from pathlib import Path

# return info about cats from the file
def get_cats_info(path):
    try: 
        with open(path, "r", encoding="utf-8") as fh:
            lines = [el.strip().split(",") for el in fh.readlines()]
            keys = ["id", "name", "age"]
            converted_lines = [dict(zip(keys, l)) for l in lines]
    except FileNotFoundError:
        print(f"File not found: {path}")
        return
    return converted_lines


with open("cats.txt", "w") as file:
    file.write("60b90c1c13067a15887e1ae1,Tayson,3\n")
    file.write("60b90c2413067a15887e1ae2,Vika,1\n")
    file.write("60b90c2e13067a15887e1ae3,Barsik,2\n")
    file.write("60b90c3b13067a15887e1ae4,Simon,12\n")
    file.write("60b90c4613067a15887e1ae5,Tessi,5\n")


cats_info = get_cats_info(Path("cats.txt"))
print(cats_info)
