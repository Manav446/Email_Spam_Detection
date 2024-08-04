from pathlib import Path

CONFIG_FILE_PATH = Path("./config/config.yaml")
PARAMS_FILE_PATH = Path("./D:/Manav/Personal_Projects/Email_Spam_Detection/params.yaml")
GOOGLE_DRIVE_DOWNLOAD_PREFIX_URL = "https://drive.google.com/uc?/export=download&id="

EMAIL_CLASSIFICATION_FOLDER_NAME = "common_data"

UNZIP_DIR = "artifacts/data_ingestion"

INPUT_FILE_NAME = "spam_Emails_data.csv"
INPUT_FILE_INDEPENDENT_VARIABLE = "text"
INPUT_FILE_TARGET_VARIABLE = "label"

INPUT_PICKLE_FILE_NAME = "input_variable.pkl"
TARGET_PICKLE_FILE_NAME = "target_variable.pkl"