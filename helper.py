import requests
import asyncio

# Set push URL to nothingness
push_url = "https://example.com"
# Set heartbeat to Uptime Kuma's default 60
heartbeat_int = 60
# Create message to show
message = """
Oliver's Tech PyKuma API
---------------------------
A Python API which allows you to integrate your scripts with Uptime Kuma.

You can hide this message by setting ShowMessage to false in the PyKuma configuration.
---------------------------
"""
showmsg = None
printPushv = False

def configure(url, heartbeat=60, ShowMessage=True, printPush=False): #Require push URL, optional heartbeat (if not specified set to 60)
    global push_url
    global heartbeat_int
    global showmsg
    global printPushv

    # Configure assignments
    push_url = url
    heartbeat_int = heartbeat
    showmsg = ShowMessage
    printPushv = printPush

async def start_main(): # Optionally print when pushed to Kuma
    if showmsg == True:
        print(message)
    # Endlessly push to Uptime Kuma in background as per heartbeat. Stop if stop variable is set.
    while True:        
        requests.get(push_url) # Kuma push
        if printPushv == True:
            print("--Pushed to uptime kuma--") # Console log if specified
        await asyncio.sleep(heartbeat_int) # Sleep for heartbeat

async def start_secondary():       
    asyncio.create_task(start_main())

def start():
    asyncio.run(start_secondary())