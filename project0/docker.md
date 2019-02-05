0. docker build -t project0 .
1. docker run -d -it --name project0  -v $PWD:/vagrant -p 8888:8888 -p 5432:5432 project0
2. docker exec -it project0 bash
3. psql --command "CREATE USER vagrant WITH SUPERUSER PASSWORD 'vagrant';"
4. createdb university -O vagrant vagrant
5. psql university
6. \i DDL.sql 
7. \i smallRelationsInsertFile.sql
8. jupyter notebook --port=8888 --no-browser --ip=0.0.0.0
