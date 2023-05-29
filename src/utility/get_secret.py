# Import the Secret Manager client library.
from google.cloud import secretmanager

def get_secret(project_id, secret_id, version : str='latest'):
    """
    Get information about the given secret. This only returns metadata about
    the secret container, not any secret material.
    """

    # Create the Secret Manager client.
    client = secretmanager.SecretManagerServiceClient()

    # Build the resource name of the secret.
    name = client.secret_path(project_id, secret_id)

    # Get the secret.
    # response = client.get_secret(request={"name": name})
    response = client.access_secret_version(request={"name": "{}/versions/{}".format(name,version)})

    # # Get the replication policy.
    # if "automatic" in response.replication:
    #     replication = "AUTOMATIC"
    # elif "user_managed" in response.replication:
    #     replication = "MANAGED"
    # else:
    #     raise "Unknown replication {}".format(response.replication)

    # Print data about the secret.
    # print("Got secret {} with replication policy {}".format(response.name, replication))
    return response.payload.data.decode("UTF-8")