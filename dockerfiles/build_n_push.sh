docker build -t tonyyang/sqlflow:jhub -f Dockerfile.jhub .
docker push tonyyang/sqlflow:jhub
docker build -t tonyyang/sqlflow:nb -f Dockerfile.nb .
docker push tonyyang/sqlflow:nb
docker build -t tonyyang/sqlflow:sqlflow -f Dockerfile.sqlflow .
docker push tonyyang/sqlflow:sqlflow

