from enum import Enum as PyEnum

class OrderStatus(str, PyEnum):
    PENDING = "pending"
    PROCESSING = "processing"
    DELIVERING = "delivering"
    COMPLETE = "complete"