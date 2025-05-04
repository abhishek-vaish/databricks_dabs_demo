from fixtures.spark_session import spark

def test_tableExist(spark):
    df = spark.sql("SELECT * from nyctaxi_dev.bronze.yellow_trips")
    assertNotEqual(df.count(), 0)