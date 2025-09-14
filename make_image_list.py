import os

# use current folder
folder = "."

files = [f for f in os.listdir(folder) if f.lower().endswith((".png", ".jpg", ".jpeg"))]
files.sort()

out_path = "images.js"
with open(out_path, "w") as out:
    out.write("const images = [\n")
    for f in files:
        out.write(f'  "images/{f}",\n')
    out.write("];\n")

print(f"✅ Wrote {len(files)} images into {out_path}")
