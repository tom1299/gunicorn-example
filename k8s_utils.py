import os
from kubernetes import client, config

def get_core_v1_client(server):

    if os.path.exists('/var/run/secrets/kubernetes.io/serviceaccount/token'):
        print("Using in-cluster configuration with service account token to access the API server")
        config.load_incluster_config()
        api_client = client.CoreV1Api()
    else:
        kubeconfig_path = os.getenv('KUBECONFIG')
        print(f"Using configuration from kubeconfig file at '{kubeconfig_path}'")

        config.load_kube_config(config_file=kubeconfig_path)

        username = os.getenv('K8S_USER')
        password = os.getenv('K8S_USER_PASSWORD')
        client.Configuration().username = username
        client.Configuration().password = password
        api_client = client.CoreV1Api()

    return api_client

def get_api_client(server):

    if os.path.exists('/var/run/secrets/kubernetes.io/serviceaccount/token'):
        print("Using in-cluster configuration with service account token to access the API server")
        config.load_incluster_config()
        api_client = client.ApiClient()
    else:
        kubeconfig_path = os.getenv('KUBECONFIG')
        print(f"Using configuration from kubeconfig file at '{kubeconfig_path}'")

        config.load_kube_config(config_file=kubeconfig_path)

        username = os.getenv('K8S_USER')
        password = os.getenv('K8S_USER_PASSWORD')
        client.Configuration().username = username
        client.Configuration().password = password
        api_client = client.ApiClient()

    return api_client