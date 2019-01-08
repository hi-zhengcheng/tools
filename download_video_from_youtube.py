from pytube import YouTube


"""The latest version dose not work correctly, You need to modify something as follows:

1. Install latest version: 
    pip install pytube
    
2. Locate where the module installed:
    import pytube
    print(pytube.__file__)
    
3. In the module path, find file: cipher.py

4. In get_initial_function_name method, add this pattern in front:
    r'\bc\s*&&\s*d\.set\([^,]+,.*?\((?P<sig>[a-zA-Z0-9$]+)\(\(0\s*,\s*window.decodeURIComponent',
    

View details from https://pypi.org/project/pytube/

"""


def download(video_id, save_dir='.'):
    """Download video from youtube by video_id.

    Video url is something like: https://youtube.com/watch?v={video_id}

    Arguments:
        video_id: video_id in the video url
        save_dir: dir to save the video
    """
    try:
        video_url = "https://youtube.com/watch?v={}".format(video_id)
        YouTube(video_url)\
            .streams\
            .first()\
            .download(output_path=save_dir, filename=video_id)

    except Exception as e:
        print(e)


if __name__ == '__main__':
    video_id = '95l18vjgmZQ'
    download(video_id)
