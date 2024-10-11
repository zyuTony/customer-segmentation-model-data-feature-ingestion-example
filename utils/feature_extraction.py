from abc import ABC, abstractmethod
from utils.config import *

class features_generator(ABC):
    def __init__(self, raw_data):
        pass

class product_features_generator(features_generator):

    def product_frequency_features(self):
        pass

    def product_monetary_features(self):
        pass

    def product_recency_features(self):
        pass

    def product_custom_tag_features(self):
        pass

    def product_diversity(self):
        pass

    def product_shopping_pattern(self):
        pass


class channel_features_generator(features_generator):
    def device_types_features(self):
        pass

    def brand_channel_features(self):
        pass

    def marketing_channels_features(self):
        pass

    def price_sensitivity_features(self):
        pass

class website_features_generator(features_generator):
    def get_browsing_habits(self):
        pass

    def get_browsed_product_types(self):
        pass
