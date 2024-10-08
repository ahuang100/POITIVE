import time
import threading
import smtplib
from email.mime.text import MIMEText
import sys
import model_predict

def send_sms_via_email(phone_number, carrier_gateway, sender_email, sender_password):
    sms_gateway = f"{phone_number}@{carrier_gateway}"
    msg = MIMEText("The curb parking spot is now empty.")
    msg['From'] = sender_email
    msg['To'] = sms_gateway
    msg['Subject'] = "Parking Spot Alert"
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, sms_gateway, msg.as_string())
    server.quit()
    print_notification("Notification sent!")

def print_notification(message):
    sys.stdout.write("\r" + " " * 80 + "\r")  # Clear the current line to flush terminal buffer 
    print(message)


def open_curb_detection(car_length, cycle_timer, phone_number, carrier_gateway, sender_email, sender_password, stop_event):
    while not stop_event.is_set():
        is_curb_open = model_predict.predict(car_length)
        
        if is_curb_open:
            print_notification("Open curb detected! Sending SMS notification...")
            send_sms_via_email(phone_number, carrier_gateway, sender_email, sender_password)
        else:
            print_notification("No open curb detected. Continuing to monitor...")

        stop_event.wait(cycle_timer * 60)  # Allow early exit if the stop_event is set, this is the interval of time before is_curb_open call is made


def control_toggle(car_length, cycle_timer, phone_number, carrier_gateway, sender_email, sender_password):
    toggle = False
    stop_event = threading.Event()
    thread = None

    try:
        while True:
            sys.stdout.write("Toggle curb detection on or off whenever by inputting (on/off): ")
            sys.stdout.flush()
            user_input = input().lower()

            if user_input == 'on' and not toggle:
                toggle = True
                stop_event.clear()  # Reset the stop event
                print_notification("Toggle is ON. Starting curb detection...")
                thread = threading.Thread(target=open_curb_detection, args=(car_length, cycle_timer, phone_number, carrier_gateway, sender_email, sender_password, stop_event))
                thread.start()

            elif user_input == 'off' and toggle:
                toggle = False
                print_notification("Toggle is OFF. Stopping curb detection...")
                stop_event.set()  # Signal the thread to stop
                if thread:
                    thread.join()  # Wait for the thread to stop
                    thread = None  # Clear the thread reference

            elif user_input not in ['on', 'off']:
                print_notification("Invalid input. Please enter 'on' or 'off'.")

    except KeyboardInterrupt:
        print("\nExiting program...")
        stop_event.set()  # Ensure the thread stops
        if thread:
            thread.join()  # Wait for the thread to stop
        sys.exit(0)

if __name__ == "__main__":
    car_length = float(input("Enter car length in inches: "))
    cycle_timer = float(input("Enter cycle timer (in minutes): "))
    phone_number = str(input("Enter phone number for SMS notifications: "))
    carrier_gateway = "txt.att.net"
    sender_email = "reedthompson776@gmail.com"
    sender_password = "lhji okgx qmzi jwwk"
    
    control_toggle(car_length, cycle_timer, phone_number, carrier_gateway, sender_email, sender_password)
