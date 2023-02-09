import zipfile
import io
from google.colab import files

# Compress the folder into a zip file
zip_file = zipfile.ZipFile("folder.zip", "w")
for root, dirs, files in os.walk("path/to/folder"):
    for file in files:
        zip_file.write(os.path.join(root, file))
zip_file.close()

# Upload the zip file to Colab
uploaded = files.upload()

# Extract the zip file in Colab
zip_file = zipfile.ZipFile(io.BytesIO(uploaded["folder.zip"]), "r")
zip_file.extractall()
zip_file.close()