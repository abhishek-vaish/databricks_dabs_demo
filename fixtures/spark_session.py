import pytest
from pyspark.sql import SparkSession

@pytest.fixtures()
def spark():
    return SparkSession.builder.appName("spark_testing").getOrCreate()