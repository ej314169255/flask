export POSTGRES_PASSWORD=1234
psql --host 127.0.0.1 -p 5431 -U user -d postgres -c "drop database netology"
# psql --host 127.0.0.1 -p 5431 -U user -d postgres -c "create database netology"
