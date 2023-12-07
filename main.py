import os, sys
import pandas as pd
import numpy as np
from insurance.constant import *
from insurance.logger import logging
from insurance.exception import CustomException
from insurance.pipeline.training_pipeline import TrainingPipeline

def main():
    try:
        pipeline = TrainingPipeline()
        pipeline.run_pipeline()
    except Exception as e:
        logging.error(f"{e}")


if __name__ == '__main__':
    main()