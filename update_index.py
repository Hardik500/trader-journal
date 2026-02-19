import os

JOURNAL_DIR = "/home/openclaw/projects/trader-journal"

def update_index():
    files = sorted([f for f in os.listdir(JOURNAL_DIR) if f.endswith(".md") and f != "README.md" and f != "index.md"], reverse=True)
    
    with open(os.path.join(JOURNAL_DIR, "index.md"), "w") as f:
        f.write("# Peter's Trading Journal\n\n")
        f.write("Daily market reflections and trade logs.\n\n")
        f.write("## Entries\n\n")
        
        for filename in files:
            date_str = filename.replace(".md", "")
            f.write(f"- [{date_str}]({filename})\n")

if __name__ == "__main__":
    update_index()
