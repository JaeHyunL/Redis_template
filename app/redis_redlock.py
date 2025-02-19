import time
from redlock import RedLock


class RedlockHelper(object):
    def __init__(self):
        # Create a RedLock instance with connection details to your Redis Server
        # You can specify multiple Redis servers for fault tolerance
        servers = [{"host": "redis", "port": 6379, "db": 0}]
        self.dlm = RedLock(servers)
        self.my_lock = None

    def acquire_lock(self, lock_name, ttl=5000):
        """Attempt to acquire a lock with the given name."""
        lock_key = f"lock:{lock_name}"
        while True:
            self.my_lock = self.dlm.lock(lock_key, ttl)
            if self.my_lock:
                return True
            # Sleep for a short inerval before retrying
            time.sleep(0.1)

    def release_lock(self):
        """Release the lock with the given name."""
        self.dlm.unlock(self.my_lock)


if __name__ == "__main__":
    RedlockHelper = RedlockHelper()
