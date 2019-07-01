# sqlflow-on-k8s

Step 0: Get a k8s cluster.

Step 1: Grant pod-related permissions for the default user.

 ```
kubectl apply -f manifests/rbac.yaml
 ```

Step 2: Deploy the JupyterHub pod on Kubernetes.

```
$ kubectl create -f sqlflow-jhub.yaml
deployment.apps/sqlflow-jhub created
service/sqlflow-jhub created
```

Step 3: Find the external ip for `service/sqlflow-jhub`. In this case, it is `34.67.182.237`.

```
$ kubectl get all
NAME                                READY   STATUS    RESTARTS   AGE
pod/sqlflow-jhub-77858f4655-7wpt8   1/1     Running   0          2m39s

NAME                   TYPE           CLUSTER-IP      EXTERNAL-IP     PORT(S)          AGE
service/kubernetes     ClusterIP      10.47.240.1     <none>          443/TCP          80m
service/sqlflow-jhub   LoadBalancer   10.47.249.179   34.67.182.237   8000:31721/TCP   2m39s

NAME                           DESIRED   CURRENT   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/sqlflow-jhub   1         1         1            1           2m39s

NAME                                      DESIRED   CURRENT   READY   AGE
replicaset.apps/sqlflow-jhub-77858f4655   1         1         1       2m40s
```

Step 4: Open a browser and go to `<EXTERNAL-IP>:8000`.