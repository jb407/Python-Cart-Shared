from typing import Union
from datetime import datetime
from pydantic import BaseModel
from common import OrderStatus

class ItemDto(BaseModel):
    id: int

    class Config:
        from_attributes = True

class VeggieDto(ItemDto):
    vegName: str

class UnitPriceVeggieDto(VeggieDto):
    unitPrice: float
    quantity: int

class PackVeggieDto(VeggieDto):
    pricePerPack: float
    quantity: int


class PersonDto(BaseModel):
    id: int
    firstName: str
    lastName: str
    userName: str

    class Config:
        from_attributes = True

class StaffDto(PersonDto):
    dateJoined: datetime
    deptName: str

class CustomerDto(PersonDto):
    custAddress: str
    custBalance: float
    maxOwing: float

class OrderDto(BaseModel):
    date: datetime
    lines: list[ItemDto]
    status: OrderStatus
    userId: int

ItemResponse = Union[UnitPriceVeggieDto, PackVeggieDto]
PersonResponse = Union[StaffDto, CustomerDto]
