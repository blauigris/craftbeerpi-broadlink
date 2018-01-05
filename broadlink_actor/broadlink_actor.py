from modules import cbpi
from modules.core.hardware import ActorBase
from modules.core.props import Property

from broadlink_actor.util import get_device


@cbpi.actor
class BroadlinkActor(ActorBase):
    # custom property
    ip = Property.Text("IP", True, None)

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