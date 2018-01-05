import broadlink


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