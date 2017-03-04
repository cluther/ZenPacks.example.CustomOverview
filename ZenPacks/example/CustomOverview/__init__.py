from Products.ZenModel.Device import Device
from Products.Zuul.infos import ProxyProperty
from Products.Zuul.infos.device import DeviceInfo


# Set a default value for a device's contact.
Device.contact = ''

# Make a device's contact available through the API.
DeviceInfo.contact = ProxyProperty('contact')

# You can swap ProxyContact with any property/attribute on Device.
# For example, if you wanted to reference a cProperty instead:
#DeviceInfo.contact = ProxyProperty('cPropContact')
# Or a zProperty
#DeviceInfo.contact = ProxyProperty('zCommandUsername')
