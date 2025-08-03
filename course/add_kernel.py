import os
import nbformat

# Root folder where your notebooks live
root_dir = "D:/GitHub/HF-notebooks"

# The kernelspec to apply
kernelspec = {
    "display_name": "Python (HF-notebooks)",
    "language": "python",
    "name": "HF-notebooks"
}

# Traverse all subdirectories
for dirpath, dirnames, filenames in os.walk(root_dir):
    for filename in filenames:
        if filename.endswith(".ipynb"):
            full_path = os.path.join(dirpath, filename)
            try:
                nb = nbformat.read(full_path, as_version=4)
                nb.metadata["kernelspec"] = kernelspec
                nbformat.write(nb, full_path)
                print(f"✅ Updated: {full_path}")
            except Exception as e:
                print(f"❌ Error with {full_path}: {e}")
