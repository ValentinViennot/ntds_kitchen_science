#taken from this StackOverflow answer: https://stackoverflow.com/a/39225039
import requests
import hashlib

def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def download_file_from_google_drive(id, destination):
    URL = "https://docs.google.com/uc?export=download"

    session = requests.Session()

    response = session.get(URL, params = { 'id' : id }, stream = True)
    token = get_confirm_token(response)

    if token:
        params = { 'id' : id, 'confirm' : token }
        response = session.get(URL, params = params, stream = True)

    save_response_content(response, destination)    

def get_confirm_token(response):
    for key, value in response.cookies.items():
        if key.startswith('download_warning'):
            return value

    return None

def save_response_content(response, destination):
    CHUNK_SIZE = 32768

    with open(destination, "wb+") as f:
        for chunk in response.iter_content(CHUNK_SIZE):
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)

checksum = '69478c5beac54447b8914f7403d6af43'
file_id = '1LFu2qxOlWYR3_07LvQYe_ydS3nkinK4S'
destination = './data/recipes_with_nutritional_info_fixed_qty.json'
download_file_from_google_drive(file_id, destination)
assert md5(destination) == checksum

print('ingredients dataset successfully downloaded!')