from pyzotero import zotero
import json
zot = zotero.Zotero(
    library_id="0", 
    library_type="user",
    api_key="",  
    local=True   
)

items = zot.top(limit=5)
print("="*40)
print(json.dumps(items, indent=2))