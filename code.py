# Name: Fernando Bezerra
# Student Number: 041100707

from adafruit_circuitplayground import cp


while True:
    
    # Try used to check the inputs from the user.
    try:
        
        # Prompt user for the number of LEDs
        num_leds = int(input("Enter the number of LEDs to switch on (1-10): "))
        
        # Check if the number is within the valid 'range'
        if 1 <= num_leds <= 10:
        
        # Turn on LEDs using a for loop
            for i in range(0, num_leds):
                cp.pixels[i]=(0,0,255)
                         
        else:
            # Message when the user trying to enter with a unavailable number
            print("Number out of range. Please enter a number between 1 and 10.")

    # Exception created in case the value entered is no available.    
    except:
        # Message when the user type a letter instead of a number
        print('That was a no valid number!')
        
    # Prompt if user wants to start again
    restart = input("Do you want to start again? (n to stop, any other key to continue): ").lower()
    
    if restart != 'n':
        # Turn the lights on
        for i in range(0, num_leds):
            cp.pixels[i]=(0,0,0)
           
    else: 
        #Initializing variable
        i = 0
        
        #Turn off the lights
        while i < 10:
                cp.pixels[i]=(0,0,0) 
                i += 1   
        print("Program ended.")
        break