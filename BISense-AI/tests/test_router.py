from ai.router.router import IntentRouter
def test_router(): assert IntentRouter().route('What is the BIS standard?').value=='standards'
