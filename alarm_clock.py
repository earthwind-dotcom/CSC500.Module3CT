def main():
    # Get user input
    current_time = int(input("Current time (0-23): "))
    hours_to_wait = int(input("Hours to wait: "))
    
    # Calculate alarm time
    alarm_time = (current_time + hours_to_wait) % 24
    
    # Display result
    print(f"\nAlarm will go off at {alarm_time}:00")

if __name__ == "__main__":
    main()