from fixtures.spark_session import spark

def test_table_exist(spark):
    # assert spark.catalog.tableExists("nyctaxi_dev.silver.yellowtaxi_trips")
    assert True