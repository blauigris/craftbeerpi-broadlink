from modules import cbpi
from modules.core.hardware import ActorBase
from modules.core.props import Property

from .util import get_device


@cbpi.actor
class BroadlinkActor(ActorBase):
    # custom property
    ip = Property.Text("IP", True, None)

    def state(self):
        """
        Retrive device state
        :return:
        """
        device = get_device(self.ip)
        return device.check_power()

    def on(self, power=0):
        """
        Code to switch on the actor
        :param power: int value between 0 - 100
        :return:
        """
        device = get_device(self.ip)
        device.set_power(True)

    def off(self):
        """
        Code to switch off the actor
        :return:
        """
        device = get_device(self.ip)
        device.set_power(False)
