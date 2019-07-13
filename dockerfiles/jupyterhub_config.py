import os
import socket


c.JupyterHub.spawner_class = 'kubespawner.KubeSpawner'

c.JupyterHub.ip = '0.0.0.0'
c.JupyterHub.hub_ip = '0.0.0.0'

# Don't try to cleanup servers on exit - since in general for k8s, we want
# the hub to be able to restart without losing user containers
c.JupyterHub.cleanup_servers = False

# First pulls can be really slow, so let's give it a big timeout
c.KubeSpawner.start_timeout = 60 * 10

# Find the IP of the machine that minikube is most likely able to talk to
# Graciously used from https://stackoverflow.com/a/166589
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
host_ip = s.getsockname()[0]
s.close()

c.KubeSpawner.hub_connect_ip = host_ip
c.JupyterHub.hub_connect_ip = c.KubeSpawner.hub_connect_ip

c.KubeSpawner.service_account = 'default'
# Do not use any authentication at all - any username / password will work.
c.JupyterHub.authenticator_class = 'dummyauthenticator.DummyAuthenticator'

c.KubeSpawner.image_pull_policy = 'Always'
c.KubeSpawner.storage_pvc_ensure = False

c.JupyterHub.allow_named_servers = True

c.KubeSpawner.extra_pod_config.update({'restartPolicy': 'Never'})

# container tonyyang/sqlflow:sqlflow need to be run at root to start MySQL
c.KubeSpawner.uid = 0
c.KubeSpawner.profile_list = [
    {
        'display_name': 'SQLFlow Playground',
        'default': True,
        'kubespawner_override': {
            'image': 'tonyyang/sqlflow:nb',
            'cpu_limit': 0.5,
        },
        'description': 'Brings SQL and AI together. <a href="https://sqlflow.org">https://sqlflow.org</a>'
    }
]

c.KubeSpawner.extra_containers = [{
    "name": "sqlflow",
    "image": "tonyyang/sqlflow:sqlflow",
    # liveness Probe to Jupyter Notebook server
    "livenessProbe": {
        "exec" : {
	    "command": ["curl", "localhost:8888"]
	},
	"initialDelaySeconds": 600,
	"periodSeconds": 60,
    }
}]

