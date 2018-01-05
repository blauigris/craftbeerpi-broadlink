import pytest

from broadlink_actor.util import get_device


class TestUtil(object):
    # TODO: Due the craftbeerpi modules import it fails, so before running the tests everything inside __init__.py mus
    # TODO: be commented. One possible solution is to patch the imports using mock.
    def test_get_device_no_ip(self):
        # MAKE SURE THERE IS A DEVICE AVAILABLE
        ip = None
        device = get_device(ip)
        assert device is not None

    def test_get_device_ip(self):
        # PUT YOUR IP HERE
        ip = '192.168.1.133'
        device = get_device(ip)
        assert device.host[0] == ip

    def test_get_device_incorrect_ip(self):
        # PUT YOUR IP HERE
        ip = '192.168.1.1'
        with pytest.raises(RuntimeError):
            device = get_device(ip)


