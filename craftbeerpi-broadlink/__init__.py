import broadlink
from modules import cbpi
from modules.core.hardware import ActorBase
from modules.core.props import Property


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


def get_device(ip):
    """
    Finds all the available broadlink smart switches and filters them by ip if needed
    :param ip:
    :return:
    """
    devices = broadlink.discover(timeout=5)
    if ip: # If we have an IP set return the required device
        try:
            device = next(device for device in devices if device.host[0] == str(ip))
        except StopIteration:
            raise RuntimeError('Broadlink actor at {} not found'.format(ip))
    else: # Otherwise return the first available
        try:
            device = devices[0]
        except IndexError:
            raise RuntimeError('Broadlink actor not found')
    # Auth before sending orders
    device.auth()
    return device
