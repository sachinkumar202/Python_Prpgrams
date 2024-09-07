import time

def countdown_timer(hours, minutes, seconds):
    total_seconds = hours * 3600 + minutes * 60 + seconds
    
    while total_seconds > 0:
        # Calculate the current hours, minutes, and seconds
        mins, secs = divmod(total_seconds, 60)
        hrs, mins = divmod(mins, 60)
        
        # Display the timer in HH:MM:SS format
        timer = f"{hrs:02d}:{mins:02d}:{secs:02d}"
        print(timer, end="\r")
        
        # Wait for 1 second
        time.sleep(1)
        
        # Decrease total time by one second
        total_seconds -= 1
    
    print("Time's up!")

def main():
    print("Countdown Timer")
    
    try:
        # Get user input for hours, minutes, and seconds
        hours = int(input("Enter hours: "))
        minutes = int(input("Enter minutes: "))
        seconds = int(input("Enter seconds: "))
        
        print(f"Starting timer for {hours:02d}:{minutes:02d}:{seconds:02d}")
        countdown_timer(hours, minutes, seconds)
        
    except ValueError:
        print("Invalid input. Please enter only numbers.")
    
if __name__ == "__main__":
    main()
