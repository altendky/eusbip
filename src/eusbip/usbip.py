import attr


@attr.s
class Device:
    bus_number = attr.ib()
    device_number = attr.ib()
    vendor_id = attr.ib()
    product_id = attr.ib()
    vendor_name = attr.ib()
    product_name = attr.ib()

    def matches(self, other):
        if type(self) != type(other):
            return False

        for this, that in zip(attr.astuple(self), attr.astuple(other)):
            if None in (this, that):
                continue

            if this != that:
                return False

        return True


device_prefix = ' - '


def group_listing_lines(lines):
    listings = []

    for line in lines:
        if line.startswith(device_prefix):
            listings.append([])

        if len(line.strip()) > 0:
            listings[-1].append(line[len(device_prefix) - 1:].strip())

    return listings


def parse_listing(listing):
    line_groups = group_listing_lines(listing.splitlines())

    return tuple(
        parse_listing_device(lines)
        for lines in line_groups
    )


def parse_listing_device(lines):
    lines = iter(lines)

    _, bus, device_id = next(lines).split()
    bus_number, device_number = bus.split('-')
    bus_number = int(bus_number)
    device_number = tuple(
        int(number)
        for number in device_number.split('.')
    )

    vendor_id, product_id = (
        int(id, 16)
        for id in device_id[1:-1].split(':')
    )

    vendor_name, product_name = (
        name.strip()
        for name in next(lines)[:-len(device_id)].split(':')
    )

    return Device(
        bus_number=bus_number,
        device_number=device_number,
        vendor_id=vendor_id,
        product_id=product_id,
        vendor_name=vendor_name,
        product_name=product_name,
    )
