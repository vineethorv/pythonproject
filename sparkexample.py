

fifa_df = spark.read.csv("path-of-file/fifa_players.csv", inferSchema = True, header = True)

fifa_df.show()