import boto3
from botocore.client import Config

ACCESS_KEY = "ВАШ_ИДЕНТИФИКАТОР_КЛЮЧА"
SECRET_KEY = "ВАШ_СЕКРЕТНЫЙ_КЛЮЧ"

def get_s3_client():
    """Создаёт и возвращает S3-клиент для Yandex Object Storage."""
    session = boto3.session.Session()
    client = session.client(
        's3',
        endpoint_url='https://storage.yandexcloud.net',
        aws_access_key_id=ACCESS_KEY,
        aws_secret_access_key=SECRET_KEY,
        config=Config(region_name='ru-central-1', signature_version='s3v4')
    )
    return client

if __name__ == "__main__":
    client = get_s3_client()
    print("S3-клиент успешно создан")
