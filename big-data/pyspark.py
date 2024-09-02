import pyspark as spk
from pyspark.sql import SparkSession
import random as rd


dados = [("volta_1", rd.randint(60, 90), rd.randint(60, 90), rd.randint(60, 90), rd.randint(60, 90), rd.randint(60, 90), rd.randint(60, 90)),
         ("volta_2", rd.randint(60, 90), rd.randint(60, 90), rd.randint(60, 90), rd.randint(60, 90), rd.randint(60, 90), rd.randint(60, 90)),
         ("volta_3", rd.randint(60, 90), rd.randint(60, 90), rd.randint(60, 90), rd.randint(60, 90), rd.randint(60, 90), rd.randint(60, 90)),
         ("volta_4", rd.randint(60, 90), rd.randint(60, 90), rd.randint(60, 90), rd.randint(60, 90), rd.randint(60, 90), rd.randint(60, 90)),
         ("volta_5", rd.randint(60, 90), rd.randint(60, 90), rd.randint(60, 90), rd.randint(60, 90), rd.randint(60, 90), rd.randint(60, 90)),
         ("volta_6", rd.randint(60, 90), rd.randint(60, 90), rd.randint(60, 90), rd.randint(60, 90), rd.randint(60, 90), rd.randint(60, 90)),
         ("volta_7", rd.randint(60, 90), rd.randint(60, 90), rd.randint(60, 90), rd.randint(60, 90), rd.randint(60, 90), rd.randint(60, 90)),
         ("volta_8", rd.randint(60, 90), rd.randint(60, 90), rd.randint(60, 90), rd.randint(60, 90), rd.randint(60, 90), rd.randint(60, 90)),
         ("volta_9", rd.randint(60, 90), rd.randint(60, 90), rd.randint(60, 90), rd.randint(60, 90), rd.randint(60, 90), rd.randint(60, 90)),
         ("volta_10", rd.randint(60, 90), rd.randint(60, 90), rd.randint(60, 90), rd.randint(60, 90), rd.randint(60, 90), rd.randint(60, 90))]

# Montar a sessão
spark = SparkSession.builder.appName('corrida').getOrCreate()
columns = ["Voltas", "Leandro", "Minoru", "Jean", "Felipe", "Rodolfo", "Ayrton"]

pysparkDF = spark.createDataFrame(data = dados, schema = columns)
pysparkDF.printSchema()
pysparkDF.show()