# services/order_service/app/utils/rabbitmq.py
import pika

def send_order_to_queue(order_data):
    connection = pika.BlockingConnection(pika.ConnectionParameters("rabbitmq"))
    channel = connection.channel()
    channel.queue_declare(queue="orders"))
    channel.basic_publish(exchange="", routing_key="orders", body=str(order_data))
    connection.close()