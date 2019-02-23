import abc


class Supper(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def hello(self):
        pass
