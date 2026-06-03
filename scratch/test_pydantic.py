import sys
from pathlib import Path

# Add business_agent src to path
sys.path.append(str(Path("/Users/nemri/Downloads/ucp-agent-demo/business_agent/src")))

from business_agent.store import RetailStore

store = RetailStore()
results = store.search_products("Cookies")
dumped = results.model_dump(mode="json")
print("First product extra fields keys:", dumped["results"][0].keys())
print("First product nutrition:", dumped["results"][0].get("nutrition"))
