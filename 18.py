import boto3
from botocore.client import Config

ACCESS_KEY = "ВАШ_ИДЕНТИФИКАТОР_КЛЮЧА"
SECRET_KEY = "ВАШ_СЕКРЕТНЫЙ_КЛЮЧ"

def upload_file(bucket_name, local_file_path, object_name=None):
    """Загружает файл в указанный бакет."""
    if object_name is None:
        object_name = local_file_path

    session = boto3.session.Session()
    client = session.client(
        's3',
        endpoint_url='https://storage.yandexcloud.net',
        aws_access_key_id=ACCESS_KEY,
        aws_secret_access_key=SECRET_KEY,
        config=Config(region_name='ru-central-1', signature_version='s3v4')
    )

    try:
        client.upload_file(local_file_path, bucket_name, object_name)
        print(f"Файл {local_file_path} успешно загружен в {bucket_name}/{object_name}")
    except Exception as e:
        print(f"Ошибка загрузки: {e}")

if __name__ == "__main__":
    upload_file("my-bucket", "image.png", "image.png")
