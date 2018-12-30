import textwrap

import eusbip.usbip


def test_parse_listing_device():
    listing = [
        'busid 1-1.1.1 (0424:7800)',
        'Standard Microsystems Corp. : unknown product (0424:7800)',
    ]

    devices = eusbip.usbip.parse_listing_device(listing)

    assert devices == eusbip.usbip.Device(
        bus_number=1,
        device_number=(1, 1, 1),
        vendor_id=0x0424,
        product_id=0x7800,
        vendor_name='Standard Microsystems Corp.',
        product_name='unknown product',
    )


def test_parse_listing():
    output = """\
 - busid 1-1.1.1 (0424:7800)
   Standard Microsystems Corp. : unknown product (0424:7800)

 - busid 1-1.1.2 (0c72:000c)
   PEAK System : PCAN-USB (0c72:000c)
"""

    devices = eusbip.usbip.parse_listing(output)

    assert devices == (
        eusbip.usbip.Device(
            bus_number=1,
            device_number=(1, 1, 1),
            vendor_id=0x0424,
            product_id=0x7800,
            vendor_name='Standard Microsystems Corp.',
            product_name='unknown product',
        ),
        eusbip.usbip.Device(
            bus_number=1,
            device_number=(1, 1, 2),
            vendor_id=0x0c72,
            product_id=0x0000c,
            vendor_name='PEAK System',
            product_name='PCAN-USB',
        ),
    )


def test_devices_match():
    this = eusbip.usbip.Device(
        bus_number=1,
        device_number=2,
        vendor_id=3,
        product_id=4,
        vendor_name=5,
        product_name=6,
    )

    that = eusbip.usbip.Device(
        bus_number=1,
        device_number=2,
        vendor_id=3,
        product_id=None,
        vendor_name=None,
        product_name=6,
    )

    assert this.matches(that)


def test_devices_do_not_match():
    this = eusbip.usbip.Device(
        bus_number=1,
        device_number=2,
        vendor_id=3,
        product_id=4,
        vendor_name=5,
        product_name=6,
    )

    that = eusbip.usbip.Device(
        bus_number=1,
        device_number=2,
        vendor_id=4,
        product_id=None,
        vendor_name=None,
        product_name=6,
    )

    assert not this.matches(that)
