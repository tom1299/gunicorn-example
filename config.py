import k8s_utils

bind = '0.0.0.0:8000'
workers = 1
loglevel = "info"

# Server Hooks
on_starting = k8s_utils.get_api_client