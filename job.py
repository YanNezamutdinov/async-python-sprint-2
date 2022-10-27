import threading
from datetime import datetime
from typing import Optional, List

from funcshions import dct_func


class Job:

    @staticmethod
    def run(key: str,
            func: str,
            cond: threading.Condition,
            start_at: Optional[str] = None,
            max_working_time: Optional[str] = None,
            tries: int = 1,
            dependencies: Optional[List[str]] = None) -> str:
        while tries > 0:
            try:
                with cond:
                    if dependencies:
                        cond.wait()
                    if start_at:
                        time_obj = datetime.combine(datetime.today().date(), datetime.strptime(start_at, '%H:%M').time())
                        delayed = int((time_obj - datetime.today()).total_seconds())
                        if delayed > 0:
                            timer = threading.Timer(delayed, dct_func.get(func))
                            timer.start()
                            timer.join(max_working_time)
                    else:
                        thread = threading.Thread(target=dct_func.get(func))
                        thread.start()
                        thread.join(max_working_time)
                        tries -= 1
                    if not dependencies:
                        cond.notify_all()
            except Exception:
                pass

        return key

