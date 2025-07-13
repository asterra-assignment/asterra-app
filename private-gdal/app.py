from flask import Flask
import subprocess

app = Flask(__name__)

@app.route("/gdal-version")
def gdal_version():
    version = subprocess.check_output(["gdalinfo", "--version"]).decode().strip()
    return {"gdal_version": version}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
