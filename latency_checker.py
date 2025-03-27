import argparse
import asyncio
import logging
from ping3 import ping

# Configure logging
logging.basicConfig(filename="latency_log.txt", level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")

async def check_latency(target, threshold, interval, count):
    """
    Pings the target server a specified number of times and logs high latency.
    """
    for i in range(count):  # Stop after 'count' pings
        latency = await asyncio.to_thread(ping, target)

        if latency is None:
            print(f"❌ Unable to reach {target}")
            logging.warning(f"⚠️ Failed to reach {target}")
        else:
            latency_ms = round(latency * 1000, 2)
            print(f"✅ {target} latency: {latency_ms} ms ({i+1}/{count})")

            # Log only when latency is above the threshold
            if latency_ms > threshold:
                logging.warning(f"⚠️ High latency for {target}: {latency_ms} ms")

        await asyncio.sleep(interval)  # Non-blocking sleep

async def main():
    tasks = [check_latency(target, args.threshold, args.interval, args.count) for target in args.targ>    await asyncio.gather(*tasks)  # Run all latency checks concurrently

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Efficient Network Latency Checker")
    parser.add_argument("targets", nargs="+", help="Target servers or IPs to ping")
    parser.add_argument("-t", "--threshold", type=int, default=100,
                        help="Latency threshold in milliseconds (default: 100ms)")
    parser.add_argument("-i", "--interval", type=int, default=5,
                        help="Ping interval in seconds (default: 5s)")
    parser.add_argument("-c", "--count", type=int, default=10,
                        help="Number of times to ping each target (default: 10)")

    args = parser.parse_args()

    # Run the asynchronous event loop
    asyncio.run(main())
