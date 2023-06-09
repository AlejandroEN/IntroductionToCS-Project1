from pandas import DataFrame, read_csv

tfidf_data: DataFrame = read_csv("../res/tfidf_matrix_and_cluster.csv")
tfidf_data.drop(tfidf_data.columns[0:-1], axis=1, inplace=True)

pokemon_data: DataFrame = read_csv("../res/smogon.csv")
tfidf_data["Pokemon"] = pokemon_data["Pokemon"]

tfidf_data.to_csv("../res/tfidf_pokemon_and_cluster.csv")
print("El archivo pokemon_and_cluster.csv se ha creado con éxito")