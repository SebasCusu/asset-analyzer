from bruh import get_current_price_BTC
import time

def check_alert(current_price, target_price, alert_option):
    #Function to check if the target price has been reached
    #Returns True if the target price has been reached
    #Else Returns False
    

    if alert_option == 1:
        if current_price >= target_price:
            return True
    
    if alert_option == 2:
        if current_price <= target_price:
            return True
        
    return False

#Main Menu
print("Bitcoin Alert")
print(f"1: Rise Alert")
print(f"2: Fall Alert")

alert_option = int(input("Select the Type of Alert: "))

    


options = {
    1: "Rise",   
    2: "Fall"
}


if alert_option not in options:
    print("Invalid Option")
    exit()
    
else:
    while True:
        try:
            alert_option = options[alert_option]
            target_price = float(input("Write the Target Price: "))
            current_price = get_current_price_BTC()
            verification = check_alert(current_price, target_price, alert_option)
            print(f"\nAlert Type: {alert_option}")
            print(f"Current Price: {current_price}")
            print(f"Target Price: {target_price}")
            print(f"Target Achieved: {verification}")
            
            if verification:
                print("Alert Activated Target Achieved")
                break
        
            time.sleep(243)
            
        except ValueError:
            print("Invalid Option")