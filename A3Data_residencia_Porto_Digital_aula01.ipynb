%%bash
# Instal Java
apt-get update && apt-get install openjdk-8-jdk-headless -qq > /dev/null

# Install PySpark
pip install -q pyspark
import os
os.environ['JAVA_HOME'] = '/usr/lib/jvm/java-8-openjdk-amd64'

from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("AtividadeSQL").getOrCreate()

def q(query, n=30):
    return spark.sql(query).show(n=n, truncate=False)
q("""
    SELECT *
    FROM tabela
""")

!curl -O https://raw.githubusercontent.com/neylsoncrepalde/titanic_data_with_semicolon/main/titanic.csv
# Leitura da tabela para realização de consultas
titanic = spark.read.csv("titanic.csv", header=True, sep=";", inferSchema=True)
titanic.printSchema()
titanic.createOrReplaceTempView("titanic")
q("""

  SELECT *
  FROM titanic
  LIMIT 10

""")
q("""
  SELECT COUNT(1) as contagem
  FROM titanic
""")
