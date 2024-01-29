import sys

import pandas as pd
#fancy pandas

print(sys.argv)

day = sys.argv[1]
print(f"job finished successfully for day {day}")

##Docker runs
# # docker run -it \
#   -e POSTGRES_USER="root" \
#   -e POSTGRES_PASSWORD="root" \
#   -e POSTGRES_DB="ny_taxi" \
#   -v "$(pwd)/ny_taxi_postgres_data:/var/lib/postgresql/data" \
#   -p 5431:5432 \
#   postgres:13

# #postgres with pgadmin
# docker run -it \
#   -e POSTGRES_USER="root" \
#   -e POSTGRES_PASSWORD="root" \
#   -e POSTGRES_DB="ny_taxi" \
#   -v "$(pwd)/ny_taxi_postgres_data:/var/lib/postgresql/data" \
#   -p 5431:5432 \
#   --network=pg-network \
#   --name pg-database \
#   postgres:13
#https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page

#docker network create pg-network


# python ingest_data.py \
#   --user=root \
#   --password=root \
#   --host=localhost \
#   --port=5432 \
#   --db=ny_taxi \
#   --table_name=yellow_taxi_trips \
#   --url=${"https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/yellow_tripdata_2021-01.csv.gz"}

# docker build -t taxi_ingest:v001 .

# URL="https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/yellow_tripdata_2021-01.csv.gz"
# URL="wget https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2019-09.csv.gz"

# docker run -it \
#   --network=pg-network \
#     taxi_ingest:v001 \
#    --user=root \
#    --password=root \
#    --host=pg-database \
#    --port=5432 \
#    --db=ny_taxi \
#    --table_name=green_taxi_trips \
#    --url=${URL}

# docker compose up

# or 

# docker compose up -d