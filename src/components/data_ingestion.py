import os
import sys
from src.exception import CUstomException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass


@dataclass
class DataIndestionConfig:
    train_data_path: str=os.path.joim('artifacts',"train.csv")
    test_data_path: str=os.path.joim('artifacts',"test.csv")
    raw_data_path: str=os.path.joim('artifacts',"data.csv")


class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIndestionConfig()