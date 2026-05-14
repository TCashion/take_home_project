from azure.storage.blob import BlobServiceClient

SERVICE_URL = "https://azurepublicdatasettraces.blob.core.windows.net/"
CONTAINER_NAME = "azurepublicdataset"


def get_container_client():
    """Return a ContainerClient for the public dataset container."""
    blob_service_client = BlobServiceClient(account_url=SERVICE_URL)
    return blob_service_client.get_container_client(CONTAINER_NAME)


def list_blobs(container_client):
    """Return a list of all blob names in the container."""
    return [blob.name for blob in container_client.list_blobs()]


def filter_blobs(blob_names, extension):
    """Return only the blob names that end with the given extension.

    Args:
        blob_names: An iterable of blob name strings.
        extension: A file extension string to filter by (e.g. ".csv.gz").

    Returns:
        A list of blob name strings matching the extension.
    """
    result = []

    if not extension: 
        return result

    for blob_name in blob_names:
        if blob_name.endswith(extension):
            result.append(blob_name)

    return result


def main():
    container_client = get_container_client()
    blob_names = list_blobs(container_client)
    filtered = filter_blobs(blob_names, ".csv.gz")
    print(f"Listing blobs ending in '.csv.gz' in container: {CONTAINER_NAME}")
    for name in filtered:
        print(name)


if __name__ == "__main__":
    main()