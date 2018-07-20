import requests
from argparse import ArgumentParser

def get_confirm_token(response):
	for key, value in response.cookies.items():
		if key.startswith('download_warning'):
			return value
	
	return None


def download(file_id, target_file_path):
	URL = "https://drive.google.com/uc?export=download"
	session = requests.Session()
	response = session.get(URL, params={'id': file_id}, stream=True)
	token = get_confirm_token(response)
	if token:
		params = {'id': file_id, 'confirm': token}
		response = session.get(URL, params=params, stream=True)

	CHUNK_SIZE = 2 ** 15
	with open(target_file_path, "wb") as f:
		for chunk in response.iter_content(CHUNK_SIZE):
			if chunk:
				f.write(chunk)
	

if __name__ == '__main__':
	parser = ArgumentParser()
	parser.add_argument('--file_id', required=True, help='file\'s id in google driver')
	parser.add_argument('--target_file_path', required=True, help='target file to save the file')
	args = parser.parse_args()

	download(args.file_id, args.target_file_path)
