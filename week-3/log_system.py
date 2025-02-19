# Task 2: Create a logging system to record script execution details.
import logging

# Configure logging settings
logging.basicConfig(
    filename="script.log",  # Log file name
    level=logging.INFO,  # Set logging level
    format="%(asctime)s - %(levelname)s - %(message)s",  # Log format
    datefmt="%Y-%m-%d %H:%M:%S"  # Timestamp format
)

def main():
    logging.info("Script execution started.")

    try:
        # Simulating some script actions
        logging.info("Performing task 1...")
        # Example: Simulate a warning
        logging.warning("Warning: Task 1 might take longer than expected.")

        logging.info("Performing task 2...")
        # Example: Simulate an error
        raise ValueError("An error occurred in task 2!")

    except Exception as e:
        logging.error(f"Error: {e}")

    finally:
        logging.info("Script execution finished.")

if __name__ == "__main__":
    main()
