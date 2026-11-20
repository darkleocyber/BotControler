import asyncio
import TeleBotControl
import inspect

try:
    print("Main arguments:", inspect.signature(TeleBotControl.main))
except Exception as e:
    print("Signature not found:", e)

asyncio.run(TeleBotControl.main())
