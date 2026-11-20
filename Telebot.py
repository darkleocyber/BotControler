import TeleBotControl
import inspect

try:
    print("Auto_run arguments:", inspect.signature(Tarmuxset.auto_run))

# যদি main কাজ করে তবে এটিই ব্যবহার করুন
import asyncio
import TeleBotControl

asyncio.run(TeleBotControl.main())
