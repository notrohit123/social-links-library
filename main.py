from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime
import sqlite3
import re
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

DATABASE = "social_library.db"


def get_db_connection():
    return sqlite3.connect(DATABASE, check_same_thread=False)


@app.on_event("startup")
def initialize_db():
    conn = get_db_connection()
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS links (
                    id INTEGER PRIMARY KEY,
                    url TEXT UNIQUE,
                    platform TEXT,
                    caption TEXT,
                    tags TEXT,
                    importance INTEGER DEFAULT 2,
                    added_date TEXT)''')
    conn.commit()
    conn.close()


class SocialLink(BaseModel):
    url: str
    caption: str = ""
    tags: str = ""
    importance: int = 2


class RenameLink(BaseModel):
    id: int
    new_caption: str
    new_tags: str
    new_importance: int


def detect_platform(url: str):
    url = url.lower()
    patterns = {
        "reddit": r'reddit\.com',
        "twitter": r'twitter\.com|x\.com',
        "youtube": r'youtube\.com|youtu\.be',
        "instagram": r'instagram\.com'
    }
    for platform, pattern in patterns.items():
        if re.search(pattern, url):
            return platform
    return "other"


@app.post("/add-link")
def add_link(link: SocialLink):
    conn = get_db_connection()
    c = conn.cursor()
    platform = detect_platform(link.url)

    try:
        c.execute('''INSERT INTO links (url, platform, caption, tags, importance, added_date)
                     VALUES (?,?,?,?,?,?)''',
                  (link.url, platform, link.caption, link.tags, link.importance, datetime.now().isoformat()))
        conn.commit()
        return {"status": "success", "id": c.lastrowid}
    except sqlite3.IntegrityError:
        raise HTTPException(status_code=400, detail="Link already exists")
    finally:
        conn.close()


@app.delete("/delete-link/{link_id}")
def delete_link(link_id: int):
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("DELETE FROM links WHERE id = ?", (link_id,))
    if c.rowcount == 0:
        raise HTTPException(status_code=404, detail="Link not found")
    conn.commit()
    conn.close()
    return {"status": "success", "message": "Link deleted successfully"}


@app.put("/rename-link")
def rename_link(rename: RenameLink):
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("UPDATE links SET caption = ?, tags = ?, importance = ? WHERE id = ?",
              (rename.new_caption, rename.new_tags, rename.new_importance, rename.id))
    if c.rowcount == 0:
        raise HTTPException(status_code=404, detail="Link not found")
    conn.commit()
    conn.close()
    return {"status": "success", "message": "Link updated successfully"}


@app.get("/get-links")
def get_links(platform: str = None, tag: str = None, priority: int = None):
    conn = get_db_connection()
    c = conn.cursor()

    query = "SELECT * FROM links"
    params = []
    conditions = []

    if platform:
        conditions.append("platform = ?")
        params.append(platform)
    if tag:
        conditions.append("tags LIKE ?")
        params.append(f'%{tag}%')
    if priority:
        conditions.append("importance = ?")
        params.append(priority)

    if conditions:
        query += " WHERE " + " AND ".join(conditions)

    query += " ORDER BY importance, added_date DESC"

    c.execute(query, params)
    results = [
        {
            "id": row[0],
            "url": row[1],
            "platform": row[2],
            "caption": row[3],
            "tags": row[4].split(',') if row[4] else [],
            "importance": row[5],
            "date": row[6]
        }
        for row in c.fetchall()
    ]
    conn.close()
    return {"results": results}
