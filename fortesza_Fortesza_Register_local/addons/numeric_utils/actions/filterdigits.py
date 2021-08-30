"""This module contains the FilterDigits proxy action class."""
from src.testproject.classes import ProxyDescriptor
from src.testproject.sdk.addons import ActionProxy


class FilterDigits(ActionProxy):
    def __init__(self, input: str):
        super().__init__()
        self.proxydescriptor = ProxyDescriptor(
            guid="GeAOQXvdY0CkfHDs9c_yHA",
            classname="io.testproject.addon.FilterDigits"
        )
        self.input = input
        self.output = None
