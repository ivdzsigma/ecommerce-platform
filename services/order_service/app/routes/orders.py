# services/order_service/app/routes/orders.py
from fastapi import APIRouter, Depends, HTTPException
from ..models import Order
from ..schemas import OrderCreate, OrderResponse
from ..utils.rabbitmq import send_order_to_queue

router = APIRouter()

@router.post("/orders", response_model=OrderResponse)
async def create_order(order: OrderCreate):
    db_order = Order(**order.dict())
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    send_order_to_queue(db_order.id)  # Send order ID to RabbitMQ
    return db_order

@router.get("/orders/{order_id}", response_model=OrderResponse)
async def get_order(order_id: int):
    db_order = db.query(Order).filter(Order.id == order_id).first()
    if not db_order:
        raise HTTPException(status_code=404, detail="Order not found")
    return db_order