# -*- coding: utf-8 -*-
import abc


class Factory:
    def process(self):
        self.get_data()
        self.parse_data()

    @abc.abstractmethod
    def get_data(self):
        pass

    @abc.abstractmethod
    def parse_data(self):
        pass

    @abc.abstractmethod
    def save_data(self):
        pass
