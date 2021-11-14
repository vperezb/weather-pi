import logging

from io import StringIO
import configparser

from flask import Flask, request
from google.cloud import storage

config = configparser.ConfigParser()
config.read('config.cfg')

def _get_google_storage_client():
    return storage.Client(config['GoogleCloud']['Project'])

def _upload_string_to_google_storage(string, bucket_name, destination_blob_name):
    """Uploads a string to the bucket."""
    storage_client = _get_google_storage_client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_string(
        string, content_type= 'text/csv')
    return blob.public_url

def list_blobs(bucket_name):
    """Lists all the blobs in the bucket."""
    # bucket_name = "your-bucket-name"

    storage_client = storage.Client()

    # Note: Client.list_blobs requires at least package version 1.17.0.
    blobs = storage_client.list_blobs(bucket_name)

    return blobs


def get_blob_as_string(blob_name):
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(config['GoogleCloud']['Bucket'])
    #blob = bucket.get_blob(blob_name) Aqui ya haría el get, por lo que al hacer el as string lo peta
    blob = bucket.blob(blob_name)
    return blob.download_as_string()
 

app = Flask(__name__)


@app.route('/', methods = ['GET'])
def root():
    print (str(list(list_blobs(config['GoogleCloud']['Bucket']))))
    return '<h1>weather-pi</h1>' + str([ '<a href="/view-file?n={bn}">{bn}</a>'.format(bn=blob.name) for blob in list_blobs(config['GoogleCloud']['Bucket']) ] )
# return jsonify({'h1': 'weather-pi-home',
#    'days-uploaded': [ '{host}view-file?n={bn}'.format(host=request.host_url, bn=blob.name) for blob in list_blobs(config['GoogleCloud']['Bucket']) ]})

@app.route('/upload', methods = ['POST'])
def upload():
    posted_file = str(request.files['inputfile.csv'].read(), 'utf-8')
    register_day = request.form['register_day']
    _upload_string_to_google_storage(posted_file, config['GoogleCloud']['Bucket'], '{}.csv'.format(register_day.replace('-','/')))
    return 'created', 201


@app.route('/view-file', methods = ['GET'])
def view_file():
    file = get_blob_as_string(request.args['n'])
    # file = file.decode('utf-8')
    # file = StringIO(file)  
    # file.read()
    return file



    
@app.errorhandler(500)
def server_error(e):
    logging.exception('An error occurred during a request.')
    return """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(e), 500


if __name__ == '__main__':
    # This is used when running locally. Gunicorn is used to run the
    # application on Google App Engine. See entrypoint in app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
