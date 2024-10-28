import logging
import k8s_utils
import kubernetes

logger = logging.getLogger(__name__)

def app(environ, start_response):

    # get to /healthz
    if environ['PATH_INFO'] == '/healthz':
        client = k8s_utils.get_api_client(None)
        api_response = kubernetes.client.VersionApi(client).get_code()
        print("Server version: " + str(api_response))

        start_response("200 OK", [("Content-Type", "text/plain")])
        return iter([b"OK\n"])

    k8s_utils.get_core_v1_client(logger)
    data = b"Hello, World!\n"
    start_response("200 OK", [
        ("Content-Type", "text/plain"),
        ("Content-Length", str(len(data)))
    ])
    return iter([data])