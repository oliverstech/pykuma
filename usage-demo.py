import pykuma

pykuma.configure(url="https://example.com/your-uptimekuma-push-url", heartbeat=1234, ShowMessage=True)

pykuma.start()

print("Your other code goes here...")