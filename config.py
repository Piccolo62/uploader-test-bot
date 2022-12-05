import os

class Config(object):
    
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5820757370:AAGsZsHjC6nA1myTmyAqc_1Deb-A0_6XY_s")
    
    API_ID = int(os.environ.get("API_ID", "13757798"))
    
    API_HASH = os.environ.get("API_HASH", "02d664f25512e22447470a7119790f6a")
    
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    
    MAX_FILE_SIZE = 50000000

    TG_MAX_FILE_SIZE = 2097152000

    FREE_USER_MAX_FILE_SIZE = 50000000
    
    CHUNK_SIZE = int(128)

    HTTP_PROXY = ""
    
    MAX_MESSAGE_LENGTH = 4096
    
    PROCESS_MAX_TIMEOUT = 3600
    
    OWNER_ID = int(os.environ.get("OWNER_ID", "846955346"))

    SESSION_NAME = "UploadLinkToFileBot"
    
    DATABASE_URL = os.environ.get("DATABASE_URL", "")

    MAX_RESULTS = "50"
