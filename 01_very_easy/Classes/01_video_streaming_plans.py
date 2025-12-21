class BasicPlan:
    can_stream: bool = True
    can_download: bool = True
    has_SD: bool = True
    has_HD: bool = False
    has_UHD: bool = False
    num_of_devices: int = 1
    price: str = "$8.99"


class StandardPlan:
    can_stream: bool = True
    can_download: bool = True
    has_SD: bool = True
    has_HD: bool = True
    has_UHD: bool = False
    num_of_devices: int = 2
    price: str = "$12.99"


class PremiumPlan:
    can_stream: bool = True
    can_download: bool = True
    has_SD: bool = True
    has_HD: bool = True
    has_UHD: bool = True
    num_of_devices: int = 4
    price: str = "$15.99"


print(BasicPlan.has_SD)
print(PremiumPlan.has_SD)
print(BasicPlan.has_UHD)
print(BasicPlan.price)
print(PremiumPlan.num_of_devices)
