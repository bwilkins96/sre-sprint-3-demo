# Import necessary libraries
import asyncio   # Enables asynchronous programming for efficient concurrent execution
import logging   # Handles logging to save latency results in a file
from argparse import ArgumentParser  # Used for handling command-line arguments (e.g., --threshold, --interval, --count
from ping3 import ping  # Import the ping function from the ping3 library to measure network latency
from pymongo import MongoClient # Import MongoClient to connect to MongoDB
import datetime
import os

def configure_logging(file_name: str) -> None:
    """
    Configures logging to save latency results to a file

    Args:
        file_name (str): Name of file for outputting logs 
    
    Returns:
        None
    """

    logging.basicConfig(
        filename=file_name,  # Log file name
        level=logging.INFO,          # Log level (INFO: logs important events)
        format="%(asctime)s - %(levelname)s - %(message)s"  # Log format with timestamp
    )

def get_mongo_collection():
    """
    Connects to MongoDB using environment variables.
    Returns a collection object for logging.
    """
    mongo_host = os.getenv("MONGO_HOST", "localhost")
    mongo_port = int(os.getenv("MONGO_PORT", 27017))

    client = MongoClient(f"mongodb://{mongo_host}:{mongo_port}")
    db = client["latency_monitor"]
    return db["latency_logs"]


def set_up_cmd_line_parser() -> ArgumentParser:
    """
    Sets up command-line parser for latency checker

    Returns:
        ArgumentParser
    """

    # Set up the command-line argument parser using argparse
    parser = ArgumentParser(description="Efficient Network Latency Checker")

    # Argument to specify target servers or IPs
    parser.add_argument("targets", nargs="+", help="Target servers or IPs to ping")

    # Argument for setting latency threshold (default: 100ms)
    parser.add_argument("-t", "--threshold", type=int, default=100,
                        help="Latency threshold in milliseconds (default: 100ms)")

    # Argument for setting ping interval (default: 5 seconds)
    parser.add_argument("-i", "--interval", type=int, default=5,
                        help="Ping interval in seconds (default: 5s)")

    # Argument for setting number of pings per target (default: 10 pings)
    parser.add_argument("-c", "--count", type=int, default=10,
                        help="Number of times to ping each target (default: 10)")

    return parser

async def check_latency(target: str, threshold: int, interval: int, count: int, collection) -> None:
    """
    Pings the target server a specified number of times and logs high latency.

    Args:
        target (str): The server or IP to ping.
        threshold (int): The latency threshold in milliseconds.
        interval (int): The time in seconds between pings.
        count (int): The number of times to ping the target.

    Returns:
        None
    """
    for i in range(count):  # Stop after 'count' pings
        latency = await asyncio.to_thread(ping, target)  # Run ping in an async-friendly way

        if latency is None:
            print(f"❌ Unable to reach {target}")  # Display error if the server is unreachable
            
            logging.warning(f"⚠️ Failed to reach {target}")  # Log failure

            collection.insert_one({ # Log to mongodb with unreachable status
                "target": target,
                "status": "unreachable",
                "latency_ms": None,
                "threshold_ms": threshold,
                "timestamp": datetime.datetime.now(datetime.timezone.utc)
            })
        else:
            latency_ms = round(latency * 1000, 2)  # Convert seconds to milliseconds
            print(f"✅ {target} latency: {latency_ms} ms ({i+1}/{count})")  # Display latency with count progress

            # Log to file only if latency exceeds the defined threshold
            if latency_ms > threshold:
                logging.warning(f"⚠️ High latency for {target}: {latency_ms} ms")

            entry = { # Create a log entry for MongoDB
                "target": target,
                "status": "high_latency" if latency_ms > threshold else "ok", # Log status based on threshold
                "latency_ms": latency_ms,
                "threshold_ms": threshold,
                "timestamp": datetime.datetime.now(datetime.timezone.utc)
            }
            collection.insert_one(entry)

        await asyncio.sleep(interval)  # Non-blocking sleep to avoid excessive CPU usage


async def main():
    """
    Creates and runs multiple latency checks concurrently for different targets.

    Returns:
        None
    """

    # Set up logging for 'latency_log.txt'
    configure_logging("latency_log.txt")

    # Parse command-line arguments
    parser = set_up_cmd_line_parser()
    args = parser.parse_args()

    # Connect to MongoDB collection for logging
    collection = get_mongo_collection() 

    # Create an asynchronous task for each target
    tasks = [check_latency(target, args.threshold, args.interval, args.count, collection) for target in args.targets]
    await asyncio.gather(*tasks)  # Run all latency checks concurrently


if __name__ == "__main__":    
    # Run the asynchronous event loop to execute the main function
    asyncio.run(main())
